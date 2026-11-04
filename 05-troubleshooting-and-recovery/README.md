# Troubleshooting and recovery

![Troubleshooting and recovery](../assets/images/05-troubleshooting-and-recovery-cover.svg)

Learn to turn an observed failure into a testable explanation, make a controlled recovery, and prove that the original user task works again. Start with evidence. A successful command, a green service status and a recovered application are different outcomes.

## Choose a guide

| What you observe | Start here | Practice environment |
| --- | --- | --- |
| You need a repeatable investigation process | [Linux troubleshooting method](linux-troubleshooting-method.md) | Temporary files and sample evidence |
| A client cannot reach a server or application | [Server is unreachable](server-is-unreachable.md) | Temporary loopback-only HTTP service |
| SSH cannot connect, authenticate or open a session | [SSH login is failing](ssh-login-is-failing.md) | Isolated client configuration and an authorized SSH lab host |
| A managed application fails to start | [Service will not start](service-will-not-start.md) | Transient systemd user service |
| Writes fail because storage resources are exhausted | [Disk space or inodes are exhausted](disk-space-or-inodes-are-exhausted.md) | Small, separately mounted tmpfs in a disposable VM |
| CPU, memory or latency is unexpectedly high | [CPU or memory usage is high](cpu-or-memory-usage-is-high.md) | Bounded single-process load in a disposable VM |
| Hostnames fail or resolve inconsistently | [DNS resolution is failing](dns-resolution-is-failing.md) | Controlled NXDOMAIN versus valid lookup, without resolver changes |
| An application reports a read-only filesystem | [Filesystem is read-only](filesystem-is-read-only.md) | Separate temporary tmpfs mount in a disposable VM |
| Startup fails before a normal login is available | [Server will not boot](server-will-not-boot.md) | Alternate fstab file first, then optional disposable-VM console inspection |
| You need to decide whether the incident is resolved | [Verify recovery after a fix](verify-recovery-after-a-fix.md) | HTTP status, content and repeated client checks |

## How to follow along

Use Bash and Python 3.8 or newer for the supplied practice helpers. Linux investigations assume the named commands are installed. Service and boot sections assume systemd unless otherwise stated. Use your distribution's installed manuals alongside the references: unit names, log paths, resolver ownership, available flags and recovery environments vary.

Read the [method](linux-troubleshooting-method.md) first. Then open one symptom guide, read the entire lab before starting, and run each step separately. Every lab has a defined scope, expected observations and cleanup. Its result demonstrates a specific mechanism, not every possible cause of the same symptom.

- **Ordinary user:** file exercises, client queries, loopback HTTP and bounded process observation.
- **Authorized administrator:** restricted journals, server configuration checks, mount inspection and lab tmpfs setup.
- **Console or rescue environment:** startup failures and storage repair planning. Establish access before changing a remote machine.

Examples with uppercase tokens such as HOST, UNIT, PID or DIRECTORY are syntax placeholders. Replace them with independently verified values. Code under diagnostic sections is a menu of checks, not a script to paste indiscriminately. Some checks intentionally return nonzero statuses; each guide explains how to interpret them. Capture `$?` immediately after the command being investigated.

For labs using files under `labs/`, run from the repository root. The helper HTTP server binds only to `127.0.0.1`, chooses an available port and has a bounded lifetime. It is a teaching tool, not a production server. Stop and inspect an unexpected result before continuing to any modifying command.

## Separate investigation from recovery

Record the affected user task, incident time window, scope, recent changes and current observations. Keep sensitive evidence private. Choose the next check that best distinguishes your competing explanations. Before a change, decide its intended result, possible impact, rollback and acceptance test.

Do not erase logs, flush firewall policy, delete lock files, broadly change permissions, fill a real filesystem or force a filesystem repair just to see whether the symptom disappears. The guides explain targeted alternatives. Escalate when evidence suggests failing hardware, corruption, unknown data ownership or a risk beyond your recovery access.

## Track the quality of your work

For each exercise, write down the initial observation, at least two hypotheses, the discriminating check, the supported conclusion, the recovery action and the verification evidence. Include what you have **not** ruled out. A learning portfolio should distinguish a controlled simulation from a production incident.

All ten guide pages are written in this installment. See the [validation record](VALIDATION.md) for executed portable checks and the Linux-only scenarios still awaiting reproduction. Written coverage is not a claim that every distribution and repair path has been tested.

[Command explanations](../04-commands-and-cheat-sheets/README.md) · [Quick command tables](../09-cheat-sheets) · [Content standard](../CONTENT-STANDARD.md) · [LINUX-WORLD](../README.md)
