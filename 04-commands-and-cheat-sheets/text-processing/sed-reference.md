# Transform text with sed

`sed` reads a stream and applies editing rules. By default it prints transformed text and leaves the source file unchanged, making it useful for previews and pipelines.

## Environment and permissions

GNU sed on Linux; normal user. Avoid in-place editing until the preview and backup are checked. BSD/macOS `sed -i` has different argument handling.

Read [how to use these references](../README.md) before running examples. Commands have no shell prompt prefix so you can copy them.

## Quick reference

| Command or syntax | Purpose and effect |
| --- | --- |
| `sed -n '1,5p' FILE` | Print only lines 1 through 5. |
| `sed 's/old/new/' FILE` | Replace the first match on each line in output. |
| `sed 's/old/new/g' FILE` | Replace every match on each line in output. |
| `sed '/^#/d' FILE` | Omit lines beginning with # from output. |
| `sed -i.bak 's/old/new/g' FILE` | GNU form: edit a file and retain a .bak copy; changes source data. |

## Follow along

```bash
sed_lab=$(mktemp -d)
printf 'mode=dev\nlabel=dev-dev\n' > "$sed_lab/config"
sed 's/dev/test/g' "$sed_lab/config" > "$sed_lab/preview"
cat -- "$sed_lab/preview"
cat -- "$sed_lab/config"
rm -i -- "$sed_lab/config" "$sed_lab/preview"
rmdir -- "$sed_lab"
```

## Expected results and verification

Preview contains `mode=test` and `label=test-test`. Original still contains `dev`. The separate output file avoids overwriting input before it is read.

## Common mistakes and next checks

Never redirect output to the same input pathname: the shell truncates it first. Patterns use regular expressions; replacement `&` expands to the full match. Choose a different delimiter for paths, such as `s|/old|/new|`. Configuration editing still requires a syntax check with the consuming application.

## Authoritative references

- [GNU sed manual](https://www.gnu.org/software/sed/manual/sed.html)

Use the installed manual for your version; upstream documentation may describe newer features.

[Category cheat sheet](README.md) · [Command index](../command-index.md) · [Collection home](../README.md)
