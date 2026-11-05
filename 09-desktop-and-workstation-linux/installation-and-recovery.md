# Install Linux with a recovery route

[Collection home](README.md) · Next: [Desktop and accessibility](desktop-and-accessibility.md)

## Environment and prerequisites

Use this guide to prepare a desktop installation, verify its inputs and establish a usable recovery route. Begin in a **disposable VM** with a new virtual disk. A VM lets you learn the installer without repartitioning your everyday computer. It does not prove that your physical Wi-Fi adapter, GPU, fingerprint reader or suspend firmware will work.

Choose the current supported desktop release from your distribution's official site. Match its CPU architecture to your machine and read its release-specific installation guide. Ubuntu Desktop, Fedora Workstation and Debian with a desktop task are different products; their installer screens and package selections differ. This guide explains checkpoints rather than pretending that one screen sequence fits all three.

For the small integrity exercise, use Bash, Python 3 and an ordinary account. No ISO download or root access is required. For the installation walkthrough you additionally need a desktop ISO, a compatible hypervisor, sufficient host capacity according to the release requirements, and permission to create a disposable VM. Download sizes and minimum requirements change; consult the selected release's guide.

## Understand the components

| Component | What it does | What you need to decide |
| --- | --- | --- |
| Installation image | Boots an installer or live environment | Correct product, supported release and architecture |
| Firmware mode | Provides the boot interface, usually UEFI on modern hardware | Use a consistent mode; do not switch firmware settings casually on an existing system |
| Secure Boot | Checks eligible signed boot components under configured trust | Third-party modules can require distribution-specific signing/enrollment; disabling checks is not a general driver fix |
| Partitioning/filesystem | Allocates storage and defines its layout | A new VM disk is expendable; an existing physical disk is not |
| Encryption | Protects stored data when appropriately locked | Keep recovery material somewhere independent and protected; losing keys can mean losing data |
| Boot loader and initramfs | Start the installed system and prepare early storage/drivers | Recovery media must be compatible with your installed architecture and storage design |
| Account | Supplies your daily identity and optional administrator access | Use an ordinary daily account; protect authentication and recovery credentials |
| Updates | Maintain packages, kernel and possibly firmware | Allow time and power for completion; verify a reboot afterward when required |

A VM snapshot is useful before an experiment, but it is not an independent backup of your host or irreplaceable files. A partition label in an installer is not sufficient identity: compare disk size, model, serial where available and attachment context.

## Follow along

### 1. Verify that you can detect changed bytes

This local exercise illustrates integrity only. It does **not** authenticate an image publisher: a malicious party could replace both an image and an untrusted checksum.

<!-- workstation:exercise -->
```bash
install_lab=$(mktemp -d) || exit 1
python3 - "$install_lab" <<'PY'
import hashlib
from pathlib import Path
import sys
root = Path(sys.argv[1])
image = root / 'example-image.bin'
image.write_bytes(b'Example only: not a bootable image\n')
expected = hashlib.sha256(image.read_bytes()).hexdigest()
(root / 'expected.sha256').write_text(expected + '\n')
assert hashlib.sha256(image.read_bytes()).hexdigest() == expected
print('PASS: original example matches its recorded digest')
image.write_bytes(image.read_bytes() + b'changed\n')
assert hashlib.sha256(image.read_bytes()).hexdigest() != expected
print('PASS: modified bytes are detected; publisher identity remains unproven')
PY
```

For a real ISO, obtain its checksum and signature instructions from the distribution. Verify the signing-key identity through the project's documented trust route, verify the signed checksum material, then compare the exact downloaded image. A “good signature” from an unidentified key is not enough. Stop if any check fails; do not bypass it to finish the installation.

### 2. Install onto a disposable virtual disk

1. Create a new VM named for your learning environment. Attach a **new empty virtual disk**, not a physical disk or shared storage containing personal data. Leave host-folder sharing off initially.
2. Attach the verified desktop image. Choose firmware and virtual hardware supported by the distribution/hypervisor. Record your choices privately.
3. Boot into the live environment if offered. Confirm keyboard layout and display readability. A live session's changes may disappear after shutdown.
4. Open the installer. Check the destination disk and installation summary before committing. On this new disposable VM only, the erase-disk option can be appropriate. Never transfer that choice to your existing computer by habit.
5. Choose locale, time zone, keyboard and account settings. If enabling encryption, understand the unlock workflow and retain the recovery information securely. Do not put passphrases in screenshots or a public lab record.
6. Complete installation, shut down or reboot as instructed, and detach the installation image when the hypervisor requires it. Boot from the virtual disk rather than starting the installer again.
7. Sign in, open a terminal and compare `/etc/os-release` with the chosen product. Use the distribution's supported updater, review the transaction and complete any required restart.

### 3. Prepare before moving to physical hardware

Make and verify an independent backup, including another OS's recovery keys and important application data. Check vendor/distribution documentation for the exact hardware. Boot the live environment and test Wi-Fi, input, display, audio and accessibility before installation. Live success is useful evidence, not proof that every post-installation feature works.

For dual boot, identify encryption, free space, firmware mode and the other OS's recovery requirements first. Partition resizing and boot configuration can affect both systems. Use the distribution's current dual-boot guide and a tested recovery route; this beginner walkthrough does not provide a universal partitioning recipe. Do not use an unreviewed raw-device write command to create media.

## Verify and recover

Your VM installation is useful when it boots with the ISO detached, accepts your account, opens a usable desktop and terminal, and retains a small test document across a reboot. Check the clock, network access you actually need and update status. If encrypted, test a normal unlock with recovery information safely available.

If it returns to the installer, inspect boot order and attached media before reinstalling. If it cannot boot, retain the VM disk and inspect the hypervisor/installer error rather than repeatedly erasing it. A fresh disposable VM is a reasonable retry; a real disk with data requires a recovery investigation.

For physical installations, verify the intended disks and any other OS still behave as expected. A working desktop does not establish a complete backup, secure key custody or hardware compatibility across suspend and docking. Continue through the hardware guides before relying on the workstation for important work.

## Cleanup

Remove the two local integrity files when finished:

<!-- workstation:cleanup -->
```bash
rm -i -- "$install_lab/example-image.bin" "$install_lab/expected.sha256"
rmdir -- "$install_lab"
```

Keep a useful installed learning VM. To discard one, power it off and verify its name and disk ownership in the hypervisor before deleting its virtual disk. Do not delete shared disks or host backups. Retain genuine recovery media and protected keys for systems you still use.

## Checkpoint

Explain the difference between integrity and publisher authenticity, identify the actual installation destination, and describe how you would recover if the installed system did not boot. You should be able to do these before installing on a physical computer.

## Sources

Use the [Ubuntu Desktop installation tutorial](https://ubuntu.com/tutorials/install-ubuntu-desktop), [Ubuntu download verification](https://ubuntu.com/tutorials/how-to-verify-ubuntu), [Fedora installation documentation](https://docs.fedoraproject.org/en-US/fedora/latest/install-guide/), [Debian installation guide](https://www.debian.org/releases/stable/installmanual) and [Debian image verification](https://www.debian.org/CD/verify). Read the guide for the actual release; older examples of signing keys or installer screens may differ.
