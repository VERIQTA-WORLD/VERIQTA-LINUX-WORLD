| Command | What you can do with it |
| --- | --- |
| `pacman -Ss KEYWORD` | Search Arch repository package metadata. |
| `pacman -Si PACKAGE` | Read repository information for a package. |
| `pacman -Qi PACKAGE` | Read installed package information. |
| `pacman -Ql PACKAGE` | List an installed package's files. |
| `pacman -Qo /path/to/FILE` | Identify the installed package owning a path. |
| `pacman -Q` | List installed packages. |
| `pacman -Qm` | List installed packages absent from configured sync databases. |
| `pacman -Qdt` | List orphaned dependency packages. |
| `sudo pacman -Syu` | Refresh Arch package databases and perform a full upgrade. |
| `sudo pacman -S PACKAGE` | Install a package from current sync databases. |
| `sudo pacman -R PACKAGE` | Remove a package, subject to dependency checks. |
| `zypper repos` | List openSUSE repositories. |
| `zypper search KEYWORD` | Search openSUSE package metadata. |
| `zypper info PACKAGE` | Inspect package information through Zypper. |
| `zypper list-updates` | List available openSUSE package updates. |
| `sudo zypper refresh` | Refresh Zypper repository metadata. |
| `sudo zypper install PACKAGE` | Install a package with Zypper. |
| `sudo zypper update` | Update installed packages with Zypper. |
| `sudo zypper remove PACKAGE` | Remove a package with Zypper. |
| `apk --version` | Print the installed APK version. |
| `apk search KEYWORD` | Search Alpine package metadata. |
| `apk info PACKAGE` | Inspect an Alpine package. |
| `apk info -L PACKAGE` | List an Alpine package's installed files. |
| `apk policy PACKAGE` | Inspect Alpine repository package versions and priorities. |
| `sudo apk update` | Refresh Alpine repository indexes. |
| `sudo apk add PACKAGE` | Install an Alpine package. |
| `sudo apk upgrade` | Upgrade Alpine packages. |
| `sudo apk del PACKAGE` | Remove an Alpine package. |
