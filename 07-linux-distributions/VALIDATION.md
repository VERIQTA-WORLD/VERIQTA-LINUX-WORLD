# Validation and source-review record

Recorded November 4, 2026. All nine guide pages are written. Sources establish documented concepts and selected release facts; portable fixtures establish example behavior. Neither substitutes for observations on a running distribution/product variant.

## Completed checks

| Check | Method | Evidence and boundary |
| --- | --- | --- |
| Guide contract | `python3 tools/check_command_content.py` | Requires scope, practical differences, follow-along lab, verification/limits, cleanup and references in each guide |
| Markdown/navigation | Same checker and `git diff --check` | Case-exact local paths, heading anchors, fences, table-code pipes and whitespace |
| Bash and embedded Python | Same content checker | Syntax parsing without Linux host queries or changes |
| Nine portable exercises | `python3 tools/check_distribution_labs.py` | Executes published fixture, selection, task-mapping and access-model examples; verifies expected observations and temporary-directory removal |
| Identity hints | Same portable runner | Thirteen ID/ID_LIKE classifications, ordered relationship fallback, preserved variant/identity and explicitly unobserved tool/policy state |
| Invalid identity input | Same portable runner | Eight missing/empty/duplicate/quote/spacing/size/encoding/executable-content cases rejected |
| No shell execution | Same portable runner | Shell-like content in ignored metadata is not executed; recognized-field executable content is rejected without creating its marker |

The portable run used macOS/Darwin, Python 3.9.6 and Bash 3.2.57. No Linux host was installed or probed, no package-manager transaction was run, no network/security setting changed and no commercial support/certification was established by these exercises.

The identity helper reads only simple ID, ID_LIKE, VERSION_ID and VARIANT_ID values from a bounded supplied file. It intentionally rejects unsupported forms and duplicates. It is not a complete implementation of every os-release field/escape rule, a detector of installed managers, or an automatic command-selection system. Real applications should use their platform's maintained parser and verify actual state.

## Reproduce the checks

From the repository root:

```bash
python3 tools/check_command_content.py
python3 tools/check_distribution_labs.py
python3 tools/check_cheat_sheets.py
git diff --check
```

The content checker does not execute commands. The distribution runner executes only the bounded supplied-data/concept exercises and reader tests using temporary files. It excludes Linux observation blocks, package queries, security-state commands and any installation/upgrade workflow.

## Dated official-source review

| Topic | Sources reviewed or linked | What the guides claim |
| --- | --- | --- |
| Identity | systemd os-release specification | Identity fields and family hints do not establish running managers or policy |
| Ubuntu | Official coverage page, Server networking documentation and AppArmor guidance | Named 24.04 LTS study track; current coverage must be checked; Netplan/backend and profile state need observation |
| Debian | Official trixie release information, release tracks and Debian Reference networking | Debian 13/trixie identified as stable at review; documented support scope/dates; no universal network-manager claim |
| Fedora | Accepted DNF5 transition, official DNF5 package metadata and Atomic desktops page | DNF5 introduced with Fedora 41; historical introduction is not installation advice; variant/deployment model matters |
| Enterprise RPM | RHEL 10 DNF/SELinux documentation, Rocky/AlmaLinux documentation and CentOS Stream page | Related concepts but distinct product identity, compatibility/coverage evidence and continuously delivered Stream positioning |
| Other models | Alpine about/user handbook, NixOS manual, official pacman and Zypper manuals | musl/BusyBox/OpenRC distinctions, declarative generations and task-based package differences |
| Mandatory policy | Ubuntu AppArmor, RHEL SELinux and kernel LSM documentation | Inspect actual process/object/policy; do not infer enforcement from installed tools or bypass it as a generic fix |

Some Fedora lifecycle and Arch wiki fetches were blocked by their sites' automated-access protection; an openSUSE narrative documentation URL was unavailable. Official pacman/Zypper manuals and the accessible Fedora project sources were used for the corresponding concrete claims. The guides retain official lifecycle/maintenance links for the reader and avoid reproducing an unverified current Fedora support deadline. Selective source review is not an exhaustive external-link availability check.

Exact point releases, newest-release rankings, prices and a universal supported-package list are deliberately not maintained here. Re-check official release notes, package scope, architecture, image variant, advisories and entitlement when making a real selection or change.

## Linux reproduction still required

| Target | Required observations | Status |
| --- | --- | --- |
| Conventional Ubuntu 24.04 LTS reference VM | Identity, package candidates/origins, Netplan backend, DNS ownership, SSH activation and actual AppArmor state | Pending |
| Debian 13 reference VM | Identity/architecture, repositories/candidate, real networking/resolver owner, service/log and policy state | Pending |
| Supported conventional Fedora release | Exact release, installed DNF implementation, repository behavior, network/policy state and support source/date | Pending |
| Actual Fedora Atomic/image product | Identity variant, deployed image/tooling, host-versus-container boundaries and supported update procedure | Pending |
| RHEL 9/10 and selected related product | Exact identity, DNF/repository access, architecture/hardware requirements, network/SELinux state and product-specific support evidence | Pending |
| openSUSE/Arch/Alpine/NixOS | Reproduce only the claimed task/model on a named supported target and record actual tool/runtime differences | Pending |
| Actual selection/upgrade | Workload/vendor compatibility, image verification, coverage, recovery and supported upgrade path | Pending |
| GitHub rendering/independent reader | Visual table/code review and reproduction without unstated setup | Pending |

No Linux VM was used during this authoring pass. Record reviewer/date, repository commit, exact product/release/variant, architecture, image source, kernel, tool versions, privileges and execution boundary for each pending run. Preserve actual outputs, interpretations, cleanup and source dates. Do not replace a missing observation with a guessed family default.

The existing custom personal-study license remains unchanged. Public availability does not make this installment an open-source license grant.

[Collection home](README.md) · [Content standard](../CONTENT-STANDARD.md)
