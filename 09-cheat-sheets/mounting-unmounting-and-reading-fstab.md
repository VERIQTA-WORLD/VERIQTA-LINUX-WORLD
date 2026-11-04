| Command | What you can do with it |
| --- | --- |
| `findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS` | List active mounts with sources, types and options. |
| `findmnt --target DIRECTORY` | Find the filesystem containing a directory. |
| `findmnt --mountpoint MOUNTPOINT` | Look up an exact mount point. |
| `findmnt --fstab` | Read configured fstab entries without mounting them. |
| `findmnt --verify --verbose` | Check mount configuration for consistency and usability. |
| `mount` | List active mounts using mount's default display. |
| `mountpoint MOUNTPOINT` | Test whether a path is a mount point. |
| `ls -l /dev/disk/by-uuid` | List stable device links by filesystem UUID. |
| `ls -l /dev/disk/by-label` | List stable device links by filesystem label. |
| `sudo mount -t FILESYSTEM_TYPE /dev/DEVICE MOUNTPOINT` | Attach a filesystem to a mount point, hiding any prior contents there. |
| `sudo mount -o ro /dev/DEVICE MOUNTPOINT` | Request a read-only mount, noting filesystem recovery behavior may still matter. |
| `sudo mount --bind SOURCE_DIRECTORY TARGET_DIRECTORY` | Expose an existing directory at another mount point. |
| `sudo mount -o loop,ro IMAGE_FILE MOUNTPOINT` | Mount a filesystem image through a loop device with read-only requested. |
| `sudo umount MOUNTPOINT` | Detach a filesystem, failing if it is busy unless otherwise handled. |
| `udisksctl status` | Show UDisks storage status. |
| `udisksctl info -b /dev/DEVICE` | Inspect a block device through UDisks. |
| `udisksctl mount -b /dev/DEVICE` | Mount a device through UDisks subject to authorization. |
| `udisksctl unmount -b /dev/DEVICE` | Unmount a device through UDisks. |
