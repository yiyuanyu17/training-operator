# coding: utf-8

"""
    Kubeflow Training SDK

    Python SDK for Kubeflow Training  # noqa: E501

    The version of the OpenAPI document: v1.5.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

from kubeflow.training.models import *
from kubeflow.training.models.v1_job_status import V1JobStatus  # noqa: E501
from kubeflow.training.rest import ApiException

class TestV1JobStatus(unittest.TestCase):
    """V1JobStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1JobStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubeflow.training.models.v1_job_status.V1JobStatus()  # noqa: E501
        if include_optional :
            return V1JobStatus(
                completion_time = None, 
                conditions = [
                    V1JobCondition(
                        last_transition_time = None, 
                        last_update_time = None, 
                        message = '0', 
                        reason = '0', 
                        status = '0', 
                        type = '0', )
                    ], 
                last_reconcile_time = None, 
                replica_statuses = {
                    'key' : V1ReplicaStatus(
                        active = 56, 
                        failed = 56, 
                        label_selector = None, 
                        selector = '0', 
                        succeeded = 56, )
                    }, 
                start_time = None
            )
        else :
            return V1JobStatus(
                conditions = [
                    V1JobCondition(
                        last_transition_time = None, 
                        last_update_time = None, 
                        message = '0', 
                        reason = '0', 
                        status = '0', 
                        type = '0', )
                    ],
                replica_statuses = {
                    'key' : V1ReplicaStatus(
                        active = 56, 
                        failed = 56, 
                        label_selector = None, 
                        selector = '0', 
                        succeeded = 56, )
                    },
        )

    def testV1JobStatus(self):
        """Test V1JobStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
