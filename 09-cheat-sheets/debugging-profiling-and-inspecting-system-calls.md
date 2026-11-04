| Command | What you can do with it |
| --- | --- |
| `strace -f -o TRACE.log COMMAND` | Trace a command and its children, saving system-call details to a file. |
| `strace -e trace=file COMMAND` | Trace file-related system calls. |
| `strace -e trace=network COMMAND` | Trace network-related system calls. |
| `strace -c COMMAND` | Summarize system-call counts and durations. |
| `sudo strace -p PID` | Attach a system-call tracer to an authorized process, potentially affecting timing. |
| `ltrace COMMAND` | Trace dynamic-library calls. |
| `gdb PROGRAM` | Open a program in GDB. |
| `gdb -p PID` | Attach GDB to an authorized process, potentially pausing it. |
| `gdb --args PROGRAM ARGUMENT` | Start GDB with a program and its arguments. |
| `coredumpctl list` | List recorded core dumps. |
| `coredumpctl info PID` | Inspect a process's recorded core-dump metadata. |
| `coredumpctl debug PID` | Open a recorded core dump in a debugger. |
| `sudo perf stat COMMAND` | Collect performance counters while running a command. |
| `sudo perf top` | Monitor sampled execution hotspots. |
| `sudo perf record -g -- COMMAND` | Record call-stack performance samples while running a command. |
| `perf report` | Explore recorded performance samples. |
| `valgrind --leak-check=full PROGRAM` | Run a program with detailed memory-leak checks. |
| `heaptrack PROGRAM` | Profile heap allocations. |
| `sudo bpftrace -l` | List available bpftrace probes. |
| `sudo bpftool prog show` | Inspect loaded BPF programs. |
| `sudo bpftool map show` | Inspect BPF maps. |
