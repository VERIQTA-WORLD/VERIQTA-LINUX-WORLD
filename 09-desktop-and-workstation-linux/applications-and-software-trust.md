# Install and integrate applications deliberately

[Collection home](README.md) · Previous: [Desktop and accessibility](desktop-and-accessibility.md) · Next: [Displays](displays-and-graphics.md)

## Environment and prerequisites

Use this guide to choose an application source, understand its update route and test desktop integration. Start with an ordinary account in a graphical Linux session. You need an existing text editor and a disposable text document for the GUI walkthrough. Administrative package installation is separate from running an application.

The isolated launcher exercise needs Bash, Python 3 and **desktop-file-validate**, supplied by the distribution's `desktop-file-utils` package on Ubuntu, Debian and Fedora. If absent, use your distribution's supported package installer after reviewing the proposed transaction. The exercise validates a file under a temporary directory; it does not install or launch it. Flatpak observations are optional and require Flatpak plus an already installed application.

## Understand the components

| Delivery route | What you should establish | Update/removal boundary |
| --- | --- | --- |
| Distribution package | Repository identity, package origin and integration with the selected release | Follow distribution maintenance; removal may retain user settings/data |
| Flatpak | Remote, application ID, scope, runtime and requested permissions | User and system installations differ; removing an app need not remove its data |
| Snap where supported | Publisher, channel, confinement and interfaces | Refresh/channel behavior differs from distribution packages |
| AppImage or standalone archive | Publisher identity, signature/checksum instructions, dependencies and update policy | A single file is still executable code; moving it to Trash may leave settings elsewhere |
| Vendor repository | Why the extra trust source is necessary, signing policy and supported release | Repository access can affect future updates, not just one installation |
| Source build | Source provenance, dependencies, build isolation and installation manifest | A successful compile does not create an update or uninstall strategy |

Prefer a source maintained for your system and explain why you trust it. Avoid piping an unreviewed download into a shell, installing competing copies without identifying them, or using sudo to solve a GUI application's file-access problem.

A sandbox's actual permissions matter. Portals can mediate file selection, camera or screen sharing without granting broad host access. A file picker displaying your files is not by itself evidence that an application has unrestricted access. Static sandbox grants, overrides and remembered portal choices are different layers.

## Follow along

### 1. Identify before adding software

Open your software manager and inspect one application you already use. Find its source, version and update controls. If it appears more than once, compare the source and packaging rather than assuming both entries are interchangeable. Open its About dialog and compare the running application's identity with the package you inspected.

For an installed Flatpak, first use `flatpak list --app` to identify the real application ID and scope. The independent fragments below inspect access; replace `APP_ID` and select the matching installation if needed:

| Observation | Meaning |
| --- | --- |
| `flatpak info APP_ID` | Installed reference, origin and other metadata |
| `flatpak info --show-permissions APP_ID` | Application permissions reported by the installed tool |
| `flatpak override --user --show APP_ID` | Application-specific user overrides |
| `flatpak override --user --show` | Global user overrides that can also affect the app |

System installations can also have system overrides. Read the installed manual for effective composition. Do not use a blanket reset or broad `--filesystem=host` grant as a generic repair; first preserve and understand the existing policy.

### 2. Validate a private desktop entry

A `.desktop` file describes launch metadata. Its `Exec` value has specification-defined token/field-code rules; it is not an arbitrary Bash command line. This example uses a harmless external `true` executable and is **not** placed in an application search directory.

<!-- workstation:exercise -->
```bash
apps_lab=$(mktemp -d) || exit 1
python3 - "$apps_lab" <<'PY'
from pathlib import Path
import shutil
import sys
root = Path(sys.argv[1])
executable = shutil.which('true')
assert executable and ' ' not in executable
entry = '[Desktop Entry]\nType=Application\nName=Linux World Example\n'
entry += 'Exec=' + executable + '\nTerminal=false\nCategories=Utility;\n'
(root / 'org.veriqta.LinuxWorldExample.desktop').write_text(entry)
PY
desktop-file-validate "$apps_lab/org.veriqta.LinuxWorldExample.desktop" || exit 1
echo 'PASS: private launcher metadata passes desktop-file validation'
```

Successful validation is usually silent, followed by the `PASS` line. It does not authenticate an executable or prove that the menu discovers or launches an application. Files copied to a desktop may require an additional trust action specific to the file manager; do not mark unknown launchers trusted just because they have familiar icons.

### 3. Test file association without losing your previous choice

Create a disposable text file with your editor and save it in a private learning directory. In the file manager, use **Open With** to select another already installed text editor if you have one. First make a one-time choice, without changing the default. Confirm you opened the intended document and save one harmless change.

If you deliberately change the default application, record the previous association first and restore it afterward through the desktop's supported controls. Desktop entries advertise supported MIME types; default selection is a separate association policy. Do not copy an entire online `mimeapps.list` over your own settings.

### 4. Check one update and removal route

Inspect how your chosen application receives updates and whether a restart is required to use the new version. For removal, distinguish program files, per-user settings, documents and runtime dependencies. Never remove an application you rely on merely to finish this lesson. Use a disposable VM if you want to rehearse installation/removal transactions.

## Verify and recover

Your result should identify the source and running version, explain the update route, and open a disposable document in the chosen application. If a packaged application works outside its sandbox but not inside, compare permission and portal behavior before granting broad access. If two copies launch differently, identify their package/application IDs and launch paths.

If a file association changes unexpectedly, restore the recorded previous default and retest the same file type. If an update regresses behavior, consult the package source's supported recovery path and application data compatibility. Downgrading executable files does not necessarily reverse a data migration.

## Cleanup

Remove only the private launcher:

<!-- workstation:cleanup -->
```bash
rm -i -- "$apps_lab/org.veriqta.LinuxWorldExample.desktop"
rmdir -- "$apps_lab"
```

Close and remove your disposable GUI document through the file manager. Restore only associations or permissions you deliberately changed. Keep applications and data you need; uninstalling is not required for successful completion.

## Checkpoint

Explain package identity versus running application identity, static permissions versus portal grants, and launcher validity versus trust. You can name an application's update and recovery route before adding it to your everyday workflow.

## Sources

Use the [Desktop Entry Specification](https://specifications.freedesktop.org/desktop-entry/latest-single/), [desktop-file-utils project](https://www.freedesktop.org/wiki/Software/desktop-file-utils/), [MIME application association specification](https://specifications.freedesktop.org/mime-apps/latest-single/), [Flatpak basic concepts](https://docs.flatpak.org/en/latest/basic-concepts.html), [Flatpak sandbox permissions](https://docs.flatpak.org/en/latest/sandbox-permissions.html), [Flathub permission troubleshooting](https://docs.flathub.org/docs/for-users/troubleshooting) and [Snap security documentation](https://snapcraft.io/docs/security-policies). Use your distribution's package documentation for repository maintenance.
