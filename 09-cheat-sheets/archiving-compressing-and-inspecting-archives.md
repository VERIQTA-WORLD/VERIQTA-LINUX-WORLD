| Command | What you can do with it |
| --- | --- |
| `tar -cf ARCHIVE.tar -C SOURCE_DIRECTORY ITEM` | Create a tar archive from an item beneath a chosen directory. |
| `tar -tf ARCHIVE.tar` | List tar archive members. |
| `tar -tvf ARCHIVE.tar` | List archive members with stored metadata. |
| `tar -xf ARCHIVE.tar -C EMPTY_RESTORE_DIRECTORY` | Extract a tar archive into a separate directory, potentially replacing matching paths. |
| `tar -czf ARCHIVE.tar.gz -C SOURCE_DIRECTORY ITEM` | Create a gzip-compressed tar archive. |
| `tar -tzf ARCHIVE.tar.gz` | List members of a gzip-compressed tar archive. |
| `tar -xzf ARCHIVE.tar.gz -C EMPTY_RESTORE_DIRECTORY` | Extract a gzip-compressed tar archive into a separate directory. |
| `tar -cJf ARCHIVE.tar.xz -C SOURCE_DIRECTORY ITEM` | Create an xz-compressed tar archive. |
| `tar -tJf ARCHIVE.tar.xz` | List members of an xz-compressed tar archive. |
| `gzip -c FILE > FILE.gz` | Write a gzip-compressed copy while retaining the source file. |
| `gzip -t FILE.gz` | Check gzip stream integrity. |
| `gunzip -c FILE.gz` | Print decompressed gzip data without replacing the source. |
| `bzip2 -c FILE > FILE.bz2` | Write a bzip2-compressed copy while retaining the source. |
| `bzip2 -t FILE.bz2` | Check bzip2 stream integrity. |
| `bzcat FILE.bz2` | Print decompressed bzip2 data. |
| `xz -c FILE > FILE.xz` | Write an xz-compressed copy while retaining the source. |
| `xz -t FILE.xz` | Check xz stream integrity. |
| `xzcat FILE.xz` | Print decompressed xz data. |
| `zstd -c FILE > FILE.zst` | Write a Zstandard-compressed copy while retaining the source. |
| `zstd -t FILE.zst` | Check Zstandard stream integrity. |
| `zstdcat FILE.zst` | Print decompressed Zstandard data. |
| `zip -r ARCHIVE.zip DIRECTORY` | Create a ZIP archive of a directory tree. |
| `unzip -l ARCHIVE.zip` | List ZIP archive members. |
| `unzip -t ARCHIVE.zip` | Test ZIP member integrity. |
| `unzip ARCHIVE.zip -d EMPTY_RESTORE_DIRECTORY` | Extract a ZIP archive into a separate directory. |
| `7z l ARCHIVE.7z` | List 7-Zip archive members. |
| `7z t ARCHIVE.7z` | Test a 7-Zip archive's integrity. |
