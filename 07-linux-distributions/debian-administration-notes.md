# Debian administration notes

Debian's stable, testing and unstable tracks serve different purposes. Stable refers to a maintained release baseline; it does not mean packages never change or that every workload is automatically supported. Debian and Ubuntu share packaging concepts while maintaining separate archives and release decisions.

## Scope and environment

The named reference track is **Debian 13, trixie**, identified as stable by the official release pages at the November 4, 2026 source review. Do not infer that a future stable alias will still refer to trixie. Point releases refresh the maintained release; they are not the same event as moving to a new major release.

Host examples assume an authorized conventional Linux installation. Optional administrative/security queries need appropriate permissions. The portable lab uses supplied metadata without querying or modifying a real Debian system.

## What changes in practice

### Release and archive identity

Use the [release information](https://www.debian.org/releases/trixie/) and release notes for support scope, architectures and upgrades. At this review, Debian documents full Debian 13 support through August 9, 2028 and LTS through June 30, 2030, with reduced architecture coverage during LTS. Verify the actual package/architecture coverage rather than assuming every component shares that horizon.

A source entry using a codename and an entry using a moving alias have different future behavior. Do not casually replace codenames with stable or testing as an update shortcut. Major-version transitions require the release notes, backups and a recovery plan.

```bash
cat /etc/os-release
dpkg --print-architecture
apt --version
apt-cache policy bash
dpkg-query -W bash
```

APT sources may use traditional .list entries or deb822 .sources entries beneath `/etc/apt/sources.list.d`. Inspect the effective repository configuration, including security/updates and optional components, without copying third-party snippets blindly. File presence alone does not prove which version is the selected candidate.

### Networking is an observed choice

Debian systems can use NetworkManager, systemd-networkd, ifupdown or another supported arrangement depending on installation and administrator choices. Do not infer an active manager solely from Debian 13 or copy Ubuntu's Netplan procedure onto every Debian host. The [Debian Reference networking chapter](https://www.debian.org/doc/manuals/debian-reference/ch05) explains the alternatives and conflicts.

Selected inspection:

```bash
systemctl is-active NetworkManager.service
systemctl is-active systemd-networkd.service
systemctl is-active networking.service
ls -l /etc/resolv.conf
ip -br address
```

An inactive/not-found result can be normal if another component owns the interface. Avoid enabling two managers for the same interface. Resolver ownership is a separate question from address configuration.

### Services and policy

Discover the installed unit and log destination. `ssh.service`, socket activation, optional rsyslog and journal persistence can vary by image and installed packages. Inspect AppArmor or other mandatory-access policy when relevant; ordinary file modes alone do not account for every denial. Do not assume Ubuntu's packaged defaults and policy contents are identical.

Security fixes may be backported. An upstream-looking version string alone does not establish whether a Debian security fix is missing: compare the distribution package version and advisory status at its authoritative source.

## Follow-along lab

Compare a Debian record with an Ubuntu record that declares Debian ancestry:

```bash
debian_lab=$(mktemp -d)
printf '%s\n' 'ID=debian' 'VERSION_ID="13"' > "$debian_lab/debian"
printf '%s\n' 'ID=ubuntu' 'ID_LIKE=debian' 'VERSION_ID="24.04"' > "$debian_lab/ubuntu"
python3 07-linux-distributions/labs/read_identity.py --file "$debian_lab/debian"
python3 07-linux-distributions/labs/read_identity.py --file "$debian_lab/ubuntu"
printf '%s\n' \
  'Shared hint: Debian-related packaging research' \
  'Different: product ID, archives, release policy and support evidence' \
  'Unobserved: networking owner, installed packages, security state' \
  > "$debian_lab/comparison.txt"
cat "$debian_lab/comparison.txt"
```

Expect both family hints to be Debian-related while IDs/releases remain distinct. Explain why this does not justify mixing their repositories.

## Verification and limits

For a real host, retain exact identity, architecture, source origins, installed/candidate package version, active network owner, resolver, unit/log arrangement and security state. Distinguish absence from an unprivileged or unavailable query.

The fixture confirms only reader behavior. It does not establish package availability, support entitlement, actual interface ownership or a successful Debian upgrade. Use [production maintenance](../06-system-administration/patching-and-maintenance.md) for a planned change.

## Cleanup

```bash
rm -i -- "$debian_lab/debian" "$debian_lab/ubuntu" "$debian_lab/comparison.txt"
rmdir -- "$debian_lab"
```

## References

- [Debian release information](https://www.debian.org/releases/trixie/) and [release tracks](https://www.debian.org/releases/).
- [Debian Reference networking](https://www.debian.org/doc/manuals/debian-reference/ch05) and [APT manual](https://manpages.debian.org/trixie/apt/apt.8.en.html), noting that the linked manual is release-specific.
- [Debian security information](https://www.debian.org/security/).

[Collection home](README.md) · [Ubuntu comparison](ubuntu-administration-notes.md)
