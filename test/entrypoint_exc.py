import logging
import json
import time

def run(data):
    s = "exc from rqworker " + json.dumps(data)
    logging.info(s)
    raise RuntimeError(s)
