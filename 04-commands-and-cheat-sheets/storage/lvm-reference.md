# Read LVM layout and capacity

Logical Volume Manager combines physical volumes (PVs) into volume groups (VGs), then allocates logical volumes (LVs). A filesystem may sit inside an LV, and each layer has its own size.

## Environment and permissions

Linux with lvm2. Reporting usually needs sudo to read metadata; it does not resize or format storage. An LVM-free host can legitimately show no volumes. The walkthrough requires only reporting permission.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `sudo pvs -o pv_name,vg_name,pv_size,pv_free` | Map physical volumes to groups and free extents. |
| `sudo vgs -o vg_name,vg_size,vg_free` | Show group capacity and unallocated space. |
| `sudo lvs -a -o lv_name,vg_name,lv_size,lv_attr` | Show logical volumes including hidden internal LVs. |
| `sudo lvs -a -o lv_name,vg_name,data_percent,metadata_percent` | Inspect thin-pool usage where applicable. |
| `lsblk -f` | Relate logical devices to filesystem types and mount points. |
| `sudo vgcfgbackup` | Write an LVM metadata backup; does not back up file data. |

## Follow along

```bash
sudo pvs -o pv_name,vg_name,pv_size,pv_free
sudo vgs -o vg_name,vg_size,vg_free
sudo lvs -a -o lv_name,vg_name,lv_size,lv_attr
lsblk -f
```

## Expected results and verification

On an LVM host, follow a PV to its VG, an LV to that VG, then its filesystem/mount in lsblk. VG free space means capacity not yet allocated to LVs; it does not measure free space inside a filesystem. No cleanup is needed.

## Common mistakes and next checks

Growing an LV and growing its filesystem are separate operations unless a supported combined workflow is explicitly used. Shrinking support differs: XFS cannot be shrunk. `pvcreate`, `lvremove` and `lvreduce` can destroy data; these require dedicated disposable disks and restore rehearsal, not a generic copy-and-paste sequence. Thin pools need monitoring of both data and metadata.

## Authoritative references

- [LVM manual](https://man7.org/linux/man-pages/man8/lvm.8.html)
- [lvs manual](https://man7.org/linux/man-pages/man8/lvs.8.html)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
