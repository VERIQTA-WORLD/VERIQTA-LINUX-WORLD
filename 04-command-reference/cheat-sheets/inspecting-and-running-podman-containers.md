| Command | What you can do with it |
| --- | --- |
| `podman version` | Inspect the Podman version. |
| `podman info` | Inspect Podman host and runtime settings. |
| `podman ps` | List running containers. |
| `podman ps -a` | List all containers. |
| `podman images` | List local images. |
| `podman inspect CONTAINER` | Inspect a container's configuration and state. |
| `podman logs --tail 100 CONTAINER` | Read a container's latest 100 log lines. |
| `podman stats --no-stream` | Take one container-resource usage snapshot. |
| `podman top CONTAINER` | Inspect a container's processes. |
| `podman port CONTAINER` | Inspect a container's published ports. |
| `podman pod ps` | List Podman pods. |
| `podman network ls` | List Podman networks. |
| `podman volume ls` | List Podman volumes. |
| `podman run --rm IMAGE COMMAND` | Run a command in a temporary container removed on exit. |
| `podman run --rm -it IMAGE sh` | Open an interactive shell in a temporary container. |
| `podman exec -it CONTAINER sh` | Open a shell inside a running container. |
| `podman build -t IMAGE:TAG .` | Build an image from the current build context. |
| `man podman-systemd.unit` | Read Quadlet configuration documentation for systemd-managed containers. |
| `podman kube play --help` | Read options for running Kubernetes YAML through Podman. |
| `podman system df` | Inspect Podman-managed disk usage. |
