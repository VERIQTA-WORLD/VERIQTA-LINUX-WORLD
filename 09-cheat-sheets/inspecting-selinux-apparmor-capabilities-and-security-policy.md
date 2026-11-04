| Command | What you can do with it |
| --- | --- |
| `getenforce` | Print SELinux enforcement mode. |
| `sestatus` | Inspect SELinux status and policy information. |
| `id -Z` | Print the current SELinux security context. |
| `ls -lZ -- PATH` | Inspect file SELinux labels. |
| `ps -eZ` | Inspect process SELinux contexts. |
| `sudo getsebool -a` | List SELinux boolean values. |
| `sudo semanage boolean -l` | List SELinux boolean policy settings. |
| `sudo semanage port -l` | List SELinux port-label mappings. |
| `sudo semanage fcontext -l` | List SELinux file-context mappings. |
| `matchpathcon PATH` | Look up the policy's expected context for a path. |
| `sudo restorecon -nRv PATH` | Preview recursive SELinux relabeling without changing labels. |
| `sudo ausearch -m AVC -ts recent` | Inspect recent SELinux access-denial audit events. |
| `sudo aa-status` | Inspect AppArmor profiles and enforcement state. |
| `sudo aa-unconfined` | Find network-facing processes without AppArmor confinement where supported. |
| `getcap -- FILE` | Inspect capabilities attached to a file. |
| `getcap -r DIRECTORY` | Inspect file capabilities beneath a directory. |
| `getpcaps PID` | Inspect a process's capabilities. |
| `capsh --print` | Display current capability and privilege settings. |
| `cat /proc/PID/attr/current` | Read a process's current security context. |
| `sudo auditctl -s` | Inspect the audit subsystem's status. |
| `sudo auditctl -l` | List installed audit rules. |
