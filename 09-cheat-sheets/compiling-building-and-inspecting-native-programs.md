```bash
cc --version
gcc --version
clang --version
gcc -Wall -Wextra -g SOURCE.c -o PROGRAM
gcc -O2 SOURCE.c -o PROGRAM
g++ -Wall -Wextra -g SOURCE.cpp -o PROGRAM
make -n
make
make -j2
cmake -S . -B build
cmake --build build
ctest --test-dir build
ninja -C build
pkg-config --cflags LIBRARY
pkg-config --libs LIBRARY
file PROGRAM
readelf -h PROGRAM
readelf -d PROGRAM
objdump -p PROGRAM
nm -C PROGRAM
size PROGRAM
ar t LIBRARY.a
strip --help
```
