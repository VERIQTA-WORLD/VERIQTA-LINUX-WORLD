```bash
cmp -- FILE_ONE FILE_TWO
cmp -s -- FILE_ONE FILE_TWO
diff -u -- FILE_ONE FILE_TWO
diff -ru -- DIRECTORY_ONE DIRECTORY_TWO
diff -q -- FILE_ONE FILE_TWO
diff -y -- FILE_ONE FILE_TWO
sdiff -- FILE_ONE FILE_TWO
sha256sum -- FILE
sha512sum -- FILE
b2sum -- FILE
cksum -- FILE
sha256sum -c MANIFEST
sha256sum -- FILE_ONE FILE_TWO > MANIFEST
patch --dry-run -p1 < CHANGE.patch
git diff --no-index -- FILE_ONE FILE_TWO
```
