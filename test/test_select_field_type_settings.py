# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.37.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from airfocus_client.models.select_field_type_settings import SelectFieldTypeSettings

class TestSelectFieldTypeSettings(unittest.TestCase):
    """SelectFieldTypeSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SelectFieldTypeSettings:
        """Test SelectFieldTypeSettings
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SelectFieldTypeSettings`
        """
        model = SelectFieldTypeSettings()
        if include_optional:
            return SelectFieldTypeSettings(
                multi = True,
                options = [
                    airfocus_client.models.select_field_type_option.SelectFieldTypeOption(
                        color = 'blue', 
                        default = True, 
                        description = '', 
                        id = '', 
                        name = '', 
                        numeric_value = 1.337, )
                    ]
            )
        else:
            return SelectFieldTypeSettings(
                multi = True,
        )
        """

    def testSelectFieldTypeSettings(self):
        """Test SelectFieldTypeSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
