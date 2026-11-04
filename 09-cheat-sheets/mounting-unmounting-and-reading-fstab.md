```bash
findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS
findmnt --target DIRECTORY
findmnt --mountpoint MOUNTPOINT
findmnt --fstab
findmnt --verify --verbose
mount
mountpoint MOUNTPOINT
ls -l /dev/disk/by-uuid
ls -l /dev/disk/by-label
sudo mount -t FILESYSTEM_TYPE /dev/DEVICE MOUNTPOINT
sudo mount -o ro /dev/DEVICE MOUNTPOINT
sudo mount --bind SOURCE_DIRECTORY TARGET_DIRECTORY
sudo mount -o loop,ro IMAGE_FILE MOUNTPOINT
sudo umount MOUNTPOINT
udisksctl status
udisksctl info -b /dev/DEVICE
udisksctl mount -b /dev/DEVICE
udisksctl unmount -b /dev/DEVICE
```
