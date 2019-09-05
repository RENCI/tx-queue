import os
import requests
import time
import pytest
import json
import redis
from rq import Queue, Worker
from multiprocessing import Process
from utils import startWorker, redisQueue

@pytest.fixture(scope="session", autouse=True)
def pause():
    yield
    if os.environ.get("PAUSE") == "1":
        input("Press Enter to continue...")

        
@pytest.fixture(scope='function', autouse=True)
def test_log(request):
    print("Test '{}' STARTED".format(request.node.nodeid)) # Here logging is used, you can use whatever you want to use for logs
    def fin():
        print("Test '{}' COMPLETED".format(request.node.nodeid))
    request.addfinalizer(fin)


json_headers = {
    "Content-Type": "application/json"
}


def post_task(img, cmd, volumes=[]):
    resp = requests.post("http://txqueue:8080/tx-queue/2/scheduler/job", headers=json_headers, data=json.dumps({
        "image": img,
        "command": cmd,
        "mounts": volumes
    }))
    print(resp)
    return resp


def get_task(taskid=None):
    if taskid is None:
        return requests.get("http://txqueue:8080/tx-queue/2/scheduler/job")
    else:
        return requests.get("http://txqueue:8080/tx-queue/2/scheduler/job/" + taskid)


def test_run_rqworker():
    resp = post_task("ubuntu:18.04", "echo from worker")
    task_id = resp.json()
    resp2 = get_task(task_id)
    print(resp2.json())
    while resp2.json()["status"] in ["queued", "started"]:
        time.sleep(1)
        resp2 = get_task(task_id)
        print(resp2.json())
        
    assert resp2.json()["result"] == "from worker\n"
    

def test_run_rqworker_volume_read():
    assert not os.path.exists("/tmpVol/read")
        
    with open("/tmpVol/read", mode="w+") as f:
        f.write("from rq")
        f.flush()

    try:
        resp = post_task("ubuntu:18.04", "/bin/bash -c \"cat /tmpVol/read > /tmpVol/read2\"",
                         volumes=[
                             {
                                 "source": "tx-queue_tmpVol",
                                 "target": "/tmpVol",
                                 "type": "volume",
                                 "read_only": False
                             }
                         ])
        task_id = resp.json()
        resp2 = get_task(task_id)
        print(resp2.json())
        while resp2.json()["status"] in ["queued", "started"]:
            time.sleep(1)
            resp2 = get_task(task_id)
            print(resp2.json())
        
        assert resp2.json()["status"] == "finished"
        #assert resp2.json()["result"] == "from rq"
        assert os.path.exists("/tmpVol/read2")
        with open("/tmpVol/read2", mode="r") as f:
            s = f.readline()
            
        assert s == "from rq"
    finally:
        os.unlink("/tmpVol/read")
        os.unlink("/tmpVol/read2")





