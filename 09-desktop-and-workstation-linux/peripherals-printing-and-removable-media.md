# Connect peripherals and handle removable storage

[Collection home](README.md) · Previous: [Power](power-battery-and-suspend.md) · Next: [Personal backups](personal-backups-and-migration.md)

## Environment and prerequisites

Use a local graphical session and a peripheral you own or are authorized to use. You can complete the observation exercise without attaching anything. A printer, scanner, Bluetooth adapter, webcam, dock and storage device each have different consumers and permission paths; “USB detected” is not a universal functional test.

For removable-media practice, use a spare drive containing no irreplaceable data, with a filesystem already supported by your system. **Do not format or repartition it for this exercise.** Stop if the desktop offers to initialize an unexpected disk. For printing, use your own authorized queue and a non-sensitive one-page document; printing consumes resources and can expose content at the physical printer.

The command exercise needs Linux, Bash, Python 3 and util-linux `lsblk`. It requests selected fields without serial numbers or filesystem UUIDs and writes a private report. No root access, device opening or mounting is performed.

## Understand the components

| Layer | Question | Typical observation |
| --- | --- | --- |
| Physical connection | Correct port, cable, power and device mode? | A charging cable may not carry the needed data/video |
| Bus discovery | Does the system enumerate the device? | USB discovery is different from a usable printer or mounted filesystem |
| Kernel driver | Does a compatible driver bind and expose interfaces? | A device can be listed without its required interface |
| User-space service | Which component manages printing, Bluetooth or storage? | CUPS, BlueZ and desktop storage services solve different tasks |
| Session authorization | Is your logged-in account allowed to use it? | Running the entire application as root is not a narrow repair |
| Application integration | Does the intended application select and use it? | A camera preview in one app does not prove browser permission |
| Safe completion | Has work finished and can the device be removed? | A copied filename is not proof that all writes are complete |

Do not install arbitrary driver scripts from search results. Check the exact model and release against the vendor/distribution's supported route. For firmware updates, retain stable power and follow the supported tool; device discovery alone is not a reason to flash firmware.

## Follow along

### 1. Inspect storage without touching it

<!-- workstation:exercise -->
```bash
peripheral_lab=$(mktemp -d) || exit 1
lsblk --json --output NAME,TYPE,SIZE,RO,RM > "$peripheral_lab/block-devices.json" || exit 1
python3 - "$peripheral_lab" <<'PY'
import json
from pathlib import Path
import sys
root = Path(sys.argv[1])
report = json.loads((root / 'block-devices.json').read_text())
assert isinstance(report.get('blockdevices'), list)
print('PASS: read-only block-device inventory captured selected non-serial fields')
print('Device names and removable flags do not identify a safe write target by themselves.')
PY
```

`RM` is a reported removable flag; some USB storage appears as non-removable. `/dev/sdX` names can change. The inventory is deliberately not a command for selecting a format target.

### 2. Copy and verify one harmless file

1. Create a small text document in your home learning directory and save it. Keep the original.
2. Connect your spare preformatted drive. In the file manager, identify it using its label and capacity, then compare with its known physical identity. If two candidates are ambiguous, stop and disconnect the spare to observe which entry disappears.
3. Open it through the file manager. If you encounter an access or filesystem error, preserve the message; do not accept formatting as a generic fix.
4. Copy the test document to a newly named learning folder on that drive. Open the copy and compare the content. For exact byte comparison, use `cmp -- ORIGINAL COPY` in a terminal with both actual paths quoted.
5. Close documents and terminals using the drive. Use **Eject**, **Safely Remove** or the desktop's corresponding action and wait for successful completion before disconnecting. A busy warning means something still holds the device; do not bypass it blindly.
6. Reconnect and open the copy again. Verify it still matches. This checks one completed transfer, not the drive's long-term health or every file on it.

If a filesystem is reported damaged or read-only, stop writing and consult its supported recovery procedure. Never run a filesystem repair against an actively mounted filesystem by habit. Do not change broad ownership or permissions recursively to make one copy work.

### 3. Add and verify an authorized printer

Open Printers settings, identify the intended device/queue and inspect the connection details before adding it. Prefer the distribution's supported driverless route for a compatible IPP printer; legacy devices may need a supported driver or Printer Application. Automatic discovery does not prove that the printer belongs to you.

Print a non-sensitive single page. Verify the correct physical output, page count and layout; a queue showing “completed” is not physical confirmation. Check the queue after completion and cancel only your own test job if it is stuck. Do not clear other users' jobs.

If CUPS tools are installed, `lpstat -p` reports configured printer status and `lpstat -o` reports jobs visible to the query. These can contact the configured print server and reveal queue/user information. Use them only in your authorized printing context. A missing discovery result can involve network name discovery, routing, service policy or the printer itself, not just a driver.

### 4. Pair Bluetooth and test the intended function

Open Bluetooth settings, enable pairing mode on your device and compare the displayed identity/passcode according to its manual. Pair only the device you control. After pairing, test its actual function: type with a keyboard, move a pointer or select an audio route. Pairing success is not functional success.

If pairing is stale, use the desktop's supported “forget device” action for that device only, then pair again with access to its recovery controls. Do not reset the entire Bluetooth database. Reconnecting after sleep is a separate test; see [power](power-battery-and-suspend.md).

### 5. Check other peripherals by their output

For a scanner, save a non-sensitive page and open the resulting file. For a camera, use a local preview and verify shutdown indicators afterward. For a dock, test display, network, USB and power as separate functions. For input devices, retain another working input method before changing mappings. One working dock function does not prove all ports and bandwidth combinations work together.

## Verify and recover

Record the exact peripheral model privately, connection type, distribution, desktop and observed failure stage. Redact serial numbers, Bluetooth addresses, printer locations and unrelated identifiers before sharing a report.

If the bus sees a device but the app does not, investigate the relevant driver/service and session authorization. If it works directly but not through a hub, compare the physical path, power and bandwidth before reinstalling software. If the device is busy, identify the application using it instead of forcing disconnection.

For recovery, undo only your own queue, pairing or application selection changes. Keep the source document and stop before any proposed operation that could erase a real storage device.

## Cleanup

<!-- workstation:cleanup -->
```bash
rm -i -- "$peripheral_lab/block-devices.json"
rmdir -- "$peripheral_lab"
```

Remove only your disposable copy/folder from the spare drive after confirming the original remains. Safely remove the drive again. Remove a printer or Bluetooth pairing only if you created it solely for practice and no longer need it.

## Checkpoint

You can separate enumeration, authorization and application behavior; verify a transfer after reconnecting; and distinguish a completed print queue entry from the correct physical output.

## Sources

Use [lsblk(8)](https://man7.org/linux/man-pages/man8/lsblk.8.html), [GNOME device help](https://help.gnome.org/gnome-help/), [OpenPrinting CUPS documentation](https://openprinting.github.io/cups/), [CUPS lpstat manual](https://openprinting.github.io/cups/cups-local/lpstat.html), [OpenPrinting driver transition](https://openprinting.github.io/cups/drivers.html), [BlueZ project](https://www.bluez.org/) and [fwupd documentation](https://fwupd.org/). Check your distribution's support and device-specific instructions before installing drivers or firmware.
