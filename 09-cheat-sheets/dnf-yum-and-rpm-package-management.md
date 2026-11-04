| Command | What you can do with it |
| --- | --- |
| `dnf --version` | Identify the installed DNF implementation and version. |
| `dnf repolist` | List enabled repositories. |
| `dnf search KEYWORD` | Search package metadata. |
| `dnf info PACKAGE` | Inspect package information. |
| `dnf list --installed` | List installed packages. |
| `dnf list --upgrades` | List packages with available upgrades. |
| `dnf provides /path/to/FILE` | Find packages that provide a path. |
| `dnf repoquery --requires PACKAGE` | Inspect package requirements using repoquery. |
| `dnf --assumeno install PACKAGE` | Resolve a proposed install and decline transaction confirmation. |
| `dnf --assumeno upgrade` | Resolve proposed upgrades and decline confirmation. |
| `dnf --assumeno remove PACKAGE` | Resolve proposed removal and decline confirmation. |
| `sudo dnf install PACKAGE` | Install a package and required dependencies. |
| `sudo dnf reinstall PACKAGE` | Reinstall a package. |
| `sudo dnf upgrade` | Upgrade packages after reviewing the proposed transaction. |
| `sudo dnf remove PACKAGE` | Remove a package and any proposed dependent packages. |
| `yum --version` | Identify the available yum implementation. |
| `yum repolist` | List repositories through yum. |
| `yum info PACKAGE` | Inspect a package through yum. |
| `rpm -qa` | List installed RPM package names and versions. |
| `rpm -q PACKAGE` | Query whether a package is installed. |
| `rpm -qi PACKAGE` | Inspect installed package metadata. |
| `rpm -ql PACKAGE` | List files recorded for an installed package. |
| `rpm -qf /path/to/FILE` | Find the installed package that owns a path. |
| `rpm -q --requires PACKAGE` | Inspect installed package requirements. |
| `rpm -V PACKAGE` | Verify installed files against recorded RPM metadata. |
| `rpm -qip PACKAGE.rpm` | Inspect a local RPM file's metadata. |
| `rpm -qlp PACKAGE.rpm` | List a local RPM file's contents. |
| `rpm -K PACKAGE.rpm` | Check an RPM file's available signatures and digests. |
