<div align="center">

![LINUX-WORLD](assets/images/linux-world-cover.svg)

# LINUX-WORLD

**Understand Linux, practise with evidence, and build systems you can explain, operate and recover.**

[Start here](00-start-here/README.md) · [Choose a learning path](00-start-here/choose-your-learning-path.md) · [Learn Linux](01-Beginner-to-Advanced) · [Practise labs](02-Labs) · [Build projects](03-Projects) · [Find commands](04-command-reference/README.md)

</div>

LINUX-WORLD connects explanations, command references, practical exercises, projects and operational judgment. Its scope is growing from Linux foundations and server operations into everyday desktop use, developer workstations, automation, containers, security, observability, declarative systems and Linux internals.

We build this collection **folder by folder**. A planned topic is not a completed course, and a written walkthrough is not automatically a tested Linux scenario. Follow each collection's validation record for actual execution evidence and remaining limits.

## Explore the current collections

| Collection | Purpose | Current scope |
| --- | --- | --- |
| [00 · Start here](00-start-here/README.md) | Orientation, safe practice and learning paths by goal and experience | Entry point for choosing a route and recording progress |
| [01 · Beginner to advanced](01-Beginner-to-Advanced) | Progressive Linux lessons | Existing collection; names, structure and lesson content retained |
| [02 · Labs](02-Labs) | Focused practice and controlled failures | Existing collection retained |
| [03 · Projects](03-Projects) | Combine skills into working systems | Existing collection retained |
| [04 · Command reference](04-command-reference/README.md) | Understand command purpose, syntax, effects and verification | Detailed references plus the consolidated [70 cheat sheets](04-command-reference/cheat-sheet-index.md) |
| [05 · Troubleshooting and recovery](05-troubleshooting-and-recovery/README.md) | Investigate evidence, test explanations and verify recovery | Written guides and selected executed portable scenarios; further Linux failure testing remains pending |
| [06 · System administration](06-system-administration/README.md) | Operate individual hosts and plan changes across fleets | Existing runbooks with single-host/fleet guidance and explicit production requirements |
| [07 · Linux distributions](07-linux-distributions/README.md) | Choose and compare releases, variants and management models | Written guides, official references and portable comparison exercises |
| [08 · Resources and reference](08-resources-and-reference/README.md) | Curated glossary, documentation map and reference library | Collection plan established; detailed reference pages remain to be built |

Folders 1–3 retain their existing names, organization and learning content. Only three existing Start Here links in folders 2–3 were updated to follow the renamed entry point.

## Planned collections: build one at a time

These folders contain scope/roadmap pages only. They are not presented as completed tutorials or validated projects.

| Collection | What belongs here | Status |
| --- | --- | --- |
| [09 · Desktop and workstation Linux](09-desktop-and-workstation-linux/README.md) | Installation, desktop environments, applications, accessibility, displays, audio, power, peripherals, backups and developer workstations | Planned |
| [10 · Automation and reproducibility](10-automation-and-reproducibility/README.md) | Reliable Bash/Python automation, configuration management, provisioning, repeatable builds and CI validation | Planned |
| [11 · Containers and isolation](11-containers-and-isolation/README.md) | Namespaces, cgroups, rootless containers, OCI images, storage/networking and host-versus-container troubleshooting | Planned |
| [12 · Security and software trust](12-security-and-software-trust/README.md) | Identity, least privilege, mandatory policy, secrets, encryption, package/image verification and security maintenance | Planned |
| [13 · Performance and observability](13-performance-and-observability/README.md) | Workload measurement, profiling, tracing, eBPF, metrics/logs/traces, service objectives and capacity | Planned |
| [14 · Image-based and declarative Linux](14-image-based-and-declarative-linux/README.md) | Image-based hosts, declarative configuration, deployments, generations, updates and rollback | Planned |
| [15 · Linux internals and development](15-linux-internals-and-development/README.md) | Boot, processes, memory, filesystems, kernel interfaces, building/debugging software and contributing upstream | Planned |

## Find your learning path

| Your goal | Begin with | Continue toward |
| --- | --- | --- |
| First steps with Linux | [Orientation and safe setup](00-start-here/README.md), then [existing lessons](01-Beginner-to-Advanced) | Navigation, files, permissions, text and small exercises |
| Everyday desktop/workstation use | Foundations and [distribution selection](07-linux-distributions/choosing-a-linux-distribution.md) | Folder 9 when its lessons are built |
| Development on Linux | Relevant existing lessons, labs and projects | Reproducible environments, automation and isolation as folders 9–11 develop |
| System administration | Foundations, [system administration](06-system-administration/README.md) and [troubleshooting](05-troubleshooting-and-recovery/README.md) | Verified recovery, fleet changes, automation, security and observability |
| Advanced Linux engineering | Demonstrated foundations and independent project work | Folders 11–15 as their tested material becomes available |

[Choose a route by goal and experience](00-start-here/choose-your-learning-path.md). Returning readers can use the [command index](04-command-reference/command-index.md) and [cheat-sheet index](04-command-reference/cheat-sheet-index.md) without following every lesson in order.

## How we build useful learning material

Understand the concept, inspect what the tool reads or changes, practise in isolation, verify the result and explain the evidence. Where appropriate, progress toward automation, a controlled failure and recovery. Use explicit prerequisites and meaningful acceptance checks rather than treating a command's exit status as proof the whole system is healthy.

- [Existing lessons](01-Beginner-to-Advanced), [labs](02-Labs) and [projects](03-Projects) remain available.
- [Command validation](04-command-reference/VALIDATION.md), [recovery validation](05-troubleshooting-and-recovery/VALIDATION.md), [administration validation](06-system-administration/VALIDATION.md) and [distribution validation](07-linux-distributions/VALIDATION.md) distinguish executed checks from pending Linux work.
- [Content standard](CONTENT-STANDARD.md) defines expectations for explanation, scope, practice and recovery.
- [Repository structure and migration](docs/repository-structure.md) records canonical paths, boundaries and the folder-by-folder plan.

## Feedback and permissions

Report incorrect explanations, broken navigation and reproducible differences with the relevant distribution/tool versions. Keep credentials and private incident evidence out of public reports. See [feedback and contribution guidance](CONTRIBUTING.md).

This repository is public educational material under the custom [VERIQTA Personal Study License](LICENSE.md). Personal study and the permitted exercise execution are allowed; modification and redistribution require written permission, subject to the license's exceptions. These are restrictive terms, not an open-source license. See [NOTICE](NOTICE.md) for third-party rights.

## About VERIQTA WORLD

[VERIQTA WORLD](https://github.com/VERIQTA-WORLD) shares engineering resources that connect learning with practical work. Names and trademarks belong to their owners; this independent resource does not imply endorsement or affiliation.
