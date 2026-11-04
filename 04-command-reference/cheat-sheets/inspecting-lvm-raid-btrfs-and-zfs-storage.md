| Command | What you can do with it |
| --- | --- |
| `sudo pvs` | Summarize LVM physical volumes. |
| `sudo vgs` | Summarize LVM volume groups. |
| `sudo lvs -a` | List logical volumes including internal volumes. |
| `sudo pvs -o pv_name,vg_name,pv_size,pv_free` | Map physical volumes to group membership and free capacity. |
| `sudo vgs -o vg_name,vg_size,vg_free` | Show group size and unallocated capacity. |
| `sudo lvs -a -o lv_name,vg_name,lv_size,lv_attr` | Show logical-volume size and attributes. |
| `sudo lvs -a -o lv_name,vg_name,data_percent,metadata_percent` | Inspect thin-volume data and metadata utilization where applicable. |
| `sudo pvdisplay` | Display detailed physical-volume information. |
| `sudo vgdisplay` | Display detailed volume-group information. |
| `sudo lvdisplay` | Display detailed logical-volume information. |
| `sudo dmsetup ls --tree` | Show the device-mapper dependency tree. |
| `sudo dmsetup info -c` | Show device-mapper status information in columns. |
| `cat /proc/mdstat` | Read software RAID state. |
| `sudo mdadm --detail /dev/MD_DEVICE` | Inspect an MD RAID array. |
| `sudo mdadm --examine /dev/DEVICE` | Read RAID metadata from a component device. |
| `sudo btrfs filesystem show` | List Btrfs filesystems and devices. |
| `sudo btrfs filesystem usage MOUNTPOINT` | Show space accounting for a mounted Btrfs filesystem. |
| `sudo btrfs subvolume list MOUNTPOINT` | List Btrfs subvolumes. |
| `sudo btrfs device stats MOUNTPOINT` | Inspect Btrfs device error counters. |
| `sudo zpool status` | Inspect ZFS pool health and topology. |
| `sudo zpool list` | List ZFS pool capacity. |
| `sudo zfs list` | List ZFS datasets and usage. |
| `sudo zfs list -t snapshot` | List ZFS snapshots. |
| `sudo zfs get all DATASET` | Inspect a dataset's properties. |
