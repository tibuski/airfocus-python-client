# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.37.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from airfocus_client.models.install_text_field_request import InstallTextFieldRequest

class TestInstallTextFieldRequest(unittest.TestCase):
    """InstallTextFieldRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InstallTextFieldRequest:
        """Test InstallTextFieldRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InstallTextFieldRequest`
        """
        model = InstallTextFieldRequest()
        if include_optional:
            return InstallTextFieldRequest(
                name = '',
                type_id = '',
                description = '',
                is_team_field = True,
                workspace_ids = [
                    ''
                    ]
            )
        else:
            return InstallTextFieldRequest(
                name = '',
                type_id = '',
        )
        """

    def testInstallTextFieldRequest(self):
        """Test InstallTextFieldRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
