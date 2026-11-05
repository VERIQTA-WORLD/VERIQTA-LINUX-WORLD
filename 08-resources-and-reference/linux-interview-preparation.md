# Explain Linux with evidence

[Reference library](README.md) · [Glossary](linux-glossary.md) · [Troubleshooting collection](../05-troubleshooting-and-recovery/README.md)

## Scope and environment

Use these questions to practice explaining what you know, checking a hypothesis and identifying the limits of your evidence. They are useful for interviews, peer discussion, project demonstrations and your own review. They are not a script to memorize or a guarantee of a hiring outcome.

The examples assume ordinary Linux concepts; where a tool is GNU-, systemd- or distribution-specific, say so in your answer. You are not expected to know every command option from memory. Explain how you would find the installed documentation and choose a safe check.

The follow-along exercise needs Bash, Python 3 and an ordinary account. It creates synthetic observations in a temporary directory and checks how narrowly they support a conclusion. It does not start a service or recreate an incident on your computer.

## Reference

### Give an answer someone can assess

Use this structure, in your own words:

1. **Define the question and scope.** Which host, account, namespace, service and time are involved?
2. **State what you know.** Separate supplied observations from assumptions.
3. **Offer a small number of explanations.** Avoid a list of unrelated commands.
4. **Choose a distinguishing check.** Say what each likely result would mean, including an error or missing permission.
5. **Choose a bounded action if needed.** Include prerequisites, authorization, verification and recovery.
6. **State the remaining uncertainty.** A hypothesis becomes stronger through evidence; it does not become fact because you sound certain.

For a real incident, preserving evidence and limiting impact may take priority over an experiment. For a learning exercise, use a disposable fixture and make cleanup part of your demonstration.

### Foundation questions

| Question to explain | What a sound answer includes | A useful check or follow-up |
| --- | --- | --- |
| 1. What is Linux, and what is a distribution? | The kernel is one component; user space, packaging, release policy and integration create a usable distribution | Compare `/etc/os-release` with `uname -r`; user-space identity and kernel identity are distinct |
| 2. How is `/` different from `/root`? | `/` is the root of the visible directory tree; `/root` is a conventional root-account home | Explain why a container has its own visible `/` without necessarily owning a separate physical disk |
| 3. What happens when you type a command name? | Shell parsing/expansion and name resolution can select aliases, functions, built-ins or executables | Use `type -a NAME` in the relevant shell; do not assume `which` describes every shell behavior |
| 4. Why quote a pathname variable? | Word splitting and pathname expansion can change arguments in shell contexts; quoting preserves the intended value | Use a private filename containing spaces; distinguish quoting from escaping an option-like operand |
| 5. What do standard input, output and error mean? | Conventional file descriptors 0, 1 and 2; redirection changes destinations independently | Explain why discarding stderr can conceal a permission error rather than fix it |
| 6. What does a command's exit status tell you? | The command's documented execution result; different tools assign meanings to nonzero values | Compare “no match” with “could not read input” using the tool's manual |
| 7. What controls access to a file? | Process identity, directory traversal, mode bits, ACLs, mandatory policy, capabilities and mount context can all matter | Check parent traversal as well as the final file; do not jump to `chmod 777` |
| 8. How do hard links and symbolic links differ? | Hard links name the same inode within a filesystem; symbolic links store a pathname interpreted during lookup | Explain a dangling symbolic link after its target name is removed; use the [glossary example](linux-glossary.md#follow-along) |
| 9. Is a process the same as a service? | A process is an execution instance; a managed service can involve multiple processes, dependencies and lifecycle policy | Explain why a PID alone does not prove readiness or the intended service instance |
| 10. What is a signal? | A process notification/control mechanism with defined handling rules; some signals cannot be caught or ignored | Describe graceful termination before a forced kill, and the verification needed afterward |

Do not claim that a conventional path, shell default or package name applies to every Linux system. A precise answer can be short when it names the relevant boundary.

### Administration and recovery questions

| Question to explain | What a sound answer includes | Distinguishing check and boundary |
| --- | --- | --- |
| 11. A service is active, but users report failure. What next? | Manager state and application readiness are separate | Check the documented endpoint/status/content in the correct network context, then correlate logs; avoid an unreasoned restart |
| 12. A configuration parser accepts a file. Can you deploy it? | Syntax, semantic values, cross-file consistency, permissions, activation and runtime behavior are distinct | Use the application's validator and a bounded post-activation check; describe rollback inputs |
| 13. Why might a file edit have no effect? | Wrong file/instance, generated configuration, precedence, unchanged running state or unsupported reload | Identify the consumer and effective input before editing again |
| 14. Disk space is low. Why might `df` and `du` disagree? | Filesystem accounting and pathname traversal measure different things; deleted-open files, hidden mounts, snapshots, reserved space and permissions can matter | Inspect the relevant filesystem and process-held files with permitted tools; never delete arbitrary state to make numbers match |
| 15. Can a filesystem reject file creation with free bytes remaining? | Inodes, quotas, read-only state, permissions and other limits are separate from byte capacity | Check the reported error and the corresponding limit; a free-space percentage alone is insufficient |
| 16. Why is free memory small on a healthy host? | Linux uses memory for cache; availability, pressure, workload and cgroup limits matter | Examine trends and the relevant scope rather than diagnosing failure from one “free” value |
| 17. Is high load average the same as high CPU utilization? | Linux load includes runnable and uninterruptible tasks; CPU utilization is a different measure | Compare CPU time, I/O waits, runnable tasks and workload capacity over time |
| 18. How would you prove a backup is useful? | Restore representative data in isolation, check consistency and application behavior, and assess recovery objectives | A successful backup command or checksum is insufficient by itself; discuss keys and dependencies |
| 19. What do RPO and RTO mean? | Recovery point objective limits acceptable data loss in time; recovery time objective limits acceptable restoration time | Measure a restore exercise against explicit objectives instead of assuming them |
| 20. How do you reduce SSH configuration risk? | Validate candidate settings, account for matching rules, retain a working recovery session and test a fresh connection | Server validation does not prove that the intended account can authenticate from the intended source |
| 21. Does an older upstream version number prove a package is vulnerable? | Distribution backports and advisories matter alongside package provenance | Check the distribution's exact package revision and security advisory, not a version-string comparison alone |
| 22. When is rollback more than restoring one file? | Packages, schema/data changes, generated assets, secrets and external dependencies may require coordinated recovery | Explain compatibility and irreversible changes before promising automatic rollback |

If you have never performed an operation, say that you would consult the runbook or reproduce it in a disposable environment first. Presenting untested guesses as production experience makes your answer less useful.

### Networking, isolation and modern systems

| Question to explain | What a sound answer includes | Distinguishing check and boundary |
| --- | --- | --- |
| 23. A hostname fails but a numeric address works. Is DNS definitely broken? | Compare application behavior, NSS, record family, resolver/cache, TLS names and the exact endpoint | `getent` and a DNS-specific query answer different questions; an IP-based TLS request may change identity validation |
| 24. A port is listening. Is it reachable? | Bind address, namespace, route, policy and protocol all matter | A local socket listing is not a remote request or application-content check |
| 25. Why can IPv4 work while IPv6 fails? | Distinct address selection, listeners, routes and policy | Test families explicitly against authorized endpoints; wildcard bind behavior can vary |
| 26. What does a container share with the host? | Common Linux containers share the host kernel while namespaces isolate views and cgroups account/control resources | A container image does not provide an independent running kernel in the usual model; VM-based runtimes can differ |
| 27. What is the difference between namespaces and cgroups? | Namespaces isolate views of selected resources; cgroups organize processes and provide resource control/accounting | Neither alone establishes a complete security boundary |
| 28. Is root inside a container equivalent to unrestricted host root? | User namespaces, capabilities, mounts, policy and runtime configuration affect authority | Do not assume either complete equivalence or automatic safety; inspect the actual boundary |
| 29. Why might a process be killed while the host has memory available? | A cgroup limit, policy or another actor may be responsible | Correlate exit/signal evidence, kernel events and the correct cgroup's counters; do not label every termination “OOM” |
| 30. When is a declarative change reproducible? | Inputs, versions, dependencies, build/deployment environment and verification must be controlled sufficiently | A configuration file in Git is useful but does not alone make an external dependency or mutable image reproducible |
| 31. How do metrics, logs and traces differ? | Metrics aggregate measurements, logs record events, traces connect work across operations/spans | Correlate scope and time; collecting all three does not automatically identify a cause |
| 32. What does a TLS failure tell you? | Determine handshake stage, name, chain, trust source and clock context | Permanently disabling certificate checks discards an important identity check rather than resolving its cause |

For deeper practice, choose a matching [project](../03-Projects/README.md) or [administration procedure](../06-system-administration/README.md). Use a complete procedure when you want to move from discussion to a modifying operation.

### Practice a scenario before seeing a model answer

**Scenario:** A teammate says, “The application is healthy: the service manager reports active and port 8443 is listening.” You have no HTTP response, no agreed readiness contract and no user-facing observation.

Before continuing, write down:

- What do the two observations establish?
- Which claims are still unsupported?
- What is your next bounded check, and where must you run it?
- What would you do if the check succeeds locally but fails from a client network?

**Model reasoning:** The manager reports its own state and a socket was observed in a particular namespace at a particular time. That supports a limited process/listener claim. It does not establish that the expected application handled a request, that the right content was returned, or that the client path works. First identify the endpoint's documented protocol and readiness contract. Make a bounded, authorized request in the appropriate context and check the expected response. If a local request succeeds but a client request fails, compare destination resolution, address family, bind address, routes, intermediaries and policy with evidence from both contexts. A restart is not justified by the supplied observations alone.

### Review the quality of your explanation

| Dimension | What to look for in your own answer |
| --- | --- |
| Accuracy | Terms have concrete meanings; Linux-specific behavior is labeled |
| Scope | You named the relevant host/account/namespace/time and authorization boundary |
| Evidence | You distinguished observations from conclusions and chose a falsifiable next check |
| Safety | Modifying actions have prerequisites, bounded impact and recovery |
| Verification | You described the expected useful result, not merely command completion |
| Communication | Another person can follow your reasoning without guessing your assumptions |
| Honesty | You identified unknowns and did not turn a fixture into a claim of production experience |

Use this as feedback, not a numerical certification. Have a peer challenge one assumption, then improve the explanation. If you practice alone, change one fact in the scenario and see whether your proposed check still distinguishes the possibilities.

## Follow along

Represent the scenario as data. The check intentionally refuses to infer readiness from process/listener observations. Adding the required application observation changes that narrow conclusion; it still cannot establish every user's experience.

<!-- reference:exercise -->
```bash
interview_lab=$(mktemp -d) || exit 1
python3 - "$interview_lab" <<'PY'
import json
from pathlib import Path
import sys
root = Path(sys.argv[1])
evidence = {'manager_active': True, 'listener_seen': True,
            'expected_response_observed': False}

def readiness_supported(observations):
    return observations['expected_response_observed'] is True

assert not readiness_supported(evidence)
print('PASS: process and listener evidence alone do not support application readiness')
evidence['expected_response_observed'] = True
assert readiness_supported(evidence)
record = {'synthetic_evidence': evidence,
          'conclusion': 'Expected response observed in the tested context only.',
          'limit': 'No proof of remote-client reachability, durability or future availability.'}
(root / 'reasoning.json').write_text(json.dumps(record, indent=2) + '\n')
assert json.loads((root / 'reasoning.json').read_text()) == record
print('PASS: conclusion records both the added evidence and its limits')
PY
cat "$interview_lab/reasoning.json"
```

## Verify your result

Expect two `PASS` lines and a JSON record explicitly labeled synthetic. This is a reasoning model, not a live health probe. The function embodies the scenario's simplified evidence rule; a real readiness contract can require dependencies, authentication, state or other application-specific conditions.

Explain what would change if the successful response came from the wrong virtual host, a stale cache or a different namespace. Then choose two questions from the tables and answer them using your own real, non-sensitive observations.

## Cleanup

<!-- reference:cleanup -->
```bash
rm -i -- "$interview_lab/reasoning.json"
rmdir -- "$interview_lab"
```

## Sources

Check technical details against [Bash documentation](https://www.gnu.org/software/bash/manual/), [path_resolution(7)](https://man7.org/linux/man-pages/man7/path_resolution.7.html), [signal(7)](https://man7.org/linux/man-pages/man7/signal.7.html), [systemd.service](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html), [proc_loadavg(5)](https://man7.org/linux/man-pages/man5/proc_loadavg.5.html), [kernel PSI documentation](https://docs.kernel.org/accounting/psi.html), [cgroup v2 documentation](https://docs.kernel.org/admin-guide/cgroup-v2.html), [namespaces(7)](https://man7.org/linux/man-pages/man7/namespaces.7.html), [capabilities(7)](https://man7.org/linux/man-pages/man7/capabilities.7.html), [Ubuntu security backport explanation](https://documentation.ubuntu.com/security/security-updates/), [OpenTelemetry signals](https://opentelemetry.io/docs/concepts/signals/) and the [curl TLS certificate guide](https://curl.se/docs/sslcerts.html). Use the linked operational collections for complete procedures rather than treating these discussion prompts as deployment instructions.
