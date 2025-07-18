# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.37.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from airfocus_client.models.milestone_with_embed_page import MilestoneWithEmbedPage

class TestMilestoneWithEmbedPage(unittest.TestCase):
    """MilestoneWithEmbedPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MilestoneWithEmbedPage:
        """Test MilestoneWithEmbedPage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MilestoneWithEmbedPage`
        """
        model = MilestoneWithEmbedPage()
        if include_optional:
            return MilestoneWithEmbedPage(
                total_items = 56,
                items = [
                    airfocus_client.models.milestone_with_embed.MilestoneWithEmbed(
                        _embedded = airfocus_client.models._embedded._embedded(), 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        description = '', 
                        id = '', 
                        last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        timezone = '', 
                        workspace_id = '', )
                    ]
            )
        else:
            return MilestoneWithEmbedPage(
                total_items = 56,
        )
        """

    def testMilestoneWithEmbedPage(self):
        """Test MilestoneWithEmbedPage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
