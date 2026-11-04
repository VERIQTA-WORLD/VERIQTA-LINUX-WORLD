| Command | What you can do with it |
| --- | --- |
| `emerge --version` | Print the Portage version. |
| `emerge --info` | Inspect Portage and system configuration. |
| `emerge --search KEYWORD` | Search Gentoo package names. |
| `emerge --searchdesc KEYWORD` | Search Gentoo package names and descriptions. |
| `emerge --pretend --verbose PACKAGE` | Preview a package merge with detailed information. |
| `emerge --pretend --update --deep --newuse @world` | Preview a deep world-set update accounting for USE changes. |
| `emerge --depclean --pretend` | Preview packages eligible for dependency cleanup. |
| `equery list '*'` | List installed packages with Gentoolkit. |
| `equery files PACKAGE` | List a package's installed files. |
| `equery belongs /path/to/FILE` | Find which package owns a path. |
| `equery depends PACKAGE` | Inspect packages that depend on another package. |
| `equery uses PACKAGE` | Inspect a package's USE flags. |
| `eix KEYWORD` | Search the optional eix package index. |
| `eselect profile list` | List available profiles and the selected profile. |
| `eselect news list` | List Gentoo news items. |
