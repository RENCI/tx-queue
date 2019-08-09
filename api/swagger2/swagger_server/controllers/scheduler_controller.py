import sys
sys.path.append('../..')
import txqueue.scheduler.dispatcher as disp


import six

from swagger_server.models.job import Job  # noqa: E501
from swagger_server import util


def delete_job(jobId):  # noqa: E501
    """Delete my job by Id

    Upon success, marks job as &#39;aborted&#39; if it must be suspended, and returns the deleted job with the appropriate status # noqa: E501

    :param jobId: Id of the job that needs to be deleted
    :type jobId: str

    :rtype: Job
    """
    return disp.delete_job(jobId)


def get_job_by_id(jobId):  # noqa: E501
    """Find my job by Id

    For valid response try integer Ids with value &gt;&#x3D; 1 and &lt;&#x3D; 1000.\\ \\ Other values will generated exceptions # noqa: E501

    :param jobId: Id of job to be fetched
    :type jobId: str

    :rtype: Job
    """
    return disp.get_job_by_id(jobId)


def get_job_queue():  # noqa: E501
    """Lists queued jobs

    Returns a map of status codes to job ids # noqa: E501


    :rtype: Dict[str, int]
    """
    return disp.get_job_queue()

def submit_job(payload):  # noqa: E501
    """Submit a job

    Set up the job to be run outside of the scheduler. The scheduler doesn&#39;t care what the job set-up looks like as long as it&#39;s well-constructed JSON. For example, the set-up could be a serialized object with all the parameters necessary for the run, or it could be a quoted unique id that the application-specific worker knows how to lookup in a database to get the parameters necessary for the run. # noqa: E501

    :param payload: The string defining the analysis to be completed.
    :type payload: str

    :rtype: Job
    """
    return disp.submit_job(payload)

