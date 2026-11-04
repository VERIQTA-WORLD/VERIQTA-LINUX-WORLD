```bash
journalctl --list-boots
journalctl -b
journalctl -b -1
journalctl -b -n 100 --no-pager
journalctl -u UNIT -n 100 --no-pager
journalctl -u UNIT --since '1 hour ago'
journalctl --since 'YYYY-MM-DD HH:MM:SS' --until 'YYYY-MM-DD HH:MM:SS'
journalctl -p warning -b
journalctl -k -b
journalctl -f
journalctl -u UNIT -f
journalctl -o short-iso --no-pager
journalctl -o json -n 10 --no-pager
journalctl --disk-usage
dmesg --level=err,warn
dmesg -w
logger -t TAG 'MESSAGE'
tail -F /var/log/syslog
tail -F /var/log/messages
sudo ausearch -m USER_LOGIN -ts today
sudo ausearch -m AVC -ts recent
sudo aureport --auth
sudo auditctl -l
sudo logrotate --debug /etc/logrotate.conf
```
