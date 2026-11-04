| Command | What you can do with it |
| --- | --- |
| `mkdir -- DIRECTORY` | Create a directory. |
| `mkdir -p -- PARENT/CHILD` | Create a directory and any missing parents. |
| `mkdir -m 700 -- DIRECTORY` | Create a directory accessible only to its owner. |
| `touch -- FILE` | Create an empty file or update an existing file's timestamps. |
| `touch -c -- FILE` | Update timestamps only if the file already exists. |
| `mktemp` | Create a uniquely named temporary file. |
| `mktemp -d` | Create a uniquely named temporary directory. |
| `mktemp --tmpdir 'practice.XXXXXXXX'` | Create a temporary file using a custom name template. |
| `printf '%s\n' 'TEXT' > NEW_FILE` | Write text to a file, replacing any existing contents. |
| `cp -i -- SOURCE DESTINATION` | Copy a file and ask before replacing an existing destination. |
| `cp -a -- SOURCE_DIRECTORY DESTINATION_DIRECTORY` | Copy a directory tree while preserving supported attributes. |
| `cp -p -- SOURCE DESTINATION` | Copy a file while preserving mode, ownership where allowed and timestamps. |
| `cp --reflink=auto -- SOURCE DESTINATION` | Attempt a copy-on-write clone, falling back to an ordinary copy. |
| `cp -u -- SOURCE DESTINATION` | Copy when the destination is absent or older than the source. |
| `install -m 644 -- SOURCE DESTINATION` | Copy a file and set mode 644. |
| `install -d -m 750 -- DIRECTORY` | Create a directory and set mode 750. |
| `mv -i -- SOURCE DESTINATION` | Move or rename a path, asking before replacement. |
| `mv -i -- OLD_NAME NEW_NAME` | Rename a file, asking before replacement. |
| `ln -- EXISTING_FILE HARD_LINK` | Create another hard link to an existing file. |
| `ln -s -- TARGET SYMBOLIC_LINK` | Create a symbolic link to a target path. |
| `readlink -- SYMBOLIC_LINK` | Read a symbolic link's stored target. |
| `unlink -- SYMBOLIC_LINK` | Remove a symbolic link without removing its target. |
| `rm -i -- FILE` | Remove a file after confirmation, without a recycle bin. |
| `rmdir -- EMPTY_DIRECTORY` | Remove an empty directory. |
