# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.37.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from airfocus_client.models.item_search_query_filter_status_category_contains_any import ItemSearchQueryFilterStatusCategoryContainsAny

class TestItemSearchQueryFilterStatusCategoryContainsAny(unittest.TestCase):
    """ItemSearchQueryFilterStatusCategoryContainsAny unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ItemSearchQueryFilterStatusCategoryContainsAny:
        """Test ItemSearchQueryFilterStatusCategoryContainsAny
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ItemSearchQueryFilterStatusCategoryContainsAny`
        """
        model = ItemSearchQueryFilterStatusCategoryContainsAny()
        if include_optional:
            return ItemSearchQueryFilterStatusCategoryContainsAny(
                categories = [
                    'active'
                    ]
            )
        else:
            return ItemSearchQueryFilterStatusCategoryContainsAny(
        )
        """

    def testItemSearchQueryFilterStatusCategoryContainsAny(self):
        """Test ItemSearchQueryFilterStatusCategoryContainsAny"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
