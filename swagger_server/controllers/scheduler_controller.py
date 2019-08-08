import connexion
import six

from swagger_server.models.job import Job  # noqa: E501
from swagger_server import util


def delete_job(jobId):  # noqa: E501
    """Delete my job by Id

    For valid response try integer Ids with positive integer value.\\ \\ Negative or non-integer values will generate API errors # noqa: E501

    :param jobId: Id of the job that needs to be deleted
    :type jobId: int

    :rtype: None
    """
    return 'do some magic!'


def get_job_by_id(jobId):  # noqa: E501
    """Find my job by Id

    For valid response try integer Ids with value &gt;&#x3D; 1 and &lt;&#x3D; 1000.\\ \\ Other values will generated exceptions # noqa: E501

    :param jobId: Id of job to be fetched
    :type jobId: int

    :rtype: Job
    """
    return 'do some magic!'


def get_job_queue():  # noqa: E501
    """Lists queued jobs

    Returns a map of status codes to job ids # noqa: E501


    :rtype: Dict[str, int]
    """
    return 'do some magic!'


def resubmit_job(body, jobId):  # noqa: E501
    """Resubmit a job

     # noqa: E501

    :param body: job created for an analysis
    :type body: dict | bytes
    :param jobId: Id of job to be fetched
    :type jobId: int

    :rtype: Job
    """
    if connexion.request.is_json:
        body = Job.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def submit_job(body):  # noqa: E501
    """Submit a job

     # noqa: E501

    :param body: job created for an analysis
    :type body: 

    :rtype: Job
    """
    return 'do some magic!'
