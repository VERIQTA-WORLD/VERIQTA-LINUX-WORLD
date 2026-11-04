```bash
systemctl --version
systemctl status UNIT --no-pager
systemctl show UNIT
systemctl cat UNIT
systemctl is-active UNIT
systemctl is-enabled UNIT
systemctl list-units --type=service
systemctl list-unit-files --type=service
systemctl list-dependencies UNIT
systemctl list-dependencies --reverse UNIT
systemctl --failed
sudo systemctl start UNIT
sudo systemctl stop UNIT
sudo systemctl restart UNIT
sudo systemctl reload UNIT
sudo systemctl enable UNIT
sudo systemctl disable UNIT
sudo systemctl daemon-reload
sudo systemctl edit UNIT
systemctl get-default
systemctl list-timers --all
systemctl list-sockets --all
systemctl --user list-units
systemctl --user status UNIT
systemd-analyze
systemd-analyze blame
systemd-analyze critical-chain
systemd-analyze verify UNIT_FILE
```
