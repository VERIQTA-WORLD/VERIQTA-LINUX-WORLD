| Command | What you can do with it |
| --- | --- |
| `apt --version` | Display the installed APT version. |
| `apt search KEYWORD` | Search available package metadata. |
| `apt show PACKAGE` | Read a package's available metadata. |
| `apt list --installed` | List installed packages through APT. |
| `apt list --upgradable` | List packages with available upgrades. |
| `apt-cache policy PACKAGE` | Inspect installed and candidate versions and repository priorities. |
| `apt-cache depends PACKAGE` | Inspect a package's dependencies. |
| `apt-cache rdepends PACKAGE` | Inspect packages that depend on the named package. |
| `apt-get -s install PACKAGE` | Simulate an install without applying a package transaction. |
| `apt-get -s upgrade` | Simulate an upgrade without applying it. |
| `apt-get -s remove PACKAGE` | Simulate package removal without applying it. |
| `sudo apt update` | Refresh repository metadata without installing updates. |
| `sudo apt install PACKAGE` | Install a package and dependencies after reviewing the proposal. |
| `sudo apt reinstall PACKAGE` | Reinstall an installed package. |
| `sudo apt upgrade` | Upgrade packages while avoiding removals of installed packages. |
| `sudo apt remove PACKAGE` | Remove a package, usually retaining its configuration files. |
| `sudo apt-get check` | Check package dependency consistency. |
| `dpkg-query -W PACKAGE` | Query the installed package database for a package. |
| `dpkg -l` | List installed and other known package states. |
| `dpkg -L PACKAGE` | List files recorded as belonging to a package. |
| `dpkg -S /path/to/FILE` | Find which installed package owns a path. |
| `dpkg -s PACKAGE` | Show installed package status and metadata. |
| `dpkg --audit` | Report incomplete or inconsistent package states. |
| `dpkg-deb -I PACKAGE.deb` | Inspect a Debian package archive's control metadata. |
| `dpkg-deb -c PACKAGE.deb` | List a Debian package archive's contents. |
| `apt-mark showmanual` | List packages marked as manually installed. |
| `apt-mark showhold` | List packages held from automatic changes. |
| `sudo apt-mark hold PACKAGE` | Place a package on hold. |
| `sudo apt-mark unhold PACKAGE` | Remove a package hold. |
