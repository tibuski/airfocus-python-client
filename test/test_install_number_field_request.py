# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.37.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from airfocus_client.models.install_number_field_request import InstallNumberFieldRequest

class TestInstallNumberFieldRequest(unittest.TestCase):
    """InstallNumberFieldRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InstallNumberFieldRequest:
        """Test InstallNumberFieldRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InstallNumberFieldRequest`
        """
        model = InstallNumberFieldRequest()
        if include_optional:
            return InstallNumberFieldRequest(
                name = '',
                settings = airfocus_client.models.number_field_type_settings.NumberFieldTypeSettings(
                    maximum = 1.337, 
                    minimum = 1.337, 
                    overflow = True, 
                    stepping = null, 
                    unit = null, ),
                type_id = '',
                description = '',
                is_team_field = True,
                workspace_ids = [
                    ''
                    ]
            )
        else:
            return InstallNumberFieldRequest(
                name = '',
                settings = airfocus_client.models.number_field_type_settings.NumberFieldTypeSettings(
                    maximum = 1.337, 
                    minimum = 1.337, 
                    overflow = True, 
                    stepping = null, 
                    unit = null, ),
                type_id = '',
        )
        """

    def testInstallNumberFieldRequest(self):
        """Test InstallNumberFieldRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
