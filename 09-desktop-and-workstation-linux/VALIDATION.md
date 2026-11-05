# Workstation examples: validation and reproducibility

[Collection home](README.md)

The ten marked command-line examples and their cleanup blocks were executed on **4 November 2026**, as ordinary users in three disposable **aarch64 Linux VMs**. The checker extracts the exact published Bash blocks from the guides. It does not substitute separately rewritten test implementations.

## Named environments

| Environment | Kernel | Python | CLI fixtures and cleanup |
| --- | --- | --- | --- |
| Ubuntu 24.04.5 LTS | `6.8.0-142-generic` | `3.12.3` | 10 of 10 passed |
| Debian 13, trixie | `6.12.111+deb13-cloud-arm64` | `3.13.5` | 10 of 10 passed |
| Fedora 44 Cloud Edition | `6.19.10-300.fc44.aarch64` | `3.14.3` | 10 of 10 passed |

The VMs used existing distribution Python and util-linux packages. The additional `desktop-file-utils` prerequisite was installed through their distribution package managers: Ubuntu `0.27-2build1`, Debian `0.28-1` and Fedora `0.28-5.fc44`. Package installation required administration **inside the disposable VMs**; the examples and checker themselves ran without sudo. No desktop environment was installed for this execution pass.

## What the checks establish

| Guide | Executed result | Limit |
| --- | --- | --- |
| Installation | Original synthetic bytes matched a digest; changed bytes were detected | No actual ISO signature verification, installer or disk operation was performed |
| Desktop/accessibility | Explicit UTF-8 content round-tripped with different byte/character counts | No font, layout, screen-reader, focus or keyboard-navigation result is claimed |
| Applications | A private `.desktop` entry passed the real `desktop-file-validate` tool | It was not installed, discovered in a menu, launched or assigned as a default |
| Displays | Actual DRM interface availability and any connector/mode information were recorded | No monitor modes or graphical output were changed |
| Audio/video | A one-second PCM WAV was generated and its parameters/payload read back exactly | No audio playback, microphone recording, camera or screen sharing was exercised |
| Power | Actual exposed power-supply attributes were read without modification | No battery endurance, power profile, suspend, hibernation or resume test was performed |
| Peripherals | Actual block-device metadata was read through `lsblk` and parsed | No real USB transfer, print job, pairing, mount or filesystem repair was performed |
| Backups | Restore bytes matched; corruption of the restored copy was detected; re-restoration recovered them | All fixture directories shared one temporary filesystem; this is not independent backup protection |
| Development | An explicit virtual environment ran a meaningful test, detected a deliberate regression and passed after source recovery | No network dependency install, editor integration, Git credential or container workflow was exercised |
| Troubleshooting | Working-directory-dependent failure was reproduced and a path repair verified in two contexts | No real desktop profile, session, launcher or package was changed |

Ubuntu and Fedora exposed an empty DRM connector inventory in these headless configurations. Debian did not expose `/sys/class/drm`; the published example recorded `interface_available: false` and an empty connector list. All three exposed an empty power-supply inventory. These are **absence/visibility observations**, not evidence that a monitor or battery works or fails.

The checker requires zero exit status, the stated success markers and no remaining fixture paths after cleanup. The Python assertions inside the examples check the specific intended behavior. Cleanup prompts receive automatic confirmation only within the isolated test process and newly created fixture directories. Raw reports contain machine-specific output and are kept outside the repository.

## Reproduce the CLI checks

Use an ordinary Linux account with Bash, Python 3 including `venv`, `desktop-file-validate` and util-linux `lsblk`. The power example additionally requires the readable `/sys/class/power_supply` interface; absent hardware within that interface is a valid empty result. Run from the repository root:

```bash
python3 tools/check_command_content.py
python3 tools/check_repository_structure.py
python3 tools/check_workstation_examples.py
```

To retain evidence, choose a new private path outside the repository:

```bash
python3 tools/check_workstation_examples.py --report /tmp/linux-world-workstation-report.json
```

The checker refuses root execution, a non-Linux platform, an existing report or a report inside the repository. Reports are created with mode `0600` and include source-page SHA-256 digests, statuses, output, platform identity and cleanup results. Inspect and redact any report before sharing it. Re-running with the same report name deliberately fails rather than overwriting evidence.

Structural checks cover required guide sections, local links/anchors, Bash syntax, embedded Python syntax and canonical collection navigation. They do not execute optional table fragments or verify external sites exhaustively.

## Verify graphical and hardware outcomes separately

The guides contain local tasks and acceptance criteria for an actual desktop. Before relying on your workstation, perform the checks relevant to you and keep a private record of distribution/release, desktop/session, hardware connection, observed outcome and recovery. Mark a missing device **not available**, and an unperformed task **not verified**.

| Workflow | Acceptance evidence on your actual machine |
| --- | --- |
| Installation | Boots with installer detached, signs in, retains a file and has a usable recovery route |
| Accessibility | Required applications, dialogs, sign-in/lock and input routes are usable with your own assistive tools |
| Displays | Intended modes/layout are readable and recover correctly after an unsuccessful change or dock reconnection |
| Media | Intended physical output, microphone, local camera preview and harmless sharing selection work; capture stops afterward |
| Power | A saved local session resumes and passes lock, input, display, network and audio checks |
| Peripherals | An authorized device performs its intended job; a copied file survives safe removal/reconnect and verifies |
| Real backup | Representative data restores into a new location from an independently protected destination and opens correctly |
| Development | Your editor and documented terminal command use the intended environment; a clean project setup passes its checks |

These graphical/hardware procedures were **not executed during this validation pass**. Headless CLI success does not establish desktop usability, driver compatibility, accessibility support or physical-device behavior. The collection's procedures are written with explicit checkpoints and recovery limits so you can verify those outcomes in the relevant environment.

Primary documentation was reviewed for the described concepts and tools. Desktop menus, firmware behavior, portals, package versions and application permissions evolve; use the documentation matching your installed release. This record is scoped technical evidence, not a hardware certification or a claim that every desktop and distribution was tested.
