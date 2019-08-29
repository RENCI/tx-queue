import logging
import json
import docker

logger = logging.getLogger()
logger.setLevel(logging.INFO)
def run(data):
    s = "from worker " + json.dumps(data)
    logging.info(s)
    client = docker.from_env()
    ret = client.containers.run(data["image"], command=data.get("command"), remove=True)
    logging.info("ret = {0}".format(ret))
    return ret.decode("utf-8")
