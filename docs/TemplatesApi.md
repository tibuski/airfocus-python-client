# airfocus_client.TemplatesApi

All URIs are relative to *https://app.airfocus.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_template**](TemplatesApi.md#apply_template) | **POST** /api/templates/{templateId} | Install template
[**apply_template_legacy**](TemplatesApi.md#apply_template_legacy) | **POST** /api/workspaces/templates/{templateId} | Install template
[**list_templates**](TemplatesApi.md#list_templates) | **GET** /api/templates | List templates
[**list_templates_legacy**](TemplatesApi.md#list_templates_legacy) | **GET** /api/workspaces/templates | List templates


# **apply_template**
> WorkspaceWithWorkspaceEmbed apply_template(template_id, apply_template_request, act_as_admin=act_as_admin)

Install template

Installs the requested template with the given parameters.
Returns a newly created workspace.
If the template creates multiple workspaces - then it still returns a single workspace which is considered by the template as "main".<br/>Requirements:<br/>- auth-client scopes: "workspace"

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.apply_template_request import ApplyTemplateRequest
from airfocus_client.models.workspace_with_workspace_embed import WorkspaceWithWorkspaceEmbed
from airfocus_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.airfocus.com
# See configuration.py for a list of all supported configuration parameters.
configuration = airfocus_client.Configuration(
    host = "https://app.airfocus.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: httpAuth
configuration = airfocus_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with airfocus_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airfocus_client.TemplatesApi(api_client)
    template_id = 'template_id_example' # str | 
    apply_template_request = airfocus_client.ApplyTemplateRequest() # ApplyTemplateRequest | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Install template
        api_response = api_instance.apply_template(template_id, apply_template_request, act_as_admin=act_as_admin)
        print("The response of TemplatesApi->apply_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->apply_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **apply_template_request** | [**ApplyTemplateRequest**](ApplyTemplateRequest.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**WorkspaceWithWorkspaceEmbed**](WorkspaceWithWorkspaceEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | If missing authentication token. |  -  |
**403** | If authenticated client does not have the required access scopes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_template_legacy**
> WorkspaceWithWorkspaceEmbed apply_template_legacy(template_id, apply_template_request, act_as_admin=act_as_admin)

Install template

Installs the requested template with the given parameters.
Returns a newly created workspace.
If the template creates multiple workspaces - then it still returns a single workspace which is considered by the template as "main".<br/>Requirements:<br/>- auth-client scopes: "workspace"

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.apply_template_request import ApplyTemplateRequest
from airfocus_client.models.workspace_with_workspace_embed import WorkspaceWithWorkspaceEmbed
from airfocus_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.airfocus.com
# See configuration.py for a list of all supported configuration parameters.
configuration = airfocus_client.Configuration(
    host = "https://app.airfocus.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: httpAuth
configuration = airfocus_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with airfocus_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airfocus_client.TemplatesApi(api_client)
    template_id = 'template_id_example' # str | 
    apply_template_request = airfocus_client.ApplyTemplateRequest() # ApplyTemplateRequest | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Install template
        api_response = api_instance.apply_template_legacy(template_id, apply_template_request, act_as_admin=act_as_admin)
        print("The response of TemplatesApi->apply_template_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->apply_template_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **apply_template_request** | [**ApplyTemplateRequest**](ApplyTemplateRequest.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**WorkspaceWithWorkspaceEmbed**](WorkspaceWithWorkspaceEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | If missing authentication token. |  -  |
**403** | If authenticated client does not have the required access scopes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_templates**
> TemplatePageWithEmbed list_templates(act_as_admin=act_as_admin, offset=offset, limit=limit)

List templates

Returns all workspace-templates available to the current team.<br/>Requirements:<br/>- auth-client scopes: "workspace:read"

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.template_page_with_embed import TemplatePageWithEmbed
from airfocus_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.airfocus.com
# See configuration.py for a list of all supported configuration parameters.
configuration = airfocus_client.Configuration(
    host = "https://app.airfocus.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: httpAuth
configuration = airfocus_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with airfocus_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airfocus_client.TemplatesApi(api_client)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    offset = 0 # int | How many elements to skip. (optional) (default to 0)
    limit = 100 # int | How many elements to return. (optional) (default to 100)

    try:
        # List templates
        api_response = api_instance.list_templates(act_as_admin=act_as_admin, offset=offset, limit=limit)
        print("The response of TemplatesApi->list_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->list_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **offset** | **int**| How many elements to skip. | [optional] [default to 0]
 **limit** | **int**| How many elements to return. | [optional] [default to 100]

### Return type

[**TemplatePageWithEmbed**](TemplatePageWithEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | If missing authentication token. |  -  |
**403** | If authenticated client does not have the required access scopes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_templates_legacy**
> TemplatePageWithEmbed list_templates_legacy(act_as_admin=act_as_admin, offset=offset, limit=limit)

List templates

Returns all workspace-templates available to the current team.<br/>Requirements:<br/>- auth-client scopes: "workspace:read"

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.template_page_with_embed import TemplatePageWithEmbed
from airfocus_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.airfocus.com
# See configuration.py for a list of all supported configuration parameters.
configuration = airfocus_client.Configuration(
    host = "https://app.airfocus.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: httpAuth
configuration = airfocus_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with airfocus_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airfocus_client.TemplatesApi(api_client)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    offset = 0 # int | How many elements to skip. (optional) (default to 0)
    limit = 100 # int | How many elements to return. (optional) (default to 100)

    try:
        # List templates
        api_response = api_instance.list_templates_legacy(act_as_admin=act_as_admin, offset=offset, limit=limit)
        print("The response of TemplatesApi->list_templates_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->list_templates_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **offset** | **int**| How many elements to skip. | [optional] [default to 0]
 **limit** | **int**| How many elements to return. | [optional] [default to 100]

### Return type

[**TemplatePageWithEmbed**](TemplatePageWithEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | If missing authentication token. |  -  |
**403** | If authenticated client does not have the required access scopes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

