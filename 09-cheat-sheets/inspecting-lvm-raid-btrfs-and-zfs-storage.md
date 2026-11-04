```bash
sudo pvs
sudo vgs
sudo lvs -a
sudo pvs -o pv_name,vg_name,pv_size,pv_free
sudo vgs -o vg_name,vg_size,vg_free
sudo lvs -a -o lv_name,vg_name,lv_size,lv_attr
sudo lvs -a -o lv_name,vg_name,data_percent,metadata_percent
sudo pvdisplay
sudo vgdisplay
sudo lvdisplay
sudo dmsetup ls --tree
sudo dmsetup info -c
cat /proc/mdstat
sudo mdadm --detail /dev/MD_DEVICE
sudo mdadm --examine /dev/DEVICE
sudo btrfs filesystem show
sudo btrfs filesystem usage MOUNTPOINT
sudo btrfs subvolume list MOUNTPOINT
sudo btrfs device stats MOUNTPOINT
sudo zpool status
sudo zpool list
sudo zfs list
sudo zfs list -t snapshot
sudo zfs get all DATASET
```
