| Command | What you can do with it |
| --- | --- |
| `cc --version` | Identify the configured C compiler. |
| `gcc --version` | Identify the GCC version. |
| `clang --version` | Identify the Clang version. |
| `gcc -Wall -Wextra -g SOURCE.c -o PROGRAM` | Compile a C program with warnings and debugging symbols. |
| `gcc -O2 SOURCE.c -o PROGRAM` | Compile a C program with optimization. |
| `g++ -Wall -Wextra -g SOURCE.cpp -o PROGRAM` | Compile a C++ program with warnings and debugging symbols. |
| `make -n` | Print planned make recipes without normally executing them, except make's special cases. |
| `make` | Run the default make target. |
| `make -j2` | Build with up to two concurrent make jobs. |
| `cmake -S . -B build` | Generate build files in a separate build directory. |
| `cmake --build build` | Build a configured CMake project. |
| `ctest --test-dir build` | Run CTest tests from the build directory. |
| `ninja -C build` | Build using Ninja's build directory. |
| `pkg-config --cflags LIBRARY` | Print compiler flags for a library. |
| `pkg-config --libs LIBRARY` | Print linker flags for a library. |
| `file PROGRAM` | Identify an executable's file type. |
| `readelf -h PROGRAM` | Inspect an ELF executable's header. |
| `readelf -d PROGRAM` | Inspect an ELF executable's dynamic section. |
| `objdump -p PROGRAM` | Inspect executable format-specific headers. |
| `nm -C PROGRAM` | List symbols with C++ name demangling. |
| `size PROGRAM` | Summarize object-file section sizes. |
| `ar t LIBRARY.a` | List members of a static-library archive. |
| `strip --help` | Read symbol-stripping options without modifying a binary. |
