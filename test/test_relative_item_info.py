# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.37.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from airfocus_client.models.relative_item_info import RelativeItemInfo

class TestRelativeItemInfo(unittest.TestCase):
    """RelativeItemInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RelativeItemInfo:
        """Test RelativeItemInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RelativeItemInfo`
        """
        model = RelativeItemInfo()
        if include_optional:
            return RelativeItemInfo(
                child_order = 56,
                item_id = '',
                parent_order = 56,
                relation_id = '',
                workspace_id = '',
                alias = '',
                item = airfocus_client.models.item.Item(
                    archived = True, 
                    assignee_user_ids = [
                        ''
                        ], 
                    color = 'amber', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    description = airfocus_client.models.rich_text.RichText(
                        blocks = [
                            null
                            ], ), 
                    fields = {
                        'key' : null
                        }, 
                    id = '', 
                    last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    name = '', 
                    number = 56, 
                    order = 56, 
                    status_category_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    status_id = '', 
                    status_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    workspace_id = '', ),
                item_type = 'bug'
            )
        else:
            return RelativeItemInfo(
                child_order = 56,
                item_id = '',
                parent_order = 56,
                relation_id = '',
                workspace_id = '',
        )
        """

    def testRelativeItemInfo(self):
        """Test RelativeItemInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
