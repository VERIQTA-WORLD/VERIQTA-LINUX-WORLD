# A repeatable Linux troubleshooting method

Troubleshooting reduces uncertainty about a failure. Recovery restores an acceptable user outcome. They overlap, but restoring service does not automatically establish why it failed. This method helps beginners avoid treating the first plausible explanation as a conclusion.

## Environment and permissions

The method applies across distributions. Diagnostic examples use Bash and common Linux utilities. Some host records need administrative access. The exercise below uses only temporary files and does not require Linux-specific privileges.

Record distribution and tool versions when they influence interpretation. A container, VM, host and network namespace can present different views of the same underlying resources.

## 1. State the observed failure

Write a statement someone else can test: “From client A, HTTPS requests to service B time out after five seconds, beginning near 14:10 UTC.” Avoid conclusions such as “the network is broken.” Include:

- The user operation and its expected result.
- Actual result, exact error and first/last observed times with timezone.
- Scope: one user, one client, one path, one node, one region or everyone.
- Impact and urgency, including whether retries or changes could damage data.
- Recent deployments, maintenance, access changes or infrastructure events.

Before changing anything, identify an authorized operator, a working recovery channel and the boundary of your permission. During a widespread incident, coordinate changes so two people do not unknowingly undo each other's work.

## 2. Preserve the useful context

```bash
date -Is
cat /etc/os-release
uname -r
uptime
```

These establish timestamp, distribution, kernel and uptime. They do not diagnose an application. On a rebooted host, distinguish records from the incident boot and current boot. Keep a narrow time window with enough context before and after the event.

Use a private evidence directory with `umask 077` if saving records. Command arguments, environment dumps, packet captures and application logs can contain secrets. Collect the minimum useful data and redact copies for public learning notes. Do not overwrite the original evidence during redaction.

## Evidence and interpretation

Keep observations, hypotheses and conclusions visibly separate:

| Type | Example | What it does not establish |
| --- | --- | --- |
| Observation | The TCP attempt to one address was refused | Which component generated the rejection |
| Hypothesis | The application has no listener on that address/port | That DNS, routing and all firewall paths are healthy |
| Discriminating check | On the target, inspect that exact port with `ss -ltn` | End-to-end user success |
| Supported conclusion | No matching listener existed in the inspected namespace during the sample | The complete historical cause of the outage |
| Recovery evidence | A real request returned the expected content from the affected client | Long-term stability or absence of another failure |

A useful hypothesis predicts an observation. “It might be permissions” becomes testable when you identify the identity, path and access operation that should fail. Ask what result would contradict your preferred explanation.

## 3. Move through boundaries deliberately

Investigate from the observed failure inward. For a remote web request, likely boundaries include client configuration, name resolution, route, transport, TLS, application, authorization and backend dependencies. You may skip already-established boundaries, but explain the evidence that supports doing so.

Choose low-impact checks first. Query an exact path, unit, device or port. A root-wide recursive scan, repeated connection attempts or a load test may create additional impact without improving the diagnosis.

## 4. Choose one controlled change

Record the current configuration and a rollback before changing it. Define what result would count as success and what would make you stop. Prefer the smallest action tied to the evidence: correct a specific wrong endpoint rather than replacing the whole network configuration.

Restarting may be an appropriate recovery action, but preserve relevant evidence first when feasible. A restart can clear queues, release memory or hide a repeatable failure. Report “recovered after restart” separately from “cause established.”

## Follow-along lab

This exercise uses synthetic evidence, so it is safe to complete without a server. It demonstrates reasoning, not real-time system diagnosis.

### Create a private case directory

```bash
case_dir=$(mktemp -d)
chmod 700 "$case_dir"
printf '%s\n' \
  '14:00 UTC client requests http://127.0.0.1:8081/health.txt' \
  '14:00 UTC client result: connection refused' \
  '14:01 UTC target listener: 127.0.0.1:8080' \
  '14:01 UTC target curl to port 8080: HTTP 200, ready' \
  > "$case_dir/evidence.txt"
cat "$case_dir/evidence.txt"
```

The sample records a request to port 8081 and a listener on 8080. It does not say whether the service was intended to move ports.

### Write competing explanations

```bash
printf '%s\n' \
  'H1: the client uses a stale port' \
  'H2: the service should listen on 8081 but starts with the wrong configuration' \
  'Next check: compare the approved endpoint with the effective client and service configuration' \
  > "$case_dir/hypotheses.txt"
cat "$case_dir/hypotheses.txt"
```

Both hypotheses fit the initial observations. A successful request to 8080 does not alone choose between them. Suppose the approved endpoint is documented as 8080: that supports correcting the client. If the approved endpoint is 8081, investigate service configuration instead.

### Record a bounded conclusion

```bash
printf '%s\n' \
  'Assumption supplied for exercise: approved port is 8080' \
  'Conclusion: observed client endpoint conflicts with the approved endpoint' \
  'Proposed action: change only the client port to 8080' \
  'Acceptance: affected client reads exact expected health content repeatedly' \
  'Unresolved: why the stale configuration was introduced' \
  > "$case_dir/conclusion.txt"
cat "$case_dir/conclusion.txt"
```

## Recovery and verification

This exercise changes no live endpoint. In a real incident, verify the corrected client configuration, make a request from the originally affected location, check status **and content**, inspect dependency health and observe a suitable time window. Use [recovery verification](verify-recovery-after-a-fix.md) to define acceptance before declaring resolution.

A good handoff includes impact, timeline, confirmed facts, unresolved hypotheses, actions, current state and the next owner. Schedule causal follow-up separately if recovery was necessarily faster than investigation.

## Cleanup

Keep a redacted learning note elsewhere if useful, then remove only these exercise files:

```bash
rm -i -- "$case_dir/evidence.txt" "$case_dir/hypotheses.txt" "$case_dir/conclusion.txt"
rmdir -- "$case_dir"
```

Confirm the paths in each prompt. Successful rmdir establishes that the temporary directory is empty and removed.

## References

- [Linux proc filesystem](https://man7.org/linux/man-pages/man5/proc.5.html): understand what host snapshots expose.
- [systemd journal queries](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html): select records by boot, unit and time.
- [Command index](../04-commands-and-cheat-sheets/command-index.md): tool syntax and effects.

[Collection home](README.md) · [Verify recovery](verify-recovery-after-a-fix.md)
