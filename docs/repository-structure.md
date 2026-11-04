# Linux World structure and migration

This is the owner-approved structural plan, implemented November 4, 2026. Collections will be expanded one at a time. A directory/roadmap page is not a completed course or a claim of tested Linux behavior.

## Canonical paths

| Number | Collection | Purpose |
| --- | --- | --- |
| 00 | [00-start-here](../00-start-here/README.md) | Orientation, environment, safety and paths by goal/experience |
| 01 | [01-Beginner-to-Advanced](../01-Beginner-to-Advanced) | Existing lesson sequence; retained |
| 02 | [02-Labs](../02-Labs) | Existing labs; retained |
| 03 | [03-Projects](../03-Projects) | Existing projects; retained |
| 04 | [04-command-reference](../04-command-reference/README.md) | Detailed explanations and consolidated command tables |
| 05 | [05-troubleshooting-and-recovery](../05-troubleshooting-and-recovery/README.md) | Evidence-led investigation and tested-scenario expansion |
| 06 | [06-system-administration](../06-system-administration/README.md) | Individual hosts, fleet boundaries and explicit production requirements |
| 07 | [07-linux-distributions](../07-linux-distributions/README.md) | Families, product variants and actual-state comparisons |
| 08 | [08-resources-and-reference](../08-resources-and-reference/README.md) | Planned curated glossary, documentation map and reference library |
| 09 | [09-desktop-and-workstation-linux](../09-desktop-and-workstation-linux/README.md) | Planned everyday/workstation Linux |
| 10 | [10-automation-and-reproducibility](../10-automation-and-reproducibility/README.md) | Planned automation, provisioning and reproducibility |
| 11 | [11-containers-and-isolation](../11-containers-and-isolation/README.md) | Planned isolation, OCI and container operations |
| 12 | [12-security-and-software-trust](../12-security-and-software-trust/README.md) | Planned identity, policy, encryption and provenance |
| 13 | [13-performance-and-observability](../13-performance-and-observability/README.md) | Planned measurement, tracing, signals and service objectives |
| 14 | [14-image-based-and-declarative-linux](../14-image-based-and-declarative-linux/README.md) | Planned image/declarative deployments and rollback |
| 15 | [15-linux-internals-and-development](../15-linux-internals-and-development/README.md) | Planned internals, software development and upstream work |

## Migration map

| Previous path | Canonical destination |
| --- | --- |
| `00-Start-Here` | `00-start-here` |
| `00-Start-Here/Choose-Your-Learning-Path.md` | `00-start-here/choose-your-learning-path.md` |
| `00-Start-Here/How-to-Use-Linux-World.md` | `00-start-here/how-to-use-linux-world.md` |
| `04-commands-and-cheat-sheets` | `04-command-reference` |
| `06-production-administration` | `06-system-administration` |
| `09-cheat-sheets` | `04-command-reference/cheat-sheets` |

There is one command-reference collection. The 70 two-column command sheets remain in its cheat-sheets subdirectory and are discovered through the [sheet index](../04-command-reference/cheat-sheet-index.md). They are not duplicated into a second top-level folder.

Links affected by the moved collections and Python tool/example paths are updated to canonical destinations. Existing published URLs to the old GitHub paths are not automatically redirected by this change; use the map above for bookmarks. Old content trees are not duplicated as compatibility folders. Existing SVG filenames are retained so their asset URLs continue to work, while the command/system-administration cover labels reflect the new names.

## Boundaries of this installment

Folders 1–3 retain their names, structure and learning content. The owner explicitly approved only three link-target corrections inside them: Start Here links in 02-Labs/README.md, 03-Projects/README.md and 03-Projects/01. Junior/README.md. No lesson, exercise or project content is rewritten.

Start Here gains orientation and routes by goal/experience. System administration's landing page distinguishes personal/lab hosts, fleet changes and production obligations. Troubleshooting's landing page identifies already executed portable scenarios and the pending Linux failure-testing backlog. Folder 8 receives a reference-library scope/status page; its empty topic files remain future work. Folders 9–15 contain roadmap READMEs only.

## Verification for the migration

Use the repository structure checker, content checker, sheet checker and relevant portable runners. The structure checker can compare protected folders and all moved cheat sheets against an explicit baseline commit during this migration. It also validates canonical folder names, roadmap status and local links in the structural navigation.

Actual results and the preservation baseline are recorded in [migration validation](structure-migration-validation.md). Passing navigation, syntax and portable checks does not complete the Linux runtime validation already pending within the existing collections.

[LINUX-WORLD](../README.md)
