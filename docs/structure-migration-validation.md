# Structure migration validation

Migration date: November 4, 2026. Preservation baseline: `6d3b987` (main after the merged folder 7 PR). This record concerns repository organization and navigation; it does not replace collection-specific Linux runtime validation.

## Intended invariants

- Canonical numbered collections run from 00 through 15, with folders 1–3 retaining their original names.
- Folders 1–3 retain their files and contents except exactly three owner-approved Start Here link targets.
- The 70 existing cheat sheets are moved without changing any bytes, including commands and descriptions.
- Cheat sheets and detailed explanations live within one command-reference collection.
- New folders 9–15 explicitly state that they are planned; folder 8 topic pages remain planned.
- Links and Python tool/example paths use the renamed canonical directories. Existing SVG asset filenames remain for compatibility, with updated command/system-administration labels.

## Checks for this migration

```bash
python3 tools/check_repository_structure.py --baseline 6d3b987
python3 tools/check_command_content.py
python3 tools/check_cheat_sheets.py
python3 tools/check_portable_examples.py
python3 tools/check_administration_labs.py
python3 tools/check_distribution_labs.py
python3 tools/check_recovery_labs.py
git diff --check
```

The structure checker compares file names, blob hashes/modes and the three exact link edits against the stated baseline. It verifies that all moved cheat-sheet contents are byte-identical and indexed, along with canonical folder names, planned labels and structural navigation.

Content/sheet checks inspect Markdown, links and syntax without running listed administration commands. The portable runners execute only their explicitly bounded examples. The recovery runner also launches local loopback listeners and needs an environment permitting that operation; it does not invoke privileged host recovery.

## Results

All checks listed above passed on the authoring host (macOS/Darwin, Python 3.9.6 and Bash 3.2.57):

- Preservation: 189 files in folders 1–3 checked; exactly the three approved link targets differ, and every other file remains unchanged. All 70 moved cheat sheets are byte-identical to the baseline.
- Structure: 16 canonical numbered collections, seven planned roadmaps, 70 indexed sheets and 156 structural navigation links checked.
- Content: 170 Markdown pages, 59 content contracts, 187 Bash blocks and 907 local links checked.
- Cheat sheets: 70 two-column tables and 1,518 command/description pairs pass format and syntax checks.
- Portable execution: nine command examples, four recovery exercises, eight administration exercises and nine distribution exercises pass, including their cleanup and helper checks.
- Changed-line whitespace check passes.

The structure checker inspects only the three approved Start Here targets within the protected lab/project READMEs. Other pre-existing links/content inside folders 1–3 are outside this migration's repair and certification scope.

No new Linux VM testing or production/fleet operation is claimed by this restructure. Existing pending Linux validation remains visible in the renamed collections' validation records.

## Compatibility and next work

The [migration map](repository-structure.md) identifies old paths for bookmarks. Old GitHub directory URLs are not automatically redirected. Folders 1–3 were not otherwise modernized or reorganized.

This installment establishes structure and orientation. It does not fill the new topic collections, complete folder 8's reference pages or turn already pending Linux scenarios into tested ones. Continue folder by folder using reproducible environments and explicit evidence.

[Root README](../README.md)
