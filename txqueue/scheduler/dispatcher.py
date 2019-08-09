# the server runs in ../../api/openAPI3 or ../../api/swagger2
# so at runtime, the relative path to any file in the directory with dispatcher.py
# is ../../
import sys
sys.path.append('../..')
# and the full path to this file will be txqueue.scheduler.dispatcher
import txqueue.scheduler.examples as ex


def delete_job(job_id):
    """Delete my job by Id

    Upon success, marks job as &#x27;aborted&#x27; if it must be suspended, and returns the deleted job with the appropriate status # noqa: E501

    :param job_id: Id of the job that needs to be deleted
    :type job_id: str

    :rtype: Job
    """
    job = ex.xJob

    return job


def get_job_by_id(job_id):  # noqa: E501
    """Find my job by Id

    For valid response try integer Ids with value &gt;&#x3D; 1 and &lt;&#x3D; 1000.\\ \\ Other values will generated exceptions # noqa: E501

    :param job_id: Id of job to be fetched
    :type job_id: str

    :rtype: Job
    """
    job = ex.xJob

    return '[dispatcher]get:'+job_id+",job="+job


def get_job_queue():  # noqa: E501
    """Lists queued jobs

    Returns a map of status codes to job ids # noqa: E501


    :rtype: Dict[str, int]
    """
    jobs = ex.xJobs

    return '[dispatcher]list jobs:'+jobs


def submit_job(body=None):  # noqa: E501
    """Submit a job

    set up the run outside of the scheduler. The scheduler doesn&#x27;t care what the set-up looks like as long as it&#x27;s well-constructed JSON. For example, the run could be a serialized object with all the run parameters, or it could be a quoted unique id that the application-specific worker knows how to lookup. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Job
    """
    job = ex.xJob

    return '[dispatcher]submit job, payload:'+body+",job="+job
