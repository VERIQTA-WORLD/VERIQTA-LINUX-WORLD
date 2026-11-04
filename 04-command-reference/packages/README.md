# Packages

Identify your distribution and package-manager implementation before reviewing any package transaction.

## Detailed references

1. [Inspect and manage APT packages](apt-reference.md)
2. [Inspect and manage DNF packages](dnf-reference.md)

## At a glance

These are lookup examples; follow the linked page for prerequisites, expected results and cleanup. Uppercase arguments are placeholders, not literal targets.

| Task | Syntax | Full explanation |
| --- | --- | --- |
| Search repository metadata. | `apt search NAME` | [Inspect and manage APT packages](apt-reference.md) |
| Describe an available package. | `apt show PACKAGE` | [Inspect and manage APT packages](apt-reference.md) |
| Show installed/candidate versions and repository priorities. | `apt-cache policy PACKAGE` | [Inspect and manage APT packages](apt-reference.md) |
| Identify installed implementation and version. | `dnf --version` | [Inspect and manage DNF packages](dnf-reference.md) |
| List enabled repositories. | `dnf repolist` | [Inspect and manage DNF packages](dnf-reference.md) |
| Describe package metadata. | `dnf info PACKAGE` | [Inspect and manage DNF packages](dnf-reference.md) |

## Practice checkpoint

Work through the references in the order above. Explain what each command reads or changes, identify the relevant permission boundary, and record one successful result and one limitation. Use each page’s cleanup instructions; do not invent a blanket recursive deletion.

[Collection home](../README.md) · [Command index](../command-index.md) · [LINUX-WORLD](../../README.md)
