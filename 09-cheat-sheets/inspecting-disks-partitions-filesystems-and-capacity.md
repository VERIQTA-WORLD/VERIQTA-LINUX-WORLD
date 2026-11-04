| Command | What you can do with it |
| --- | --- |
| `lsblk -f` | List devices with filesystem types, UUIDs and mount points. |
| `lsblk -o NAME,TYPE,SIZE,FSTYPE,UUID,MOUNTPOINTS` | Show storage topology with explicit identity and mount columns. |
| `lsblk -d -o NAME,MODEL,SERIAL,SIZE` | List whole-disk model, serial number and capacity. |
| `sudo blkid` | Probe block-device filesystem identifiers. |
| `sudo fdisk -l` | List partition tables and sizes. |
| `sudo parted -l` | List partition layouts using parted. |
| `sudo sfdisk --dump /dev/DEVICE` | Print a device's partition table in sfdisk format. |
| `sudo wipefs --no-act /dev/DEVICE` | Inspect filesystem signatures without removing them. |
| `df -hT` | Show mounted filesystem capacity and types. |
| `df -hT DIRECTORY` | Show capacity for the filesystem containing a directory. |
| `df -i` | Inspect inode consumption. |
| `stat -f -- DIRECTORY` | Inspect a directory's containing filesystem. |
| `du -sh -- DIRECTORY` | Sum allocated space beneath a directory. |
| `du -xhd1 -- DIRECTORY` | Show one level of directory sizes without crossing filesystems. |
| `du -ah -- DIRECTORY \| sort -h` | List allocated sizes and sort them using readable units. |
| `ncdu -x DIRECTORY` | Browse disk usage interactively without crossing filesystems. |
| `findmnt` | Display the active mount hierarchy. |
| `findmnt --target DIRECTORY` | Find the mount containing a directory. |
| `sudo blockdev --getsize64 /dev/DEVICE` | Read a block device's byte capacity. |
| `sudo smartctl -a /dev/DEVICE` | Read a drive's SMART information. |
| `sudo smartctl -H /dev/DEVICE` | Read a drive's SMART health summary. |
| `sudo nvme list` | List NVMe devices. |
| `sudo nvme smart-log /dev/NVME_DEVICE` | Read NVMe health and SMART counters. |
