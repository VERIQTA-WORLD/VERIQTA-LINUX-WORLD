| Command | What you can do with it |
| --- | --- |
| `systemctl --version` | Display the installed systemd version. |
| `systemctl status UNIT --no-pager` | Inspect a unit's current status without a pager. |
| `systemctl show UNIT` | List a unit's properties. |
| `systemctl cat UNIT` | Display a unit file and its drop-ins. |
| `systemctl is-active UNIT` | Query whether a unit is currently active. |
| `systemctl is-enabled UNIT` | Query a unit's enablement state. |
| `systemctl list-units --type=service` | List loaded service units. |
| `systemctl list-unit-files --type=service` | List installed service unit files and enablement. |
| `systemctl list-dependencies UNIT` | Show a unit's dependency tree. |
| `systemctl list-dependencies --reverse UNIT` | Show units that depend on this unit. |
| `systemctl --failed` | List units currently marked failed. |
| `sudo systemctl start UNIT` | Start a unit now. |
| `sudo systemctl stop UNIT` | Stop a unit now. |
| `sudo systemctl restart UNIT` | Stop and start a unit, potentially interrupting service. |
| `sudo systemctl reload UNIT` | Ask a unit to reload supported application configuration. |
| `sudo systemctl enable UNIT` | Configure a unit for activation at boot or through dependencies. |
| `sudo systemctl disable UNIT` | Remove a unit's enablement links without stopping it. |
| `sudo systemctl daemon-reload` | Reload systemd unit definitions without restarting applications. |
| `sudo systemctl edit UNIT` | Create or edit a unit override. |
| `systemctl get-default` | Print the default boot target. |
| `systemctl list-timers --all` | List timers, including inactive ones. |
| `systemctl list-sockets --all` | List loaded socket units and listening endpoints. |
| `systemctl --user list-units` | List units managed by the current user's service manager. |
| `systemctl --user status UNIT` | Inspect a user unit's status. |
| `systemd-analyze` | Summarize boot time. |
| `systemd-analyze blame` | List units by initialization duration. |
| `systemd-analyze critical-chain` | Show timing along the boot critical chain. |
| `systemd-analyze verify UNIT_FILE` | Check unit-file syntax and dependencies. |
