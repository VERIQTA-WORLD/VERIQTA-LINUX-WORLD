# Validation record and reviewer checklist

Recorded November 3, 2026. Content status: all existing folder 4 topic pages are written; Linux execution review remains pending. Do not equate complete written coverage with release certification.

## Completed checks

| Check | Method | Result and boundary |
| --- | --- | --- |
| Reference contract | `python3 tools/check_command_content.py` from repository root | Checks all 30 detailed references for the required sections and an upstream reference |
| Navigation | Same checker | Checks local links in folder 4, root README, assessment, licensing and contribution pages, including exact case and linked Markdown heading anchors |
| Shell syntax | Same checker with installed Bash | Parses all fenced Bash walkthroughs without executing them; not a check of Linux option support |
| Markdown hygiene | `git diff --check` | Checks introduced whitespace problems; table pipes are also checked by the content checker |
| Portable walkthroughs | `python3 tools/check_portable_examples.py` | Nine actual walkthroughs executed on macOS; expected text, explicit file comparisons where present, final status and removal of temporary directories checked |
| Review of dangerous effects | Editorial inspection | Modification syntax separated from read-only walkthroughs; no partition formatting, LVM resizing, account removal or firewall activation walkthrough |

The portable run covers navigation, file management, file search, grep, sed, awk, pipes/redirection, tar and rsync. It supplies yes responses to the documented cleanup prompts inside those isolated scripts. It is an optional **execution** check, unlike the non-executing structural checker. Review scripts before running them.

The authoring host is Darwin/macOS with Bash and BSD/platform utilities; those successful runs do not validate GNU-specific variants elsewhere in the collection. Docker CLI exists but its daemon was unavailable. No Linux VM or container execution was completed in this installment.

Selected upstream documentation was consulted for semantics, including systemctl, ip, APT, DNF5 install, rsync, LVM, mount, OpenSSH, firewalld and vmstat. GNU documentation requests timed out in this session; links point to upstream manuals but their content was not fetched successfully. No exhaustive external-link availability check or independent expert review is claimed.

## Linux execution review still required

Use disposable machines and one walkthrough at a time. Do not turn table syntax into an automated privileged test suite.

| Environment | Review focus | Status |
| --- | --- | --- |
| Debian/Ubuntu-family VM with systemd | GNU file/text examples; users/modes/sudo; systemctl and journalctl; APT simulation; ip/ss/DNS; procps/sysstat; archive/restore | Pending |
| Fedora/RHEL-family VM | Installed DNF implementation and proposal behavior; RPM query; firewalld inspection; names/defaults that differ | Pending |
| VM with pre-existing disposable LVM storage | pvs/vgs/lvs visibility and relation to filesystems; no creation or resize required | Pending |
| Authorized SSH lab client/server | Host-key verification, configured port, authentication, real remote connection and exit | Pending |
| Target hosting preview | GitHub-rendered tables, code fences, images and navigation reviewed visually | Pending |

For each walkthrough record:

```text
Review date and reviewer:
Page and repository revision:
Distribution / release (/etc/os-release):
Kernel / architecture (uname -r; uname -m):
Shell and relevant tool versions:
Privileges and installed optional packages:
Exact commands exercised:
Expected observations:
Actual observations and exit statuses:
Differences, warnings or missing tools:
Cleanup verified / state changed:
Conclusion and follow-up:
```

If a command differs, update its environment note and expected results using the installed manual and official distribution documentation. Re-run the affected walkthrough and structural checks. Preserve meaningful error outcomes: no grep match, a missing service, a denied sudo request or an absent LVM layout are not interchangeable with command success.

## Acceptance before publication as tested content

- [ ] Record actual versions and results on the chosen Linux environments.
- [ ] Review syntax tables and walkthroughs for the named utility versions.
- [ ] Confirm negative cases and expected nonzero statuses are explained.
- [ ] Verify every created resource is removed or intentionally retained with instructions.
- [ ] Check GitHub rendering and navigation visually.
- [ ] Resolve license rights-holder identity and obtain legal review of the custom terms.
- [ ] Have another reviewer reproduce representative examples without unstated setup.

The collection is ready for content review, with these execution and publication gates visible. Folders 5–8 remain outside this implementation.

[Collection home](README.md) · [Architecture assessment](../docs/folders-04-08-assessment.md)
