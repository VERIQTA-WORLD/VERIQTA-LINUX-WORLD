```bash
lsblk -f
lsblk -o NAME,TYPE,SIZE,FSTYPE,UUID,MOUNTPOINTS
lsblk -d -o NAME,MODEL,SERIAL,SIZE
sudo blkid
sudo fdisk -l
sudo parted -l
sudo sfdisk --dump /dev/DEVICE
sudo wipefs --no-act /dev/DEVICE
df -hT
df -hT DIRECTORY
df -i
stat -f -- DIRECTORY
du -sh -- DIRECTORY
du -xhd1 -- DIRECTORY
du -ah -- DIRECTORY | sort -h
ncdu -x DIRECTORY
findmnt
findmnt --target DIRECTORY
sudo blockdev --getsize64 /dev/DEVICE
sudo smartctl -a /dev/DEVICE
sudo smartctl -H /dev/DEVICE
sudo nvme list
sudo nvme smart-log /dev/NVME_DEVICE
```
