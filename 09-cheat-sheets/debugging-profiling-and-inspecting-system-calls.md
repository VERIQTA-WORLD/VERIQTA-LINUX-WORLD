```bash
strace -f -o TRACE.log COMMAND
strace -e trace=file COMMAND
strace -e trace=network COMMAND
strace -c COMMAND
sudo strace -p PID
ltrace COMMAND
gdb PROGRAM
gdb -p PID
gdb --args PROGRAM ARGUMENT
coredumpctl list
coredumpctl info PID
coredumpctl debug PID
sudo perf stat COMMAND
sudo perf top
sudo perf record -g -- COMMAND
perf report
valgrind --leak-check=full PROGRAM
heaptrack PROGRAM
sudo bpftrace -l
sudo bpftool prog show
sudo bpftool map show
```
