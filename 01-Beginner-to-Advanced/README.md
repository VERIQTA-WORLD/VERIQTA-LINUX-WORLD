# Linux foundations to administration

Learn Linux through 20 ordered lessons, from your first terminal session to an integrated administration and troubleshooting project. Build each skill through explanation, guided practice, investigation and verification.

Start at Part 1 if you are new to Linux. If you already use Linux, use the checkpoints below to identify gaps before moving ahead. The lesson numbers define the learning sequence; “advanced” topics build on demonstrated foundations rather than command memorization.

[Linux World](../README.md) · [Start here](../00-start-here/README.md) · [Choose a learning path](../00-start-here/choose-your-learning-path.md)

## Before you begin

No previous Linux experience is required for Part 1. You should be able to open a terminal, read and enter text, and keep notes about your work. Programming experience is useful later but is not a prerequisite; Part 17 introduces Bash scripting.

Prepare the following before practical work:

- **A recoverable Linux environment.** Use a disposable Linux VM for host administration. Ubuntu is the introductory default; read each lesson for the package manager, service names and environment it assumes. Record the distribution/release and tool versions you actually use.
- **An ordinary user account.** Use it for normal practice. Administrative lessons require authorized sudo access; read the effect of a command before elevating privileges.
- **Console and reset access.** Confirm recovery before changes to SSH, firewall policy, storage, boot or authentication. A snapshot helps reset a lab but does not replace a verified data backup.
- **A private exercise workspace.** Keep personal files, real credentials, production systems and unrelated services outside the exercises. Check for existing resources before creating named lab users, paths or services.
- **Tools appropriate to the lesson.** Bash and basic command-line utilities support the foundations; later lessons introduce additional packages, systemd, SSH and scheduling. Install prerequisites through your distribution’s supported workflow after reading the relevant setup.

Use [environment setup](../00-start-here/set-up-your-linux-environment.md) and [lab safety](../00-start-here/linux-lab-safety.md) for the shared preparation steps. A container or non-Linux shell can support selected command exercises, but it does not reproduce a Linux host’s boot, devices, service manager or security policy.

For storage practice, use only an explicitly identified disposable disk or image. For SSH practice, use only a client/server pair you are authorized to administer. Keep generated load bounded and stop the exact workers you created. Do not introduce high-impact changes just to complete a checkpoint.

## All 20 lessons in order

Each checkpoint describes something you should be able to demonstrate after the lesson. Complete it in the lesson’s stated lab environment, retain evidence and follow its cleanup or recovery instructions.

| Part | Lesson | Learning checkpoint |
| --- | --- | --- |
| 01 | [Linux Foundations and Getting Started](01.%20Part%201%3A%20Linux%20Foundations%20and%20Getting%20Started.md) | Identify your user, host and shell; explain the difference between a kernel, terminal and shell; find help for an unfamiliar command. |
| 02 | [Linux Filesystem and Navigation](02.%20Part%202%3A%20Linux%20Filesystem%20and%20Navigation.md) | Navigate with absolute and relative paths; explain the purpose of common top-level directories and return to a known location. |
| 03 | [Creating, Copying, Moving, Finding, and Deleting Files](03.%20Part%203%3A%20Creating%2C%20Copying%2C%20Moving%2C%20Finding%2C%20and%20Deleting%20Files.md) | Create a disposable workspace, copy and compare files, locate a target, distinguish hard and symbolic links, and remove only your exercise data. |
| 04 | [Linux Users, Groups, Root, and sudo](04.%20Part%204%3A%20Linux%20Users%2C%20Groups%2C%20Root%2C%20and%20sudo.md) | Explain UID/GID and process identity; verify a test account’s group membership and distinguish ordinary access from sudo authority. |
| 05 | [Linux Permissions, Ownership, and Access Control](05.%20Part%205%3A%20Linux%20Permissions%2C%20Ownership%2C%20and%20Access%20Control.md) | Explain file and directory permission effects; diagnose a denied operation and verify the smallest appropriate change as the affected user. |
| 06 | [Viewing, Editing, and Searching Text in Linux](06.%20Part%206%3A%20Viewing%2C%20Editing%2C%20and%20Searching%20Text%20in%20Linux.md) | Inspect and edit sample text, find matching lines and summarize fields while preserving the original input. |
| 07 | [Linux Pipes, Redirection, and Command Chaining](07.%20Part%207%3A%20Linux%20Pipes%2C%20Redirection%2C%20and%20Command%20Chaining.md) | Build a pipeline in stages, separate stdout from stderr, quote paths and explain meaningful exit statuses and conditional execution. |
| 08 | [Linux Processes and Job Management](08.%20Part%208%3A%20Linux%20Processes%20and%20Job%20Management.md) | Identify a lab process, move a job between foreground and background, stop only your own verified process and confirm it has exited. |
| 09 | [Linux Services, systemd, and the Boot Process](09.%20Part%209%3A%20Linux%20Services%2C%20systemd%2C%20and%20the%20Boot%20Process.md) | Distinguish process, unit and application state; inspect service logs and verify the outcome of a lab service change. |
| 10 | [Linux Package Management and Software Installation](10.%20Part%2010%3A%20Linux%20Package%20Management%20and%20Software%20Installation.md) | Identify the installed package manager, inspect package information and distinguish repository refresh, installation and upgrade operations. |
| 11 | [Linux Environment Variables and Shell Configuration](11.%20Part%2011%3A%20Linux%20Environment%20Variables%20and%20Shell%20Configuration.md) | Explain shell variables, exported environment and PATH; check a configuration edit before using it in a new shell. |
| 12 | [Linux Networking Fundamentals](12.%20Part%2012%3A%20Linux%20Networking%20Fundamentals.md) | Read addresses, routes and listening sockets; distinguish a local listener from a service reachable by a client. |
| 13 | [DNS, SSH, and Remote Server Administration](13.%20Part%2013%3A%20DNS%2C%20SSH%2C%20and%20Remote%20Server%20Administration.md) | Separate DNS, connectivity, host-key and authentication failures; verify an authorized SSH connection and a transferred file. |
| 14 | [Linux Disks, Partitions, Filesystems, and Mounting](14.%20Part%2014%3A%20Linux%20Disks%2C%20Partitions%2C%20Filesystems%2C%20and%20Mounting.md) | Distinguish device, partition, filesystem and mount; inspect capacity and mount state before touching a confirmed disposable storage target. |
| 15 | [Linux CPU, Memory, Swap, and Performance Fundamentals](15.%20Part%2015%3A%20Linux%20CPU%2C%20Memory%2C%20Swap%2C%20and%20Performance%20Fundamentals.md) | Collect a baseline, distinguish CPU, memory, swap and I/O evidence, and verify recovery after stopping your lab workload. |
| 16 | [Linux Logs, Monitoring, and Troubleshooting](16.%20Part%2016%3A%20Linux%20Logs%2C%20Monitoring%2C%20and%20Troubleshooting.md) | Filter relevant logs by time and service, build a short incident timeline and support a hypothesis with evidence. |
| 17 | [Bash Shell Scripting From Zero](17.%20Part%2017%3A%20Bash%20Shell%20Scripting%20From%20Zero.md) | Write and syntax-check a small Bash script; test success and failure paths, quote variables and return meaningful statuses. |
| 18 | [Linux Automation, Cron, Archives, and Backups](18.%20Part%2018%3A%20Linux%20Automation%2C%20Cron%2C%20Archives%2C%20and%20Backups.md) | Run an automation task manually before scheduling it; create an archive and verify restored sample data rather than just archive creation. |
| 19 | [Linux Security and Beginner Server Hardening](19.%20Part%2019%3A%20Linux%20Security%20and%20Beginner%20Server%20Hardening.md) | Review accounts, SSH, listeners, firewall policy, updates and secrets; preserve access and verify each scoped lab change. |
| 20 | [Complete Linux Administration and Troubleshooting Project](20.%20Part%2020%3A%20Complete%20Linux%20Administration%20and%20Troubleshooting%20Project.md) | Combine the preceding skills in the administration project; diagnose controlled failures, verify restoration and document the final system. |

## Work through the course in stages

| Stage | Parts | Readiness check before continuing |
| --- | --- | --- |
| Terminal, files and access | 1–7 | Work safely in a temporary directory, explain ownership and permission effects, and construct a text pipeline with interpretable results. |
| Processes and host operation | 8–11 | Inspect processes and services, explain package operations and distinguish a shell setting from an exported environment value. |
| Connectivity, storage and investigation | 12–16 | Trace a failure through the relevant layers, establish a resource baseline and use logs to test a specific hypothesis. |
| Automation and security | 17–19 | Test scripts and failure paths, verify a sample restore and justify a scoped access or exposure change with a recovery route. |
| Integrated practical assessment | 20 | Operate the lab system, investigate controlled faults and prove recovery with application and data checks. |

If a readiness check exposes a gap, revisit the relevant lesson and reproduce a smaller example. There is no requirement to finish a long lesson in one sitting. Stop at a verified checkpoint, record the current state and resume from known prerequisites.

## Use each lesson actively

1. **Read the goal and prerequisites.** Identify the machine, account, tools and resources involved. Read the complete exercise, including cleanup, before making changes.
2. **Predict the effect.** Explain what a command reads or modifies. Replace placeholders deliberately; distinguish complete commands from syntax fragments, output examples and examples of mistakes.
3. **Practise one step at a time.** Compare the actual output with the explanation. An expected permission denial or no-match result can be useful evidence; investigate unexpected differences before continuing.
4. **Verify the intended outcome.** Check the affected file, identity, service or user operation. A successful command or an active service alone may not establish the desired result.
5. **Recover and clean up.** Undo only the exercise resources you have identified. Verify stopped workers, removed temporary files and restored configuration as appropriate.
6. **Reproduce independently.** Repeat from the stated setup without relying on hidden state. Answer the lesson’s questions in your own words and explain one controlled variation.

Command examples describe particular tools and environments. Compare your installed help/manuals and distribution documentation when an option, package or service differs. Avoid translating an unfamiliar error into a broader privilege or permission change.

## Keep a learning record

Use the [learning progress checklist](../00-start-here/learning-progress-checklist.md) to distinguish reading, following, independent reproduction and extension. For each part, record:

- Lesson number and repository revision.
- Distribution, tool versions, account and relevant prerequisites.
- Goal, predicted effect, actual observations and meaningful exit statuses.
- Verification, cleanup or recovery completed.
- Your explanation of any discrepancy and the next checkpoint to revisit.

Mark a part complete when you can explain its concepts, perform its relevant checkpoint independently and show the outcome. Reading every page is useful preparation; demonstrated work is the evidence of progress. This course does not by itself certify production readiness or a professional seniority level.

## Complete the final project

Begin Part 20 after meeting the earlier stage checks. It combines server baselining, users and permissions, application configuration, remote access, monitoring, automation, backups, security and troubleshooting in a disposable environment.

Retain a final evidence set: environment and system layout, important configuration decisions, acceptance results, a controlled incident timeline, restoration results and cleanup or retained lab state. Explain what the exercise proves and what would need additional testing for a real service. A working web response, a successful backup command and a verified restore establish different outcomes; document each relevant check.

## Connect lessons to practice and reference

| Your next task | Where to go |
| --- | --- |
| Find a focused exercise | [Labs](../02-Labs/README.md); check the selected lesson’s own prerequisites and recovery instructions |
| Combine skills into a larger implementation | [Projects](../03-Projects/README.md) |
| Look up syntax, effects and examples | [Command reference](../04-command-reference/README.md) and [cheat-sheet index](../04-command-reference/cheat-sheet-index.md) |
| Investigate a symptom methodically | [Troubleshooting and recovery](../05-troubleshooting-and-recovery/README.md) |
| Develop administration procedures | [System administration](../06-system-administration/README.md) |
| Compare distribution behavior | [Linux distributions](../07-linux-distributions/README.md) |

[Start here](../00-start-here/README.md) · [Linux World](../README.md)
