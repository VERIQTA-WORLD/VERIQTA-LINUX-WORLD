| Command | What you can do with it |
| --- | --- |
| `sudo useradd -m -s /bin/bash ACCOUNT` | Create an account with a home directory and Bash shell. |
| `sudo adduser ACCOUNT` | Create an account using the distribution's adduser frontend. |
| `sudo groupadd GROUP` | Create a group. |
| `sudo usermod -aG GROUP ACCOUNT` | Append an account to a supplementary group. |
| `sudo usermod -s /bin/bash ACCOUNT` | Change an account's login shell. |
| `sudo usermod -c 'ACCOUNT DESCRIPTION' ACCOUNT` | Change an account's descriptive comment. |
| `sudo gpasswd -a ACCOUNT GROUP` | Add an account to a group. |
| `sudo gpasswd -d ACCOUNT GROUP` | Remove an account from a supplementary group. |
| `sudo passwd ACCOUNT` | Set or change an account's password interactively. |
| `sudo passwd -S ACCOUNT` | Inspect password status. |
| `sudo chage -l ACCOUNT` | Inspect password-aging settings. |
| `sudo chage -M 90 ACCOUNT` | Set the maximum password age to 90 days. |
| `sudo chage -E YYYY-MM-DD ACCOUNT` | Set the account expiration date. |
| `sudo usermod -L ACCOUNT` | Lock password authentication for an account, without disabling every access method. |
| `sudo usermod -U ACCOUNT` | Unlock an account's password authentication. |
| `sudo groupmod -n NEW_GROUP OLD_GROUP` | Rename a group. |
| `sudo pwck -r` | Check passwd and shadow consistency without changes. |
| `sudo grpck -r` | Check group database consistency without changes. |
| `su - ACCOUNT` | Start a login shell as another account, subject to authentication policy. |
| `sudo -iu ACCOUNT` | Start an authorized login shell as another account through sudo. |
