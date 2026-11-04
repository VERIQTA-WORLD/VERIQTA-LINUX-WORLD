# Choose your learning path

Choose a goal first, then select a starting point based on what you can demonstrate. Experience labels help navigation; they do not certify professional seniority or require you to skip foundational topics.

## Start from your experience

| Starting point | Evidence you can demonstrate | Recommended entry |
| --- | --- | --- |
| New to Linux or the terminal | You are still learning paths, command syntax and file operations | [Environment setup](set-up-your-linux-environment.md), [safety](linux-lab-safety.md), then [existing lesson sequence](../01-Beginner-to-Advanced) |
| Comfortable with basic commands | Navigate, quote paths, inspect permissions, search text and explain exit statuses | Fill gaps using [command references](../04-command-reference/README.md), then practise with [existing labs](../02-Labs) |
| Beginning administration | Explain users/groups, processes, services, network endpoints and storage mounts | [System administration](../06-system-administration/README.md), [distributions](../07-linux-distributions/README.md) and [troubleshooting method](../05-troubleshooting-and-recovery/linux-troubleshooting-method.md) |
| Experienced operator/developer | Reproduce a system, investigate failures and verify recovery independently | Select deeper [projects](../03-Projects), reproduce pending Linux checks and follow new tracks as they are built |

If a checkpoint is unfamiliar, study that prerequisite rather than advancing by title alone. A command memorized without its effects, evidence and cleanup is not yet an independently demonstrated skill.

## Route A: Linux foundations

**Goal:** work confidently in a shell and explain what changed.

Follow the existing lesson sequence, using [files](../04-command-reference/files-and-directories/README.md), [text](../04-command-reference/text-processing/README.md) and [permissions](../04-command-reference/users-and-permissions/README.md) references as needed. Continue into processes, services, networking, packages and storage.

Checkpoint: create temporary sample data, find and transform it, explain its permissions, compare copies, interpret a meaningful nonzero status and remove only your exercise resources. Record exact commands and observations.

## Route B: Everyday desktop and workstation Linux

**Goal:** choose and operate a recoverable personal Linux environment.

Begin with foundations, [distribution selection](../07-linux-distributions/choosing-a-linux-distribution.md), safe environment practice and [backup/restore concepts](../06-system-administration/backup-and-restore-operations.md). The dedicated [desktop/workstation collection](../09-desktop-and-workstation-linux/README.md) is planned for installation, accessibility, applications, devices and developer workstations.

Checkpoint now: identify your chosen environment and recovery path, understand file ownership and reproduce the static backup exercise. Dedicated hardware/desktop walkthroughs remain future work; do not treat a VM lesson as a tested dual-boot installation guide.

## Route C: Development on Linux

**Goal:** build and debug software in an environment another person can reproduce.

Study foundations and the relevant existing labs/projects. Use [command tables](../04-command-reference/cheat-sheet-index.md) to find tools, then read their prerequisites. The dedicated [automation](../10-automation-and-reproducibility/README.md), [container](../11-containers-and-isolation/README.md) and [internals/development](../15-linux-internals-and-development/README.md) tracks are planned.

Checkpoint now: record dependencies and tool versions, reproduce an existing project from its stated setup, verify its output and document one independent change. Planned topics are a direction, not completed instruction.

## Route D: System administration and operations

**Goal:** make controlled changes and establish recoverable service outcomes.

Work through [system administration](../06-system-administration/README.md), [distribution differences](../07-linux-distributions/README.md) and [troubleshooting](../05-troubleshooting-and-recovery/README.md). Pair each change with prerequisites, a baseline, a recovery path and a user-level acceptance operation.

Checkpoint: distinguish observation from hypothesis, reject an invalid configuration, rehearse rollback and verify restored data. Inspect the validation record before claiming a Linux-specific scenario has been reproduced. Fleet work adds grouping, canaries, concurrency, rollout gates and per-host evidence; production adds explicit ownership and impact/recovery requirements even for a single host.

## Route E: Advanced Linux engineering

**Goal:** explain isolation, performance, security and operating-model trade-offs through evidence.

Demonstrate foundations and independent recovery first. Then follow the planned [security](../12-security-and-software-trust/README.md), [observability](../13-performance-and-observability/README.md), [image/declarative systems](../14-image-based-and-declarative-linux/README.md) and internals tracks as they gain actual lessons.

Checkpoint now: identify the boundary of an existing experiment, explain alternative hypotheses and reproduce it on a named target. Future advanced content must include real environments and validation; knowing terminology alone is not the goal.

## Record progress honestly

Use the [progress checklist](learning-progress-checklist.md) to distinguish read, followed, independently reproduced and extended. Note the operating system, versions, permissions, expected/actual results and cleanup. A small verified experiment is more useful than an untested claim of broad mastery.

[Start here](README.md) · [Root roadmap](../README.md)
