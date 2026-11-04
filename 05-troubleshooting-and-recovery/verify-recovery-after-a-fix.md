# Verify recovery after a fix

Recovery means the affected operation works within acceptable limits and the system is safe to continue using. A command completing, a process running, or an error disappearing is weaker evidence. Define acceptance before making the change so the result cannot be judged only by the easiest green indicator.

## Environment and permissions

Apply this approach across distributions. Read-only checks should use the originally affected client and the application's actual identity where authorized. Mutating acceptance tests need explicit ownership, bounded test data and cleanup: a real payment, mail delivery or deletion is not a harmless health check.

The exercise uses Bash, Python 3, curl and temporary files from the repository root. It runs a bounded loopback-only HTTP helper without root. It demonstrates a reachable endpoint serving the **wrong content**, followed by exact-content verification. It does not simulate database consistency, distributed recovery or production readiness.

## Define acceptance at several levels

| Level | Example acceptance | Common false confidence |
| --- | --- | --- |
| Process/manager | Intended unit is active without a restart loop | A process exists but is not ready |
| Local application | Correct response from the intended local endpoint | Health page works while a dependency fails |
| Affected client path | Original request succeeds from the affected location | Only an administrator's alternate path works |
| Data integrity | Expected records, ordering and durability checks pass | Service resumes after losing recent writes |
| Performance | Errors, latency and queues return to agreed limits | One quick request during a quiet minute |
| Stability | Repeated checks at an appropriate workload over a defined window | One sample immediately after a restart |
| Persistence | Intended configuration survives its supported lifecycle | Only an ephemeral workaround is active |

Not every incident needs every test, but record which levels apply and why. Stability windows should match the symptom's cadence: five seconds is a teaching interval, not universal production acceptance.

## Evidence and interpretation

Compare before and after using the same operation, identity, endpoint, relevant payload, time window and workload. If any of these change, explain the limitation.

A useful verification record contains:

- The original impact, acceptance criteria and rollback trigger.
- What changed, who changed it, and the observation time with timezone.
- Command/request result, exit status and meaningful returned data.
- Current errors, queues, resource headroom and relevant dependency state.
- Any data loss, replay, retries or side effects requiring reconciliation.
- Remaining uncertainty, monitoring ownership and follow-up work.

If a recovery action fails acceptance or creates a new problem, stop adding unrelated changes. Use the planned rollback when it is still safe, or escalate if rollback could worsen data consistency. Rollback is itself a change and needs verification.

## Follow-along lab

### 1. Create an endpoint that responds successfully with wrong content

```bash
verify_lab=$(mktemp -d)
mkdir "$verify_lab/site"
printf 'starting\n' > "$verify_lab/site/health.txt"
printf 'ready\n' > "$verify_lab/expected"
python3 05-troubleshooting-and-recovery/labs/loopback_http.py \
  --directory "$verify_lab/site" --ready-file "$verify_lab/port" \
  > "$verify_lab/server.log" 2>&1 &
verify_pid=$!
for attempt in {1..50}; do
  test -s "$verify_lab/port" && break
  sleep 0.1
done
test -s "$verify_lab/port"
```

Stop if readiness fails. The helper has a 180-second lifetime; complete the exercise within that window. Its port file signals that a socket is listening, not that the served content satisfies your acceptance criterion.

```bash
verify_port=$(cat "$verify_lab/port")
curl --noproxy '*' --fail --max-time 3 \
  "http://127.0.0.1:$verify_port/health.txt" > "$verify_lab/actual"
printf 'request status: %s\n' "$?"
cat "$verify_lab/actual"
cmp -- "$verify_lab/expected" "$verify_lab/actual"
printf 'content comparison status: %s\n' "$?"
```

Expect request status 0 and body `starting`, but comparison status 1. HTTP 200 and a successful transport are insufficient for this acceptance criterion. A cmp status above 1 means a comparison error, not simply different content.

### 2. Make the controlled correction

```bash
printf 'ready\n' > "$verify_lab/site/health.txt"
curl --noproxy '*' --fail --max-time 3 \
  "http://127.0.0.1:$verify_port/health.txt" > "$verify_lab/actual"
cmp -- "$verify_lab/expected" "$verify_lab/actual"
printf 'content comparison status: %s\n' "$?"
```

Expect comparison status 0 with no comparison output. The only change was the known exercise response file. In a real application, a file replacement may not represent effective configuration until the application uses it.

### 3. Repeat a bounded client-level check

```bash
for attempt in 1 2 3 4 5; do
  if curl --noproxy '*' --fail --silent --show-error --max-time 3 \
      "http://127.0.0.1:$verify_port/health.txt" > "$verify_lab/actual" \
      && cmp -s -- "$verify_lab/expected" "$verify_lab/actual"; then
    printf 'sample %s: accepted\n' "$attempt"
  else
    printf 'sample %s: FAILED; stop and investigate\n' "$attempt"
    break
  fi
  sleep 1
done
```

Expect five accepted samples. Stop on any failure. The conditional checks both transport/HTTP success and exact bytes, so a partial download or stale previous response cannot silently pass after curl fails.

## Recovery and verification

The supported conclusion is that five local samples met the exercise's response criterion over a short window. This does not prove external reachability, authentication, dependency correctness or resilience after reboot.

For a real service, include appropriate application-level evidence and observe the original failure condition. Check for a growing retry backlog, repeated restarts, new errors and user-visible latency. Confirm data recovery objectives with the data owner rather than inferring them from uptime.

Close the incident with its actual scope: recovered, cause established or still under investigation, data consequences, temporary changes, next owner and follow-up date. Keep customer-facing updates consistent with the evidence. Avoid reporting “root cause fixed” when only a workaround is known.

## Cleanup

While the helper is still your running child:

```bash
kill -TERM "$verify_pid"
wait "$verify_pid"
rm -i -- "$verify_lab/site/health.txt" "$verify_lab/expected" \
  "$verify_lab/actual" "$verify_lab/port" "$verify_lab/server.log"
rmdir -- "$verify_lab/site" "$verify_lab"
```

If its lifetime already elapsed, inspect jobs/process identity before signalling any numeric PID. No production service or system setting was changed.

## References

- [curl response and failure handling](https://curl.se/docs/manpage.html).
- [File comparison with cmp](https://www.gnu.org/software/diffutils/manual/diffutils.html).
- [Restore command reference](../04-commands-and-cheat-sheets/backup-and-recovery/recovery-command-reference.md).
- [Troubleshooting method](linux-troubleshooting-method.md).

[Collection home](README.md)
