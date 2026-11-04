| Command | What you can do with it |
| --- | --- |
| `whoami` | Print the effective account name. |
| `id` | Show the current UID, GIDs and group memberships. |
| `id ACCOUNT` | Inspect a named account's identity. |
| `id -u ACCOUNT` | Print an account's numeric UID. |
| `id -nG ACCOUNT` | Print an account's group names. |
| `groups ACCOUNT` | List an account's group memberships. |
| `getent passwd` | List passwd entries returned by configured identity services. |
| `getent passwd ACCOUNT` | Resolve one account through configured identity services. |
| `getent group` | List groups returned by configured identity services. |
| `getent group GROUP` | Resolve one group. |
| `getent shadow ACCOUNT` | Query protected password-aging data when authorized. |
| `who` | List recorded login sessions. |
| `who -b` | Show the recorded last boot time. |
| `w` | Show logged-in sessions and their activity. |
| `users` | Print account names recorded as logged in. |
| `logname` | Print the login account name. |
| `last -n 20` | Show the latest 20 recorded login-history entries. |
| `lastlog` | Show recorded last-login information where supported. |
| `loginctl list-sessions` | List systemd login sessions. |
| `loginctl list-users` | List users known to systemd-logind. |
| `loginctl show-user ACCOUNT` | Inspect a user's logind properties. |
| `loginctl session-status` | Inspect the current logind session. |
