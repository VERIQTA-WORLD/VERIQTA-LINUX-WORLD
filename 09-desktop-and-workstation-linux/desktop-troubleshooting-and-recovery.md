# Troubleshoot the desktop without erasing your profile

[Collection home](README.md) · Previous: [Developer workstation](developer-workstation.md)

## Environment and prerequisites

Use this guide to distinguish application, session, account, hardware and system problems. Start with a narrow symptom and preserve the work you can still access. A terminal command succeeding does not prove a GUI application works, and one broken application does not prove the whole desktop is damaged.

The isolated exercise needs Bash, Python 3 and an ordinary account. It reproduces a working-directory error in a tiny local application and repairs the application to find its own input reliably. It does not change a real launcher, desktop profile, user service or system package.

For manual recovery, you need a documented way back into your computer and any encryption/recovery credentials. Graphical logout, display-manager restart and reboot can end sessions and lose unsaved work; do not perform them simply because a checklist mentions them.

## Understand the components

| Failure boundary | Useful question | What to preserve |
| --- | --- | --- |
| One document | Does another harmless document open in the same application? | Original file, exact error and application version |
| One application | Do other applications work in the same session? | Package source, launch method and bounded application diagnostics |
| One launch method | Does terminal launch differ from the desktop launcher? | Working directory, executable identity and specific required environment |
| One account/session | Does the issue follow your profile or session type? | Relevant settings and recent changes; not an indiscriminate configuration dump |
| Hardware path | Does a direct connection differ from dock/hub use? | Exact connection and component behavior |
| System/startup | Can the installed system boot and provide a local recovery route? | Boot/upgrade context and the distribution's recovery instructions |

Do not publish full environment dumps, browser profiles, screenshots of private windows or unredacted journals. Tokens and personal data can appear in mundane diagnostic output. Collect only what distinguishes the competing explanations.

## Follow along

### 1. Write a symptom you can retest

Choose a statement such as “The editor opens from the menu but cannot find its project file” rather than “Linux is broken.” Record when it last worked, what changed and which exact action reproduces it. Note whether other documents/apps/users are affected without changing all of them at once.

Identify the application package and source using the [application guide](applications-and-software-trust.md). A shell alias, Flatpak and native package can launch different copies. Compare the process and document context before assuming they are equivalent.

### 2. Reproduce a launch-context failure safely

The first program looks for a relative file in the caller's working directory. It succeeds from its project directory and fails from another directory. The corrected program anchors its input to its own location. That is appropriate for this fixture's design; real applications may intentionally use a caller-supplied directory instead.

<!-- workstation:exercise -->
```bash
recovery_lab=$(mktemp -d) || exit 1
python3 - "$recovery_lab" <<'PY'
import os
from pathlib import Path
import subprocess
import sys
root = Path(sys.argv[1])
project = root / 'project'
other = root / 'other'
project.mkdir()
other.mkdir()
(project / 'message.txt').write_text('Expected local application message\n')
app = project / 'app.py'
original = 'from pathlib import Path\nprint(Path("message.txt").read_text(), end="")\n'
app.write_text(original)
(root / 'original-app.txt').write_text(original)
env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
def run(directory):
    return subprocess.run([sys.executable, str(app)], cwd=directory, env=env,
                          capture_output=True, text=True, timeout=10)
assert run(project).returncode == 0
failed = run(other)
assert failed.returncode == 1 and 'FileNotFoundError' in failed.stderr
(root / 'failure.txt').write_text(failed.stderr)
print('PASS: identical program succeeds or fails depending on caller directory')
app.write_text('from pathlib import Path\n'
               'path = Path(__file__).resolve().parent / "message.txt"\n'
               'print(path.read_text(), end="")\n')
for directory in [project, other]:
    result = run(directory)
    assert result.returncode == 0, result.stderr
    assert result.stdout == 'Expected local application message\n'
assert (root / 'original-app.txt').read_text() == original
print('PASS: repaired input lookup works from both directories; original source retained')
PY
```

Read the last line of `failure.txt`. The evidence concerns a missing relative path in a specific context; it does not justify reinstalling Python or changing filesystem permissions. Launching an application from a terminal can also change environment, arguments or sandbox context, so a terminal/menu difference is a lead to investigate, not proof of one universal cause.

### 3. Choose the smallest next check

| Symptom | First distinguishing checks | Avoid as a first response |
| --- | --- | --- |
| One app freezes | Unsaved work, reproducible document/action, app-specific status/logs | Killing the whole session |
| Login loops | Storage capacity, exact session error, recent user changes and installed session availability | Deleting all home dotfiles |
| Desktop is slow | Actual workload, CPU/memory/I/O pressure and relevant process/account scope | Clearing every cache or disabling security policy |
| Settings change has no effect | Correct account, active session, consumer and precedence | Editing several guessed configuration files |
| Audio/display disappears after docking | Device selection, connector path and session observations | Replacing the entire graphics/audio stack |
| App cannot see a selected file | File path, permissions, sandbox/portal grant and app identity | Running the GUI as root |
| Update appears related | Exact package/transaction and repeatable before/after behavior | Assuming every nearby log warning is the cause |

For local journals, choose the relevant user/system unit and time window using the [log reference](../08-resources-and-reference/linux-log-location-reference.md). A user-service query is meaningful only if that application actually runs as that unit. Lack of permission or an empty query is a limit, not proof that nothing happened.

### 4. Check everyday connectivity in the right context

Open the desktop's Network or Wi-Fi settings and identify the intended connection. Check airplane mode, a hardware radio switch and whether the network is your own or an authorized one. For enterprise Wi-Fi, use the organization's supplied identity/certificate procedure; do not disable certificate validation to make a connection succeed. Captive portals and VPNs can change access after the link connects.

If a browser fails, compare another authorized application and identify the exact failure: name lookup, connection, TLS or application response. Check the clock, proxy and intended VPN route without publishing credentials or private endpoints. A Wi-Fi icon does not establish internet access; a successful public website request does not prove access to an internal service. Do not bypass a required VPN or organizational policy as a permanent fix. Use the [networking reference](../08-resources-and-reference/linux-networking-reference.md) for layer-specific observations.

### 5. Recover with a verification target

Save accessible work first. If the application offers safe mode or a supported way to disable one recently added extension, use that route and retest the same action. Back up the specific relevant setting before resetting it; preserve your assistive configuration and application data.

A fresh test account can distinguish some profile-related failures, but creating it requires authorized administration and it does not automatically explain the cause. Use a disposable VM for experiments when possible. For a real account, do not remove or rename the entire profile while applications are using it.

If a session must end, explain the expected loss of running state and retain another usable sign-in/recovery route. Display-manager restarts can affect other users too. For boot failures or filesystem problems, move to the distribution's recovery procedure and the [troubleshooting collection](../05-troubleshooting-and-recovery/README.md), preserving the storage and evidence rather than repeatedly reinstalling.

## Verify and recover

The fixture should print two `PASS` lines. The original failure has the specific `FileNotFoundError`, and the repaired program returns the expected content from both directories. Merely changing the exit status would not meet the acceptance criterion.

For a real desktop repair, repeat the original failing action, then check an adjacent normal workflow for regressions. Record what changed and how to undo it. If the result is inconclusive, say so and preserve a narrower report rather than escalating into unrelated changes.

A useful public bug report includes product/version, session type, minimal reproduction, expected/actual behavior and a small redacted evidence excerpt. Do not upload a whole profile or another person's logs. Follow the project's reporting process and avoid claiming a cause you have not established.

## Cleanup

<!-- workstation:cleanup -->
```bash
rm -i -- "$recovery_lab/project/app.py" "$recovery_lab/project/message.txt" "$recovery_lab/original-app.txt" "$recovery_lab/failure.txt"
rmdir -- "$recovery_lab/project" "$recovery_lab/other"
rmdir -- "$recovery_lab"
```

Restore only real settings you changed deliberately. Keep needed backups and do not delete diagnostic evidence required for an ongoing incident. The exercise has no real session changes to undo.

## Checkpoint

You can describe a reproducible symptom, choose a check that distinguishes two explanations and verify the actual user operation after recovery. You can explain why deleting a profile is a high-impact action rather than a routine troubleshooting step.

## Sources

Use [GNOME troubleshooting help](https://help.gnome.org/gnome-help/), [KDE bug reporting guidance](https://community.kde.org/Get_Involved/Issue_Reporting), [Python pathlib](https://docs.python.org/3/library/pathlib.html), [Python subprocess](https://docs.python.org/3/library/subprocess.html), [systemd journalctl](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html) and the application's own diagnostic documentation. A language fixture demonstrates its stated failure, not the behavior of every graphical application.
