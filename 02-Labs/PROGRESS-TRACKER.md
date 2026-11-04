# Track your Linux lab progress

Keep this record in your own private notes. You do not need to edit the public repository to record personal progress. Use the [Junior index](Junior/README.md) to open each of the 83 numbered lab guides.

[Lab home](README.md) · [Lab standard](LAB-STANDARD.md) · [Safety](LAB-SAFETY.md)

## Distinguish the kind of progress

| State | What you can demonstrate |
| --- | --- |
| Read | Explain the concept, environment and likely effects in your own words. |
| Followed | Complete the documented steps and record actual output, expected failures and cleanup. |
| Reproduced | Repeat from the stated prerequisites without relying on hidden state or copying the solution path blindly. |
| Extended | Predict and verify one independent variation, including a negative case and its limitations. |

Do not mark an unavailable prerequisite or skipped Linux extension as executed. You can complete the portable portion while honestly recording which host behavior you have not reproduced.

## Copy one record per lab

```text
Lab ID and title:
Guide / repository revision:
Date and progress state:

Environment:
Distribution, kernel, architecture, shell and relevant tool versions:
Account, privileges, VM/container/host boundary:
Required prerequisites confirmed:
Workspace and resource ownership:
Recovery route:

Practice:
Goal and acceptance criterion:
Expected observations and statuses:
Actual output, stderr and meaningful statuses:
What differs and why:

Investigation:
Controlled fault and its limit:
Observed symptom and evidence:
Alternative hypotheses and discriminating check:
Repair or revised interpretation:
Repeated acceptance results:

Completion:
Cleanup or deliberately retained resources:
Private evidence location / sanitized report:
Linux-specific steps skipped or not yet reproduced:
Independent extension and result:
What I can explain without looking at the guide:
Next lab or prerequisite to revisit:
```

## Check your progression by capability

| Range | Checkpoint before moving on |
| --- | --- |
| JUN-001–034 | Navigate deliberately, manage private files, explain identity/access, inspect processes/services and interpret command results. |
| JUN-035–043 | Identify the correct storage layer and mount, understand capacity and use only confirmed disposable storage for changes. |
| JUN-044–057 | Explain addresses, routes, names, ports and the client/server boundary; preserve recovery access. |
| JUN-058–068 | Write and explain Bash input/output, conditions, loops, functions, statuses, failure handling and scheduled execution. |
| JUN-069–076 | Interpret scoped logs and interval measurements without inventing a diagnosis from a single counter. |
| JUN-077–078 | Combine fresh evidence, retain unknowns, investigate alternatives and repeat the same acceptance operation after repair. |
| JUN-079–083 | Recover controlled service, access, storage and connectivity failures within exact lab boundaries. |

A range being read does not mean every capability is demonstrated. Choose the lab whose checkpoint exposes the gap and reproduce a smaller exercise before proceeding.

## Make your report useful to another reader

Retain enough setup information for someone to reproduce your result. Explain units, sample interval, target identity, permissions and what your test does not establish. Use synthetic data in shared examples and keep raw captures private.

Screenshots can support a report but do not replace exact commands, statuses and expected/actual comparisons. Do not claim a full Linux runtime test from a supplied JSON fixture or a macOS portable execution.

Before starting a larger [project](../03-Projects/README.md), demonstrate the relevant prerequisites and a verified restore/recovery path. A checked list does not certify professional seniority or readiness to modify someone else's system.
