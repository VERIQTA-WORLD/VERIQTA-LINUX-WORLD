```bash
getenforce
sestatus
id -Z
ls -lZ -- PATH
ps -eZ
sudo getsebool -a
sudo semanage boolean -l
sudo semanage port -l
sudo semanage fcontext -l
matchpathcon PATH
sudo restorecon -nRv PATH
sudo ausearch -m AVC -ts recent
sudo aa-status
sudo aa-unconfined
getcap -- FILE
getcap -r DIRECTORY
getpcaps PID
capsh --print
cat /proc/PID/attr/current
sudo auditctl -s
sudo auditctl -l
```
