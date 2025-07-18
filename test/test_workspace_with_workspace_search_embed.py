# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.37.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from airfocus_client.models.workspace_with_workspace_search_embed import WorkspaceWithWorkspaceSearchEmbed

class TestWorkspaceWithWorkspaceSearchEmbed(unittest.TestCase):
    """WorkspaceWithWorkspaceSearchEmbed unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkspaceWithWorkspaceSearchEmbed:
        """Test WorkspaceWithWorkspaceSearchEmbed
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkspaceWithWorkspaceSearchEmbed`
        """
        model = WorkspaceWithWorkspaceSearchEmbed()
        if include_optional:
            return WorkspaceWithWorkspaceSearchEmbed(
                embedded = airfocus_client.models.workspace_search_embed.WorkspaceSearchEmbed(
                    current_permission = 'comment', 
                    item_count = 56, 
                    permissions = {
                        'key' : 'comment'
                        }, 
                    statuses = {
                        'key' : airfocus_client.models.status.Status(
                            category = 'active', 
                            color = 'blue', 
                            default = True, 
                            id = '', 
                            name = '', 
                            order = 56, 
                            workspace_id = '', )
                        }, ),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                description = airfocus_client.models.rich_text.RichText(
                    blocks = [
                        null
                        ], ),
                id = '',
                last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                namespace = 'main',
                order = 56,
                progress_mode = 'count',
                team_id = '',
                alias = '',
                default_permission = 'comment',
                item_color = 'amber',
                item_type = 'bug',
                metadata = airfocus_client.models.workspace_workspace_metadata.WorkspaceWorkspaceMetadata(
                    duplicated = True, 
                    template_id = '', 
                    template_workspace_ref = '', 
                    version = '', )
            )
        else:
            return WorkspaceWithWorkspaceSearchEmbed(
                embedded = airfocus_client.models.workspace_search_embed.WorkspaceSearchEmbed(
                    current_permission = 'comment', 
                    item_count = 56, 
                    permissions = {
                        'key' : 'comment'
                        }, 
                    statuses = {
                        'key' : airfocus_client.models.status.Status(
                            category = 'active', 
                            color = 'blue', 
                            default = True, 
                            id = '', 
                            name = '', 
                            order = 56, 
                            workspace_id = '', )
                        }, ),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                description = airfocus_client.models.rich_text.RichText(
                    blocks = [
                        null
                        ], ),
                id = '',
                last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                namespace = 'main',
                order = 56,
                progress_mode = 'count',
                team_id = '',
        )
        """

    def testWorkspaceWithWorkspaceSearchEmbed(self):
        """Test WorkspaceWithWorkspaceSearchEmbed"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
