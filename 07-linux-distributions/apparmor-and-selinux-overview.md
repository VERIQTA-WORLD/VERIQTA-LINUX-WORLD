# AppArmor and SELinux overview

Linux access decisions can involve more than user/group mode bits. Mandatory access control can constrain a process even when ordinary file permissions appear to allow its operation. Learn to identify the active policy, the process and the attempted operation before changing enforcement.

## Scope and environment

This is an operational comparison, not a complete policy-writing course. Standard Ubuntu documents AppArmor as installed/loaded by default; RHEL documents SELinux enforcing as its normal installed default. Other releases, derivatives, images, containers and administrator choices can differ. See [Ubuntu's guide](https://ubuntu.com/server/docs/how-to/security/apparmor/) and [RHEL's guide](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/using_selinux/index).

Actual tools, audit records and securityfs access depend on installation and permission. The portable exercise models two necessary checks with synthetic booleans; it probes or changes no host policy.

## What changes in practice

### Different policy models, shared investigation discipline

| Area | AppArmor | SELinux |
| --- | --- | --- |
| Primary organizing model | Profiles associated with programs, frequently expressing pathname-based access | Security contexts/types associated with processes and objects, governed by policy |
| State to inspect | Loaded profiles, profile modes and whether the process is confined | Global mode, process domain, object labels and relevant policy settings |
| Read-only starting tools | `sudo aa-status`, process context and kernel/audit records | `getenforce`, `sestatus`, context-aware ls/ps and audit queries |
| Investigative focus | Exact profile, operation, path and denied permission | Exact source domain, target context, class, permission and applicable policy |
| Common mistake | Assuming every process is confined because AppArmor is loaded | Assuming a readable mode bit guarantees access from every domain |

These are organizing descriptions, not a full implementation equivalence. Profile inheritance, transitions, namespaces, capabilities, other LSMs and application sandboxes can add complexity. Active LSM combinations depend on kernel support and configuration; installed utilities alone do not establish enforcement.

### Observe the actual context

On a relevant Linux system, select the tools that exist:

```bash
cat /sys/kernel/security/lsm
sudo aa-status
getenforce
sestatus
```

The LSM file requires securityfs to be mounted and readable. Missing output or a permission error is not proof that all policy is disabled. AppArmor's loaded/enforce/complain states and SELinux's enforcing/permissive/disabled states describe different scopes. A system mode alone does not identify the particular process's access decision.

For a known process/path, investigate identity and context:

```bash
ps -p PID -o pid,user,comm
cat /proc/PID/attr/current
namei -l -- DIRECTORY
ls -Zd -- DIRECTORY
ps -eZ
```

Replace PID and DIRECTORY first. Context-aware flags depend on the installed tools/policy. Do not publish unrelated process arguments, identity details or private file paths. Repeat the actual failed operation only if authorized and safe.

### Interpret a denial before proposing policy

Collect a narrow time window. SELinux systems can use `sudo ausearch -m AVC -ts recent`; AppArmor events may be present in kernel/journal/audit records. Confirm timestamp, process identity, attempted path/object and operation. A denial adjacent to an incident is not automatically causal; compare the original application's result.

| Finding | Appropriate next question |
| --- | --- |
| File moved into a service path has an unexpected SELinux label | What persistent file-context mapping is intended, and does a no-change relabel preview match it? |
| AppArmor profile omits an intended application path | Is that path part of the supported deployment and which narrow permission is justified? |
| Ordinary traversal/identity check already fails | Is the Unix/ACL identity boundary correct before considering a policy grant? |
| Policy logs but does not enforce this access | Is another layer causing the observed denial? |
| No matching audit event | Are logging/access/time/context assumptions correct, and could another layer deny access? |

A quick context change can be overwritten by relabeling; persistent policy and current labels are separate. Policy-generation suggestions can include permissions broader than intended. Do not blindly accept generated allow rules, put all profiles into learning mode, disable mandatory enforcement or use chmod 777 as a generic fix.

### Make policy changes as reviewed configuration

Define the legitimate operation, smallest intended access, owner, affected domains/profiles, rollback and verification. Test both the intended operation and a representative access that should remain denied. Use the distribution's documented persistent configuration and local policy packaging. A successful application action after disabling a control is diagnostic evidence at most, not a satisfactory permanent security state.

## Follow-along lab

This simplified exercise considers ordinary permission and a separate mandatory-policy result. It does not reproduce a real Linux access-control engine:

```bash
policy_lab=$(mktemp -d)
python3 - "$policy_lab/decisions.txt" <<'PY'
from pathlib import Path
import sys
cases = [
    ('ordinary allowed, policy denied', True, False),
    ('ordinary denied, policy allowed', False, True),
    ('both example checks allow', True, True),
]
rows = []
for name, ordinary, policy in cases:
    rows.append(name + ': ' + ('ALLOW in this model' if ordinary and policy else 'DENY in this model'))
rows.append('Real decisions need actual process, object, operation and complete policy context')
Path(sys.argv[1]).write_text('\n'.join(rows) + '\n')
PY
cat "$policy_lab/decisions.txt"
```

Expect the first two cases denied and the third allowed **in this model**. Explain why changing mode bits alone cannot make the first case pass, and why a mandatory-policy allowance alone does not solve the second. Actual capability/identity/kernel rules can change which checks apply; this is a conceptual boundary exercise only.

## Verification and limits

For a real investigation, retain the exact failing operation, identity/domain/profile, object/path, time, ordinary access evidence, policy decision and tested correction. Verify intended enforcement remains enabled and unrelated access was not broadened. Inspect a new successful request and the absence of recurring relevant denials over an appropriate window.

The exercise changed no mode, label, boolean, profile or host enforcement. It cannot establish a specific system's security posture. Separate VM observations confirmed loaded AppArmor profiles on Ubuntu/Debian and SELinux enforcing on Fedora 44. No targeted policy change was validated; see the [execution record](VALIDATION.md).

## Cleanup

```bash
rm -i -- "$policy_lab/decisions.txt"
rmdir -- "$policy_lab"
```

## References

- [Ubuntu AppArmor operations](https://ubuntu.com/server/docs/how-to/security/apparmor/).
- [RHEL 10 SELinux concepts and operations](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/using_selinux/index).
- [Linux Security Modules](https://docs.kernel.org/admin-guide/LSM/index.html).
- [Permission command reference](../04-command-reference/users-and-permissions/permissions-and-ownership.md) and [security inspection commands](../04-command-reference/security/access-audit-commands.md).

[Collection home](README.md)
