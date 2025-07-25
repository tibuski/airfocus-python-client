# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.37.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from airfocus_client.models.template import Template

class TestTemplate(unittest.TestCase):
    """Template unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Template:
        """Test Template
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Template`
        """
        model = Template()
        if include_optional:
            return Template(
                abstract = '',
                description = '',
                featured = True,
                id = '',
                name = '',
                views_section_title = '',
                workspaces_count = 56,
                apps = [
                    airfocus_client.models.template_app.TemplateApp(
                        description = '', 
                        name = '', 
                        type_id = '', )
                    ],
                image_url = '',
                views = [
                    airfocus_client.models.template_view.TemplateView(
                        description = '', 
                        icon_name = '', 
                        image_url = '', 
                        name = '', )
                    ]
            )
        else:
            return Template(
                abstract = '',
                description = '',
                featured = True,
                id = '',
                name = '',
                views_section_title = '',
                workspaces_count = 56,
        )
        """

    def testTemplate(self):
        """Test Template"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
