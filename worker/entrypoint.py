import logging
import json
import time

def run(data):
    s = "from rqworker " + json.dumps(data)
    logging.info(s)
    return s
