# Make the desktop usable for you

[Collection home](README.md) · Previous: [Installation](installation-and-recovery.md) · Next: [Applications](applications-and-software-trust.md)

## Environment and prerequisites

Your desktop should support how you see, hear, move, read and concentrate. Set up essential accessibility and input before optimizing appearance. You can use a keyboard, pointer, touch, assistive device or a combination; this guide does not require one preferred interaction style.

The walkthrough needs an installed **graphical Linux session**, access to its Settings application and a plain-text editor. GNOME and KDE Plasma are examples; distributions can rename panels and customize shortcuts. Use Settings search and the desktop's own help rather than assuming an exact menu label. For screen-reader work, use a desktop/application combination with documented assistive-technology support and a usable recovery input method.

The small UTF-8 exercise needs Bash and Python 3. It does not change your language, input settings or desktop database. No administrator privileges are needed. A headless shell cannot establish that magnification, speech, focus or keyboard navigation works.

## Understand the components

| Component | Purpose | Distinction |
| --- | --- | --- |
| Desktop environment | Windows, panels, settings, applications and integration | GNOME and Plasma are not different kernels |
| Display server/compositor | Coordinates input, windows and display output | Wayland and X11 sessions expose different control interfaces |
| Display manager | Graphical sign-in and session selection | A working sign-in screen does not prove that your user session starts successfully |
| Session bus and user services | Communication and background work for your account | Running a GUI application with sudo can select the wrong environment and ownership |
| Accessibility framework | Exposes application semantics to assistive tools | A visually drawn control may still lack a useful accessible label |
| Input method/layout | Produces characters and text | Keyboard layout, interface language and document encoding are different settings |
| Portal | Mediates selected desktop interactions for applications | A file-picker or screen-sharing permission can be separate from static sandbox access |

Workspaces organize windows; they are not security isolation. Locking protects the session when configured correctly but is not the same as logging out, suspending or encrypting an unlocked machine's memory.

## Follow along

### 1. Establish an accessible baseline

1. Open Settings and locate Accessibility. Use the desktop's accessibility menu or documented keyboard route if pointer navigation is difficult. Do not disable a tool you depend on just to reproduce a default screenshot.
2. Change **one reversible setting** that is useful to you: text size, contrast, magnification, cursor size, reduced animation, visual alerts, repeat-key behavior or another supported option. Record its previous value privately.
3. Open a text editor. Check menus, text selection, scrolling, focus visibility and any speech/braille output you use. Test an ordinary application as well as Settings; toolkit/application support can differ.
4. Confirm that you can return to the setting and restore it. If the new behavior obstructs use, restore it before changing anything else. Keep useful improvements if they work for you.

For a screen reader, start with the desktop's documented setup and command reference. Check that controls announce useful names, typing feedback matches your preference, dialogs expose focus and you can stop speech or return to the previous window. Do not equate “the process is running” with usable access. If you cannot complete a path, record the exact application and control without blaming your input method.

### 2. Make a keyboard and workspace route

Use the desktop's documented launcher shortcut or menu, find the text editor, create a document, switch to another application and return. Find the documented keyboard route for closing a window and locking the session. Save work before testing logout; logout ends applications and can lose unsaved state.

Move a window to another workspace using the desktop's supported controls. Bring it back. If multiple layouts or input methods are required, switch deliberately and type a short sample in the editor. Check punctuation and the characters used in your passphrase without displaying the passphrase itself.

### 3. Keep language and encoding separate

This example writes multilingual text as explicit UTF-8, reads it back and distinguishes character count from byte count. It does not require every font to display every script on your system.

<!-- workstation:exercise -->
```bash
desktop_lab=$(mktemp -d) || exit 1
python3 - "$desktop_lab" <<'PY'
from pathlib import Path
import sys
root = Path(sys.argv[1])
text = 'Linux — café — مرحبا — こんにちは\n'
path = root / 'reading-sample.txt'
path.write_text(text, encoding='utf-8')
assert path.read_text(encoding='utf-8') == text
assert len(path.read_bytes()) > len(text)
print('PASS: UTF-8 text round-trips; byte count differs from character count')
PY
```

In your graphical editor, use **Open** to select the printed directory's `reading-sample.txt` (run `printf '%s\n' "$desktop_lab"` to see its location). Confirm that text renders and the editor reports UTF-8 where it exposes encoding. A missing glyph can be a font problem even when the stored bytes are correct. This file is only a mixed-script sample, not a comprehensive test of bidirectional editing or accessibility.

## Verify and recover

Check these outcomes using your actual input/assistive tools:

| Task | Evidence |
| --- | --- |
| Launch and close an application | You can do both without losing focus or access |
| Read and edit text | Content, selection and cursor/focus are understandable to you |
| Navigate a dialog | You can identify the selected control, accept and cancel |
| Lock and unlock | The session requires the intended authentication and remains usable afterward |
| Change layout | Typed characters match the selected layout; you can return |
| Recover a setting | You can restore the previous value without resetting your whole profile |

If an application fails accessibility while others work, narrow the report to its version, toolkit/session and exact interaction. If a new extension or theme breaks the shell, use the desktop's documented way to disable that particular addition. Do not delete your entire home configuration. A new disposable user account can distinguish a profile issue, but creating one is an administrator action and not required for this exercise.

Screen-reader support, login-screen accessibility and secure prompts can have different behavior. Verify each path you rely on rather than assuming one successful application covers all of them.

## Cleanup

Close the sample document without saving additional changes, then remove it:

<!-- workstation:cleanup -->
```bash
rm -i -- "$desktop_lab/reading-sample.txt"
rmdir -- "$desktop_lab"
```

Restore only settings you changed for experimentation. Keep accommodations you need. Record their names and values securely if you want to reproduce them later; do not publish your entire desktop settings database.

## Checkpoint

You can explain the difference between language, keyboard layout, encoding and font coverage. You can navigate the applications you need, recover from one settings change and describe an accessibility problem as an observable interaction.

## Sources

Start with [GNOME Help](https://help.gnome.org/gnome-help/), its [accessibility guide](https://help.gnome.org/gnome-help/a11y.html), [KDE accessibility resources](https://community.kde.org/Accessibility), [Orca documentation](https://help.gnome.org/orca/) and [Python text encoding documentation](https://docs.python.org/3/library/functions.html#open). Session and application versions determine the actual controls and assistive behavior.
