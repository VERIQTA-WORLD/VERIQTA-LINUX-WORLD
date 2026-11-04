```bash
mkdir -- DIRECTORY
mkdir -p -- PARENT/CHILD
mkdir -m 700 -- DIRECTORY
touch -- FILE
touch -c -- FILE
mktemp
mktemp -d
mktemp --tmpdir 'practice.XXXXXXXX'
printf '%s\n' 'TEXT' > NEW_FILE
cp -i -- SOURCE DESTINATION
cp -a -- SOURCE_DIRECTORY DESTINATION_DIRECTORY
cp -p -- SOURCE DESTINATION
cp --reflink=auto -- SOURCE DESTINATION
cp -u -- SOURCE DESTINATION
install -m 644 -- SOURCE DESTINATION
install -d -m 750 -- DIRECTORY
mv -i -- SOURCE DESTINATION
mv -i -- OLD_NAME NEW_NAME
ln -- EXISTING_FILE HARD_LINK
ln -s -- TARGET SYMBOLIC_LINK
readlink -- SYMBOLIC_LINK
unlink -- SYMBOLIC_LINK
rm -i -- FILE
rmdir -- EMPTY_DIRECTORY
```
