```bash
podman version
podman info
podman ps
podman ps -a
podman images
podman inspect CONTAINER
podman logs --tail 100 CONTAINER
podman stats --no-stream
podman top CONTAINER
podman port CONTAINER
podman pod ps
podman network ls
podman volume ls
podman run --rm IMAGE COMMAND
podman run --rm -it IMAGE sh
podman exec -it CONTAINER sh
podman build -t IMAGE:TAG .
man podman-systemd.unit
podman kube play --help
podman system df
```
