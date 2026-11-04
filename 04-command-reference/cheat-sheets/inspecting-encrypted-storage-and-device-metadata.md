| Command | What you can do with it |
| --- | --- |
| `sudo cryptsetup status MAPPER_NAME` | Inspect an active dm-crypt mapping. |
| `sudo cryptsetup luksDump /dev/DEVICE` | Read a device's LUKS header metadata. |
| `sudo cryptsetup isLuks /dev/DEVICE` | Test whether a device contains a recognized LUKS header. |
| `sudo dmsetup ls --target crypt` | List device-mapper mappings using the crypt target. |
| `ls -l /dev/mapper` | List device-mapper paths. |
| `sudo losetup --list` | List configured loop devices. |
| `sudo losetup --find` | Find the next unused loop device without attaching an image. |
| `lsblk -o NAME,TYPE,FSTYPE,UUID,MOUNTPOINTS` | Map devices to filesystem identities and mount points. |
| `sudo tune2fs -l /dev/DEVICE` | Read ext-family filesystem parameters. |
| `sudo dumpe2fs -h /dev/DEVICE` | Read ext-family superblock information without group details. |
| `sudo xfs_info MOUNTPOINT` | Read mounted XFS filesystem geometry. |
| `sudo btrfs filesystem df MOUNTPOINT` | Read Btrfs space allocation by data and metadata class. |
| `sudo file -s /dev/DEVICE` | Identify data signatures by reading a device. |
