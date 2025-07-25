# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.37.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from airfocus_client.models.template_search_embed import TemplateSearchEmbed

class TestTemplateSearchEmbed(unittest.TestCase):
    """TemplateSearchEmbed unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TemplateSearchEmbed:
        """Test TemplateSearchEmbed
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TemplateSearchEmbed`
        """
        model = TemplateSearchEmbed()
        if include_optional:
            return TemplateSearchEmbed(
                categories = [
                    airfocus_client.models.template_category.TemplateCategory(
                        name = '', 
                        slug = '', 
                        template_ids = [
                            ''
                            ], )
                    ]
            )
        else:
            return TemplateSearchEmbed(
        )
        """

    def testTemplateSearchEmbed(self):
        """Test TemplateSearchEmbed"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
