# Folders 4–8: assessment and content architecture

Assessment date: November 3, 2026. Starting point: `origin/main` at `bb13687366da1ba08fae346efe9f9bbc6f5dba35`. Work branch: `codex/folder-4-foundations`.

## What existed

The repository already had an appropriate subject taxonomy and a concise content standard. These provide a useful foundation, but navigation alone was not a learning resource.

| Collection | Tracked Markdown files | Empty files | Starting condition |
| --- | ---: | ---: | --- |
| 04 commands and cheat sheets | 42 | 31 | Collection landing page, 10 category indexes, empty command index and 30 empty topic references |
| 05 troubleshooting and recovery | 11 | 10 | Topic index; no diagnostic procedures |
| 06 production administration | 11 | 10 | Topic index; no operating procedures |
| 07 Linux distributions | 10 | 9 | Topic index; no distribution guidance |
| 08 resources and reference | 9 | 8 | Topic index; no reference content |

The root README linked to lowercase variants of several actual mixed-case folder names. This can fail on GitHub/Linux even when local filesystem behavior hides the mismatch. The initial repository had no LICENSE file; NOTICE preserved third-party terms but granted no reuse rights. There was no content-validation tool or recorded Linux execution evidence for folder 4. This assessment is about content and navigation; it is not a security audit of the whole repository or a full review of folders 0–3.

## The reader journey

A reader should be able to arrive from a search result, understand the environment, choose a task, see what will change, run a bounded exercise and explain the evidence. Navigation must work on GitHub without requiring a separate website or build system.

```text
Repository README
  └─ 04 collection home: conventions, compatibility, learning order
       ├─ command index: task → syntax → detailed reference
       └─ category README: scope → compact cheat sheet → references
            └─ topic reference: purpose → prerequisites → practice
                                → expected evidence → limitations → cleanup
```

Relative links keep the content usable in a checkout and in GitHub. Category names and existing topic paths are retained so future links have stable destinations. Each page links to its category, index and collection home. A separate website can later reuse this structure; a website deployment is outside this installment.

## Responsibilities across folders

| Folder | Primary question | Content contract | Avoid duplicating |
| --- | --- | --- | --- |
| 04 | How do I use this tool? | Syntax, effects, bounded examples, evidence and caveats | Full incident trees or production change plans |
| 05 | Why is this failing? | Impact, environment, observations, competing hypotheses, safe discriminating tests, recovery and verification | Repeating every command option |
| 06 | How do I operate this repeatedly? | Owner, prerequisites, change window, prechecks, steps, rollback, acceptance and evidence | Unreviewed one-line fixes |
| 07 | What differs on this distribution? | Release-specific packages, defaults, configuration owners, support assumptions and sources | Treating a family as one identical operating system |
| 08 | Where do I look something up? | Definitions, maintained official links, paths with exceptions and further study | Unlicensed copied material or unexplained link lists |

## Folder 4 implementation

All 30 existing reference pages are populated. Ten category READMEs now provide quick lookup tables and learning order. The command index groups syntax by operational task. The collection home explains shell syntax, permissions, tool availability, expected variation and how to use examples.

Each detailed page includes:

- A plain-language explanation of what the tool sees or changes.
- Assumptions, privileges, dependencies and distribution/version caveats.
- A compact syntax table distinguishing queries from changes.
- A bounded walkthrough using temporary data or read-only host inspection.
- Expected observations and their limits; no invented host-specific output.
- Cleanup where resources were created, and explicit no-cleanup notes otherwise.
- Common mistakes and links to upstream documentation.

A command reference cannot contain every Linux feature. This installment covers the existing folder’s ten domains. Future additions can include shell environment, scheduling, ACL practice and advanced network/storage labs when those have defined exercises and validation environments.

## Quality gates and evidence

Structural checks enforce nonempty pages, the reference contract, balanced fences, Bash syntax and case-exact local links in folder 4 and the root README. Portable walkthroughs can be checked locally in temporary directories. Linux-specific commands require real distribution testing; a macOS syntax check is not Linux execution evidence. The [validation record](../04-command-reference/VALIDATION.md) separates completed checks from pending ones.

Before claiming a tested Linux release, record its `/etc/os-release`, kernel, shell/tool versions, exact walkthrough, expected and actual observations, cleanup result and reviewer/date. Prioritize Debian/Ubuntu with systemd for APT and service checks, and a Fedora/RHEL-family VM for DNF and firewalld. Confirm installed versions rather than assuming current defaults.

## Next installments

1. Validate folder 4 on real Linux environments and refine any distribution-specific findings.
2. Build folder 5 around a shared diagnostic method, then complete one symptom guide at a time with controlled failures.
3. Build folder 6 around change safety, evidence, rollback and service ownership; reuse folder 4 references.
4. Build folder 7 with release-labelled comparisons verified against distribution documentation.
5. Build folder 8 with a glossary, filesystem/configuration/log reference and maintained official learning sources.

At the initial November 3 assessment, folders 5–8 remained scaffolded. See the follow-up below for later progress. Their existing index links are not evidence of completed guides. They should not be promoted as finished learning paths until their content and exercises pass review.

## Publication and licensing

The owner selected personal-study permission with written permission required for modification or redistribution. The custom license is restrictive and should be described as public educational content, not open source. GitHub’s public-repository viewing/forking rights and applicable statutory rights remain exceptions. Third-party rights and any prior grants must be respected; the draft cannot relicense material the owner does not control.

The [custom license](../LICENSE.md) is an owner-requested drafting aid, not a legal opinion. Obtain legal review of the rights-holder identity, jurisdiction, permissions workflow and compatibility with public hosting before publication. No remote push is part of this local implementation.

## Follow-up: November 4, 2026

Folder 5 now contains the shared troubleshooting method, eight symptom guides and recovery-verification guidance. Each guide includes environment assumptions, evidence interpretation, a controlled exercise, recovery acceptance and cleanup. Two bounded Python helpers support loopback HTTP and process observation.

The portable method, offline SSH, reachability and verification exercises have execution evidence. Linux-only systemd, DNS/NSS, tmpfs, /proc and boot checks remain pending. See the [folder 5 validation record](../05-troubleshooting-and-recovery/VALIDATION.md) before treating a scenario as tested. Folders 6–8 remain scaffolded. The remaining sequence is Linux reproduction and review, then production administration, distribution-specific notes and supporting references.

## Follow-up: production administration, November 4, 2026

Folder 6 now has ten runbooks with prerequisites, operating procedures, isolated practice, verification/rollback and cleanup. Eight portable exercises and the demonstration configuration validator have execution evidence; systemd, logrotate, visudo, package proposals and actual host/notification/retirement workflows still require Linux or platform review. See the [folder 6 validation record](../06-system-administration/VALIDATION.md). Folders 7–8 remain scaffolded.

## Follow-up: Linux distributions, November 4, 2026

Folder 7 now has nine guides covering distribution families, workload-based selection, Ubuntu/Debian/Fedora/enterprise-RPM administration, package tasks, mandatory policy and cross-family comparison. The guides separate identity hints from observed managers, product variants, enforcement and support evidence. Official-source review is dated; nine portable fixture/concept exercises and the limited identity reader have execution evidence. Real Linux product observations and upgrade/management compatibility remain pending in the [folder 7 validation record](../07-linux-distributions/VALIDATION.md). Folder 8 remains scaffolded.
