# Prepare your Linux lab environment

Use an environment you can inspect, recover and discard without losing important work. Read the selected lab's requirements before creating machines or installing software. A temporary-file exercise needs much less infrastructure than a boot, service or multi-host network exercise.

[Lab home](README.md) · [Safety](LAB-SAFETY.md) · [Lab standard](LAB-STANDARD.md)

## 1. Match the environment to your exercise

| Environment | Appropriate work | Boundary you must understand |
| --- | --- | --- |
| Disposable full Linux VM | Host services, users, storage, networking and boot | You need a functioning console and a known reset/recovery procedure. |
| Linux container | Exercises that explicitly support userland or isolation study | Host kernel, devices, boot, service management and privilege differ. |
| Existing workstation | Selected read-only observations and private temporary files | Keep failure injection and high-impact changes off your working system. |
| Non-Linux host | Exercises explicitly identified as portable | Portable results do not establish Linux kernel, manager or policy behavior. |

Ubuntu Server 24.04 LTS is the introductory reference environment. Use the distribution's official image and verification/installation instructions. Match architecture to your host and virtualization platform. Read the lab for any different release, variant or tool requirement.

Do not repartition or dual-boot your main machine just to practice file commands. Use a disposable VM with its own virtual disk. For cloud resources, confirm authorization, cost, exposure and deletion ownership before provisioning; a local VM is sufficient for the ordinary introductory path.

## 2. Establish recovery first

Before modifying authentication, SSH, firewall rules, routing, mounts or boot configuration:

1. Open the VM console and prove that you can log in independently of SSH.
2. Identify how you will stop and reset the VM through your hypervisor.
3. Record the baseline snapshot/reset point and the data it discards.
4. Keep recovery credentials outside the VM's disposable filesystem.
5. Confirm that important personal files and production credentials are not inside the lab.

A snapshot can reset a lab but is not automatically a separate, application-consistent backup. If a lab teaches recovery, perform its actual restore verification instead of treating snapshot availability as the completed exercise.

For storage labs, attach only explicitly disposable virtual disks and record their identifiers and sizes before modification. Never infer that `/dev/sdb` is safe because an example uses that name.

## 3. Use an ordinary account

Log in as your normal lab user and elevate only for an explicitly described administrative operation. Your ordinary account can still delete its own data, so verify targets even without sudo.

Run these read-only checks on your intended Linux VM:

```bash
cat /etc/os-release
uname -r
uname -m
id
bash --version
python3 --version
```

Record actual versions. If a command is absent, read the lab to determine whether it is required before installing it. Use that distribution's supported package workflow and review proposed changes. Do not run a downloaded install script merely to match a screenshot.

Each lab has its own tool and interpreter requirements. Check them individually rather than installing every named utility at once.

## 4. Verify the service manager and network boundary

A systemd exercise needs a running manager of the stated scope. These observations help you identify your actual environment:

```bash
ps -p 1 -o pid,comm,args
systemctl --version
ip -brief address show
ip route show
```

Installed systemctl alone does not establish that the expected manager is running. For a user-unit exercise, check `systemctl --user show-environment` and stop if the bus/manager prerequisite is unavailable. Do not replace a user command with sudo or alter login policy to hide the difference.

For networking, keep the lab private. Use host-only/isolated networks where the exercise calls for them and a deliberate package-download route when needed. Record each VM's role and address. Do not bridge an experimental DHCP server into your home, workplace or public network.

When an exercise uses a local listener, follow its stated bind address and port. If your environment prohibits listeners, record that restriction; never substitute a public bind address.

## 5. Create private workspaces

Follow the exact workspace setup in each lab. Inspect the destination before creating or replacing files, and keep earlier investigations separate from a fresh run.

Keep your current shell and workspace variable until cleanup. If you resume later, recover the exact directory deliberately and inspect it before using cleanup commands; do not guess from an old path or PID.

Keep generated evidence private by default. Synthetic fixtures can still include misleading strings or executable-looking text; read them as data, never with source/eval.

## 6. Check readiness before starting

- [ ] You identified the target VM, release, architecture and account.
- [ ] Required tools and privileges match the selected lab.
- [ ] You can recover without relying on the service you will change.
- [ ] The intended paths, ports, users and devices are disposable or assigned to this lab.
- [ ] Resource bounds and network exposure are understood.
- [ ] You read the expected failures, acceptance checks and cleanup.
- [ ] You started a record of versions, assumptions and actual observations.

If a requirement is unmet, resolve it or choose an exercise compatible with your environment. Continue with the [Junior index](Junior/README.md) once those prerequisites are established.
