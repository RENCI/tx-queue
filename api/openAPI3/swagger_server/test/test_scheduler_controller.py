# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.job import Job  # noqa: E501
from swagger_server.test import BaseTestCase

jobId_example="1"
class TestSchedulerController(BaseTestCase):
    """SchedulerController integration test stubs"""

    def test_delete_job(self):
        """Test case for delete_job

        Delete my job by Id
        """
        response = self.client.open(
            '/tx-queue/2/scheduler/job/{jobId}'.format(jobId=1),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_job_by_id(self):
        """Test case for get_job_by_id

        Find my job by Id
        """
        response = self.client.open(
            '/tx-queue/2/scheduler/job/{jobId}'.format(jobId=1),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_job_queue(self):
        """Test case for get_job_queue

        Lists queued jobs
        """
        response = self.client.open(
            '/tx-queue/2/scheduler/job',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_submit_job(self):
        """Test case for submit_job

        Submit a job
        """
        body = '\"{train: \\\"http:/github.com/path/file1\\\", seed:5, epochs: 5000}\"'
        response = self.client.open(
            '/tx-queue/2/scheduler/job',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
