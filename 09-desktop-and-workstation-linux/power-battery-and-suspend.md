# Check power, battery and suspend behavior

[Collection home](README.md) · Previous: [Audio/video](audio-video-and-screen-sharing.md) · Next: [Peripherals](peripherals-printing-and-removable-media.md)

## Environment and prerequisites

Use a local Linux computer you can safely resume or restart, with work saved and a recovery sign-in route. Battery checks require a battery-backed device; a desktop or VM may expose none. Suspend/resume and hibernation are hardware-, firmware-, driver- and distribution-dependent. Do not test sleep over your only remote connection.

The command exercise requires Bash, Python 3 and readable Linux power-supply interfaces under `/sys/class/power_supply`. It reads selected attributes only. A valid empty inventory on a VM is not evidence that a laptop's battery or sleep works. No administrator privilege is needed for the exercise.

## Understand the components

| Feature | Purpose | What it does not establish |
| --- | --- | --- |
| Display blanking | Stops visible output after inactivity | Not necessarily session locking or system sleep |
| Session lock | Requires configured authentication before reuse | Not the same as logging out or powering off |
| Power profile | Selects supported performance/energy policy | Actual savings depend on workload, hardware and implementation |
| Runtime power management | Reduces power for individual idle devices | Different from suspending the whole system |
| Suspend-to-idle/deeper suspend | Pauses the system using supported platform states | Resume reliability and energy use must be checked on the actual machine |
| Hibernation | Stores a recoverable memory image using a supported design | Requires compatible storage, resume, encryption and security policy; swap size alone is not a complete setup |
| Battery percentage | A reported estimate relative to current charge model | Not a direct measurement of remaining working hours or long-term battery health |
| Charge threshold | Optional hardware/firmware policy limiting charge range | Not available or useful in the same way on all models |

Power managers can conflict if several independently change the same policy. Use your distribution's supported integration before installing another tuning service. Avoid copying sysfs writes or kernel parameters from a different laptop model.

## Follow along

### 1. Record the visible policy

Open Power settings. Note AC/battery behavior, display blanking, automatic sleep and available profiles. Open Privacy or Screen Lock settings and identify how locking relates to idle blanking and resume. Keep a secure lock policy; disabling it is not required to diagnose sleep.

Where installed, `powerprofilesctl list` and `powerprofilesctl get` inspect the tool's supported profiles/current selection. `upower -e` enumerates power devices; detailed device reports can contain identifiers. Neither tool is guaranteed on every desktop. Do not install a second policy daemon just to make these commands exist.

### 2. Read battery attributes without changing them

The exercise records a few operational values, excluding serial/model identifiers. Some attributes are absent by design.

<!-- workstation:exercise -->
```bash
power_lab=$(mktemp -d) || exit 1
python3 - "$power_lab" <<'PY'
import json
from pathlib import Path
import sys
root = Path(sys.argv[1])
base = Path('/sys/class/power_supply')
assert base.is_dir(), 'Linux power-supply class directory is unavailable'
results = []
for device in sorted(base.iterdir()):
    item = {'device': device.name}
    for name in ['type', 'online', 'status', 'capacity']:
        path = device / name
        if path.exists():
            item[name] = path.read_text().strip()
    results.append(item)
(root / 'power.json').write_text(json.dumps(results, indent=2) + '\n')
assert json.loads((root / 'power.json').read_text()) == results
print('PASS: power-supply attributes read without modification; devices=' + str(len(results)))
PY
cat "$power_lab/power.json"
```

Values can change while you read them; the inventory is not an atomic hardware snapshot. A percentage is an observation at one time. To compare battery endurance, use the same workload, brightness, peripherals, elapsed time and environmental conditions, and repeat measurements rather than extrapolating from one minute.

### 3. Perform one controlled suspend/resume cycle

1. Save all work. Finish updates, backups and external-drive transfers. Disconnect peripherals not needed for the first test, using their safe-removal procedure where appropriate.
2. Record the time, AC/battery condition and current input/network/audio state. Keep another means of reading your distribution's recovery instructions.
3. Use the desktop's **Suspend** action locally. Do not close the lid as your first test if its configured action is unknown.
4. Resume using the device's documented method. Confirm lock-screen behavior and sign in. Check display, keyboard, pointer, network reconnection and audio separately.
5. Save the outcome privately, including delay and any failed component. If it works, repeat with your normal dock/peripherals as a separate test.

A successful one-time cycle does not establish overnight battery drain or repeated reliability. Hibernation is a separate setup and test. Do not enable it by an assumed swap-size recipe or use a firmware reboot as evidence of a successful memory resume.

### 4. Investigate one failure without piling on changes

If resume fails, preserve the time and conditions. After recovering safely, inspect a narrow journal time window or boot boundary if your account can read it. Distinguish a full restart from a resumed session. Compare AC versus battery and direct versus docked operation one variable at a time.

Current sleep-state interfaces such as `/sys/power/state` and `/sys/power/mem_sleep`, when present, describe supported/selected kernel states. Reading them is different from writing to them. Do not force a state that the distribution/hardware does not support. Firmware and kernel updates may affect behavior; review vendor and distribution guidance and maintain a recovery route before updating.

## Verify and recover

You have demonstrated suspend only when the actual machine resumes, preserves the expected session and passes your required input/display/network checks. A headless inventory pass does not meet that criterion. If reliability is uncertain, choose a supported shutdown workflow for unattended travel and keep data saved until you resolve the issue.

Restore only policy changes you made for the test. If the system is unresponsive, use the vendor/distribution's documented recovery procedure; forced power-off can lose unsaved data and should not become a normal suspend method. Do not repeatedly run an unreliable sleep cycle with valuable unsaved work.

## Cleanup

<!-- workstation:cleanup -->
```bash
rm -i -- "$power_lab/power.json"
rmdir -- "$power_lab"
```

Return experimental power profiles and timeouts to your intended values. Keep session locking enabled according to your needs. Do not write kernel power attributes for cleanup.

## Checkpoint

Explain blanking versus locking versus sleep, report a real suspend outcome with its hardware context, and identify which power data is absent rather than inventing a value.

## Sources

Use [kernel sleep-state documentation](https://docs.kernel.org/admin-guide/pm/sleep-states.html), [kernel runtime power management](https://docs.kernel.org/power/runtime_pm.html), [power-supply class documentation](https://docs.kernel.org/power/power_supply_class.html), [UPower documentation](https://upower.freedesktop.org/docs/), [power-profiles-daemon project](https://gitlab.freedesktop.org/upower/power-profiles-daemon) and your desktop's [GNOME help](https://help.gnome.org/gnome-help/) or [KDE documentation](https://docs.kde.org/). Use the hardware vendor's supported firmware instructions for your exact model.
