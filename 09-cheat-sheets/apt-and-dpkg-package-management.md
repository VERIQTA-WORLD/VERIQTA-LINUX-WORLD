```bash
apt --version
apt search KEYWORD
apt show PACKAGE
apt list --installed
apt list --upgradable
apt-cache policy PACKAGE
apt-cache depends PACKAGE
apt-cache rdepends PACKAGE
apt-get -s install PACKAGE
apt-get -s upgrade
apt-get -s remove PACKAGE
sudo apt update
sudo apt install PACKAGE
sudo apt reinstall PACKAGE
sudo apt upgrade
sudo apt remove PACKAGE
sudo apt-get check
dpkg-query -W PACKAGE
dpkg -l
dpkg -L PACKAGE
dpkg -S /path/to/FILE
dpkg -s PACKAGE
dpkg --audit
dpkg-deb -I PACKAGE.deb
dpkg-deb -c PACKAGE.deb
apt-mark showmanual
apt-mark showhold
sudo apt-mark hold PACKAGE
sudo apt-mark unhold PACKAGE
```
