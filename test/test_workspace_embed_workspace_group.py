# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.37.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from airfocus_client.models.workspace_embed_workspace_group import WorkspaceEmbedWorkspaceGroup

class TestWorkspaceEmbedWorkspaceGroup(unittest.TestCase):
    """WorkspaceEmbedWorkspaceGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkspaceEmbedWorkspaceGroup:
        """Test WorkspaceEmbedWorkspaceGroup
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkspaceEmbedWorkspaceGroup`
        """
        model = WorkspaceEmbedWorkspaceGroup()
        if include_optional:
            return WorkspaceEmbedWorkspaceGroup(
                id = '',
                name = '',
                order = 56,
                parent_id = ''
            )
        else:
            return WorkspaceEmbedWorkspaceGroup(
                id = '',
                name = '',
                order = 56,
        )
        """

    def testWorkspaceEmbedWorkspaceGroup(self):
        """Test WorkspaceEmbedWorkspaceGroup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
