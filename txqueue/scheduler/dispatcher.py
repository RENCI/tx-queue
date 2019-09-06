# the server runs in ../../api/openAPI3 or ../../api/swagger2
# so at runtime, the relative path to any file in the directory with dispatcher.py
# is ../../
import sys
sys.path.append('../..')
# and the full path to this file will be txqueue.scheduler.dispatcher

import json
import redis
from rq import Queue
import os
import entrypoint

q = Queue(connection=redis.StrictRedis(host=os.environ["REDIS_QUEUE_HOST"], port=int(os.environ["REDIS_QUEUE_PORT"]), db=int(os.environ["REDIS_QUEUE_DB"])))

TASK_TIME=os.environ["TASK_TIME"]
RESULT_TTL=int(os.environ["RESULT_TTL"])

def delete_job(job_id):
    """Delete my job by Id

    Upon success, marks job as &#x27;aborted&#x27; if it must be suspended, and returns the deleted job with the appropriate status # noqa: E501

    :param job_id: Id of the job that needs to be deleted
    :type job_id: str

    :rtype: Job
    """
    job = q.fetch_job(job_id)
    job.cancel()
    return job_id



def get_job_by_id(job_id):  # noqa: E501
    """Find my job by Id

    For valid response try integer Ids with value &gt;&#x3D; 1 and &lt;&#x3D; 1000.\\ \\ Other values will generated exceptions # noqa: E501

    :param job_id: Id of job to be fetched
    :type job_id: str

    :rtype: Job
    """
    job = q.fetch_job(job_id)
    if job == None:
        return 'Not Found', 404
    else:
        return {
            "status": job.get_status(),
            "name": job.func_name,
            "created_at": str(job.created_at),
            "enqueued_at": str(job.enqueued_at),
            "started_at": str(job.started_at),
            "ended_at": str(job.ended_at),
            "description": job.description,
            "result": job.result,
            "exc_info": job.exc_info
        }


def get_job_queue():  # noqa: E501
    """Lists queued jobs

    Returns a map of status codes to job ids # noqa: E501


    :rtype: Dict[str, int]
    """
    return q.job_ids


def submit_job(job_timeout, result_ttl, body=None):  # noqa: E501
    """Submit a job

    set up the run outside of the scheduler. The scheduler doesn&#x27;t care what the set-up looks like as long as it&#x27;s well-constructed JSON. For example, the run could be a serialized object with all the run parameters, or it could be a quoted unique id that the application-specific worker knows how to lookup. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Job
    """
    if job_timeout == None:
        job_timeout = TASK_TIME

    if result_ttl == None:
        result_ttl = RESULT_TTL
    pTable = q.enqueue(entrypoint.run, args=[body], job_timeout=job_timeout, result_ttl=result_ttl)
    return pTable.id            


