import sys
sys.path.append('../..')
import txqueue.scheduler.dispatcher as disp

import connexion
import six

from swagger_server.models.job import Job  # noqa: E501
from swagger_server import util


def delete_job(jobId):  # noqa: E501
    """Delete my job by Id

    Upon success, marks job as &#x27;aborted&#x27; if it must be suspended, and returns the deleted job with the appropriate status # noqa: E501

    :param job_id: Id of the job that needs to be deleted
    :type job_id: str

    :rtype: Job
    """
    return disp.delete_job(jobId)


def get_job_by_id(jobId):  # noqa: E501
    """Find my job by Id

    For valid response try integer Ids with value &gt;&#x3D; 1 and &lt;&#x3D; 1000.\\ \\ Other values will generated exceptions # noqa: E501

    :param job_id: Id of job to be fetched
    :type job_id: str

    :rtype: Job
    """

    return disp.get_job_by_id(jobId)


def get_job_queue():  # noqa: E501
    """Lists queued jobs

    Returns a map of status codes to job ids # noqa: E501


    :rtype: Dict[str, int]
    """

    return disp.get_job_queue()


def submit_job(job_timeout=None, result_ttl=None, body=None):  # noqa: E501
    """Submit a job

    set up the run outside of the scheduler. The scheduler doesn&#x27;t care what the set-up looks like as long as it&#x27;s well-constructed JSON. For example, the run could be a serialized object with all the run parameters, or it could be a quoted unique id that the application-specific worker knows how to lookup. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Job
    """
    return disp.submit_job(job_timeout, result_ttl, body)
