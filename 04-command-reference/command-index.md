# Command and task index

Find the task first, then open its reference for assumptions, options, examples and verification. This is a curated Linux administration reference, not a list of every available executable.

## Files and directories

| Command or syntax | Purpose | Reference |
| --- | --- | --- |
| `pwd -P` | Print the physical current directory, resolving symbolic links. | [Navigate and inspect directories](files-and-directories/navigation-commands.md) |
| `ls -lah` | List ordinary and hidden entries with metadata and readable sizes. | [Navigate and inspect directories](files-and-directories/navigation-commands.md) |
| `cd -- PATH` | Change this shell’s directory; quote paths containing spaces. | [Navigate and inspect directories](files-and-directories/navigation-commands.md) |
| `cd ..` | Move to the parent directory. | [Navigate and inspect directories](files-and-directories/navigation-commands.md) |
| `cd -` | Return to the previous working directory. | [Navigate and inspect directories](files-and-directories/navigation-commands.md) |
| `realpath -- PATH` | Resolve a path; GNU utility, availability varies. | [Navigate and inspect directories](files-and-directories/navigation-commands.md) |
| `stat -- PATH` | Inspect ownership, mode, size and timestamps. | [Navigate and inspect directories](files-and-directories/navigation-commands.md) |
| `mkdir -p -- PATH` | Create a directory and missing parents. | [Create, copy, move and remove files](files-and-directories/file-management-commands.md) |
| `touch -- FILE` | Create an empty file or update an existing file’s timestamps. | [Create, copy, move and remove files](files-and-directories/file-management-commands.md) |
| `cp -i -- SOURCE DEST` | Copy; ask before replacing an existing destination. | [Create, copy, move and remove files](files-and-directories/file-management-commands.md) |
| `cp -a -- SOURCE DEST` | Copy a tree preserving attributes where permissions allow. | [Create, copy, move and remove files](files-and-directories/file-management-commands.md) |
| `mv -i -- SOURCE DEST` | Move or rename; ask before replacement. | [Create, copy, move and remove files](files-and-directories/file-management-commands.md) |
| `ln -s -- TARGET LINK` | Create a symbolic link; relative targets are resolved from the link’s parent. | [Create, copy, move and remove files](files-and-directories/file-management-commands.md) |
| `rm -i -- FILE` | Remove a file with confirmation; no automatic undo. | [Create, copy, move and remove files](files-and-directories/file-management-commands.md) |
| `rmdir -- DIR` | Remove an empty directory. | [Create, copy, move and remove files](files-and-directories/file-management-commands.md) |
| `find PATH -type f -name PATTERN` | Find regular files matching a case-sensitive shell pattern. | [Find files by name, type and metadata](files-and-directories/file-search-commands.md) |
| `find PATH -type d` | Find directories. | [Find files by name, type and metadata](files-and-directories/file-search-commands.md) |
| `find PATH -iname PATTERN` | Match names without case sensitivity; GNU extension. | [Find files by name, type and metadata](files-and-directories/file-search-commands.md) |
| `find PATH -type f -size +100M` | Find regular files larger than 100 units of 1 MiB. | [Find files by name, type and metadata](files-and-directories/file-search-commands.md) |
| `find PATH -type f -mtime +7` | Match files with rounded-down age in days greater than 7. | [Find files by name, type and metadata](files-and-directories/file-search-commands.md) |
| `find PATH -type f -exec COMMAND {} +` | Pass found paths as arguments in batches; handles spaces. | [Find files by name, type and metadata](files-and-directories/file-search-commands.md) |

## Text processing

| Command or syntax | Purpose | Reference |
| --- | --- | --- |
| `grep -nF -- TEXT FILE` | Print line numbers and lines containing literal text. | [Search text with grep](text-processing/grep-reference.md) |
| `grep -nE -- PATTERN FILE` | Use extended regular expressions. | [Search text with grep](text-processing/grep-reference.md) |
| `grep -i -- PATTERN FILE` | Ignore letter case. | [Search text with grep](text-processing/grep-reference.md) |
| `grep -v -- PATTERN FILE` | Select nonmatching lines. | [Search text with grep](text-processing/grep-reference.md) |
| `grep -rIl -- TEXT DIR` | Recursively list matching text-file names, skipping binary files. | [Search text with grep](text-processing/grep-reference.md) |
| `grep -c -- PATTERN FILE` | Count matching lines, not every individual occurrence. | [Search text with grep](text-processing/grep-reference.md) |
| `sed -n '1,5p' FILE` | Print only lines 1 through 5. | [Transform text with sed](text-processing/sed-reference.md) |
| `sed 's/old/new/' FILE` | Replace the first match on each line in output. | [Transform text with sed](text-processing/sed-reference.md) |
| `sed 's/old/new/g' FILE` | Replace every match on each line in output. | [Transform text with sed](text-processing/sed-reference.md) |
| `sed '/^#/d' FILE` | Omit lines beginning with # from output. | [Transform text with sed](text-processing/sed-reference.md) |
| `sed -i.bak 's/old/new/g' FILE` | GNU form: edit a file and retain a .bak copy; changes source data. | [Transform text with sed](text-processing/sed-reference.md) |
| `awk '{print $1}' FILE` | Print the first whitespace-separated field. | [Select fields and summarize with awk](text-processing/awk-reference.md) |
| `awk -F: '{print $1, $3}' /etc/passwd` | Print account names and numeric UIDs from the local account file. | [Select fields and summarize with awk](text-processing/awk-reference.md) |
| `awk 'NR > 1 {print}' FILE` | Skip a header record. | [Select fields and summarize with awk](text-processing/awk-reference.md) |
| `awk '$2 > 10 {print $1}' FILE` | Print names whose second field exceeds 10. | [Select fields and summarize with awk](text-processing/awk-reference.md) |
| `awk '{s += $2} END {print s}' FILE` | Sum the second field across records. | [Select fields and summarize with awk](text-processing/awk-reference.md) |
| `COMMAND > FILE` | Replace FILE with stdout; creates or truncates it. | [Pipes, redirection and exit status](text-processing/pipes-and-redirection.md) |
| `COMMAND >> FILE` | Append stdout; creates FILE if needed. | [Pipes, redirection and exit status](text-processing/pipes-and-redirection.md) |
| `COMMAND 2> ERRORS` | Write standard error separately. | [Pipes, redirection and exit status](text-processing/pipes-and-redirection.md) |
| `COMMAND > FILE 2>&1` | Send stdout and stderr to the same file; order matters. | [Pipes, redirection and exit status](text-processing/pipes-and-redirection.md) |
| `A \| B` | Pipe stdout from A to B; stderr stays on the terminal. | [Pipes, redirection and exit status](text-processing/pipes-and-redirection.md) |
| `set -o pipefail` | Make a pipeline fail if any component fails; status is the rightmost failure. | [Pipes, redirection and exit status](text-processing/pipes-and-redirection.md) |
| `A && B` | Run B only if A succeeds. | [Pipes, redirection and exit status](text-processing/pipes-and-redirection.md) |
| `A \|\| B` | Run B only if A fails. | [Pipes, redirection and exit status](text-processing/pipes-and-redirection.md) |

## Users and permissions

| Command or syntax | Purpose | Reference |
| --- | --- | --- |
| `whoami` | Print the effective account name. | [Inspect users and groups](users-and-permissions/user-and-group-commands.md) |
| `id` | Show current UID, primary group and supplementary groups. | [Inspect users and groups](users-and-permissions/user-and-group-commands.md) |
| `id ACCOUNT` | Inspect a named identity. | [Inspect users and groups](users-and-permissions/user-and-group-commands.md) |
| `getent passwd ACCOUNT` | Resolve through configured name services, not only /etc/passwd. | [Inspect users and groups](users-and-permissions/user-and-group-commands.md) |
| `getent group GROUP` | Resolve a group; listed members may omit users whose primary group is this group. | [Inspect users and groups](users-and-permissions/user-and-group-commands.md) |
| `who` | Show login sessions recorded in utmp; may be empty in containers. | [Inspect users and groups](users-and-permissions/user-and-group-commands.md) |
| `sudo useradd -m ACCOUNT` | Administrative syntax: create an account and home directory. | [Inspect users and groups](users-and-permissions/user-and-group-commands.md) |
| `sudo usermod -aG GROUP ACCOUNT` | Administrative syntax: append group membership; omitting -a replaces supplementary groups. | [Inspect users and groups](users-and-permissions/user-and-group-commands.md) |
| `ls -ld -- PATH` | Inspect the object itself, including a directory’s mode. | [Understand modes, ownership and access](users-and-permissions/permissions-and-ownership.md) |
| `stat -c "%a %U %G" -- PATH` | Print octal mode, owner and group (GNU syntax). | [Understand modes, ownership and access](users-and-permissions/permissions-and-ownership.md) |
| `chmod u=rw,go= -- FILE` | Give only the owner read and write access. | [Understand modes, ownership and access](users-and-permissions/permissions-and-ownership.md) |
| `chmod 640 -- FILE` | Owner read/write, group read, others no access. | [Understand modes, ownership and access](users-and-permissions/permissions-and-ownership.md) |
| `chmod 750 -- DIR` | Owner full access; group list/traverse; others none. | [Understand modes, ownership and access](users-and-permissions/permissions-and-ownership.md) |
| `chown OWNER:GROUP PATH` | Change ownership subject to privilege checks. | [Understand modes, ownership and access](users-and-permissions/permissions-and-ownership.md) |
| `umask` | Show the permission mask applied when creating new objects. | [Understand modes, ownership and access](users-and-permissions/permissions-and-ownership.md) |
| `getfacl -- PATH` | Inspect ACLs, if installed. | [Understand modes, ownership and access](users-and-permissions/permissions-and-ownership.md) |
| `sudo -l` | List permissions granted to your identity; may authenticate. | [Use sudo deliberately](users-and-permissions/sudo-reference.md) |
| `sudo -v` | Validate or refresh cached credentials without running a target command. | [Use sudo deliberately](users-and-permissions/sudo-reference.md) |
| `sudo -k` | Invalidate cached credentials for the applicable session. | [Use sudo deliberately](users-and-permissions/sudo-reference.md) |
| `sudo -u ACCOUNT COMMAND` | Run one authorized command as another account. | [Use sudo deliberately](users-and-permissions/sudo-reference.md) |
| `sudoedit /path/to/file` | Edit via sudo policy using an unprivileged editor; the resulting file change is privileged. | [Use sudo deliberately](users-and-permissions/sudo-reference.md) |
| `sudo visudo` | Edit sudo policy with syntax checking; a bad policy can break administrative access. | [Use sudo deliberately](users-and-permissions/sudo-reference.md) |

## Processes and services

| Command or syntax | Purpose | Reference |
| --- | --- | --- |
| `ps -eo pid,ppid,user,stat,comm` | Snapshot process IDs, parents, owners, state and command names. | [Observe processes and send signals](processes-and-services/process-management-commands.md) |
| `pgrep -a -u USER PATTERN` | Find matching process names for one owner; inspect results before acting. | [Observe processes and send signals](processes-and-services/process-management-commands.md) |
| `ps -p PID -o pid,ppid,stat,etime,args` | Inspect a specific PID; args may expose secrets. | [Observe processes and send signals](processes-and-services/process-management-commands.md) |
| `top` | Interactive process view; q exits. | [Observe processes and send signals](processes-and-services/process-management-commands.md) |
| `kill -TERM PID` | Request graceful termination; successful delivery is not proof of exit. | [Observe processes and send signals](processes-and-services/process-management-commands.md) |
| `kill -KILL PID` | Force termination; can lose in-memory state and skip cleanup. | [Observe processes and send signals](processes-and-services/process-management-commands.md) |
| `jobs -l` | List jobs belonging to this shell. | [Observe processes and send signals](processes-and-services/process-management-commands.md) |
| `wait PID` | Wait for this shell’s child and collect its exit status. | [Observe processes and send signals](processes-and-services/process-management-commands.md) |
| `systemctl --failed` | List units currently marked failed. | [Inspect and control systemd services](processes-and-services/systemctl-reference.md) |
| `systemctl list-unit-files --type=service` | List installed service unit files and enablement. | [Inspect and control systemd services](processes-and-services/systemctl-reference.md) |
| `systemctl status UNIT --no-pager` | Show recent status; a nonzero exit may mean inactive or failed. | [Inspect and control systemd services](processes-and-services/systemctl-reference.md) |
| `systemctl cat UNIT` | Show unit definition and drop-ins; may expose configuration details. | [Inspect and control systemd services](processes-and-services/systemctl-reference.md) |
| `systemctl is-active UNIT` | Query current activity. | [Inspect and control systemd services](processes-and-services/systemctl-reference.md) |
| `systemctl is-enabled UNIT` | Query boot enablement; static units can still be activated by dependencies. | [Inspect and control systemd services](processes-and-services/systemctl-reference.md) |
| `sudo systemctl start UNIT` | Start now; does not enable at boot. | [Inspect and control systemd services](processes-and-services/systemctl-reference.md) |
| `sudo systemctl enable UNIT` | Configure boot/dependency activation; does not start now. | [Inspect and control systemd services](processes-and-services/systemctl-reference.md) |
| `sudo systemctl restart UNIT` | Stop then start, interrupting service. | [Inspect and control systemd services](processes-and-services/systemctl-reference.md) |
| `sudo systemctl daemon-reload` | Reload unit definitions; does not reload application configuration. | [Inspect and control systemd services](processes-and-services/systemctl-reference.md) |
| `journalctl -b --no-pager -n 50` | Read the last 50 records for the current boot. | [Read systemd journal evidence](processes-and-services/journalctl-reference.md) |
| `journalctl --list-boots` | Show boots retained in this journal. | [Read systemd journal evidence](processes-and-services/journalctl-reference.md) |
| `journalctl -b -1 --no-pager` | Inspect the previous retained boot. | [Read systemd journal evidence](processes-and-services/journalctl-reference.md) |
| `journalctl -u UNIT --since "1 hour ago"` | Filter one unit by time. | [Read systemd journal evidence](processes-and-services/journalctl-reference.md) |
| `journalctl -p warning -b` | Show warning and more severe events this boot. | [Read systemd journal evidence](processes-and-services/journalctl-reference.md) |
| `journalctl -k -b` | Show kernel records this boot. | [Read systemd journal evidence](processes-and-services/journalctl-reference.md) |
| `journalctl -f` | Follow new records; Ctrl-C stops the viewer. | [Read systemd journal evidence](processes-and-services/journalctl-reference.md) |
| `journalctl --disk-usage` | Report journal storage usage. | [Read systemd journal evidence](processes-and-services/journalctl-reference.md) |

## Networking

| Command or syntax | Purpose | Reference |
| --- | --- | --- |
| `ip -br link` | Summarize interfaces and link state. | [Inspect interfaces, addresses and routes](networking/ip-command-reference.md) |
| `ip -br address` | Show interface addresses including prefixes. | [Inspect interfaces, addresses and routes](networking/ip-command-reference.md) |
| `ip route show` | Show IPv4 routing entries. | [Inspect interfaces, addresses and routes](networking/ip-command-reference.md) |
| `ip -6 route show` | Show IPv6 routing entries. | [Inspect interfaces, addresses and routes](networking/ip-command-reference.md) |
| `ip route get ADDRESS` | Ask how the kernel would route to a numeric destination; sends no probe. | [Inspect interfaces, addresses and routes](networking/ip-command-reference.md) |
| `ip neigh show` | Show neighbor cache; absence does not by itself prove failure. | [Inspect interfaces, addresses and routes](networking/ip-command-reference.md) |
| `ip -s link` | Show per-interface traffic and error counters. | [Inspect interfaces, addresses and routes](networking/ip-command-reference.md) |
| `ss -ltn` | List listening TCP sockets using numeric addresses and ports. | [Inspect listening and connected sockets](networking/ss-command-reference.md) |
| `ss -lun` | List bound UDP sockets; UDP does not have TCP’s handshake states. | [Inspect listening and connected sockets](networking/ss-command-reference.md) |
| `ss -tn state established` | List established TCP connections. | [Inspect listening and connected sockets](networking/ss-command-reference.md) |
| `ss -ltnp` | Include process details where permitted. | [Inspect listening and connected sockets](networking/ss-command-reference.md) |
| `ss -ltn 'sport = :22'` | Filter listeners by local port 22. | [Inspect listening and connected sockets](networking/ss-command-reference.md) |
| `ss -s` | Summarize socket counts. | [Inspect listening and connected sockets](networking/ss-command-reference.md) |
| `getent ahosts example.com` | Resolve through configured name services as many applications do. | [Check name resolution](networking/dns-troubleshooting-commands.md) |
| `dig example.com A` | Query IPv4 DNS data; inspect status and sections. | [Check name resolution](networking/dns-troubleshooting-commands.md) |
| `dig example.com AAAA` | Query IPv6 DNS data. | [Check name resolution](networking/dns-troubleshooting-commands.md) |
| `dig example.com MX` | Inspect mail-exchanger records. | [Check name resolution](networking/dns-troubleshooting-commands.md) |
| `dig +time=2 +tries=1 example.com A` | Bound the time spent waiting for a DNS response. | [Check name resolution](networking/dns-troubleshooting-commands.md) |
| `resolvectl status` | Inspect systemd-resolved per-link DNS state when available. | [Check name resolution](networking/dns-troubleshooting-commands.md) |
| `cat /etc/resolv.conf` | Read resolver configuration; this may be a managed symlink. | [Check name resolution](networking/dns-troubleshooting-commands.md) |
| `ssh USER@HOST` | Connect after verifying the expected host identity. | [Use SSH and inspect connection settings](networking/ssh-reference.md) |
| `ssh -p PORT USER@HOST` | Use a nondefault TCP port. | [Use SSH and inspect connection settings](networking/ssh-reference.md) |
| `ssh -i KEY USER@HOST` | Offer a specified private identity file. | [Use SSH and inspect connection settings](networking/ssh-reference.md) |
| `ssh -G HOST` | Print evaluated client configuration without opening a remote session. | [Use SSH and inspect connection settings](networking/ssh-reference.md) |
| `ssh -v USER@HOST` | Emit diagnostic connection details; redact before sharing. | [Use SSH and inspect connection settings](networking/ssh-reference.md) |
| `ssh-keygen -lf PUBLIC_KEY_FILE` | Print a key fingerprint. | [Use SSH and inspect connection settings](networking/ssh-reference.md) |
| `sftp USER@HOST` | Open an encrypted file-transfer session. | [Use SSH and inspect connection settings](networking/ssh-reference.md) |
| `ssh -N -L 127.0.0.1:8080:127.0.0.1:80 USER@HOST` | Forward a local loopback port to port 80 as seen by the remote host; changes local access paths. | [Use SSH and inspect connection settings](networking/ssh-reference.md) |

## Storage

| Command or syntax | Purpose | Reference |
| --- | --- | --- |
| `lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS` | Show storage topology with explicit columns; older releases may need MOUNTPOINT singular. | [Inspect disks, filesystems and capacity](storage/disk-and-filesystem-commands.md) |
| `df -hT /` | Report mounted filesystem type, capacity and usage for /. | [Inspect disks, filesystems and capacity](storage/disk-and-filesystem-commands.md) |
| `df -i /` | Report inode usage; free bytes do not guarantee free inodes. | [Inspect disks, filesystems and capacity](storage/disk-and-filesystem-commands.md) |
| `du -sh -- PATH` | Sum allocated file space beneath a path. | [Inspect disks, filesystems and capacity](storage/disk-and-filesystem-commands.md) |
| `du -xhd1 -- PATH` | Show one directory level without crossing filesystem boundaries (GNU syntax). | [Inspect disks, filesystems and capacity](storage/disk-and-filesystem-commands.md) |
| `findmnt --target PATH` | Identify the filesystem that contains a path. | [Inspect disks, filesystems and capacity](storage/disk-and-filesystem-commands.md) |
| `sudo blkid` | Probe block-device filesystem identities; elevated read-only inspection. | [Inspect disks, filesystems and capacity](storage/disk-and-filesystem-commands.md) |
| `findmnt --target /` | Find the filesystem containing the root path. | [Inspect mounts and understand mount syntax](storage/mount-reference.md) |
| `findmnt --mountpoint /` | Match an exact mount point. | [Inspect mounts and understand mount syntax](storage/mount-reference.md) |
| `findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS` | List mount sources and options. | [Inspect mounts and understand mount syntax](storage/mount-reference.md) |
| `findmnt --fstab` | Read configured fstab entries; does not mount them. | [Inspect mounts and understand mount syntax](storage/mount-reference.md) |
| `mount -t TYPE -o OPTIONS DEVICE DIRECTORY` | Administrative syntax: attach a filesystem to a directory. | [Inspect mounts and understand mount syntax](storage/mount-reference.md) |
| `umount DIRECTORY` | Administrative syntax: detach a filesystem; may fail while busy. | [Inspect mounts and understand mount syntax](storage/mount-reference.md) |
| `mountpoint DIRECTORY` | Check whether a directory is itself a mount point. | [Inspect mounts and understand mount syntax](storage/mount-reference.md) |
| `sudo pvs -o pv_name,vg_name,pv_size,pv_free` | Map physical volumes to groups and free extents. | [Read LVM layout and capacity](storage/lvm-reference.md) |
| `sudo vgs -o vg_name,vg_size,vg_free` | Show group capacity and unallocated space. | [Read LVM layout and capacity](storage/lvm-reference.md) |
| `sudo lvs -a -o lv_name,vg_name,lv_size,lv_attr` | Show logical volumes including hidden internal LVs. | [Read LVM layout and capacity](storage/lvm-reference.md) |
| `sudo lvs -a -o lv_name,vg_name,data_percent,metadata_percent` | Inspect thin-pool usage where applicable. | [Read LVM layout and capacity](storage/lvm-reference.md) |
| `lsblk -f` | Relate logical devices to filesystem types and mount points. | [Read LVM layout and capacity](storage/lvm-reference.md) |
| `sudo vgcfgbackup` | Write an LVM metadata backup; does not back up file data. | [Read LVM layout and capacity](storage/lvm-reference.md) |

## Packages

| Command or syntax | Purpose | Reference |
| --- | --- | --- |
| `apt search NAME` | Search repository metadata. | [Inspect and manage APT packages](packages/apt-reference.md) |
| `apt show PACKAGE` | Describe an available package. | [Inspect and manage APT packages](packages/apt-reference.md) |
| `apt-cache policy PACKAGE` | Show installed/candidate versions and repository priorities. | [Inspect and manage APT packages](packages/apt-reference.md) |
| `dpkg-query -W PACKAGE` | Inspect the local package database. | [Inspect and manage APT packages](packages/apt-reference.md) |
| `sudo apt update` | Refresh metadata; does not install upgrades. | [Inspect and manage APT packages](packages/apt-reference.md) |
| `apt-get -s install PACKAGE` | Simulate an installation using current metadata; no package transaction. | [Inspect and manage APT packages](packages/apt-reference.md) |
| `sudo apt install PACKAGE` | Install with dependencies after transaction review. | [Inspect and manage APT packages](packages/apt-reference.md) |
| `sudo apt upgrade` | Upgrade without removing installed packages. | [Inspect and manage APT packages](packages/apt-reference.md) |
| `sudo apt full-upgrade` | May remove installed packages to resolve dependencies. | [Inspect and manage APT packages](packages/apt-reference.md) |
| `sudo apt remove PACKAGE` | Remove the package, usually retaining configuration; purge also removes package-managed configuration. | [Inspect and manage APT packages](packages/apt-reference.md) |
| `dnf --version` | Identify installed implementation and version. | [Inspect and manage DNF packages](packages/dnf-reference.md) |
| `dnf repolist` | List enabled repositories. | [Inspect and manage DNF packages](packages/dnf-reference.md) |
| `dnf info PACKAGE` | Describe package metadata. | [Inspect and manage DNF packages](packages/dnf-reference.md) |
| `dnf search NAME` | Search package names and descriptions. | [Inspect and manage DNF packages](packages/dnf-reference.md) |
| `rpm -q PACKAGE` | Query installed RPM state without contacting repositories. | [Inspect and manage DNF packages](packages/dnf-reference.md) |
| `dnf --assumeno install PACKAGE` | Resolve a proposed install and decline confirmation; may refresh cache. | [Inspect and manage DNF packages](packages/dnf-reference.md) |
| `sudo dnf install PACKAGE` | Install package and required dependencies. | [Inspect and manage DNF packages](packages/dnf-reference.md) |
| `sudo dnf upgrade` | Resolve system updates; review before confirming. | [Inspect and manage DNF packages](packages/dnf-reference.md) |
| `sudo dnf remove PACKAGE` | Remove a package and possibly dependent packages. | [Inspect and manage DNF packages](packages/dnf-reference.md) |

## Performance

| Command or syntax | Purpose | Reference |
| --- | --- | --- |
| `uptime` | Show load averages over 1, 5 and 15 minutes. | [Read CPU and memory pressure](performance/cpu-and-memory-commands.md) |
| `nproc` | Show processing units available to the current process, subject to tool/version behavior. | [Read CPU and memory pressure](performance/cpu-and-memory-commands.md) |
| `free -h` | Show memory accounting; focus on available rather than only free. | [Read CPU and memory pressure](performance/cpu-and-memory-commands.md) |
| `vmstat 1 5` | Take five reports; first includes since-boot CPU/I/O averages. | [Read CPU and memory pressure](performance/cpu-and-memory-commands.md) |
| `ps -eo pid,comm,%cpu,%mem --sort=-%cpu` | Sort lifetime CPU averages; not an instantaneous interval measurement. | [Read CPU and memory pressure](performance/cpu-and-memory-commands.md) |
| `pidstat -u -r 1 5` | Sample per-task CPU and memory over intervals, if installed. | [Read CPU and memory pressure](performance/cpu-and-memory-commands.md) |
| `cat /proc/pressure/memory` | Show memory-stall pressure if supported by the kernel. | [Read CPU and memory pressure](performance/cpu-and-memory-commands.md) |
| `iostat -xz 1 5` | Show extended device statistics; suppress inactive devices. | [Observe disk I/O and latency](performance/disk-io-commands.md) |
| `pidstat -d 1 5` | Sample per-task I/O accounting where permitted. | [Observe disk I/O and latency](performance/disk-io-commands.md) |
| `vmstat 1 5` | Compare blocked tasks, block I/O and CPU wait. | [Observe disk I/O and latency](performance/disk-io-commands.md) |
| `lsblk -o NAME,TYPE,SIZE,MOUNTPOINTS` | Relate reported devices to storage topology. | [Observe disk I/O and latency](performance/disk-io-commands.md) |
| `cat /proc/pressure/io` | Inspect I/O stall pressure where supported. | [Observe disk I/O and latency](performance/disk-io-commands.md) |
| `sudo iotop -o` | Interactive view of tasks doing I/O; implementation/permissions vary, q exits. | [Observe disk I/O and latency](performance/disk-io-commands.md) |
| `date -Is` | Record sample time and offset (GNU date). | [A first performance investigation](performance/performance-investigation-cheat-sheet.md) |
| `uptime` | Observe load trend and uptime context. | [A first performance investigation](performance/performance-investigation-cheat-sheet.md) |
| `free -h` | Inspect available memory and swap accounting. | [A first performance investigation](performance/performance-investigation-cheat-sheet.md) |
| `vmstat 1 5` | Collect interval CPU, run queue and paging evidence. | [A first performance investigation](performance/performance-investigation-cheat-sheet.md) |
| `df -hT /` | Check capacity on the root filesystem; repeat for the application’s actual data path. | [A first performance investigation](performance/performance-investigation-cheat-sheet.md) |
| `df -i /` | Check inode exhaustion. | [A first performance investigation](performance/performance-investigation-cheat-sheet.md) |
| `ss -s` | Summarize connections. | [A first performance investigation](performance/performance-investigation-cheat-sheet.md) |
| `journalctl -b -p warning -n 50 --no-pager` | Inspect recent warnings, where available. | [A first performance investigation](performance/performance-investigation-cheat-sheet.md) |

## Security

| Command or syntax | Purpose | Reference |
| --- | --- | --- |
| `id` | Show your effective identity and groups. | [Inspect account and access evidence](security/access-audit-commands.md) |
| `getent passwd` | Enumerate accounts exposed by configured identity sources; enumeration may be incomplete. | [Inspect account and access evidence](security/access-audit-commands.md) |
| `getent group sudo` | Inspect one common Debian-family administrator group. | [Inspect account and access evidence](security/access-audit-commands.md) |
| `getent group wheel` | Inspect one common RPM-family administrator group. | [Inspect account and access evidence](security/access-audit-commands.md) |
| `sudo -l` | Inspect effective sudo policy; group membership alone is not proof. | [Inspect account and access evidence](security/access-audit-commands.md) |
| `who` | Inspect recorded login sessions; records may be absent. | [Inspect account and access evidence](security/access-audit-commands.md) |
| `last -n 10` | Read recent wtmp records if the utility and database exist. | [Inspect account and access evidence](security/access-audit-commands.md) |
| `journalctl -u ssh -u sshd --since today` | Look for SSH service events under common names; discover the actual unit on your host. | [Inspect account and access evidence](security/access-audit-commands.md) |
| `sudo ufw status verbose` | UFW: inspect status and rules. | [Inspect firewall policy and plan changes](security/firewall-reference.md) |
| `sudo ufw status numbered` | UFW: inspect rule numbering; numbers change after deletion. | [Inspect firewall policy and plan changes](security/firewall-reference.md) |
| `sudo firewall-cmd --state` | firewalld: check daemon state. | [Inspect firewall policy and plan changes](security/firewall-reference.md) |
| `sudo firewall-cmd --get-active-zones` | firewalld: map active interfaces/sources to zones. | [Inspect firewall policy and plan changes](security/firewall-reference.md) |
| `sudo firewall-cmd --zone=ZONE --list-all` | firewalld: inspect one runtime zone. | [Inspect firewall policy and plan changes](security/firewall-reference.md) |
| `sudo firewall-cmd --permanent --zone=ZONE --list-all` | firewalld: inspect saved policy separately. | [Inspect firewall policy and plan changes](security/firewall-reference.md) |
| `sudo nft list ruleset` | Read underlying nftables policy when applicable; do not edit manager-owned tables directly. | [Inspect firewall policy and plan changes](security/firewall-reference.md) |

## Backup and recovery

| Command or syntax | Purpose | Reference |
| --- | --- | --- |
| `tar -czf ARCHIVE -C DIRECTORY NAME` | Create a gzip-compressed archive from NAME relative to DIRECTORY. | [Create and restore a tar archive](backup-and-recovery/tar-reference.md) |
| `tar -tzf ARCHIVE` | List members without extracting. | [Create and restore a tar archive](backup-and-recovery/tar-reference.md) |
| `tar -xzf ARCHIVE -C DIRECTORY` | Extract into an existing directory; may overwrite matching files. | [Create and restore a tar archive](backup-and-recovery/tar-reference.md) |
| `tar -tvzf ARCHIVE` | Inspect member names and stored metadata. | [Create and restore a tar archive](backup-and-recovery/tar-reference.md) |
| `sha256sum ARCHIVE` | Compute a digest for transfer/corruption checks; not authenticity without a trusted expected digest. | [Create and restore a tar archive](backup-and-recovery/tar-reference.md) |
| `rsync -av SOURCE/ DEST/` | Copy contents of SOURCE into DEST; may replace existing destination files. | [Preview, copy and verify with rsync](backup-and-recovery/rsync-reference.md) |
| `rsync -avni SOURCE/ DEST/` | Dry run with verbose itemized proposed changes. | [Preview, copy and verify with rsync](backup-and-recovery/rsync-reference.md) |
| `rsync -av SOURCE DEST/` | Copy the SOURCE directory itself beneath DEST. | [Preview, copy and verify with rsync](backup-and-recovery/rsync-reference.md) |
| `rsync -acni SOURCE/ DEST/` | Checksum-based dry-run comparison; reads file data and can be expensive. | [Preview, copy and verify with rsync](backup-and-recovery/rsync-reference.md) |
| `rsync -av -e ssh SOURCE/ USER@HOST:DEST/` | Copy over SSH; host and destination must be verified. | [Preview, copy and verify with rsync](backup-and-recovery/rsync-reference.md) |
| `rsync -avni --delete SOURCE/ DEST/` | Preview removal of destination-only entries; omit -n only with an explicit deletion plan. | [Preview, copy and verify with rsync](backup-and-recovery/rsync-reference.md) |
| `sha256sum FILE` | Compute content digest; compare against a trusted manifest. | [Verify a restore before replacing data](backup-and-recovery/recovery-command-reference.md) |
| `sha256sum -c MANIFEST` | Verify files against recorded digests; paths are relative to the current directory. | [Verify a restore before replacing data](backup-and-recovery/recovery-command-reference.md) |
| `tar -tzf ARCHIVE` | Inspect archive members before extraction. | [Verify a restore before replacing data](backup-and-recovery/recovery-command-reference.md) |
| `cmp -- EXPECTED RESTORED` | Compare file bytes; 0 identical, 1 different, higher status indicates trouble. | [Verify a restore before replacing data](backup-and-recovery/recovery-command-reference.md) |
| `diff -ru -- EXPECTED RESTORED` | Compare text trees recursively; contents may reveal secrets. | [Verify a restore before replacing data](backup-and-recovery/recovery-command-reference.md) |
| `stat -- FILE` | Inspect mode, owner, group and timestamps; bytes alone do not verify metadata. | [Verify a restore before replacing data](backup-and-recovery/recovery-command-reference.md) |

[Collection home](README.md) · [Reading and practice conventions](README.md#before-you-run-a-command)
