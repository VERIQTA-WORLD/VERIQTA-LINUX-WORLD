# Package-manager comparison

Translate the task before translating syntax. Searching a repository, querying installed files, refreshing metadata, resolving an upgrade and installing it are different actions. Similar verbs across tools do not guarantee the same dependency, removal or script behavior.

## Scope and environment

The comparison targets conventional Debian/Ubuntu APT, DNF-family RPM systems, openSUSE Zypper, Arch pacman and Alpine apk. NixOS and image/deployment products need their own model. Commands depend on installed versions and configured repositories. Uppercase PACKAGE and PATH are placeholders, not literal targets.

Queries can still refresh caches or use the network. Installing/upgrading/removing normally needs authorization and can run scripts or restart services. The lab creates a task-mapping record only: no package manager is invoked by its portable steps.

## What changes in practice

### Database tools and transaction frontends

`dpkg` and `rpm` expose installed package metadata and lower-level package operations. APT and DNF add repository/dependency workflows. Do not bypass dependency handling with low-level force flags as a routine installation strategy.

| Intent | APT/dpkg | DNF/RPM | Zypper/RPM | pacman | apk |
| --- | --- | --- | --- | --- | --- |
| Search available metadata | `apt search PACKAGE` | `dnf search PACKAGE` | `zypper search PACKAGE` | `pacman -Ss PACKAGE` | `apk search PACKAGE` |
| Inspect installed version | `dpkg-query -W PACKAGE` | `rpm -q PACKAGE` | `rpm -q PACKAGE` | `pacman -Q PACKAGE` | `apk info -v PACKAGE` |
| List installed files | `dpkg -L PACKAGE` | `rpm -ql PACKAGE` | `rpm -ql PACKAGE` | `pacman -Ql PACKAGE` | `apk info -L PACKAGE` |
| Find installed file owner | `dpkg -S PATH` | `rpm -qf PATH` | `rpm -qf PATH` | `pacman -Qo PATH` | `apk info --who-owns PATH` |
| Proposed change, no accepted transaction | `apt-get -s install PACKAGE` | `dnf --assumeno install PACKAGE` | `zypper install --dry-run PACKAGE` | Review installed help and its transaction proposal carefully | Review installed `apk --help` for simulation support |

The last row is deliberately not a claim of identical dry-run behavior. A declined DNF operation may return nonzero and update cache metadata. APT simulation uses current metadata and may have unprivileged limitations. For automation, use documented stable interfaces appropriate to the installed implementation.

### Refreshing metadata is not a universal standalone update pattern

On APT, `apt update` refreshes available metadata, while upgrade applies package changes. DNF/Zypper/APK have their own refresh/cache behavior. Arch's [maintenance guidance](https://wiki.archlinux.org/title/System_maintenance) expects a coherent rolling system and warns about partial upgrades: do not translate `apt update` mechanically into a standalone sync-database update followed by arbitrary package installs.

Use the release's official workflow and transaction proposal. Review additions, removals, replacements, origins, architectures and available rollback. `full-upgrade`, `dist-upgrade` and repository/major-version transitions have different scopes; sharing the word upgrade does not make them interchangeable.

### Repositories, signatures and coverage

Use trusted origins and verify signing/key ownership through the product's documented process. Do not disable verification to suppress an error. Third-party repositories can introduce unsupported dependency combinations, replace base packages or stop publishing compatible updates.

A package can be split differently or named differently across distributions. Search for the required capability or owning file using the appropriate repository tools, then inspect the candidate rather than guessing a one-to-one name map.

### Other management models

NixOS manages declared system configuration and generations; system activation is not equivalent to copying a random package file into place. Atomic/image products maintain host deployments/images and may use development containers for mutable tooling. User applications through Flatpak/Snap are another layer, not proof of how the base host receives updates.

## Follow-along lab

Write an intent-first mapping and explicitly separate the unexecuted transaction:

```bash
packages_lab=$(mktemp -d)
printf '%s\n' \
  'Task: identify the installed package that owns a verified path' \
  'Debian/Ubuntu candidate: dpkg -S PATH' \
  'RPM candidate: rpm -qf PATH' \
  'Arch candidate: pacman -Qo PATH' \
  'Required evidence: actual manager, verified path and interpretation of no owner' \
  'Package transaction accepted: no' \
  > "$packages_lab/mapping.txt"
cat "$packages_lab/mapping.txt"
```

On one actual disposable Linux VM, choose its appropriate **query** and a path that exists there. If a file was created locally or belongs to a container/image layer outside that database, “no owner” can be an honest result. Do not install another distribution's database tool to force a match.

As an extension, compare the same capability on a second family, recording actual owning package names, versions and repository origins. Keep every installation proposal unaccepted until it belongs to a reviewed maintenance plan.

## Verification and limits

A correct translation records task, manager/implementation, scope, operands, side effects, expected statuses and actual result. A table entry is not proof that a tool or repository is installed or supported on the target.

The portable exercise verifies a written task mapping only. Package availability, repository queries and transaction simulations remain pending Linux reproduction. Use [patching and maintenance](../06-system-administration/patching-and-maintenance.md) for an accepted change.

## Cleanup

```bash
rm -i -- "$packages_lab/mapping.txt"
rmdir -- "$packages_lab"
```

## References

- [APT simulation](https://manpages.debian.org/bookworm/apt/apt-get.8.en.html), [DNF4 reference](https://dnf.readthedocs.io/en/latest/command_ref.html) and [DNF5](https://dnf5.readthedocs.io/en/latest/).
- [Zypper manual](https://manpages.opensuse.org/Tumbleweed/zypper/zypper.8.en.html), [pacman manual](https://man.archlinux.org/man/pacman.8.en) and [apk manuals](https://docs.alpinelinux.org/user-handbook/0.1a/Working/apk.html).
- [NixOS manual](https://nixos.org/manual/nixos/stable/).

[Collection home](README.md) · [Package command references](../04-command-reference/packages/README.md)
