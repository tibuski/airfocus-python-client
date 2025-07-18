# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.37.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from airfocus_client.models.item_search_query_filter import ItemSearchQueryFilter

class TestItemSearchQueryFilter(unittest.TestCase):
    """ItemSearchQueryFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ItemSearchQueryFilter:
        """Test ItemSearchQueryFilter
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ItemSearchQueryFilter`
        """
        model = ItemSearchQueryFilter()
        if include_optional:
            return ItemSearchQueryFilter(
                inner = None,
                mode = 'after',
                value = None,
                field_id = '',
                filter = airfocus_client.models.js_object.JsObject(),
                integration_id = '',
                case_sensitive = True,
                text = '',
                item_id = '',
                workspace_id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                var_property = None,
                status_ids = [
                    ''
                    ],
                categories = [
                    'active'
                    ]
            )
        else:
            return ItemSearchQueryFilter(
                inner = None,
                mode = 'after',
                value = None,
                field_id = '',
                filter = airfocus_client.models.js_object.JsObject(),
                integration_id = '',
                case_sensitive = True,
                text = '',
                item_id = '',
                workspace_id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testItemSearchQueryFilter(self):
        """Test ItemSearchQueryFilter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
