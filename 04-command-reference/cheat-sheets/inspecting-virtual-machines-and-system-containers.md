| Command | What you can do with it |
| --- | --- |
| `virsh --version` | Print the virsh version. |
| `virsh list --all` | List virtual-machine domains, including stopped ones. |
| `virsh dominfo DOMAIN` | Inspect a domain's configuration summary. |
| `virsh domstate DOMAIN` | Read a domain's current state. |
| `virsh domifaddr DOMAIN` | Inspect domain interface addresses when available. |
| `virsh domblklist DOMAIN` | List block devices attached to a domain. |
| `virsh domstats DOMAIN` | Inspect domain statistics. |
| `virsh net-list --all` | List virtual networks. |
| `virsh pool-list --all` | List storage pools. |
| `virsh snapshot-list DOMAIN` | List recorded domain snapshots. |
| `virsh dumpxml DOMAIN` | Print a domain's XML definition. |
| `virt-host-validate` | Check host capabilities for virtualization. |
| `virt-top` | Monitor virtual-machine resource usage. |
| `qemu-img info IMAGE_FILE` | Inspect a disk image's format and size. |
| `qemu-img info --backing-chain IMAGE_FILE` | Inspect a disk image and its backing chain. |
| `machinectl list` | List systemd-managed machines. |
| `machinectl status MACHINE` | Inspect a systemd-managed machine. |
| `lxc list` | List LXD instances through lxc. |
| `lxc info INSTANCE` | Inspect an LXD instance. |
| `lxc image list` | List locally known LXD images. |
| `incus list` | List Incus instances. |
| `incus info INSTANCE` | Inspect an Incus instance. |
