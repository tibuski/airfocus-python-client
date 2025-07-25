# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.37.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from airfocus_client.models.item import Item

class TestItem(unittest.TestCase):
    """Item unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Item:
        """Test Item
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Item`
        """
        model = Item()
        if include_optional:
            return Item(
                archived = True,
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
                order = 56,
                status_id = '',
                workspace_id = '',
                assignee_user_ids = [
                    ''
                    ],
                number = 56,
                status_category_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return Item(
                archived = True,
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
                order = 56,
                status_id = '',
                workspace_id = '',
        )
        """

    def testItem(self):
        """Test Item"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
