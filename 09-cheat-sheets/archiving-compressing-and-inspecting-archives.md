```bash
tar -cf ARCHIVE.tar -C SOURCE_DIRECTORY ITEM
tar -tf ARCHIVE.tar
tar -tvf ARCHIVE.tar
tar -xf ARCHIVE.tar -C EMPTY_RESTORE_DIRECTORY
tar -czf ARCHIVE.tar.gz -C SOURCE_DIRECTORY ITEM
tar -tzf ARCHIVE.tar.gz
tar -xzf ARCHIVE.tar.gz -C EMPTY_RESTORE_DIRECTORY
tar -cJf ARCHIVE.tar.xz -C SOURCE_DIRECTORY ITEM
tar -tJf ARCHIVE.tar.xz
gzip -c FILE > FILE.gz
gzip -t FILE.gz
gunzip -c FILE.gz
bzip2 -c FILE > FILE.bz2
bzip2 -t FILE.bz2
bzcat FILE.bz2
xz -c FILE > FILE.xz
xz -t FILE.xz
xzcat FILE.xz
zstd -c FILE > FILE.zst
zstd -t FILE.zst
zstdcat FILE.zst
zip -r ARCHIVE.zip DIRECTORY
unzip -l ARCHIVE.zip
unzip -t ARCHIVE.zip
unzip ARCHIVE.zip -d EMPTY_RESTORE_DIRECTORY
7z l ARCHIVE.7z
7z t ARCHIVE.7z
```
