```bash
crontab -l
crontab -e
sudo crontab -u ACCOUNT -l
cat /etc/crontab
ls -l /etc/cron.d
ls -l /etc/cron.daily
run-parts --test /etc/cron.daily
atq
at -l
at -c JOB_ID
at 14:00 tomorrow
batch
systemctl list-timers --all
systemctl status TIMER.timer
systemctl cat TIMER.timer
systemd-analyze calendar '*-*-* 02:00:00'
systemd-run --user --on-active=5m /usr/bin/printf '%s\n' MESSAGE
systemctl --user list-timers --all
```
