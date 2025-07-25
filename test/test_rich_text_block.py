# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.37.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from airfocus_client.models.rich_text_block import RichTextBlock

class TestRichTextBlock(unittest.TestCase):
    """RichTextBlock unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RichTextBlock:
        """Test RichTextBlock
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RichTextBlock`
        """
        model = RichTextBlock()
        if include_optional:
            return RichTextBlock(
                attachment_id = '',
                content_type = '',
                content = [
                    null
                    ],
                id = '',
                raw = '',
                url = '',
                level = 56,
                ordered = True,
                color_hex = '',
                caption = '',
                meta = airfocus_client.models.meta.meta(),
                width = 56,
                language = '',
                height = 56,
                bullet_list_marker = '',
                items = [
                    airfocus_client.models.rich_text_list_item.RichTextListItem(
                        content = null, )
                    ],
                ordered_list_delimiter = '',
                ordered_list_starts_at = 56
            )
        else:
            return RichTextBlock(
                attachment_id = '',
                content_type = '',
                content = [
                    null
                    ],
                id = '',
                raw = '',
                url = '',
                level = 56,
                ordered = True,
                color_hex = '',
        )
        """

    def testRichTextBlock(self):
        """Test RichTextBlock"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
