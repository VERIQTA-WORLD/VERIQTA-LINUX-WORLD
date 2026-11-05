# Desktop and workstation Linux

Build a Linux computer you can use, maintain and recover. Work through installation, accessible everyday use, applications, hardware, personal data and development with clear checks at each step. You will learn how the pieces connect and how to investigate failures without resetting everything.

## Choose your route

| Your goal | Start with | Continue with |
| --- | --- | --- |
| Try Linux safely | Installation in a disposable VM | Desktop/accessibility, applications and personal backups |
| Use Linux on your own computer | Installation and recovery preparation | Display, media, power and peripheral checks on your actual hardware |
| Make your session accessible | Desktop and accessibility | Check the applications, sign-in and hardware routes you rely on |
| Set up a developer workstation | Backups and developer workstation | Application trust, documented project setup and troubleshooting |
| Investigate a broken workflow | Desktop troubleshooting | The guide for the failing component and the broader recovery collection |

## Work through the guides

| Order | Guide | What you will do |
| --- | --- | --- |
| 1 | [Installation and recovery](installation-and-recovery.md) | Verify image inputs, install onto a disposable virtual disk and establish a recovery route; detect changed bytes locally |
| 2 | [Desktop and accessibility](desktop-and-accessibility.md) | Navigate your session, adjust useful accommodations, test input and inspect a UTF-8 document |
| 3 | [Applications and software trust](applications-and-software-trust.md) | Identify package sources, permissions and update routes; validate a private launcher and test file associations |
| 4 | [Displays and graphics](displays-and-graphics.md) | Configure readable layouts, test docking and distinguish connector evidence from usable rendering |
| 5 | [Audio, video and screen sharing](audio-video-and-screen-sharing.md) | Trace input/output, generate a known local WAV and verify camera/capture permissions with harmless content |
| 6 | [Power, battery and suspend](power-battery-and-suspend.md) | Inspect policy and available power data, then test a controlled local suspend/resume cycle |
| 7 | [Peripherals, printing and removable media](peripherals-printing-and-removable-media.md) | Inspect devices, verify a safe transfer, test an authorized printer and pair your own peripherals |
| 8 | [Personal backups and migration](personal-backups-and-migration.md) | Detect restore corruption, recover exact bytes and design a real independent backup/migration workflow |
| 9 | [Developer workstation](developer-workstation.md) | Use an explicit project interpreter, detect a deliberate regression and recover without global package changes |
| 10 | [Desktop troubleshooting and recovery](desktop-troubleshooting-and-recovery.md) | Reproduce a launch-context failure, repair the actual cause and build a bounded diagnostic/recovery method |

Each guide explains its environment and components, provides follow-along tasks, states useful evidence, discusses recovery and ends with cleanup, a checkpoint and primary sources. Read the explanation before running commands. Tables contain independent observations, not scripts to paste from top to bottom.

## Prepare your environment

Know basic shell navigation, quoting and file permissions. Use the [foundation lessons](../01-Beginner-to-Advanced/README.md), [safe environment setup](../00-start-here/set-up-your-linux-environment.md) and [distribution selection](../07-linux-distributions/choosing-a-linux-distribution.md) if these are new to you.

For graphical work, use a supported desktop installation in a VM or on hardware you control. GNOME and KDE Plasma are reference points, not required choices; panel names, shortcuts and supported features differ by desktop/version. A container, SSH shell or headless server cannot substitute for a local screen-reader, microphone, docking or suspend test.

The ten isolated command-line examples need **Linux, Bash and Python 3**. The launcher example additionally needs `desktop-file-validate` from `desktop-file-utils`; the peripheral inventory needs util-linux `lsblk`; the developer example needs Python's `venv` module. Use your distribution's supported packages if these are absent. Examples run as an ordinary account, create new temporary fixtures and do not require sudo. Keep each exercise and its cleanup in the same disposable Bash session; stop on errors and inspect them before continuing.

Hardware tasks need the relevant device and a safe local recovery/input method. Save work before display, sleep, logout or device tests. Never format a real drive, reset an entire profile or grant broad permissions just to match an example. Preserve accommodations you depend on.

## Check your progress with evidence

| Milestone | Demonstration |
| --- | --- |
| Installation | VM boots from its disk with the installer image detached, signs in and retains a test file |
| Usability | You can launch, edit, navigate, lock and recover using your required input/assistive tools |
| Applications | You can identify the running app's source, update route and relevant permissions |
| Hardware | You have separately tested the real display, audio, camera, sleep and peripherals you need, or identified unavailable checks |
| Data protection | You can restore representative content to an isolated location and explain the real backup's protection boundaries |
| Development | A clean project environment runs a meaningful test, detects failure and passes after recovery |
| Troubleshooting | You can repeat the original operation, distinguish observations from causes and undo your changes |

Keep personal progress notes outside this public repository unless you deliberately prepare them as instructional material. A checklist entry is not evidence until you performed the operation. You can complete the command-line fixtures while leaving a hardware-specific outcome honestly unverified.

Read [validation and reproducibility](VALIDATION.md) for executed Linux environments and the boundary between tested fixtures and manual graphical/hardware procedures. The technical documentation review date is **4 November 2026**; use installed help and your release's official instructions when interfaces differ.

## Continue learning

Use the [command reference](../04-command-reference/README.md) for syntax, [troubleshooting collection](../05-troubleshooting-and-recovery/README.md) for deeper failures, [system administration](../06-system-administration/README.md) for host operations and [reference library](../08-resources-and-reference/README.md) for concepts and authoritative manuals.

[LINUX-WORLD](../README.md) · [Content standard](../CONTENT-STANDARD.md)
