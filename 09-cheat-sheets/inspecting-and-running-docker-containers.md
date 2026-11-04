| Command | What you can do with it |
| --- | --- |
| `docker version` | Inspect Docker client and server versions. |
| `docker info` | Inspect daemon configuration and runtime state. |
| `docker context ls` | List Docker endpoint contexts. |
| `docker ps` | List running containers. |
| `docker ps -a` | List all containers. |
| `docker images` | List local images. |
| `docker image inspect IMAGE` | Inspect image metadata. |
| `docker inspect CONTAINER` | Inspect a container's configuration and state. |
| `docker logs --tail 100 CONTAINER` | Read a container's latest 100 log lines. |
| `docker logs -f CONTAINER` | Follow a container's logs. |
| `docker stats --no-stream` | Take one container-resource usage snapshot. |
| `docker top CONTAINER` | Inspect a container's processes. |
| `docker port CONTAINER` | Inspect a container's published ports. |
| `docker network ls` | List container networks. |
| `docker network inspect NETWORK` | Inspect a container network. |
| `docker volume ls` | List managed volumes. |
| `docker volume inspect VOLUME` | Inspect a managed volume. |
| `docker run --rm IMAGE COMMAND` | Run a command in a temporary container and remove the container on exit. |
| `docker run --rm -it IMAGE sh` | Open an interactive shell in a temporary container. |
| `docker exec -it CONTAINER sh` | Open a shell inside a running container. |
| `docker build -t IMAGE:TAG .` | Build an image from the current build context. |
| `docker compose config` | Render and validate the effective Compose configuration. |
| `docker compose ps` | Inspect Compose project containers. |
| `docker compose logs --tail 100` | Read recent Compose service logs. |
| `docker compose up -d` | Create or update Compose services in the background. |
| `docker compose stop` | Stop Compose services without removing their containers. |
| `docker system df` | Inspect Docker-managed disk usage. |
