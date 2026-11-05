# Set up displays and identify the graphics path

[Collection home](README.md) · Previous: [Applications](applications-and-software-trust.md) · Next: [Audio and video](audio-video-and-screen-sharing.md)

## Environment and prerequisites

Use an active local graphical session and the desktop's Displays settings. One monitor is enough for resolution/scale checks; a second monitor or dock is required to test multi-display behavior. Save your work and retain a usable input method before changing layout. Do not experiment during a presentation or remote session you cannot recover.

The supporting exercise needs Bash, Python 3 and Linux; it reads `/sys/class/drm` when available. A headless VM can legitimately report **no display connectors**. The exercise inventories that absence honestly; it does not simulate a connected display or validate rendering. No root privileges or graphics-driver installation is required.

## Understand the components

| Component | What it contributes | Observation boundary |
| --- | --- | --- |
| GPU and kernel driver | Device support and display/memory interfaces | A detected PCI device does not prove accelerated rendering |
| Mesa/vendor user-space driver | Rendering interfaces used by applications | Package/architecture/version must match the intended stack |
| Compositor | Window composition and display policy | Wayland compositor settings are not generally controlled by X11's `xrandr` |
| Connector and cable/dock | Physical signal path | A charging USB-C port/cable need not support the required display mode |
| Mode and refresh rate | Pixel dimensions and update frequency | Advertised support depends on the whole path, including adapters and bandwidth |
| Scale | Mapping interface size to pixels | Mixed-scale behavior and application sharpness vary by toolkit/session |
| Color/HDR profile | Color interpretation and output behavior | Support varies; a bright image is not a color-calibration result |
| Screen-sharing portal | User-approved capture path for supported applications | A visible monitor does not prove that a sandboxed app can capture it |

`XDG_SESSION_TYPE` is a useful hint for a logged-in session, not a universal detector in SSH, containers or nested sessions. XWayland permits some X11 applications inside Wayland sessions; it does not turn the whole session into X11.

## Follow along

### 1. Establish your baseline

Open Displays settings and record, privately, the current resolution, scale, orientation, refresh rate and primary display where applicable. Note your desktop/session version. Identify monitor labels in the UI; physical connector names and user-visible labels can differ.

Keep the current mode if readability or accessibility depends on it. Test one change at a time. Prefer settings with a timed **Keep/Revert** confirmation; if the result is unusable, wait for the desktop's documented timeout instead of confirming blindly. Not every desktop/version provides automatic reversion for every change, so check the control before applying.

### 2. Adjust and test the actual workflow

1. Choose a supported scale or resolution and apply it. Confirm only if the image and controls remain usable.
2. Read text in your browser, editor and terminal. Check cursor size, focus visibility and any magnification you use. Sharpness and comfortable size are separate outcomes.
3. With two displays, use **Identify**, arrange their relative positions to match your desk, and choose extend or mirror deliberately. Move the pointer and a window across the boundary in both directions.
4. Recheck after disconnecting and reconnecting a dock, if that is part of your normal workflow. Save work first; hotplug can move windows.
5. Test the intended refresh rate and application behavior. Do not force an unsupported custom mode to meet a number in a tutorial.

A second display that is detected but blank can involve mode selection, adapter/cable bandwidth, input selection, dock firmware or a driver problem. Compare a direct connection and a known-good cable where available before changing global driver policy.

### 3. Inspect connector information read-only

The script checks the Linux DRM interface and records only connector status and advertised mode strings. It does not read EDID serial numbers or modify a kernel interface.

<!-- workstation:exercise -->
```bash
display_lab=$(mktemp -d) || exit 1
python3 - "$display_lab" <<'PY'
import json
from pathlib import Path
import sys
root = Path(sys.argv[1])
drm = Path('/sys/class/drm')
available = drm.is_dir()
connectors = []
for status in sorted(drm.glob('card*-*/status')):
    modes = status.parent / 'modes'
    try:
        connectors.append({'connector': status.parent.name,
                           'status': status.read_text().strip(),
                           'modes': modes.read_text().splitlines() if modes.exists() else []})
    except OSError as error:
        raise SystemExit('Cannot read connector information: ' + str(error))
report = {'interface_available': available, 'connectors': connectors}
(root / 'connectors.json').write_text(json.dumps(report, indent=2) + '\n')
assert json.loads((root / 'connectors.json').read_text()) == report
print('PASS: DRM availability and read-only inventory recorded; connectors=' + str(len(connectors)))
print('No connectors means no connector evidence here; it does not prove graphics failure.')
PY
cat "$display_lab/connectors.json"
```

## Verify and recover

The command exercise should produce a `PASS` line and JSON; an empty connector list or unavailable interface is valid on a headless environment. On your actual desktop, verify readable applications, correct pointer movement, the intended primary/extended layout and recovery from a rejected settings change. Those are separate manual outcomes.

| Symptom | Next bounded check |
| --- | --- |
| Only one application is blurry | Compare another native application and its toolkit/session scaling behavior |
| No external display detected | Check monitor input, cable capability and connector/dock path |
| Layout resets after docking | Record which session, connector and profile changed; compare desktop's saved layout behavior |
| Desktop works but app rendering fails | Identify the application's graphics backend and package source; do not infer a kernel failure from one app |
| Screen sharing is blank | Check capture selection and portal/session support in the [audio/video guide](audio-video-and-screen-sharing.md) |

Restore the recorded baseline through Settings. If a change prevents normal login, use the desktop/distribution's documented recovery route; do not delete all display configuration or install a different driver without diagnosis. Driver changes can affect boot and require a separate recovery plan.

## Cleanup

<!-- workstation:cleanup -->
```bash
rm -i -- "$display_lab/connectors.json"
rmdir -- "$display_lab"
```

Restore experimental modes/layouts you do not want to keep. Retain useful accessibility settings. Do not write to `/sys/class/drm` for cleanup.

## Checkpoint

You can distinguish connector detection, an advertised mode, usable rendering and successful application capture. You know which display settings your actual session controls and how to undo an unsuccessful change.

## Sources

Use [GNOME Help](https://help.gnome.org/gnome-help/), [KDE Plasma documentation](https://docs.kde.org/), [Wayland architecture](https://wayland.freedesktop.org/architecture.html), [kernel DRM documentation](https://docs.kernel.org/gpu/drm-uapi.html) and [Mesa documentation](https://docs.mesa3d.org/). Hardware and compositor capabilities determine which settings exist; these references do not certify any particular monitor or dock.
