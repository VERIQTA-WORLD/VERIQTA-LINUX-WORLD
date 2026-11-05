# Make audio, camera and screen sharing work

[Collection home](README.md) · Previous: [Displays](displays-and-graphics.md) · Next: [Power](power-battery-and-suspend.md)

## Environment and prerequisites

Use a local graphical session with an output device and, for recording, a microphone you control. Camera and screen-sharing checks need the relevant hardware and an application with a local preview or a meeting test page. You do not need to join a public call, record another person or enable remote desktop access.

PipeWire and WirePlumber are common on current desktops, but PulseAudio-only and other setups exist. Inspect the installed stack before selecting commands. Run session tools as your ordinary user, not with sudo. A headless VM with no audio devices cannot establish that your speakers, Bluetooth profile or camera work.

The isolated exercise needs Bash and Python 3. It generates and inspects a quiet, short PCM WAV file without playing it. Manual playback is optional and should begin with low system volume; avoid unexpected output through headphones or assistive audio.

## Understand the components

| Component | Role | Typical confusion |
| --- | --- | --- |
| ALSA/kernel driver | Exposes audio hardware interfaces | Hardware presence alone does not select the desktop output |
| PipeWire | Media graph and processing infrastructure | A running process does not prove the right route or application stream exists |
| WirePlumber | Session/routing policy on applicable PipeWire setups | Numeric object IDs can change; do not copy another person's ID |
| PulseAudio compatibility | Allows PulseAudio clients to use a compatible server | `pactl` working does not necessarily mean a standalone PulseAudio daemon is in use |
| Sink/output | Playback destination | HDMI audio can become the selected output when a monitor is connected |
| Source/input | Recording source, possibly a microphone or monitor | A monitor source captures output audio, not your physical microphone |
| Device profile | Supported mode/combination of channels and routes | Bluetooth call and music profiles can differ in quality and microphone availability |
| Application stream | One application's audio/video connection | Per-app mute/volume can differ from global volume |
| Camera portal/permissions | Mediated access where supported | Browser site permission and operating-system permission can both matter |
| Screen capture | Selected screen/window stream | Sharing a window is different from allowing remote control |

Microphone hardware mute switches, privacy shutters and keyboard indicators are part of the path. Check them before changing drivers. Permissions should be specific to the application and activity; broad device access is not a default troubleshooting step.

## Follow along

### 1. Select and test output

Open Sound settings. Note your previous output and volume. Choose the intended speakers/headphones and start at a comfortable low volume. Use the desktop's test control if provided. Confirm the correct physical device plays the sound; seeing a level meter is not proof that the right person can hear it.

Open one media application with known local content. Check its mute and volume controls as well as the system's per-application controls. If a dock or monitor is attached, compare output selection before and after connection without raising volume aggressively.

On a PipeWire/WirePlumber desktop, `wpctl status` can show devices, sinks, sources and streams. It is an observation of the current graph, not an audio-quality test. To inspect one object, use `wpctl inspect ID` with an ID you just observed. Do not reuse an ID after reconnecting hardware without checking it again. `systemctl --user status pipewire wireplumber` is relevant only where those are the actual managed services.

### 2. Generate a known local signal

This creates a one-second mono signal at 440 Hz, 16 kHz sampling rate and a low digital amplitude. Low digital amplitude does not guarantee a safe physical volume setting.

<!-- workstation:exercise -->
```bash
audio_lab=$(mktemp -d) || exit 1
python3 - "$audio_lab" <<'PY'
import math
from pathlib import Path
import struct
import sys
import wave
root = Path(sys.argv[1])
rate = 16000
samples = [int(1000 * math.sin(2 * math.pi * 440 * n / rate)) for n in range(rate)]
payload = b''.join(struct.pack('<h', sample) for sample in samples)
path = root / 'quiet-test.wav'
with wave.open(str(path), 'wb') as output:
    output.setnchannels(1)
    output.setsampwidth(2)
    output.setframerate(rate)
    output.writeframes(payload)
with wave.open(str(path), 'rb') as recorded:
    assert recorded.getnchannels() == 1
    assert recorded.getsampwidth() == 2
    assert recorded.getframerate() == rate
    assert recorded.getnframes() == rate
    assert recorded.readframes(rate) == payload
print('PASS: one-second PCM signal written and read back exactly; no sound was played')
PY
```

Optionally open the WAV from your player using its file picker. Print the directory with `printf '%s\n' "$audio_lab"` if needed. Start at low output volume and stop if uncomfortable. For hearing access, a waveform or meter can verify the application's handling of a signal, but physical output and your required assistive route need their own appropriate check.

### 3. Test input and camera locally

Select the intended microphone in Sound settings. Speak only non-sensitive test words and observe the input meter. Use a local recording application, if installed, for a short sample. Listen back through the intended output or inspect the recording in the way appropriate to you. A moving meter does not establish recording quality, echo control or meeting-app access.

Use the camera application's local preview. Check the intended lens, orientation and privacy controls. In a browser/application, review the permission prompt and select the correct microphone/camera. Test in a local preview or private test context. Close previews afterward and verify indicators behave as expected.

### 4. Test sharing with a harmless window

Open a document containing only disposable text. Use your application's supported screen-sharing control, select that single window where supported, and inspect the preview. Keep password managers, notifications and private documents out of the shared area. Stop sharing and verify the preview/indicator ends.

On Wayland, a portal and compatible backend commonly mediate capture; an X11-only capture path may not behave the same. Do not disable the session's isolation or switch the entire desktop merely to bypass a missing permission prompt. Identify application, portal backend and session versions first.

## Verify and recover

Verify output, input, recording, camera preview and sharing separately. Record which succeeded and which were unavailable rather than marking the entire media stack “working.”

| Symptom | Next check |
| --- | --- |
| Meters move but you hear nothing | Output selection, application mute, hardware volume and cable |
| Recording contains system audio | Selected source may be a monitor rather than microphone |
| Bluetooth music works but calls sound different | Active profile and microphone requirements; hardware/protocol limitations |
| One browser site cannot capture | Site permission, device selection and application/portal integration |
| Share selector opens but capture is blank | Selected window, session/backend compatibility and application version |
| IDs changed after reconnect | Refresh the device graph rather than applying commands to stale IDs |

Restore the previous output, input and volume if your experiment disrupted them. Close applications holding a device before retesting another one. Do not restart shared/session services or delete audio state as a first step; that can interrupt calls and obscure the original evidence. Use distribution-specific recovery only after preserving the relevant observations.

## Cleanup

Close the WAV in your player, then remove it:

<!-- workstation:cleanup -->
```bash
rm -i -- "$audio_lab/quiet-test.wav"
rmdir -- "$audio_lab"
```

Delete only recordings you intentionally made for this exercise, revoke temporary permissions through the application's supported controls, stop sharing and close camera previews. Retain accessibility routes and permissions you actually require.

## Checkpoint

You can trace an application's stream to the intended input/output, explain why a meter alone is incomplete evidence, and demonstrate that sharing/recording has stopped.

## Sources

Use [PipeWire documentation](https://docs.pipewire.org/), [WirePlumber wpctl manual](https://pipewire.pages.freedesktop.org/wireplumber/man/wpctl.html), [WirePlumber getting started](https://pipewire.pages.freedesktop.org/wireplumber/daemon/getting_started.html), [GNOME sound and media help](https://help.gnome.org/gnome-help/), [ScreenCast portal API](https://flatpak.github.io/xdg-desktop-portal/docs/doc-org.freedesktop.portal.ScreenCast.html) and [Python wave documentation](https://docs.python.org/3/library/wave.html). Configuration formats and capture support depend on the installed versions.
