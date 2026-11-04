# Build, verify and recover a Linux project

Use this workflow with the detailed instructions in your chosen project. It gives you explicit checkpoints for deciding whether to continue, investigate or restore the lab. Start with the guide’s prerequisites and architecture, then follow its implementation sequence.

[All projects](README.md) · [Junior](01.%20Junior/README.md) · [Mid-Level](02.%20Mid-Level/README.md) · [Senior](03.%20Senior/README.md)

## 1. Confirm prerequisites and ownership

Before running a modifying command, record:

| Requirement | What to confirm |
| --- | --- |
| Knowledge | You can demonstrate the listed prerequisite skills; use the [foundation lessons](../01-Beginner-to-Advanced/README.md) to fill gaps. |
| Environment | Distribution/release, architecture, shell/tool versions, required VM count and available CPU, memory and storage match the exercise. |
| Topology | Hostnames, addresses, routes and client/server roles are deliberate; example addresses do not collide with your real networks. |
| Access | Ordinary and administrative accounts work; console access and recovery credentials are available outside the service being changed. |
| Resource ownership | Named users, groups, paths, ports, volumes and services are absent or explicitly assigned to this project. Stop on a collision rather than overwriting an existing resource. |
| Recovery | A known-good baseline, configuration copies, restorable data and a VM reset route exist where required. A snapshot alone is not an independent backup. |
| Scope | You own or are authorized to use every target. Failure injection stays inside dedicated disposable lab infrastructure. |

**Continue when:** prerequisites are met and you can identify both the target and recovery route. If a dependency is missing, resolve it before proceeding. Read the [environment setup](../00-start-here/set-up-your-linux-environment.md) and [lab safety](../00-start-here/linux-lab-safety.md) guidance.

## 2. Implement in verified stages

Read setup, implementation, failure experiments and cleanup before modifying the lab. Identify which host and account runs each command. Work from the documented directory and preserve variables only for the shell session where they are defined.

Treat complete scripts, configuration files, syntax illustrations, representative output and deliberately incorrect examples differently. Replace placeholders before execution. Never paste a whole guide into a shell. Review package proposals, effective policies and changes to persistent configuration before accepting them.

For each stage, record the intended effect, run the smallest documented change, inspect the result and preserve evidence. Validate a candidate with the relevant parser before activation where supported. Keep the previous compatible state for rollback. Do not mask an unexplained failure simply to reach the next stage.

**Continue when:** the stage’s check passes and you can explain what changed. A parser passing proves syntax within its scope; it does not prove application readiness or data correctness.

## 3. Verify behavior from the affected user path

Define acceptance criteria before the first failure experiment. Use the project’s tests and final validation, adding environment-specific observations where needed.

| Capability | Evidence to collect |
| --- | --- |
| Identity and access | Expected operations succeed as the intended account; denied operations fail for the expected policy reason. |
| Application or network service | The real client path returns the expected content/result; process state and a listening socket are supporting checks. |
| Automation | Valid inputs succeed, invalid inputs fail clearly, required output is correct and a repeated run has understood effects. |
| Backup | Restore to an isolated destination; compare required data and metadata and check application consistency where relevant. |
| Monitoring | A bounded test produces the expected signal and recovery state; distinguish a generated alert from actual notification delivery. |
| Availability and performance | Record baseline, measurement interval, workload and failed requests; compare like conditions and identify shared failure domains. |

**Continue when:** relevant functional, negative and data checks pass. Record meaningful nonzero statuses rather than treating every nonzero result as the same failure.

## 4. Introduce one controlled failure and recover

Start only from a verified healthy baseline. Choose one documented fault, the exact resource affected, a maximum impact/duration and an explicit recovery trigger. Do not combine faults until the individual experiments are understood and the project calls for a combined scenario.

1. Record healthy application/data checks and relevant service, policy and resource state.
2. Introduce the scoped fault and confirm the expected symptom with a failing acceptance check.
3. Form a hypothesis; collect evidence that distinguishes it from alternatives.
4. Apply the documented repair or compatible rollback. A code rollback may not reverse a database or data-format change.
5. Repeat the same user-path and data checks used before the fault, then observe stability over an appropriate interval.
6. Restore the baseline before another experiment; record changes intentionally retained.

**Continue when:** recovery is demonstrated and the evidence explains both the failure and repair. One successful HTTP request does not establish sustained recovery. If access or target identity is uncertain, stop dependent changes and use the recovery console.

## 5. Clean up or retain the lab deliberately

Choose an end state before cleanup: retain a known-good lab, restore its baseline or dismantle dedicated project resources. Some advanced guides intentionally retain their platform after removing failure artifacts. Record that choice rather than assuming all cleanup means uninstalling everything.

- Preserve useful evidence after redaction. Confirm that credentials, keys and private data are absent before publishing.
- Disable the project’s schedules, timers and workload generators before removing files they use.
- Inspect process ownership, start time and command before signaling an exact lab process. Old PID files and process-name matches are discovery aids, not proof of ownership.
- Stop and remove only project-owned units, containers, accounts, rules and paths. Review package removal proposals interactively; retain shared dependencies.
- Confirm lab mounts and backing devices before unmounting or deleting storage. If unmount fails, investigate; do not continue with backing-file deletion.
- Restore the recorded configuration, sysctls and access path where required. Preserve a working session while verifying an independent login after authentication or firewall changes.
- Re-run the guide’s cleanup verification and compare against the original baseline. Check for remaining workers, listeners, mounts, schedules and intentionally retained resources.

**Finish when:** the chosen end state is verified, residual resources are accounted for and unrelated services remain healthy. For complex dedicated VM labs, a verified baseline reset can be more reliable than attempting to undo undocumented changes manually.

## Record the result

```text
Project / repository revision:
Host roles, distribution and tool versions:
Prerequisites and resource ownership confirmed:
Baseline and recovery route:
Implementation stages and decisions:
Acceptance criteria and actual results:
Controlled fault, observed symptom and diagnostic evidence:
Repair / rollback and repeated acceptance results:
Cleanup or retained state, including any unresolved resources:
Limits of the experiment and next independent improvement:
```

Use the [progress checklist](../00-start-here/learning-progress-checklist.md) to distinguish following instructions from independent reproduction. Publish only claims supported by your own evidence. These guides do not establish that a deployment is production-ready merely because its title includes “production” or “enterprise.” Review [permissions and contribution guidance](../CONTRIBUTING.md) before sharing adaptations of repository content.
