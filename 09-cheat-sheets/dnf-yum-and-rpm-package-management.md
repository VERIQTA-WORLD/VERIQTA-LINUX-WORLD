```bash
dnf --version
dnf repolist
dnf search KEYWORD
dnf info PACKAGE
dnf list --installed
dnf list --upgrades
dnf provides /path/to/FILE
dnf repoquery --requires PACKAGE
dnf --assumeno install PACKAGE
dnf --assumeno upgrade
dnf --assumeno remove PACKAGE
sudo dnf install PACKAGE
sudo dnf reinstall PACKAGE
sudo dnf upgrade
sudo dnf remove PACKAGE
yum --version
yum repolist
yum info PACKAGE
rpm -qa
rpm -q PACKAGE
rpm -qi PACKAGE
rpm -ql PACKAGE
rpm -qf /path/to/FILE
rpm -q --requires PACKAGE
rpm -V PACKAGE
rpm -qip PACKAGE.rpm
rpm -qlp PACKAGE.rpm
rpm -K PACKAGE.rpm
```
