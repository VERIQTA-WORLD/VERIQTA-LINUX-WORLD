# Linux glossary

Use this glossary to connect a term to an observable Linux behavior. Read the definition, try the small example where appropriate, then follow the linked reference when you need command syntax or a full procedure. Recognizing a word is a starting point; explaining its scope and effects is the useful skill.

[Library home](README.md) · [Filesystem paths](linux-filesystem-reference.md) · [Networking](linux-networking-reference.md)

## Scope and environment

The definitions describe common Linux concepts, with systemd and GNU tools identified where relevant. Linux distributions, containers, alternative service managers and image-based systems do not share every implementation. Uppercase names in examples are placeholders. Command fragments in the tables explain a term; they are not a sequence to paste into a shell.

The follow-along exercise uses Bash and Python 3 in an ordinary account. It creates only a private temporary directory, links and one tiny file. It needs no sudo, account change, mount or network connection.

## Reference

### Operating system and software

| Term | Meaning in plain language | Example or distinction to remember |
| --- | --- | --- |
| Linux | The kernel; in everyday conversation the name also refers to systems built around it | Specify kernel versus complete distribution when that distinction matters. |
| Kernel | Privileged core that exposes interfaces for processes, memory, devices and other resources | `uname -r` identifies the running kernel release, not the distribution release. |
| User space | Programs and libraries outside the kernel | Bash, your editor and a web server run in user space. |
| Distribution | A coordinated operating-system product with packages, configuration and maintenance policy | Read `/etc/os-release`, then observe the actual installed tools. |
| Release | A named/versioned distribution delivery with its own maintenance scope | A kernel version alone does not identify Ubuntu or Debian coverage. |
| Architecture | The instruction-set/platform target of software | aarch64/arm64 labels come from different naming conventions; inspect the relevant tool. |
| System call | An interface through which user-space code requests kernel work | Opening a file ultimately involves an interface such as openat; a shell command is not itself a system call. |
| C library | User-space library providing interfaces used by many applications | glibc and musl differ; not every application uses glibc NSS. |
| ABI | Binary interface assumptions between compiled components | A matching command name does not guarantee binary compatibility. |
| API | A programming interface with defined operations and data | A kernel API and a CLI option grammar have different compatibility boundaries. |
| Package | A distribution-managed unit of installed software/data | Installed package metadata and upstream source releases are different evidence. |
| Repository | A source of package metadata/artifacts, or a version-control project depending on context | State whether you mean an APT archive or this Git repository. |
| Dependency | Something another component needs | A package dependency is not the complete runtime service architecture. |
| Backport | A change adapted to an older maintained codebase | An older-looking version string alone does not prove a security fix is absent. |
| Signature | Cryptographic evidence tied to a key and signed content | Verification still requires a trusted key and intended artifact identity. |
| Checksum / digest | A value computed from bytes to detect a mismatch | A digest stored beside compromised data is not independent proof of authenticity. |
| Source / binary | Human-readable program input versus an executable/build artifact | Studying source is different from establishing which binary is running. |

### Shell, commands and data flow

| Term | Meaning in plain language | Example or distinction to remember |
| --- | --- | --- |
| Terminal | Interface through which you exchange text with programs | It is not the shell interpreter itself. |
| Shell | Command-language interpreter and execution environment | Bash and dash have different supported syntax. |
| Builtin | Command implemented by the shell | `type printf` can identify the selected builtin; a separate executable may also exist. |
| Executable | File the execution environment can invoke as a program | Execute mode alone does not make arbitrary text a valid program. |
| Interpreter | Program that reads and executes a language | A script's shebang and an explicit `python3 script.py` choose execution differently. |
| PATH | Search list used for command lookup | Adding a directory changes which executable may be selected; it does not grant file access. |
| Variable | Named shell/program value | A shell variable is not automatically present in child-process environments. |
| Environment | Named values passed to a process at execution | Exporting a variable affects subsequently launched children, not every process on the host. |
| Expansion | Transformation the shell performs before command execution | Globs, variable substitution and command substitution have distinct rules. |
| Quoting | Shell syntax that controls interpretation and splitting | `"$path"` preserves a path as one argument in the ordinary case. |
| Glob | A shell pattern matching pathnames | `*.log` is not the same grammar as a regular expression. |
| Regular expression | Pattern language used by a particular matching engine | Basic/extended regex and different tools' engines are not interchangeable. |
| Standard input | A process's conventional input stream, descriptor 0 | A program may instead read a named file or terminal directly. |
| Standard output | Conventional normal output stream, descriptor 1 | A successful diagnostic can print an unhealthy state. |
| Standard error | Conventional diagnostic stream, descriptor 2 | Empty stdout is not proof that a command succeeded. |
| Redirection | Shell arrangement of a command's streams/files | `>` can truncate an existing output file before the program runs. |
| Pipeline | Connected output/input streams between commands | Its status normally comes from the last command unless shell options change that rule. |
| Exit status | Numeric completion result interpreted by the command's contract | grep no-match and a parser error have different meanings despite both being nonzero. |
| Signal | A notification/action mechanism for a process | SIGTERM requests termination; delivery is not proof every child exited. |
| Job | A shell's tracked command or pipeline | A shell job identifier is not a system-wide process identity. |
| Subshell | A separate shell execution environment | Changes there do not generally update the parent's working directory/variables. |
| Idempotence | Repeating an operation has the same intended resulting state | It does not mean every repeated run is free of side effects or safe without review. |

See [command purpose and syntax](../04-command-reference/README.md) and the [foundation course](../01-Beginner-to-Advanced/README.md) for complete examples.

### Files, storage and paths

| Term | Meaning in plain language | Example or distinction to remember |
| --- | --- | --- |
| Pathname | A name used to locate an object through a directory hierarchy | The same text can resolve differently in another mount namespace. |
| Absolute / relative path | Path starting at root versus one interpreted from a current directory | `/etc/hosts` and `./hosts` need not identify the same file. |
| Root directory | `/`, the starting point of the visible path tree | Do not confuse it with the root account or `/root`. |
| Inode | Filesystem metadata object identified within its filesystem | Device/filesystem identity plus inode number matters; inode numbers are not globally unique. |
| Directory entry | Association between a name and an object in a directory | Removing a name does not necessarily destroy the file's last reference. |
| Hard link | Another directory entry referring to the same underlying inode | It is not an independent backup and normally cannot cross filesystem boundaries. |
| Symbolic link | Object containing a target pathname | The target can be absent; relative targets are resolved from the link's directory. |
| File descriptor | Process-local handle referring to an open object | An open file can remain readable after its last pathname is removed. |
| Mount | Attachment of a filesystem/view at a path | Mounting over a directory can hide its previous contents from that view. |
| Mountpoint | Path at which a mount is attached | An existing directory is not proof the expected filesystem is mounted there. |
| Block device | Device abstraction for block-addressable storage | A device can contain partitions, encryption, LVM or a filesystem; inspect the layers. |
| Partition | Region described by a storage device's partition layout | Partition existence does not establish a valid filesystem. |
| Filesystem | Implementation organizing storage objects and metadata | ext4, XFS, Btrfs and tmpfs have different properties and repair procedures. |
| UUID | Identifier used in several interfaces, including filesystems | Record the exact identifier type; not every UUID identifies the same layer. |
| LVM PV / VG / LV | Physical volume, pooled volume group and allocated logical volume | A logical volume and its filesystem have separate size/accounting boundaries. |
| Inode exhaustion | No metadata objects available for the required allocation | Bytes can remain available while file creation fails. |
| Quota | Limit/accounting assigned to an identity or project | Quota exhaustion differs from whole-filesystem exhaustion. |
| tmpfs | Filesystem backed by virtual memory with configurable limits | It can use swap; it is not an unlimited harmless scratch area. |
| Cache | Data retained to avoid recomputation or I/O | Reclaimable cache, essential application state and an independent backup differ. |
| Snapshot | Point-in-time state maintained by a specific storage/VM mechanism | Shared failure domains and consistency determine whether it meets a backup requirement. |
| Backup | Retained recoverable copy under a defined protection policy | Prove it with an isolated restore and required data/application checks. |
| Restore | Recovery of selected state from a retained copy | Copy completion alone does not establish application consistency. |
| Read-only | A restriction at a particular layer on modifications | Changing mode bits does not override a read-only mount. |
| Atomic replacement | A namespace operation exposing an old or new object rather than a partially replaced name | Atomicity, crash durability, metadata preservation and activation are distinct properties. |

### Identity, processes and isolation

| Term | Meaning in plain language | Example or distinction to remember |
| --- | --- | --- |
| UID / GID | Numeric user/group identities used in access decisions | Names are resolved labels; inspect the actual runtime identity. |
| Effective identity | Identity used for many permission checks by a process | Your interactive account may differ from the service account. |
| Supplementary groups | Additional group memberships held by a process | A changed membership does not automatically alter every existing login process. |
| Root | Conventionally UID 0, with authority depending on capabilities and namespace context | Container-root does not automatically equal unrestricted host-root. |
| Mode bits | Ordinary owner/group/other read, write and execute permissions | Directory execute means search/traversal; file execute has another role. |
| ACL | Extended access-control entries beyond the basic mode classes | Effective entries can be constrained by an ACL mask. |
| Capability | A division of privileged Linux authority into specific powers | A capability still has namespace and policy context. |
| Least privilege | Grant only the authority required for the intended operation | A passing sudo syntax check does not establish an appropriately narrow role. |
| MAC policy | Mandatory access-control rules beyond ordinary discretionary permissions | SELinux/AppArmor decisions need actual process/object/profile context. |
| Process / thread | Execution instance and an execution flow within a process | A process can have several threads consuming more than one CPU. |
| PID / PPID | Process identifier and parent identifier within the applicable PID view | A PID can be reused after exit; preserve start/boot context. |
| Zombie | Exited process whose status has not yet been reaped | It is not a running CPU worker that SIGKILL can repair. |
| Daemon | A service-style background process | Backgrounding a shell command does not supply all service-management behavior. |
| Unit | systemd object describing a managed resource or action | Services, sockets, mounts and timers have different state meanings. |
| Service manager | Component supervising or coordinating services | An installed systemctl binary does not prove a running systemd manager. |
| Readiness | Whether the required operation can currently be served | Process existence, port listening and application correctness are separate checks. |
| Namespace | Kernel mechanism giving a process a scoped view of a resource category | Mount, PID, user and network namespaces isolate different views. |
| cgroup | Process organization with resource-accounting/control mechanisms | Host capacity can differ from a workload's configured limits. |
| Container | Packaged process environment using isolation/resource mechanisms | It usually shares the host kernel; it is not a complete independent VM boot. |
| Virtual machine | Guest machine environment with a guest kernel | VMs on one physical host still share that host's failure domain. |
| Rootless | Operation without an ordinary host-root daemon/authority for that workflow | It does not mean there are no privileges, kernel risks or resource limits. |
| OCI image | Artifact format/model used in container ecosystems | An application image and a bootable host image have different lifecycle expectations. |
| Declarative configuration | Description of intended state interpreted by tooling | Declaring a value does not prove convergence or successful activation. |
| Image-based host | Host updated through a managed image/deployment model | Do not apply mutable-host package procedures without checking the product. |

### Networking and operational evidence

| Term | Meaning in plain language | Example or distinction to remember |
| --- | --- | --- |
| Interface | Network attachment within a network namespace | Link up does not establish end-to-end application connectivity. |
| IP address / prefix | Endpoint address and the prefix length used for network interpretation | An address alone does not determine all policy-routing decisions. |
| Route / gateway | A forwarding decision and an associated next hop where required | Some routes are directly connected or local and need no gateway. |
| Socket / port | Communication endpoint abstraction and protocol-specific numeric selector | TCP 53 and UDP 53 are not the same transport endpoint. |
| DNS | Distributed naming data/protocols | System name resolution may also use hosts files and other sources. |
| NSS | glibc-configured name-service selection for supported databases | A DNS-only query need not reproduce an application's lookup path. |
| Loopback | Local network interface/address scope for a host/namespace | 127.0.0.1 inside a container normally refers to that namespace, not the host. |
| Firewall | Traffic policy applied at a particular boundary | Local frontend state does not account for every cloud/router/namespace layer. |
| TLS | Protocol protecting a connection with cryptographic mechanisms | Encryption without intended peer verification does not establish the intended service identity. |
| Latency / throughput | Time per operation versus work completed per interval | One can improve while the other becomes worse. |
| Utilization / saturation | Resource busy proportion versus demand exceeding available service capacity | High utilization alone does not establish user impact. |
| Load average | Linux time-averaged runnable/uninterruptible-task measure | It is not CPU percent. |
| RSS | Resident memory attributed by a process view | Summing RSS can count shared pages more than once. |
| Pressure | Time workloads are stalled by resource contention | Occupancy/capacity and stall measurements answer different questions. |
| OOM | Allocation/limit failure leading to out-of-memory handling | Identify the victim, cgroup/host scope and timestamp before changing limits. |
| Log / metric / trace | Recorded event, numerical measurement and request-related execution context | Each has sampling, retention, visibility and interpretation limits. |
| Observation / hypothesis | Recorded evidence versus a proposed explanation | A log line adjacent to failure is not automatically the cause. |
| Acceptance criterion | Observable condition defining the intended result | Repeat the same relevant operation after a repair. |
| Rollback | Return toward a compatible previously approved state | Code rollback may not undo a database migration. |
| RPO / RTO | Acceptable recovery-point loss and recovery-time objectives | Measure actual restore behavior rather than copying a target into a result field. |
| SLI / SLO | Measured service indicator and an objective over a stated window | A host CPU threshold is not automatically a customer availability objective. |
| Failure domain | Boundary within which one cause can affect several components | Two replicas on one laptop do not remove the laptop failure. |

Use the [networking reference](linux-networking-reference.md) and [troubleshooting guides](../05-troubleshooting-and-recovery/README.md) to investigate a real symptom.

## Follow along

### Observe names, inodes and an open descriptor

Run this from an ordinary Bash shell. The Python checks exercise one tiny file, two directory entries and an open descriptor. They do not inspect or delete any existing data.

<!-- reference:exercise -->
```bash
glossary_lab=$(mktemp -d) || exit 1
python3 - "$glossary_lab" <<'PY'
import os
from pathlib import Path
import sys
root = Path(sys.argv[1])
original = root / 'original'
hard = root / 'hard'
alias = root / 'alias'
original.write_bytes(b'Linux reference example\n')
os.link(original, hard)
alias.symlink_to('original')
first, second = original.stat(), hard.stat()
assert (first.st_dev, first.st_ino) == (second.st_dev, second.st_ino)
assert first.st_nlink == 2
print('PASS: two names share one inode in this filesystem')
with original.open('rb') as opened:
    original.unlink()
    assert hard.read_bytes() == b'Linux reference example\n'
    assert alias.is_symlink() and not alias.exists()
    print('PASS: hard link survives; pathname-based symbolic link is dangling')
    hard.unlink()
    assert os.fstat(opened.fileno()).st_nlink == 0
    assert opened.read() == b'Linux reference example\n'
    print('PASS: open descriptor still reads after the final hard-link name is removed')
print('PASS: descriptor closed; only the dangling symbolic link remains')
PY
```

## Verify your result

Expect all four PASS messages. The inode numbers themselves vary, but the two hard-link names initially share the same device/inode pair. After removing the original name, the hard link still resolves, while the symbolic link's target name no longer does. After removing the final hard-link name, the already-open descriptor still supplies the bytes until it closes.

This explains one reason `df` and `du` can disagree during a deleted-open-file incident. The example does not prove how a particular filesystem, snapshot, quota or application handles durability or accounting. Do not delete real logs to reproduce it.

Explain in your own words which object each operation removed: a name, a symbolic-link target path, or an open reference. If an assertion fails, inspect the filesystem and actual links before continuing; stop rather than broadening the cleanup.

## Cleanup

After the checks pass, remove only the remaining symbolic link and empty temporary directory:

<!-- reference:cleanup -->
```bash
rm -i -- "$glossary_lab/alias"
rmdir -- "$glossary_lab"
```

## Sources

- [Linux link semantics](https://man7.org/linux/man-pages/man2/link.2.html), [unlink/open-reference semantics](https://man7.org/linux/man-pages/man2/unlink.2.html) and [path resolution](https://man7.org/linux/man-pages/man7/path_resolution.7.html).
- [Bash manual](https://www.gnu.org/software/bash/manual/) for shell language; [Linux man-pages](https://man7.org/linux/man-pages/) for kernel/libc interfaces.
- [Kernel namespaces](https://man7.org/linux/man-pages/man7/namespaces.7.html), [cgroup v2](https://docs.kernel.org/admin-guide/cgroup-v2.html) and [pressure accounting](https://docs.kernel.org/accounting/psi.html).
- [systemd service semantics](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html) and [OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/).

These are starting references, not a claim that every term has one implementation across all distributions. Use the [documentation map](linux-official-documentation.md) to find the installed-version interface behind a specific question.
