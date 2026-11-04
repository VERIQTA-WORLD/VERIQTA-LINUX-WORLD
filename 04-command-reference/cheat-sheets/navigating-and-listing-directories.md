| Command | What you can do with it |
| --- | --- |
| `pwd` | Print the current working directory. |
| `pwd -P` | Print the physical path with symbolic links resolved. |
| `cd` | Change to your home directory. |
| `cd /` | Change to the filesystem root. |
| `cd ~` | Change to your home directory. |
| `cd ..` | Move to the parent directory. |
| `cd -` | Return to the previous working directory. |
| `cd -- DIRECTORY` | Change to the specified directory. |
| `pushd DIRECTORY` | Save the current directory and enter another directory. |
| `popd` | Return to the directory at the top of the directory stack. |
| `dirs -v` | Show the directory stack with numbered entries. |
| `ls` | List visible directory entries. |
| `ls -la` | List hidden entries and detailed metadata. |
| `ls -lh` | List metadata with human-readable sizes. |
| `ls -lah` | Include hidden entries, metadata and human-readable sizes. |
| `ls -ld -- DIRECTORY` | Inspect a directory entry rather than listing its contents. |
| `ls -lt` | List entries newest first by modification time. |
| `ls -ltr` | List entries oldest first by modification time. |
| `ls -lS` | Sort entries by file size, largest first. |
| `ls -li` | Include inode numbers in a detailed listing. |
| `ls -lR -- DIRECTORY` | List directory contents recursively. |
| `tree DIRECTORY` | Display a directory tree. |
| `tree -a -L 2 DIRECTORY` | Include hidden entries and limit the tree to two levels. |
| `realpath -- PATH` | Resolve a path to its canonical absolute form. |
| `readlink -- LINK` | Print the target stored in a symbolic link. |
| `readlink -f -- LINK` | Resolve a link and its parent path components. |
| `basename -- PATH` | Extract the final component of a path. |
| `dirname -- PATH` | Extract a path's parent directory. |
| `namei -l -- PATH` | Inspect permissions and ownership along a path. |
