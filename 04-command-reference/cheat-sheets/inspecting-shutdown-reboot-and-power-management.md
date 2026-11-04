| Command | What you can do with it |
| --- | --- |
| `systemctl list-jobs` | List queued systemd jobs. |
| `systemctl is-system-running` | Query the overall systemd operational state. |
| `systemd-inhibit --list` | List locks that can inhibit shutdown or sleep. |
| `who -b` | Read the recorded last boot time. |
| `uptime -s` | Print the system start time. |
| `last -x -n 20` | Inspect recent recorded shutdown, reboot and runlevel events. |
| `loginctl list-sessions` | List logind sessions that may be affected by maintenance. |
| `shutdown --show` | Inspect a scheduled shutdown where this option is supported. |
| `shutdown --help` | Read shutdown scheduling options without scheduling a shutdown. |
| `reboot --help` | Read reboot options without requesting a reboot. |
| `poweroff --help` | Read poweroff options without powering off. |
| `halt --help` | Read halt options without halting. |
| `systemctl reboot --help` | Read systemctl help without requesting a reboot. |
| `systemctl poweroff --help` | Read systemctl help without requesting poweroff. |
| `systemctl suspend --help` | Read systemctl help without requesting suspend. |
| `systemctl hibernate --help` | Read systemctl help without requesting hibernation. |
