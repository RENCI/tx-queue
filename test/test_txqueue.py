import os
import requests
import time
import pytest
import json
import redis
from rq import Queue, Worker
from multiprocessing import Process
import shutil
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


@pytest.fixture(autouse=True, scope="function")
def run_around_test():
    yield
    clear_task()


def wait_for_task_to_finish(taskid):
    os.chdir("/")
    ctx = reload.context()
    resp = requests.get("http://txqueue:8080/tx-queue/2/scheduler/job/" + taskid)
    print(resp.json())
    while resp.json()["status"] in ["queued", "started"]:
        time.sleep(1)
        resp = requests.get("http://txqueue:8080/tx-queue/2/scheduler/job/" + taskid)
        print(resp.json())


json_headers = {
    "Content-Type": "application/json"
}


def runWorker():
    p = Process(target = startWorker)
    workers = Worker.all(connection=redisQueue())
    assert len(list(workers)) == 0
    p.start()
    time.sleep(10)
    p.terminate()


def post_task():
    resp = requests.post("http://txqueue:8080/tx-queue/2/scheduler/job", headers=json_headers, data=json.dumps("task"))
    print(resp)
    return resp


def get_task(taskid=None):
    if taskid is None:
        return requests.get("http://txqueue:8080/tx-queue/2/scheduler/job")
    else:
        return requests.get("http://txqueue:8080/tx-queue/2/scheduler/job/" + taskid)


def delete_task(task_id):
    return requests.delete("http://txqueue:8080/tx-queue/2/scheduler/job/" + task_id)


def clear_task():
    for task in get_task().json():
        delete_task(task)

    
def test_post_job():
    resp = post_task()
    assert resp.status_code == 200
    assert isinstance(resp.json(), str)

    
def test_get_job():
    resp0 = get_task()
    assert len(resp0.json()) == 0
    resp = post_task()
    resp2 = get_task()
    assert len(resp2.json()) == 1
    assert resp.json() in resp2.json()


def test_get_task():
    resp = post_task()
    resp2 = get_task(resp.json())
    assert "name" in resp2.json()
    assert "created_at" in resp2.json()
    assert "ended_at" in resp2.json()
    assert "started_at" in resp2.json()
    assert "enqueued_at" in resp2.json()
    assert "description" in resp2.json()
    assert "status" in resp2.json()


def test_delete_task():
    resp0 = get_task()
    assert len(resp0.json()) == 0
    resp = post_task()
    resp1 = post_task()
    resp2 = get_task()
    assert len(resp2.json()) == 2
    assert resp.json() in resp2.json()
    assert resp1.json() in resp2.json()
    delete_task(resp1.json())
    resp3 = get_task()
    assert len(resp3.json()) == 1
    assert resp.json() in resp3.json()
    assert resp1.json() not in resp3.json()


def test_run_rqworker():
    resp0 = get_task()
    assert len(resp0.json()) == 0
    resp = post_task()
    resp2 = get_task()
    assert len(resp2.json()) == 1
    assert resp.json() in resp2.json()
    runWorker()
    resp3 = get_task()
    assert len(resp3.json()) == 0
    resp4 = get_task(resp.json())
    assert resp4.json()["status"] == "finished"    
    assert resp4.json()["result"] == "from rqworker \"task\""
    

def test_run_rqworker_exc():
    shutil.move("entrypoint.py", "entrypoint.py.original")
    shutil.copy("entrypoint_exc.py", "entrypoint.py")
    resp0 = get_task()
    assert len(resp0.json()) == 0
    resp = post_task()
    resp2 = get_task()
    assert len(resp2.json()) == 1
    assert resp.json() in resp2.json()
    runWorker()
    resp3 = get_task()
    assert len(resp3.json()) == 0
    resp4 = get_task(resp.json())
    assert resp4.json()["status"] == "failed"    
    assert "exc from rqworker \"task\"" in resp4.json()["exc_info"]
    os.unlink("entrypoint.py")
    shutil.move("entrypoint.py.original", "entrypoint.py")





