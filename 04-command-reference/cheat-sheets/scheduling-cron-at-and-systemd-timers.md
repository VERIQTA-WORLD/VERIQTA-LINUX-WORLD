| Command | What you can do with it |
| --- | --- |
| `crontab -l` | List the current account's crontab. |
| `crontab -e` | Edit the current account's crontab. |
| `sudo crontab -u ACCOUNT -l` | Inspect another account's crontab with authorization. |
| `cat /etc/crontab` | Read the system crontab. |
| `ls -l /etc/cron.d` | List system cron definition files. |
| `ls -l /etc/cron.daily` | List daily cron jobs. |
| `run-parts --test /etc/cron.daily` | List scripts run-parts would select without executing them. |
| `atq` | List pending at jobs. |
| `at -l` | List pending at jobs using the alternate at form. |
| `at -c JOB_ID` | Inspect a queued at job's script. |
| `at 14:00 tomorrow` | Schedule commands entered interactively for tomorrow at 14:00. |
| `batch` | Read commands interactively for execution when load permits. |
| `systemctl list-timers --all` | List systemd timers including inactive ones. |
| `systemctl status TIMER.timer` | Inspect a timer's status. |
| `systemctl cat TIMER.timer` | Read a timer definition and overrides. |
| `systemd-analyze calendar '*-*-* 02:00:00'` | Interpret and check a systemd calendar expression. |
| `systemd-run --user --on-active=5m /usr/bin/printf '%s\n' MESSAGE` | Schedule a one-off user task for five minutes from now. |
| `systemctl --user list-timers --all` | List timers managed by the current user's service manager. |
