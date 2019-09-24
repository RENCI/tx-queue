# tx-queue

## Running the server
### Configure the server
Edit config/server/params.py to set a basePath that doesn't interfere with other servers.

If you don't edit that file, the basePath and port will be set in the API's yaml file, which is:
```
api/<api>/swagger_server/swagger/swagger.yaml
```
where ```<api>``` is either openAPI3 or swagger2
  
Otherwise edit the file, it should look something like this:
```
port=<an-open-port-like-8080>
basePath=/<your-username>
```
### Install and start the server
Use the swagger2 api for now, the openAPI3's request body is broken for the 'job submit' function.

Upon first run, you may need to install the requirements for the API, then start the server.
```
cd api/swagger2
pip3 install -r requirements.txt
python3 -m swagger_server
```
Open your browser; if you didn't edit the config/server/param.py file, you'll navigate to:
```
http://cellfie2.renci.org:8080/tx-queue/2/ui/
```
Your Swagger definition lives here:
```
http://cellfie2.renci.org:8080/tx-queue/2/swagger.json
```

To launch the integration tests, use tox (not for swagger2, and broken on openAPI3):
```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
```


## job submission format
```
{
  "image": docker image,
  "command": command to run in image,
  "mounts": [
    "source": source path,
    "target": target path,
    "type": type,
    "read_only": read only
  ]
}
```



## run
```
docker-compose -f docker-compose.yml up --build -V
```

## run with worker
```
docker-compose -f docker-compose.yml -f worker/docker-compose.yml up --build -V
```


## test
```
docker-compose -f docker-compose.yml -f test/docker-compose.yml up --build -V --exit-code-from txqueue-test
docker-compose -f docker-compose.yml -f worker/docker-compose.yml -f worker/test/docker-compose.yml up --build -V --exit-code-from txqueue-worker-test

```
