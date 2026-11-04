# Folders 1–7: quality review before the reference library

Reviewed November 4, 2026 against repository revision `e69456f`. This review changes no learning collection. It records concrete entry-point defects, coverage gaps and the scope of execution evidence before work on folder 8.

The priority is to repair the reader journey through folders 1–3. Folders 4–7 have consistent authored structure and passing bounded exercises; their Linux-specific runtime behavior still needs reproduction on named Linux targets. Neither content length nor a passing syntax check establishes teaching accuracy or operational readiness.

## Collection assessment

| Folder | Inventory | Assessment and next action |
| --- | --- | --- |
| 01 · Beginner to advanced | 21 Markdown files: 20 populated lessons and one empty README | The numbered lessons provide substantial explanations, examples and questions, but the collection entry page is blank. Add an ordered lesson index, prerequisites, checkpoints and a clear route into labs before expanding this collection. |
| 02 · Labs | 103 Markdown files: 70 populated numbered Junior labs, one populated root README and 32 empty support/category pages | The root advertises 352 labs while only JUN-001–070 exist as numbered lesson files. The four environment/safety/standard/progress pages are empty. Restore a usable entry route and publish functional prerequisites and safety guidance before extending the lab sequence. |
| 03 · Projects | 36 Markdown files: 30 populated project guides, three populated navigation pages and three empty asset READMEs | All 30 project guides exist, but 75 inline link occurrences point to missing paths. Repair root/level navigation, then reproduce representative projects at each difficulty with recorded acceptance and recovery evidence. Empty asset READMEs are lower priority than reader navigation. |
| 04 · Command reference | 114 populated Markdown files, including 30 detailed references and 70 two-column cheat sheets | Content contracts, syntax, table structure and checked local navigation pass. Nine portable walkthroughs pass. Reproduce distribution-dependent commands and GNU/Linux behavior on named Linux targets. |
| 05 · Troubleshooting and recovery | 12 populated Markdown files: ten guides, README and validation record | Four portable recovery scenarios and helper checks pass. Full Linux service, DNS/NSS, storage, process and boot scenarios require actual target execution. |
| 06 · System administration | 12 populated Markdown files: ten runbooks, README and validation record | Eight portable sequences and validator cases pass. The examples support learning change control; actual systemd, logrotate, sudo-policy, package and fleet behavior needs separate Linux evidence. |
| 07 · Linux distributions | 11 populated Markdown files: nine guides, README and validation record | Nine bounded comparison exercises and identity-reader checks pass. Fixtures do not establish installed managers, enforcement, support coverage or successful installation/update on real distributions. |

## Findings that affect readers

### High: the lab inventory does not match the advertised journey

[The lab entry page](../../02-Labs/README.md) presents 83 Junior, 126 Mid-Level and 143 Senior labs: 352 total. The checkout contains 70 numbered lab pages, all Junior. The missing Junior sequence is JUN-071–083; Mid-Level and Senior contain empty navigation/category files rather than numbered lab content.

The first-lab link targets `Junior/01-Linux-Fundamentals-and-Command-Line/001-Linux-Terminal-Navigation/README.md`, which does not exist. The actual lesson is a Markdown file named `01. JUN-001: Linux Terminal Navigation.md` in that category. This is an immediate blocker for someone selecting “Start with Lab 001.”

Acceptance: every advertised lesson resolves to an actual lesson; counts come from the delivered inventory; the first-lab route works; each level has usable navigation. Reconcile the existing inventory before adding more breadth.

### High: the safety and environment entry pages contain no guidance

The lab README directs readers to `LAB-ENVIRONMENT.md` and `LAB-SAFETY.md`, but both files are empty. `LAB-STANDARD.md` and `PROGRESS-TRACKER.md` are also empty. The README itself includes safety advice, and individual inspected lessons have environment notes; those strengths do not make the linked support pages functional.

Acceptance: provide environment prerequisites, isolation and recovery requirements, boundaries for privileged/storage/network exercises, cleanup expectations and a progress record. Test those instructions from a fresh environment.

### High: navigation in labs and projects uses missing paths

The scan found 87 missing-path link occurrences across four pages:

| Page | Occurrences pointing to missing paths |
| --- | ---: |
| `02-Labs/README.md` | 12 |
| `03-Projects/README.md` | 43 |
| `03-Projects/01. Junior/README.md` | 12 |
| `03-Projects/02. Mid-Level/README.md` | 20 |

Examples include old collection names such as `../04-Projects/README.md`, `../02-Commands-and-Cheat-Sheets/README.md` and `../07-Labs/README.md`. Several project links also assume filenames or directories that differ from the delivered files. The [evidence file](folders-01-07-evidence.json) records each source line and target. These are occurrence counts, not 87 distinct missing documents. The three previously authorized Start Here link corrections are intact.

Acceptance: resolve each intended destination, check spelling and case on Linux/GitHub, and verify the complete path from root to lesson/project and back. Do not create duplicate collections to satisfy obsolete links.

### Medium: folder 1 has no collection landing page

`01-Beginner-to-Advanced/README.md` is empty. Readers reach the collection without an ordered course map or prerequisites even though all 20 numbered lessons contain content.

Acceptance: link all 20 lessons in order and offer entry points by demonstrated experience, with concrete checkpoints and links to relevant labs/reference pages.

### Medium: validation coverage is uneven

The existing content checker covers authored references and guides in folders 4–7; it does not audit all lessons, labs and projects in folders 1–3. Its passing result must not be interpreted as a repository-wide quality pass.

The additional scan parsed 18,847 fenced Bash/sh blocks in folders 1–3 and flagged 28 blocks: 15 in lessons, nine in labs and four in projects. Inspection found operator/conditional fragments, intentional syntax-error examples, unresolved angle-bracket placeholders, and four Bash 3.2 incompatibilities involving `[[ -v ... ]]`. These are not 28 confirmed executable-script bugs. Classify runnable blocks separately from syntax illustrations and expected failures before enforcing a parser across those collections. Validate complete scripts with the documented target Bash version.

Acceptance: checks distinguish commands to execute, fragments to explain and deliberate failures; a modern target-shell check covers actual runnable examples; results name their environment.

### Medium: lengthy lessons need a usability pass

The 20 foundation lessons total 112,037 lines; populated lab Markdown totals 212,040 lines; populated project Markdown totals 144,248 lines. These are source-line counts, not reading-time or quality measures. Selected pages contain extensive explanation, command breakdowns and recovery reasoning. Their size also makes prerequisites, restart points and acceptance criteria harder to locate without consistent navigation.

Acceptance: test representative pages with a fresh reader, add visible milestones and checkpoints where needed, and remove repeated explanation only when doing so improves comprehension. Do not split or shorten pages solely to meet a numerical limit.

## Safety review boundary

Selected storage material explicitly warns that formatting destroys data, and a broad `chmod -R 777 /` example is explicitly presented as something not to do. A search hit for a dangerous command is therefore not automatically an unsafe recommendation. No such command was executed during this audit.

The next editorial pass should verify that disposable devices, console recovery, privilege boundaries and exact cleanup are established before every actionable high-impact exercise. This review does not certify all storage, firewall, SSH, failover or incident-response procedures across the 30 projects and 70 labs.

## Checks rerun

| Check | Result |
| --- | --- |
| `python3 tools/check_command_content.py` | Pass: 170 checked pages, 59 contracts, 187 Bash blocks, 914 local links |
| `python3 tools/check_cheat_sheets.py` | Pass: 70 two-column sheets and 1,518 command examples |
| `python3 tools/check_repository_structure.py` | Pass: canonical collection names, sheet index and scoped navigation |
| `python3 tools/check_portable_examples.py` | Pass: nine file/text/archive walkthroughs and cleanup |
| `python3 tools/check_recovery_labs.py` | Pass: four published sequences plus bounded loopback/load helper checks |
| `python3 tools/check_administration_labs.py` | Pass: eight sequences plus valid input and nine invalid validator cases |
| `python3 tools/check_distribution_labs.py` | Pass: nine exercises, 13 identity classifications, eight invalid inputs and no-shell-execution checks |
| `git diff --check` | Pass for this audit addition |

The execution host is macOS/Darwin; the shell scan uses Bash 3.2.57. The recovery checks use temporary files, loopback-only listeners and bounded processes. No Linux VM, privileged administration command, real package transaction or production change was executed. External URLs and current release facts were not revalidated in this local audit; consult the existing source/validation records when reviewing those claims.

## Recommended work order

1. Repair folder 1's entry page and folder 2's environment/safety entry points.
2. Reconcile lab counts and routes; repair the 87 missing-path occurrences in folders 2–3.
3. Reproduce a representative foundation lesson, Junior lab and project on a disposable Linux target, then extend checks based on observed failures.
4. Exercise the Linux-specific scenarios in folders 4–7 and record results in their validation records.
5. Develop folder 8 as the glossary, official-documentation map and reference library, linking to canonical lessons and guides rather than duplicating them.

Folders 1–3 remain unchanged by this review, consistent with the previously agreed preservation boundary. Findings are recorded here for the next focused changes; no collection README was rewritten as a project-status page.
