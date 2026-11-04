# Monitoring and alerting

Monitoring makes system behavior observable. Alerting asks a person or automated process to act. Start from meaningful service outcomes, then collect the host, application and dependency signals that help explain them. A dashboard full of green host metrics can coexist with a broken user operation.

## Environment and permissions

Tool examples use Linux with systemd, procps and curl where applicable. Monitoring agents need only the access their checks require; credentials and exported labels can reveal sensitive information. The mandatory lab evaluates synthetic check results in Python and contacts no service or notification provider.

The sample alert state machine is intentionally small. It demonstrates consecutive-sample rules and recovery, not a complete monitoring product or a production alert policy.

## Before you begin

Name the service owner, user operation, error/latency expectations and business hours or continuous response requirement. Define what each alert means, who receives it, how they acknowledge it, the runbook and what to do if the first route fails.

Identify monitoring blind spots: a missing agent, stale scrape, expired check credential or disconnected notification route can look like missing rather than unhealthy data. Choose explicit missing-data behavior; do not silently convert unknown into healthy.

## Operating procedure

### 1. Select complementary signals

| Signal | Useful question | Limitation |
| --- | --- | --- |
| External user-path check | Can an authorized client complete the intended operation? | A synthetic path may miss other user/data combinations |
| Errors and latency | How much user impact is occurring? | Aggregates can hide a slow region or request class |
| Queues/backlogs | Is work accumulating faster than it drains? | Empty queues can also mean ingestion failed |
| Host/service state | Are resources or processes contributing? | Active processes do not prove correct responses |
| Backup/replication freshness | Is recovery protection still meeting objectives? | A recent job is not necessarily a usable recovery point |
| Collector/notification health | Can failures actually reach a responder? | Self-reporting alone may fail with the system being observed |

For a known endpoint and unit, bounded diagnostic examples include:

```bash
curl --connect-timeout 3 --max-time 10 --fail https://HOST/APPROVED_CHECK
systemctl status UNIT --no-pager
vmstat 1 5
```

Do not send a mutating production request just to get a green check. HTTP success also needs meaningful content/status interpretation; see [verification practice](../05-troubleshooting-and-recovery/verify-recovery-after-a-fix.md).

### 2. Define actionability and persistence

Use the service's tolerable impact and workload cadence to set thresholds/windows. Require enough evidence to avoid alerting on every harmless sample, while preserving detection speed for serious failures. Define recovery conditions and grouping so one broken dependency does not cause hundreds of unrelated pages.

For every alert, retain its expression, missing-data policy, routing, severity, labels, owner, runbook and a test record. Rate/ratio alerts need adequate denominators: one failure out of one request is different evidence from many failures under normal traffic.

### 3. Test the full route

Use an approved synthetic test or staging target. Confirm detection, notification delivery, acknowledgement, escalation and recovery notification. A rule evaluating correctly does not prove the human route works. Schedule maintenance handling with an owner and expiry rather than leaving a permanent silence.

## Follow-along lab

This sequence represents six observations, with two consecutive failures needed to enter alerting and two successes needed to recover. A single early failure should not alert:

```bash
monitor_lab=$(mktemp -d)
python3 - "$monitor_lab/transitions.txt" <<'PY'
from pathlib import Path
import sys
samples = [False, True, False, False, True, True]
bad = good = 0
alerting = False
rows = []
for number, healthy in enumerate(samples, 1):
    bad = 0 if healthy else bad + 1
    good = good + 1 if healthy else 0
    if not alerting and bad >= 2:
        alerting = True
        rows.append(f'sample {number}: ALERT')
    elif alerting and good >= 2:
        alerting = False
        rows.append(f'sample {number}: RECOVERED')
    else:
        rows.append(f'sample {number}: no state change')
Path(sys.argv[1]).write_text('\n'.join(rows) + '\n')
PY
cat "$monitor_lab/transitions.txt"
```

Expect ALERT at sample 4 and RECOVERED at sample 6. Samples 1 and 3 alone are insufficient. No message is sent anywhere.

As an independent extension, change the samples on your own exercise copy to include a missing observation represented by None. Decide and implement what missing means before running it. Do not let Python's false-like behavior silently choose your operational missing-data policy.

## Verification and rollback

Confirm the transition times match the stated rule, then explain the detection delay in terms of sampling cadence. Six samples are not automatically six seconds. The lab says nothing about real notification delivery or threshold suitability.

For a real rule, use the platform's supported syntax/unit tests plus an authorized end-to-end route test. If a rollout produces noise or misses impact, restore the reviewed previous rule/routing and verify it; keep a temporary observation path while adjusting the design. Do not disable all alerts to silence one noisy rule.

## Cleanup

```bash
rm -i -- "$monitor_lab/transitions.txt"
rmdir -- "$monitor_lab"
```

No agent, monitoring rule, silence or external notification changed.

## References

- [Prometheus alerting-rule behavior](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/) and [rule testing](https://prometheus.io/docs/prometheus/latest/configuration/unit_testing_rules/): one implementation to study, not a required stack.
- [curl](https://curl.se/docs/manpage.html) and [performance interpretation](../04-command-reference/performance/performance-investigation-cheat-sheet.md).

[Collection home](README.md)
