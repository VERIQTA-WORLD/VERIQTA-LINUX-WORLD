| Command | What you can do with it |
| --- | --- |
| `journalctl --list-boots` | List boots retained in the journal. |
| `journalctl -b` | Read journal entries from the current boot. |
| `journalctl -b -1` | Read journal entries from the previous retained boot. |
| `journalctl -b -n 100 --no-pager` | Read the latest 100 records from the current boot without a pager. |
| `journalctl -u UNIT -n 100 --no-pager` | Read the latest 100 records for one unit. |
| `journalctl -u UNIT --since '1 hour ago'` | Read a unit's records from the last hour. |
| `journalctl --since 'YYYY-MM-DD HH:MM:SS' --until 'YYYY-MM-DD HH:MM:SS'` | Read records within a specified time window. |
| `journalctl -p warning -b` | Read warning and higher-severity records from the current boot. |
| `journalctl -k -b` | Read kernel records from the current boot. |
| `journalctl -f` | Follow newly written journal records. |
| `journalctl -u UNIT -f` | Follow new records from one unit. |
| `journalctl -o short-iso --no-pager` | Format journal timestamps in an ISO-like form. |
| `journalctl -o json -n 10 --no-pager` | Print ten journal records as JSON. |
| `journalctl --disk-usage` | Report journal storage consumption. |
| `dmesg --level=err,warn` | Read kernel messages classified as errors or warnings. |
| `dmesg -w` | Follow new kernel messages. |
| `logger -t TAG 'MESSAGE'` | Write a tagged message to the system logging service. |
| `tail -F /var/log/syslog` | Follow Debian-style syslog output across rotation, when present. |
| `tail -F /var/log/messages` | Follow a traditional messages log across rotation, when present. |
| `sudo ausearch -m USER_LOGIN -ts today` | Search today's recorded user-login audit events. |
| `sudo ausearch -m AVC -ts recent` | Search recent SELinux access-denial audit events. |
| `sudo aureport --auth` | Summarize authentication audit events. |
| `sudo auditctl -l` | List active audit rules. |
| `sudo logrotate --debug /etc/logrotate.conf` | Preview log rotation decisions without rotating logs. |
