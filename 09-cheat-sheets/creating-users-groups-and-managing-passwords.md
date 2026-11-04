```bash
sudo useradd -m -s /bin/bash ACCOUNT
sudo adduser ACCOUNT
sudo groupadd GROUP
sudo usermod -aG GROUP ACCOUNT
sudo usermod -s /bin/bash ACCOUNT
sudo usermod -c 'ACCOUNT DESCRIPTION' ACCOUNT
sudo gpasswd -a ACCOUNT GROUP
sudo gpasswd -d ACCOUNT GROUP
sudo passwd ACCOUNT
sudo passwd -S ACCOUNT
sudo chage -l ACCOUNT
sudo chage -M 90 ACCOUNT
sudo chage -E YYYY-MM-DD ACCOUNT
sudo usermod -L ACCOUNT
sudo usermod -U ACCOUNT
sudo groupmod -n NEW_GROUP OLD_GROUP
sudo pwck -r
sudo grpck -r
su - ACCOUNT
sudo -iu ACCOUNT
```
