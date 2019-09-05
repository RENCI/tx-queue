import logging
import json
import docker
from docker.types import Mount

logger = logging.getLogger()
logger.setLevel(logging.INFO)
def run(data):
    s = "from worker " + json.dumps(data)
    logging.info(s)
    client = docker.from_env()

    volumes = list(map(lambda l: Mount(l["target"], l["source"], type=l["type"], read_only=l["read_only"]), data["mounts"]))
    logging.info("volumes = {0}".format(volumes))
    ret = client.containers.run(data["image"], command=data.get("command"), mounts=volumes, remove=True, stdout=True, stderr=True)
    logging.info("ret = {0}".format(ret))
    return ret.decode("utf-8")
