| Command | What you can do with it |
| --- | --- |
| `sudo -l` | List sudo permissions for your identity. |
| `sudo -ll` | List sudo permissions in a detailed format. |
| `sudo -v` | Validate or refresh cached sudo credentials. |
| `sudo -k` | Invalidate cached sudo credentials. |
| `sudo -n COMMAND` | Attempt an authorized command without an interactive password prompt. |
| `sudo -u ACCOUNT COMMAND` | Run an authorized command as a specified account. |
| `sudo -g GROUP COMMAND` | Run an authorized command with a specified group. |
| `sudo -iu ACCOUNT` | Start an authorized login shell as another account. |
| `sudoedit /etc/CONFIG_FILE` | Edit a protected configuration file through sudoedit. |
| `sudo visudo -c` | Validate sudoers policy syntax. |
| `sudo visudo` | Edit sudoers policy with syntax checking. |
| `sudo visudo -f /etc/sudoers.d/RULE_FILE` | Edit a dedicated sudoers include with syntax checking. |
| `pkcheck --action-id ACTION --process PID` | Check whether a process is authorized for a PolicyKit action. |
| `pkaction` | List available PolicyKit actions. |
