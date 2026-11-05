# Find and use official Linux documentation

[Reference library](README.md) · [Glossary](linux-glossary.md) · [Learning resources](linux-books-and-learning-resources.md)

## Scope and environment

Use this page when you have a specific question about a command, file, API or distribution. Your goal is to find the source that describes the system you actually have, then check your interpretation with a small observation.

Linux documentation has several owners. The kernel project documents kernel interfaces; GNU projects document many user-space tools; distributions document packaging and integration; individual applications document their own configuration. No single website describes every installed Linux system.

The exercise needs Bash and an ordinary account. It creates one temporary directory. Optional manual-page lookups need `man` and the relevant manual packages. A minimal container can lack those packages even when the command itself is installed. You do not need root privileges or an internet connection for the exercise.

## Reference

### Choose a source by the question

| Your question | Start here | What to check before applying the answer |
| --- | --- | --- |
| Which options does this installed command accept? | Its installed `--help`, manual page or built-in help | Executable path, implementation and package version |
| What does a shell expression mean? | Your shell's manual | Bash, dash, zsh and fish have different languages; your interactive shell and a script's interpreter can differ |
| What does this configuration key mean? | The application's installed configuration manual | Version, accepted value, default, precedence and whether activation requires a reload or restart |
| How did this distribution configure the service? | The distribution's release-specific documentation and packaged unit/configuration | Package patches, generated files and the selected release |
| What does a kernel interface guarantee? | Kernel documentation and the relevant Linux manual page | Kernel version, enabled features, privileges and namespace |
| Is this behavior portable? | POSIX plus each implementation's documentation | The standard's scope; a Linux extension is not automatically available elsewhere |
| How should I use a library/API? | That library's versioned API reference | Language binding, return values, error handling and compatibility policy |
| Why does a tutorial disagree with my machine? | Installed help, upstream release notes and distribution documentation | The tutorial's date, platform, assumptions and package origin |

Installed documentation often matches your package, but it can be incomplete or separately packaged. Upstream `latest` documents a moving version. A distribution may backport a fix without adopting the upstream version number. Treat apparent disagreements as questions to resolve, not a reason to copy whichever command looks newest.

### Read a manual page deliberately

A manual section identifies the kind of interface. It does not grant permission to use it.

| Section | Usual subject | Example lookup |
| --- | --- | --- |
| 1 | User commands | `man 1 printf` |
| 2 | Kernel system calls | `man 2 open` |
| 3 | Library functions | `man 3 printf` |
| 4 | Device interfaces | `man 4 null` |
| 5 | File formats and configuration | `man 5 fstab` |
| 6 | Games | Availability depends on installed packages |
| 7 | Overviews, conventions and protocols | `man 7 signal` |
| 8 | Administration commands | `man 8 mount` |

`man printf` can select a different subject from `man 3 printf`. `man -w 1 printf` asks where the page is stored. `man -k keyword` searches a manual database that might need installation or rebuilding. A failed lookup does not establish that Linux lacks the feature.

Read these sections in order:

1. **NAME and SYNOPSIS:** confirm the exact interface. Optional notation such as `[OPTION]` is usually explanatory; do not type the brackets unless the tool says they are literal.
2. **DESCRIPTION and OPTIONS:** identify the behavior and its defaults. Check how the tool distinguishes an option from an operand, including whether it accepts `--`.
3. **EXIT STATUS or RETURN VALUE:** distinguish successful execution from a useful application result. A successful HTTP connection, for example, does not by itself establish application readiness.
4. **FILES, ENVIRONMENT and NOTES:** find inputs outside your command line, including locale, configuration and inherited variables.
5. **EXAMPLES, CAVEATS and SEE ALSO:** use examples after understanding their prerequisites. Follow related pages when a term or dependency is unfamiliar.

In an interactive `man` pager, `/word` commonly searches and `q` exits. Pager bindings depend on your configured pager. You can use `MANPAGER=cat man 5 fstab` to print a page without an interactive pager; that changes presentation, not the manual's meaning.

### A documentation map

| Source | What you can learn | Boundary |
| --- | --- | --- |
| [Linux kernel documentation](https://docs.kernel.org/) | Administration, interfaces, filesystems, development and subsystem behavior | Some pages target kernel developers; choose the matching kernel documentation where available |
| [Linux man-pages](https://www.kernel.org/doc/man-pages/) | Linux system calls, library interfaces and conventions | Not a complete manual for every distribution package |
| [man7 manual collection](https://man7.org/linux/man-pages/) | Searchable rendered manual pages and cross-references | Online pages can be newer than your installed package |
| [GNU Bash manual](https://www.gnu.org/software/bash/manual/) | Expansion, quoting, built-ins, scripting and startup files | Bash behavior does not define every shell |
| [GNU Coreutils manual](https://www.gnu.org/software/coreutils/manual/) | Common file, text and environment utilities | BusyBox and BSD implementations have different option sets |
| [GNU Findutils manual](https://www.gnu.org/software/findutils/manual/) | `find`, `xargs`, expressions and argument handling | Test selection before performing a modifying action |
| [GNU Grep manual](https://www.gnu.org/software/grep/manual/) | Pattern matching, options and exit statuses | A match failure and an execution error are different results |
| [systemd manuals](https://www.freedesktop.org/software/systemd/man/latest/) | Units, services, journal, timers, boot and related components | Not every Linux system uses systemd; `latest` may differ from your release |
| [OpenSSH manuals](https://www.openssh.com/manual.html) | SSH client/server configuration and authentication | Distribution defaults and enabled algorithms can differ |
| [util-linux project](https://github.com/util-linux/util-linux) | Tools including `findmnt`, `lsblk`, `mount` and `unshare` | Check the installed utility's version and manual before using newer flags |
| [iproute2 project](https://git.kernel.org/pub/scm/network/iproute2/iproute2.git) | Sources and manuals for modern Linux network tools | Tools observe the current network namespace and may require capabilities to change it |
| [POSIX specifications](https://pubs.opengroup.org/onlinepubs/9799919799/) | Standardized shell, utility and API behavior | A portability reference, not a promise that all Linux software or extensions are standardized |
| [Ubuntu Server documentation](https://ubuntu.com/server/docs/) | Ubuntu installation, services and operating procedures | Select guidance appropriate to your release and package source |
| [Debian documentation](https://www.debian.org/doc/) | Release notes, installation guides, reference and administration | Distinguish the installed stable release from testing/unstable |
| [Fedora documentation](https://docs.fedoraproject.org/) | Fedora editions, administration and release-specific changes | Rapid release changes make the release context important |
| [Red Hat Enterprise Linux documentation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/) | RHEL administration, security and supported integration | Select the product's major/minor release and applicable support policy |
| [ArchWiki](https://wiki.archlinux.org/) | Detailed integration explanations and troubleshooting | Arch-specific package names, rolling-release assumptions and community-maintained guidance |
| [Alpine documentation](https://docs.alpinelinux.org/) | Alpine installation, administration and package ecosystem | musl, BusyBox and OpenRC change assumptions from GNU/systemd tutorials |
| [NixOS manual](https://nixos.org/manual/nixos/stable/) | Declarative system configuration, generations and deployment | A conventional `/etc` editing procedure may not persist on NixOS |
| [Python documentation](https://docs.python.org/3/) | Standard library, language and platform interfaces | Select your installed Python version; Linux distributions may package optional modules separately |

For a particular application, add its own manual and release notes to this map. A search engine result, forum answer or AI-generated explanation can suggest an investigation; verify consequential behavior against the responsible project and your installed version.

### Record an answer you can reproduce

Keep private notes with these fields:

| Field | What you record |
| --- | --- |
| Question | One observable question, such as “Which `printf` does this shell run?” |
| Environment | Distribution/release, shell and relevant package version |
| Source | Manual section or upstream URL, version and access date |
| Interpretation | Your answer in your own words, including defaults and exceptions |
| Check | The smallest safe command or fixture that could disprove your interpretation |
| Observation | Actual output and exit status, with sensitive values removed before sharing |
| Limit | What the check did not establish |

Do not publish credentials, full environment dumps, private hostnames or unredacted incident logs as learning evidence.

## Follow along

Answer one narrow question: does your Bash session use a built-in `printf`, and can it also find an external implementation?

<!-- reference:exercise -->
```bash
docs_lab=$(mktemp -d) || exit 1
type -a printf > "$docs_lab/implementations.txt"
help printf > "$docs_lab/builtin-help.txt"
printf '%s\n' 'A command name can have more than one implementation.' > "$docs_lab/answer.txt"
python3 - "$docs_lab" <<'PY'
from pathlib import Path
import sys
root = Path(sys.argv[1])
implementations = (root / 'implementations.txt').read_text()
help_text = (root / 'builtin-help.txt').read_text()
assert 'printf' in implementations
assert 'printf' in help_text
assert (root / 'answer.txt').read_text().endswith('\n')
print('PASS: captured command resolution, built-in help and an observation')
PY
cat "$docs_lab/implementations.txt"
```

Read the implementation list. `printf is a shell builtin` identifies Bash's built-in; additional paths identify external programs found through your current `PATH`. Your list can differ from another reader's. An alias or function can also change name resolution. `help printf` documents the Bash built-in even when another executable exists.

If manual pages are available, separately compare `man 1 printf` and `man 3 printf`. The first is a command interface; the second is a C library interface. Do not treat a missing section as a failed exercise, and do not install a package merely to make an optional observation look complete.

## Verify your result

You should see one `PASS` line and a list that describes your session's `printf` resolution. Inspect the first part of `builtin-help.txt`; find the format string and argument syntax. Explain why a tutorial about an external utility might not describe the shell built-in exactly.

This checks command discovery and help lookup. It does not establish POSIX conformance, prove every format conversion or test every distribution. If the exercise fails, check that you used Bash rather than another shell, and that Python 3 is available.

## Cleanup

<!-- reference:cleanup -->
```bash
rm -i -- "$docs_lab/implementations.txt" "$docs_lab/builtin-help.txt" "$docs_lab/answer.txt"
rmdir -- "$docs_lab"
```

## Sources

Use your installed `man 1 man`, `help type` and `help help` alongside the [man-db manual](https://man7.org/linux/man-pages/man1/man.1.html), [Bash built-in documentation](https://www.gnu.org/software/bash/manual/html_node/Bash-Builtins.html) and [Linux man-pages project description](https://www.kernel.org/doc/man-pages/). The documentation map above links each project directly; it is a set of entry points, not a guarantee that every page is reachable offline or unchanged over time.
