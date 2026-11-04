# Linux lab safety

A good exercise has a known boundary, a recoverable setup and an acceptance check. Read its setup, effects and cleanup before running anything. Stop when evidence differs from the stated assumptions rather than escalating privileges or expanding scope blindly.

## Before each exercise

- Identify the machine, account, directory and namespace you are using.
- Confirm it is the intended disposable environment and that console/reset access works where needed.
- Keep important data, real secrets and unrelated workloads outside the experiment.
- Check tool availability, version, permission requirements and resource bounds.
- Know what will change, what an expected failure looks like and how to clean up.

## Protect the boundary

Quote paths and variables. Verify file, device, interface, unit and account names before changes. A placeholder such as DEVICE must never be replaced by a guessed disk. Temporary exercises should use their unique directory; do not translate cleanup into a broad command against your home, root filesystem or application data.

A normal account can still delete its own important files. Sudo adds authority, not correctness. Avoid experiments that disable enforcement, flush networking policy, fill a real filesystem, force repairs, expose a service publicly or consume unbounded resources unless a dedicated, tested lab explicitly establishes the required isolation and recovery.

## Keep evidence useful and private

Record expected versus actual results and meaningful exit statuses. Logs, environment variables, command arguments, packet captures and configuration can contain secrets or personal data. Keep raw evidence protected and publish only reviewed redacted material.

A failed step can be intentional teaching evidence. Distinguish that from an unmet prerequisite. If a filesystem, service or package manager enters an unexpected state, stop dependent changes and follow the relevant recovery guide.

## Cleanup is part of the skill

Identify the exact resources created by the exercise. Stop only its known running processes, undo only its temporary configuration, unmount only its confirmed lab mounts and remove only its disposable data. Do not signal an old numeric PID without rechecking identity because PIDs can be reused.

Verify cleanup rather than assuming a command succeeded. Record deliberately retained evidence and any incomplete cleanup. Reusing a machine does not excuse leaving an unknown service, mount or credential behind.

[Environment setup](set-up-your-linux-environment.md) · [Troubleshooting method](../05-troubleshooting-and-recovery/linux-troubleshooting-method.md) · [Start here](README.md)
