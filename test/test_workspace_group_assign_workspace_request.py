# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.37.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from airfocus_client.models.workspace_group_assign_workspace_request import WorkspaceGroupAssignWorkspaceRequest

class TestWorkspaceGroupAssignWorkspaceRequest(unittest.TestCase):
    """WorkspaceGroupAssignWorkspaceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkspaceGroupAssignWorkspaceRequest:
        """Test WorkspaceGroupAssignWorkspaceRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkspaceGroupAssignWorkspaceRequest`
        """
        model = WorkspaceGroupAssignWorkspaceRequest()
        if include_optional:
            return WorkspaceGroupAssignWorkspaceRequest(
                workspace_id = '',
                workspace_group_id = ''
            )
        else:
            return WorkspaceGroupAssignWorkspaceRequest(
                workspace_id = '',
        )
        """

    def testWorkspaceGroupAssignWorkspaceRequest(self):
        """Test WorkspaceGroupAssignWorkspaceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
