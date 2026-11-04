```bash
sudo cryptsetup status MAPPER_NAME
sudo cryptsetup luksDump /dev/DEVICE
sudo cryptsetup isLuks /dev/DEVICE
sudo dmsetup ls --target crypt
ls -l /dev/mapper
sudo losetup --list
sudo losetup --find
lsblk -o NAME,TYPE,FSTYPE,UUID,MOUNTPOINTS
sudo tune2fs -l /dev/DEVICE
sudo dumpe2fs -h /dev/DEVICE
sudo xfs_info MOUNTPOINT
sudo btrfs filesystem df MOUNTPOINT
sudo file -s /dev/DEVICE
```
