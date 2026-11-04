```bash
docker version
docker info
docker context ls
docker ps
docker ps -a
docker images
docker image inspect IMAGE
docker inspect CONTAINER
docker logs --tail 100 CONTAINER
docker logs -f CONTAINER
docker stats --no-stream
docker top CONTAINER
docker port CONTAINER
docker network ls
docker network inspect NETWORK
docker volume ls
docker volume inspect VOLUME
docker run --rm IMAGE COMMAND
docker run --rm -it IMAGE sh
docker exec -it CONTAINER sh
docker build -t IMAGE:TAG .
docker compose config
docker compose ps
docker compose logs --tail 100
docker compose up -d
docker compose stop
docker system df
```
