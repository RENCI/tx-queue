# Swagger v2 scheduler API code
refer to tx-queue/README.md for notes on how to start the server

docker is untested, tips follow.

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
```
