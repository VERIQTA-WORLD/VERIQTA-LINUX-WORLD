| Command | What you can do with it |
| --- | --- |
| `cmp -- FILE_ONE FILE_TWO` | Compare two files byte by byte. |
| `cmp -s -- FILE_ONE FILE_TWO` | Test byte equality without normal output. |
| `diff -u -- FILE_ONE FILE_TWO` | Show text differences in unified format. |
| `diff -ru -- DIRECTORY_ONE DIRECTORY_TWO` | Compare directory trees recursively in unified format. |
| `diff -q -- FILE_ONE FILE_TWO` | Report whether files differ without printing the differences. |
| `diff -y -- FILE_ONE FILE_TWO` | Display differences side by side. |
| `sdiff -- FILE_ONE FILE_TWO` | Compare files side by side with sdiff. |
| `sha256sum -- FILE` | Calculate a SHA-256 digest. |
| `sha512sum -- FILE` | Calculate a SHA-512 digest. |
| `b2sum -- FILE` | Calculate a BLAKE2 digest. |
| `cksum -- FILE` | Calculate the default checksum and byte count. |
| `sha256sum -c MANIFEST` | Verify file digests against a manifest. |
| `sha256sum -- FILE_ONE FILE_TWO > MANIFEST` | Write digests for two files into a manifest, replacing that file. |
| `patch --dry-run -p1 < CHANGE.patch` | Preview whether a patch applies without changing target files. |
| `git diff --no-index -- FILE_ONE FILE_TWO` | Compare arbitrary paths using Git's diff display. |
