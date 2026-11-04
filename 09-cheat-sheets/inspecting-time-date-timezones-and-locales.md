| Command | What you can do with it |
| --- | --- |
| `date` | Print the current local date and time. |
| `date -Is` | Print an ISO-like timestamp with timezone offset. |
| `date -u` | Print the current UTC date and time. |
| `date +'%Y-%m-%d %H:%M:%S %z'` | Print a timestamp in a specified format. |
| `date +%s` | Print seconds since the Unix epoch. |
| `date -d @UNIX_TIMESTAMP` | Convert a Unix timestamp to a readable date. |
| `date -d 'tomorrow'` | Parse and display tomorrow's date. |
| `TZ=UTC date` | Print the current time using UTC for this command. |
| `cal` | Display the current month's calendar. |
| `cal -y` | Display the current year's calendar. |
| `timedatectl` | Inspect clock, timezone and synchronization state. |
| `timedatectl list-timezones` | List supported timezone names. |
| `timedatectl timesync-status` | Inspect systemd time-synchronization status where used. |
| `chronyc tracking` | Inspect Chrony's clock-tracking statistics. |
| `chronyc sources -v` | Inspect Chrony's time sources. |
| `chronyc sourcestats -v` | Inspect Chrony's source statistics. |
| `ntpq -p` | Inspect ntpd peers. |
| `sudo hwclock --show` | Read the hardware clock. |
| `locale` | Display current locale settings. |
| `locale -a` | List installed locales. |
| `localectl status` | Inspect system locale and keyboard settings. |
| `localectl list-locales` | List available locale names through systemd. |
| `localectl list-keymaps` | List available console keyboard maps. |
