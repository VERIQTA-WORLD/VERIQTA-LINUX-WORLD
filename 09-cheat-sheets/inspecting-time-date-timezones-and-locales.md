```bash
date
date -Is
date -u
date +'%Y-%m-%d %H:%M:%S %z'
date +%s
date -d @UNIX_TIMESTAMP
date -d 'tomorrow'
TZ=UTC date
cal
cal -y
timedatectl
timedatectl list-timezones
timedatectl timesync-status
chronyc tracking
chronyc sources -v
chronyc sourcestats -v
ntpq -p
sudo hwclock --show
locale
locale -a
localectl status
localectl list-locales
localectl list-keymaps
```
