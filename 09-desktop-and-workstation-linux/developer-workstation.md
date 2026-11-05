# Build a developer workstation you can reproduce

[Collection home](README.md) · Previous: [Backups](personal-backups-and-migration.md) · Next: [Troubleshooting](desktop-troubleshooting-and-recovery.md)

## Environment and prerequisites

Use an ordinary account on a supported Linux installation. Begin with an editor, terminal and the language toolchain your project needs. A productive workstation is one you can update, explain and rebuild; installing every available tool is not the goal.

The exercise requires Bash, Python 3 with its `venv` module and enough temporary space for a small environment. It uses **no pip downloads**, global packages, credentials, containers or administrator access. Some distributions separately package language-environment support; use the distribution's documented package if `venv` is missing. `--without-pip` is intentional because this project needs only the standard library.

For real projects, assess repository trust before opening them in an editor that can run tasks, extensions or environment hooks. Cloning source does not make its build scripts safe. Do not paste personal tokens into a terminal history or commit them to a repository.

## Understand the components

| Component | Keep explicit | Why |
| --- | --- | --- |
| OS packages | Repository, release and update route | Host maintenance and project dependencies are different layers |
| Language runtime | Version and installation source | A command called `python3` can select different interpreters in different contexts |
| Project environment | Local dependencies and activation/invocation | Isolation reduces accidental coupling; it is not a security sandbox |
| Dependency lock/constraints | Resolved versions and applicable platform/runtime | Reproducibility depends on tool semantics and artifact availability |
| Editor/IDE | Extensions, task commands and workspace trust | Opening a workspace can trigger project-defined behavior |
| Git | Identity, ignore rules, remotes and credential handling | Version control does not automatically back up untracked or unpushed work |
| Build/test | Documented inputs, commands and acceptance criteria | A build passing on one machine does not prove every deployment target |
| Secrets | Approved storage and injection route | `.gitignore` does not remove a secret already committed |
| Containers/VMs | Explicit isolation and resource needs | Privileged containers, host mounts and daemon access change authority |

Avoid replacing distribution Python, using sudo pip, or disabling externally managed environment protections to install a project's library. Use project-local environments or a supported language/application tool. Different languages have different isolation mechanisms; Python's `venv` is not a universal package manager.

## Follow along

### 1. Run a dependency-free project with an explicit interpreter

The test checks a concrete behavior, deliberately introduces a regression in the disposable source, observes a failed test and restores the known source. The environment stays inside the fixture.

<!-- workstation:exercise -->
```bash
dev_lab=$(mktemp -d) || exit 1
python3 -m venv --without-pip "$dev_lab/venv" || exit 1
python3 - "$dev_lab" <<'PY'
from pathlib import Path
import subprocess
import sys
root = Path(sys.argv[1])
project = root / 'project'
project.mkdir()
(root / '.linux-world-fixture').write_text('developer-workstation\n')
source = 'def greeting(name):\n    return "Hello, " + name + "!"\n'
(project / 'greet.py').write_text(source)
(project / 'test_greet.py').write_text(
    'import unittest\nfrom greet import greeting\n'
    'class GreetingTest(unittest.TestCase):\n'
    '    def test_named_reader(self):\n'
    '        self.assertEqual(greeting("Linux learner"), "Hello, Linux learner!")\n')
interpreter = root / 'venv/bin/python'
def check():
    import os
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    return subprocess.run([str(interpreter), '-m', 'unittest', '-v'], cwd=project,
                          env=env, capture_output=True, text=True, timeout=20)
result = check()
assert result.returncode == 0, result.stderr
print('PASS: explicit project interpreter passes the behavior test')
(project / 'greet.py').write_text('def greeting(name):\n    return "Wrong response"\n')
result = check()
assert result.returncode == 1 and 'FAIL:' in result.stderr, result.stderr
print('PASS: deliberate source regression is detected by the test')
(project / 'greet.py').write_text(source)
result = check()
assert result.returncode == 0, result.stderr
version = subprocess.run([str(interpreter), '-c',
                          'import sys; assert sys.prefix != sys.base_prefix; print(sys.version.split()[0])'],
                         check=True, capture_output=True, text=True).stdout.strip()
print('PASS: restored source passes again in a virtual environment; Python ' + version)
PY
```

If environment creation fails, stop and inspect the error before continuing. The exercise's explicit interpreter avoids reliance on an interactive activation script. Activation is convenient but not necessary; a scheduler or editor can invoke a different interpreter unless you configure it.

### 2. Connect your editor to the project

Open only the new `project` directory in your editor after inspecting the files. Select the fixture's `venv/bin/python` if your editor supports interpreter selection. Run the test using the same documented command from that directory. Check that an editor's green status corresponds to the intended test and environment, not another open workspace.

For your actual project, keep setup and test commands in its documentation. Record the runtime version and dependency installation procedure. Use a reviewed lock/constraints strategy where supported, and validate a clean setup rather than relying on a long-lived environment with hidden packages.

### 3. Add version control deliberately

For a real project, initialize or clone only in the intended directory. Review `git status` before staging. Ignore generated environments, caches and local secrets using patterns appropriate to your project; inspect the staged diff, not just the file count. Configure a suitable identity and approved authentication route.

Do not commit private keys or tokens. If a real secret enters history, follow the provider's revocation/rotation process; deleting the working-tree file is insufficient. Do not rewrite shared history as an unannounced “cleanup.”

### 4. Keep the workstation maintainable

Separate host updates from project dependency changes so failures can be localized. Save work and test the project after relevant runtime/editor updates. Record extension sources and review their privileges. Keep a lightweight inventory of essential tools rather than a dump of your whole environment, which may contain secrets.

If you later use containers, understand bind mounts, socket access, exposed ports and resource limits before running project instructions. A local environment under your account can still read your account's files; `venv` provides dependency isolation, not containment of untrusted code.

## Verify and recover

Expect three `PASS` lines. The deliberate regression must fail the test with status 1; an import error or missing interpreter is not the intended demonstration. After recovery, the source and test pass under the fixture's explicit interpreter.

For a real workstation, you should be able to create a fresh project environment from documented inputs and run the same meaningful checks without copying your old environment directory. Re-create virtual environments after moving machines or changing their base interpreter; they are not generally portable archives.

If an editor disagrees with the terminal, compare interpreter paths, working directories, environment values relevant to the project and the exact test command. Do not solve it by installing dependencies globally until the paths happen to converge.

## Cleanup

Close the project in your editor first. This cleanup verifies a fixture marker and removes only its generated environment, then explicitly removes the small source files:

<!-- workstation:cleanup -->
```bash
python3 - "$dev_lab" <<'PY'
from pathlib import Path
import shutil
import sys
root = Path(sys.argv[1])
assert (root / '.linux-world-fixture').read_text() == 'developer-workstation\n'
assert (root / 'venv/pyvenv.cfg').is_file()
assert not (root / 'venv').is_symlink()
shutil.rmtree(root / 'venv')
PY
rm -i -- "$dev_lab/project/greet.py" "$dev_lab/project/test_greet.py" "$dev_lab/.linux-world-fixture"
rmdir -- "$dev_lab/project"
rmdir -- "$dev_lab"
```

If your editor created additional files, inspect them in this temporary directory before removing them; an `rmdir` refusal is a cue to inspect, not to broaden deletion. Keep real project repositories and backup procedures separate.

## Checkpoint

You can identify the interpreter actually running a project, demonstrate a meaningful failing/passing test, and rebuild an environment without global package changes or copied credentials.

## Sources

Use [Python venv documentation](https://docs.python.org/3/library/venv.html), [Python unittest](https://docs.python.org/3/library/unittest.html), [externally managed environments specification](https://packaging.python.org/en/latest/specifications/externally-managed-environments/), [Python packaging environment guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/), [Git documentation](https://git-scm.com/doc) and your editor's official workspace-trust and interpreter documentation. Dependency pinning alone does not establish complete build reproducibility.
