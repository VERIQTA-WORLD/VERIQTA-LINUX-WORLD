# Reference examples: validation and reproducibility

[Reference library](README.md)

The eight marked examples and their cleanup steps were executed on **4 November 2026** in ordinary accounts on three disposable **aarch64 Linux virtual machines**. The checks used the published Markdown blocks, including their assertions, rather than separately rewritten examples.

## Named environments and results

| Environment | Kernel | Bash / Python | systemd / util-linux | Result |
| --- | --- | --- | --- | --- |
| Ubuntu 24.04.5 LTS | `6.8.0-142-generic` | `5.2.21` / `3.12.3` | `255` / `2.39.3` | 8 examples and cleanup passed; 10 read-only observations completed |
| Debian 13, trixie | `6.12.111+deb13-cloud-arm64` | `5.2.37` / `3.13.5` | `257` / `2.41.5` | 8 examples and cleanup passed; 10 read-only observations completed |
| Fedora 44 Cloud Edition | `6.19.10-300.fc44.aarch64` | `5.3.9` / `3.14.3` | `259` / `2.41.3` | 8 examples and cleanup passed; 10 read-only observations completed |

The examples also passed on a macOS development host using Bash 3.2 and Python 3.9.6. That supplementary result concerns the private fixtures; it does not establish Linux behavior on macOS. The named Linux results are the evidence for the Linux observations.

## What was exercised

| Published example | Executed check |
| --- | --- |
| Glossary | Shared device/inode identity, hard-link lifetime, dangling symbolic link and an open descriptor after unlink |
| Documentation map | Bash command discovery, built-in help capture and a small observation file |
| Filesystem reference | Selective model-cache removal, preservation of configuration/data/state and cache re-creation |
| Configuration reference | JSON syntax success, expected application rejection with status 2, corrected acceptance and byte comparison |
| Log reference | Compressed-stream integrity, exact decompression, synthetic filtering and a distinct missing-source condition |
| Networking reference | Explicit IPv4/IPv6 prefix membership, non-overlap, strict host-bit rejection and requested normalization |
| Learning resources | Installed help capture and a structured learning card with an explicit evidence limit |
| Interview preparation | Synthetic evidence classification and a conclusion with a restricted context |

Each example used a fresh temporary parent. The check required the expected success markers, status zero and no remaining fixture paths after the page's cleanup. Interactive deletion confirmations were supplied only within the test harness for these new private fixtures.

The ten Linux observations were Bash command discovery/help, the root mount, root metadata, `/bin` entry type, interface/address summary, the route lookup for `127.0.0.1`, local `localhost` address lookup, TCP listener listing, retained journal boot metadata and journal disk usage. All returned status zero in the named environments. The journal metadata queries produced no access warnings in those accounts; another account can legitimately have less visibility. No journal message contents were collected by this check.

No sudo, network reconfiguration, service restart, system-file edit, packet probe or external application request was needed. Raw reports can include machine-specific paths and network metadata; retain them privately and redact before sharing.

## Reproduce the checks

From the repository root, in an ordinary account with Bash, Python 3 and gzip:

```bash
python3 tools/check_command_content.py
python3 tools/check_repository_structure.py
python3 tools/check_reference_examples.py
```

On a Linux environment with `findmnt`, `stat`, `ls`, `ip`, `getent`, `ss`, `journalctl` and `systemctl`, include the read-only observations:

```bash
python3 tools/check_reference_examples.py --linux-observations
```

You can add `--report /absolute/path/to/new-report.json` to retain evidence. Choose a new private path outside the repository; the checker creates the file with mode `0600` and refuses to overwrite an existing report. A report includes source-page digests, command statuses, output and observed versions. Inspect errors and visibility notices even when a command exits successfully.

The structural checker covers page contracts, local link targets and anchors, fenced Bash syntax and embedded Python syntax. It does not execute a table fragment merely because the fragment looks like a command.

## Boundaries

These results cover the eight marked fixtures and the ten named Linux observations. They do not establish that every reference-table command has been executed, every application configuration has been validated, every distribution behaves alike or any production system is ready. Optional manual-page lookups and application-specific procedures remain dependent on installed packages and context.

Author/publisher pages were consulted for the selected books and primary documentation was used for technical references. This is not an exhaustive external-link availability test, a review of every book page or a guarantee of future editions, translations or website availability. An upstream manual can describe a newer interface than the package used in these tests.

The networking fixture is offline; it does not demonstrate remote reachability. The log fixture contains synthetic events; it does not establish an actual incident cause. The learning-card and interview fixtures validate their stated models, not a learner's competence or professional certification.
