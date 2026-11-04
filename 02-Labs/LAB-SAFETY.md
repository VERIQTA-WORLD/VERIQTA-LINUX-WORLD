# Work safely in your Linux lab

Read the entire exercise before running modifying commands. Identify what changes, why it changes, what an expected failure looks like and how you will restore or remove the lab resources.

[Lab home](README.md) · [Environment](LAB-ENVIRONMENT.md) · [Progress](PROGRESS-TRACKER.md)

## Confirm the target every time

Before a change, identify the machine, account, directory, namespace and exact resource. Distinguish a local shell from an SSH session. Use the lab's own checks to confirm device, interface, unit, path and account names.

Uppercase placeholders and angle-bracket examples are instructions to substitute verified values. They are not literal commands to paste. Do not infer that a named disk, process or service belongs to you merely because it appears in an example.

If a target already exists and ownership is unclear, stop. Choose a fresh isolated environment rather than overwriting the resource.

## Bound the effects

| Area | Boundary to establish before practice |
| --- | --- |
| Files and cleanup | A private known workspace; quoted paths; exact created-file inventory; no broad home/root wildcards. |
| Processes and load | Known child/process identity, bounded lifetime and resource use, and an explicit wait/cleanup route. |
| Storage | Dedicated disposable disks or a verified bounded lab mount; source/target identity; no host-root filling or guessed formatting. |
| Access and SSH | Console recovery, a working session and independent verification before changing access controls. |
| Firewall and networking | Exact private lab flow; no policy flushing, public listeners or unsolicited scans of unrelated hosts. |
| Services and scheduling | Unique lab unit/job, correct manager scope and removal of that exact schedule before deleting its files. |
| Evidence | Synthetic data where possible; private raw captures; reviewed redacted copies for sharing. |

Root authority increases the consequences of a wrong target. Sudo is not a troubleshooting strategy and does not make a guessed operation correct.

## Treat expected failures explicitly

Several labs deliberately return nonzero statuses. Read the stated contract: a comparison mismatch, missing match, invalid candidate and unavailable manager have different meanings. Capture status immediately and do not suppress every error with `|| true`.

Use an ordinary interactive Bash shell for manual follow-along commands unless the lab specifies otherwise. A global `set -e` can end a session during an intentional negative case; the published test runners handle those expected outcomes explicitly.

Stop dependent changes when you see an unexpected error. Preserve the output, verify prerequisites and inspect the failed boundary before continuing. Never apply recursive 777 permissions, disable mandatory policy or flush firewall rules to make a result resemble the guide.

## Protect storage and mounts

Map the exact path to its mount before interpreting capacity. Inspect bytes, inodes, quota evidence and mount state independently. Never fill the real filesystem hosting your OS or application to reproduce a space problem.

The optional JUN-081 kernel experiment requires an exact verified tmpfs mount with an 8 MiB size and 128-inode cap. If its mount verification fails, do not run the writer against the ordinary parent directory. If unmount fails, stop deletion and investigate mount users; a failed unmount must not be followed by recursive workspace removal.

Do not remove a backing image, logical volume or mountpoint while it is still in use. A lab reset can discard data; preserve any evidence you intend to retain before using it.

## Protect identities and network trust

Keep host-key and certificate verification enabled. Verify a changed identity through an independent authorized source before updating a specific trust entry. A warning is evidence to investigate, not an obstacle to bypass.

Do not use real production keys, customer records or employer configuration in exercises. Verbose SSH logs, process arguments, environment variables and network captures can contain sensitive information even when no obvious password string appears.

Use only authorized clients and destinations. A loopback test does not need a public listener, a remote server or firewall changes.

## Stop exact lab processes

A command-name match is a discovery aid; it can include unrelated work. Old PID files may refer to a reused PID. Verify ownership, start time, parent, command and scope before signaling a known process.

Prefer a retained child handle or known job that you can wait for. A successful signal does not prove child workers exited. Verify the intended workload is gone and the surrounding system remains healthy.

If a process has already exited, do not signal its old number to “make sure.”

## Finish with verified cleanup

1. Preserve reviewed evidence and decide whether you are retaining or dismantling the lab.
2. Stop the exact schedules, timers, helpers and generators you created.
3. Undo only the temporary configuration and policy belonging to the exercise.
4. Unmount only confirmed lab mounts and verify they are no longer mounted.
5. Remove only the exact disposable files, accounts and resources you own.
6. Repeat the relevant acceptance check and compare remaining state with the baseline.

Record deliberately retained resources and unresolved cleanup. If the boundary is uncertain, stop deletion and recover the information needed to act safely. Continue only when you can explain the target and effect.
