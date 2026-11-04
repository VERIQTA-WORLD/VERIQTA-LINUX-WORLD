# A server or application is unreachable

“Unreachable” describes a client result, not a single fault. A wrong name, stale address, route, packet filter, missing listener or unhealthy application can all make a service unusable. Diagnose the exact protocol, address, port and client path.

## Environment and permissions

Diagnostic examples target Linux with iproute2, curl and optional DNS tools. Use the client that experiences the problem and, when authorized, the target's console. Read-only socket queries are normally unprivileged; process attribution and firewall state may require sudo. Test only systems you own or are authorized to investigate.

The lab uses Bash, Python 3 and curl from the repository root. It creates a temporary HTTP service bound only to loopback and needs no administrator privileges. It demonstrates a missing listener after shutdown, not a cloud routing or firewall outage.

## First checks

Record the requested hostname, resolved address, port, protocol, exact error, affected clients and time window. Distinguish an HTTP error response from inability to establish a connection.

On the affected Linux client, replace HOST and ADDRESS with verified values:

```bash
date -Is
getent ahosts HOST
ip route get ADDRESS
curl --connect-timeout 3 --max-time 10 -I https://HOST
```

`getent` follows configured name services. `ip route get` predicts the route without probing it. curl includes DNS, transport and TLS for HTTPS. Its timeout is a bound on this test, not an expected service latency. HEAD can behave differently from GET, so repeat with the real operation where appropriate.

If console access works, inspect the target without restarting it:

```bash
ip -br address
ip route show
ss -ltn
systemctl --failed --no-pager
```

For a known service, inspect its actual unit and bounded logs. A cloud console being reachable does not prove the application network path is reachable.

## Evidence and interpretation

| Observation | Plausible explanations | Next discriminating check |
| --- | --- | --- |
| Name cannot resolve | Wrong name, resolver failure, split-DNS mismatch | Compare system lookup with DNS query and intended records |
| Connection refused | No listener, explicit rejection, wrong endpoint | Inspect the exact target address/port and network namespace |
| Connection times out | Filtering, routing loss, unavailable host, overloaded listener | Compare client route, target state and authorized intermediate telemetry |
| TCP connects, TLS fails | Wrong name/certificate, clock, protocol or trust problem | Read TLS error and verify hostname, trust chain and time |
| HTTP 401/403 | Application authorization or policy | Compare identity and request permissions, not routing |
| HTTP 502/503 | Frontend reachable, backend or capacity problem | Inspect frontend/backend health and relevant logs |
| Works locally, fails remotely | Loopback bind, remote policy, different route or DNS | Compare bind address, affected client resolution and allowed source path |

A failed ping is not proof the host is down: ICMP may be filtered. A successful ping does not establish that an application port or TLS works. An IPv6 path can fail while IPv4 works, so compare the resolved families rather than silently forcing one forever.

## Recovery decisions

Correct the confirmed boundary: a stale client endpoint, an unintended bind address, a specific missing policy rule or a failed application. Obtain console access and preserve the current configuration before network changes. Do not flush firewall rules or restart the network stack as a general diagnostic step.

If the target has no console access and every path is lost, use the infrastructure owner's recovery channel. Repeated remote changes without feedback can make recovery harder.

## Follow-along lab

### 1. Start a known-good loopback endpoint

Use a normal shell from the repository root:

```bash
reach_lab=$(mktemp -d)
mkdir "$reach_lab/site"
printf 'ready\n' > "$reach_lab/site/health.txt"
python3 05-troubleshooting-and-recovery/labs/loopback_http.py \
  --directory "$reach_lab/site" --ready-file "$reach_lab/port" \
  > "$reach_lab/server.log" 2>&1 &
reach_pid=$!
for attempt in {1..50}; do
  test -s "$reach_lab/port" && break
  sleep 0.1
done
test -s "$reach_lab/port"
```

The final test must succeed. If it fails, inspect server.log and stop here. The helper chooses an available port and exits after at most 180 seconds. Complete the exercise within that window or start a fresh instance.

```bash
reach_port=$(cat "$reach_lab/port")
curl --noproxy '*' --fail --max-time 3 "http://127.0.0.1:$reach_port/health.txt"
```

Expected body: `ready`. On Linux, `ss -ltn "sport = :$reach_port"` should show a loopback listener. A proxy is explicitly bypassed so this test stays local.

### 2. Introduce one known failure

Stop only the child created in this shell, then wait for it to exit:

```bash
kill -TERM "$reach_pid"
wait "$reach_pid"
curl --noproxy '*' --fail --max-time 3 "http://127.0.0.1:$reach_port/health.txt"
printf 'curl status: %s\n' "$?"
```

The request should fail, commonly with curl status 7 for inability to connect. If another process claimed the port, inspect the new listener instead of assuming the outcome. The known cause is that the lab server stopped. It would be unjustified to conclude a real timeout had this cause without equivalent evidence.

### 3. Recover the teaching service

Delete only the stale readiness file before starting a new instance. A new available port may be chosen:

```bash
rm -i -- "$reach_lab/port"
python3 05-troubleshooting-and-recovery/labs/loopback_http.py \
  --directory "$reach_lab/site" --ready-file "$reach_lab/port" \
  > "$reach_lab/server.log" 2>&1 &
reach_pid=$!
for attempt in {1..50}; do
  test -s "$reach_lab/port" && break
  sleep 0.1
done
test -s "$reach_lab/port"
```

Stop if readiness fails. This lab changes the test endpoint when necessary because its port is ephemeral. A real service must recover on its approved endpoint rather than asking clients to chase arbitrary ports.

## Recovery and verification

```bash
reach_port=$(cat "$reach_lab/port")
curl --noproxy '*' --fail --max-time 3 "http://127.0.0.1:$reach_port/health.txt"
```

Expect `ready` again. Record the failed request, absent listener and recovered response as separate evidence. In a real incident, retest the approved endpoint from the originally affected client and inspect dependency health, errors and latency over a suitable observation window.

## Cleanup

Stop the known child while it is still this shell's running job. If you waited past its bounded lifetime, use `jobs -l` first and do not signal a stale PID that may have been reused.

```bash
kill -TERM "$reach_pid"
wait "$reach_pid"
rm -i -- "$reach_lab/site/health.txt" "$reach_lab/port" "$reach_lab/server.log"
rmdir -- "$reach_lab/site" "$reach_lab"
```

## References

- [ip route](https://man7.org/linux/man-pages/man8/ip-route.8.html) and [ss](https://man7.org/linux/man-pages/man8/ss.8.html).
- [curl manual](https://curl.se/docs/manpage.html).
- [DNS investigation](dns-resolution-is-failing.md) and [SSH investigation](ssh-login-is-failing.md).

[Collection home](README.md) · [Troubleshooting method](linux-troubleshooting-method.md)
