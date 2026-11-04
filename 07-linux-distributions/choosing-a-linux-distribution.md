# Choosing a Linux distribution

Choose for the workload, learning objective and maintenance capability. A familiar desktop, the smallest image or the longest advertised support period is not automatically the right production choice. Separate requirements that must pass from preferences you can trade off.

## Scope and environment

The decision process applies to personal labs, development and operated services. Product licensing/support, hardware, architecture, packages and release availability require current official verification. Source review here is dated November 4, 2026; do not treat a saved comparison as a future support guarantee.

The exercise uses synthetic candidates in Python and a temporary record. It installs nothing, needs no root and does not rank real products as universally best.

## What changes in practice

### Start with disqualifying constraints

| Requirement | Evidence to seek | Why it matters |
| --- | --- | --- |
| Application/vendor support | Exact product, release, architecture and runtime support statement | Similar package names do not establish a supported deployment |
| Hardware/virtualization | Supported CPU level, drivers, firmware and provider image | A newer major release can raise requirements |
| Lifecycle and update responsibility | Current release/package coverage, team owner and upgrade plan | Long advertised coverage can depend on package scope or entitlement |
| Recovery | Console access, compatible backups, reproducible image and tested restore | An unfamiliar recovery model increases operational risk |
| Repository trust | Official origins, approved third-party dependencies and signing policy | Installation convenience can create an unmaintained dependency chain |
| Security/organization policy | Required enforcement, identity integration and validated controls | A product name alone does not prove configured compliance |
| Team capability | Time and experience for updates, troubleshooting and release transitions | A release cadence must fit the operating model |

Requirements should be specific enough to verify. “Needs Linux” is weaker than an application's supported release/architecture/runtime matrix. “Has LTS” is weaker than verified coverage for the actual packages through the required operating period.

### Choose learning depth deliberately

For first host-administration exercises, a supported conventional Ubuntu/Debian or Fedora/enterprise-RPM VM can expose the tools used elsewhere in this repository. Choose one family first, learn its recovery path, then compare another. This is a scoped learning approach, not a claim that those products are best for every user.

For learning lightweight userspace and compatibility, Alpine exposes musl/BusyBox and a different init approach. For declarative system management, NixOS teaches a different configuration/activation model. Rolling and image-based products can be valuable learning targets when their maintenance model is part of the goal.

Do not substitute a container for every VM exercise: kernel, storage mounting, boot recovery, device access and full service-management behavior need the relevant host context.

### Verify the chosen artifact

Obtain images from the official project/vendor or trusted cloud publisher. Verify checksums/signatures using that provider's documented process and trusted keys. Match architecture and product variant. Record release source, image identity, verification result, required subscription/entitlement where applicable and recovery instructions. Do not publish credentials or purchased-access secrets.

## Follow-along lab

A fictional service requires vendor support, sufficient support horizon and an approved recovery process. Candidate A is familiar but fails vendor support. Candidate B meets all supplied requirements:

```bash
choice_lab=$(mktemp -d)
python3 - "$choice_lab/decision.txt" <<'PY'
from pathlib import Path
import sys
candidates = {
    'Candidate A': {'vendor_support': False, 'horizon': True, 'recovery': True},
    'Candidate B': {'vendor_support': True, 'horizon': True, 'recovery': True},
}
rows = []
for name, checks in candidates.items():
    missing = [key for key, value in checks.items() if value is not True]
    rows.append(name + (': REJECTED: ' + ', '.join(missing) if missing else ': eligible for further comparison'))
rows.append('Preference scoring happens only after mandatory requirements pass')
Path(sys.argv[1]).write_text('\n'.join(rows) + '\n')
PY
cat "$choice_lab/decision.txt"
```

Expect A rejected and B eligible, not automatically approved for production. The booleans are supplied exercise assumptions, not real vendor evidence. As an extension, replace the candidates with your own shortlist and attach dated official evidence to every required condition before any preference score.

## Verification and limits

A defensible choice names the exact product/release/variant, workload, required conditions, supporting sources, operating owner and rejected alternatives with reasons. Revisit when support, hardware, dependencies or the team changes.

The exercise tests decision logic only. Before selecting a real image, review the official current lifecycle and support matrix. Examples of starting points are [Ubuntu coverage](https://ubuntu.com/about/release-cycle), [Debian release information](https://www.debian.org/releases/), [Fedora lifecycle](https://docs.fedoraproject.org/en-US/releases/lifecycle/) and [RHEL lifecycle](https://access.redhat.com/support/policy/updates/errata).

## Cleanup

```bash
rm -i -- "$choice_lab/decision.txt"
rmdir -- "$choice_lab"
```

No image was downloaded or deployed.

## References

- [Ubuntu releases and coverage](https://ubuntu.com/about/release-cycle).
- [Debian releases](https://www.debian.org/releases/) and [RHEL lifecycle policy](https://access.redhat.com/support/policy/updates/errata).
- [Server readiness](../06-system-administration/linux-server-readiness-checklist.md).

[Collection home](README.md) · [Distribution families](understanding-linux-distribution-families.md)
