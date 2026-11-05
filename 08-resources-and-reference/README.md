# Resources and reference

![Resources and reference](../assets/images/08-resources-and-reference-cover.svg)

Understand a Linux term, locate a file, find the right manual and check an interpretation on your own system. This library connects explanations to small examples and authoritative sources. Use it alongside the lessons, labs and operational guides whenever a question needs context.

## Choose the reference you need

| Your question | Reference | What you will do |
| --- | --- | --- |
| What does this term mean? | [Linux glossary](linux-glossary.md) | Connect kernel, shell, storage, security and networking vocabulary to concrete distinctions; inspect links and an open file descriptor |
| Which documentation should I trust for this question? | [Official documentation map](linux-official-documentation.md) | Choose installed, upstream, distribution or standards documentation; distinguish shell built-ins from external commands |
| What belongs at this path? | [Filesystem reference](linux-filesystem-reference.md) | Identify configuration, data, state, cache and runtime paths; verify a bounded cache-removal model |
| Who reads this configuration, and when does it take effect? | [Configuration file reference](linux-configuration-file-reference.md) | Identify ownership, precedence, validation and activation; distinguish valid JSON from accepted application values |
| Where can I find evidence of an event? | [Log-location reference](linux-log-location-reference.md) | Follow producer, destination, permissions and retention; archive and restore synthetic events byte for byte |
| Which network layer does this observation describe? | [Networking reference](linux-networking-reference.md) | Connect addresses, routes, resolution, sockets and application responses; calculate prefix membership offline |
| What should I read next, and how should I study it? | [Books and learning resources](linux-books-and-learning-resources.md) | Choose by goal, prerequisites, edition and access; create a learning card grounded in installed help |
| Can I explain Linux clearly from evidence? | [Interview preparation](linux-interview-preparation.md) | Work through 32 discussion questions, evaluate a scenario and state the limits of a conclusion |

## Use the library as you work

Start with the question you have now. For example, if a service ignores a changed setting, use the configuration reference to identify its consumer and effective input, the filesystem reference to interpret the path, and the documentation map to find the matching manual. Then use an operational guide for the actual change and rollback procedure.

| What you want to accomplish | Continue here |
| --- | --- |
| Choose a learning route for your experience and goal | [Start here](../00-start-here/README.md) |
| Learn concepts in sequence | [Lessons](../01-Beginner-to-Advanced/README.md) |
| Practice a delivered numbered lab | [Labs](../02-Labs/README.md) |
| Build and verify a project | [Projects](../03-Projects/README.md) |
| Look up a command or compact example | [Command reference](../04-command-reference/README.md) and [cheat sheets](../04-command-reference/cheat-sheet-index.md) |
| Diagnose a failure and verify recovery | [Troubleshooting and recovery](../05-troubleshooting-and-recovery/README.md) |
| Operate a host with validation and rollback | [System administration](../06-system-administration/README.md) |
| Understand a distribution or product variant | [Linux distributions](../07-linux-distributions/README.md) |

## Follow the examples safely

Each topic has a scope, reference material, a complete small example, expected results, cleanup and sources. Read its explanation before running commands. The tables contain independent fragments and placeholders; they are not scripts to run from top to bottom.

The eight examples need **Bash, Python 3 and an ordinary account**; the log example also uses `gzip`. Start from the repository root so the configuration example can find folder 6's demonstration validator. Use a disposable Bash session, keep each page's exercise and cleanup in the same session, and answer the cleanup prompts only for the files you created. Temporary-directory variables are deliberately different across pages. Do not replace them with paths to real application data.

Optional Linux observations use tools such as `man`, `ip`, `ss`, `findmnt` and `journalctl` where available. Missing packages, restricted visibility and different implementations are context to investigate. Do not use root privileges or install software merely to force an optional observation to match another reader's output.

The examples create private fixtures, not production changes. A passed check proves its stated result within that fixture. Read [validation and reproducibility](VALIDATION.md) for the named environments, checks and limits.

## Read sources with their context

The technical and bibliographic review date for this collection is **4 November 2026**. Prefer documentation matching your installed version; upstream `latest`, books and distribution defaults can disagree for legitimate reasons. Every topic links its sources and explains relevant boundaries. External sites, editions and releases change over time; this is a curated library, not a promise that every Linux resource is included or every external link is always available.

Explain concepts in your own words and respect each linked resource's license. Free access does not automatically permit copying, modification or redistribution. Keep credentials, private logs, account inventories and personal study notes out of public examples.

[LINUX-WORLD](../README.md) · [Content standard](../CONTENT-STANDARD.md)
