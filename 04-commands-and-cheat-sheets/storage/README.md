# Storage

Map devices to filesystems and mounts, then distinguish filesystem free space from volume-group free capacity.

## Detailed references

1. [Inspect disks, filesystems and capacity](disk-and-filesystem-commands.md)
2. [Inspect mounts and understand mount syntax](mount-reference.md)
3. [Read LVM layout and capacity](lvm-reference.md)

## At a glance

These are lookup examples; follow the linked page for prerequisites, expected results and cleanup. Uppercase arguments are placeholders, not literal targets.

| Task | Syntax | Full explanation |
| --- | --- | --- |
| Show storage topology with explicit columns; older releases may need MOUNTPOINT singular. | `lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS` | [Inspect disks, filesystems and capacity](disk-and-filesystem-commands.md) |
| Report mounted filesystem type, capacity and usage for /. | `df -hT /` | [Inspect disks, filesystems and capacity](disk-and-filesystem-commands.md) |
| Report inode usage; free bytes do not guarantee free inodes. | `df -i /` | [Inspect disks, filesystems and capacity](disk-and-filesystem-commands.md) |
| Find the filesystem containing the root path. | `findmnt --target /` | [Inspect mounts and understand mount syntax](mount-reference.md) |
| Match an exact mount point. | `findmnt --mountpoint /` | [Inspect mounts and understand mount syntax](mount-reference.md) |
| List mount sources and options. | `findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS` | [Inspect mounts and understand mount syntax](mount-reference.md) |
| Map physical volumes to groups and free extents. | `sudo pvs -o pv_name,vg_name,pv_size,pv_free` | [Read LVM layout and capacity](lvm-reference.md) |
| Show group capacity and unallocated space. | `sudo vgs -o vg_name,vg_size,vg_free` | [Read LVM layout and capacity](lvm-reference.md) |
| Show logical volumes including hidden internal LVs. | `sudo lvs -a -o lv_name,vg_name,lv_size,lv_attr` | [Read LVM layout and capacity](lvm-reference.md) |

## Practice checkpoint

Work through the references in the order above. Explain what each command reads or changes, identify the relevant permission boundary, and record one successful result and one limitation. Use each page’s cleanup instructions; do not invent a blanket recursive deletion.

[Collection home](../README.md) · [Command index](../command-index.md) · [LINUX-WORLD](../../README.md)
