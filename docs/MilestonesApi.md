# airfocus_client.MilestonesApi

All URIs are relative to *https://app.airfocus.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_milestones**](MilestonesApi.md#bulk_milestones) | **POST** /api/workspaces/{workspaceId}/milestones/bulk | Perform multiple operations with milestones
[**create_milestone**](MilestonesApi.md#create_milestone) | **POST** /api/workspaces/{workspaceId}/milestones | Create a new milestone
[**delete_milestone**](MilestonesApi.md#delete_milestone) | **DELETE** /api/workspaces/{workspaceId}/milestones/{milestoneId} | Delete an existing milestone
[**list_milestones**](MilestonesApi.md#list_milestones) | **POST** /api/workspaces/{workspaceId}/milestones/list | Retrieve multiple milestones by their IDs
[**patch_milestone**](MilestonesApi.md#patch_milestone) | **PATCH** /api/workspaces/{workspaceId}/milestones/{milestoneId} | Patch an existing milestone
[**retrieve_milestone**](MilestonesApi.md#retrieve_milestone) | **GET** /api/workspaces/{workspaceId}/milestones/{milestoneId} | Retrieve a single milestone by its ID
[**search_milestones**](MilestonesApi.md#search_milestones) | **POST** /api/workspaces/{workspaceId}/milestones/search | Retrieve or search milestones
[**update_milestone**](MilestonesApi.md#update_milestone) | **PUT** /api/workspaces/{workspaceId}/milestones/{milestoneId} | Update an existing milestone


# **bulk_milestones**
> List[MilestoneWithEmbed] bulk_milestones(workspace_id, act_as_admin=act_as_admin, milestone_bulk_action=milestone_bulk_action)

Perform multiple operations with milestones

Accepts a list of create/update/patch/delete operations (see the request model for more details).<br/>
Each operation can target a single or multiple milestones.<br/>
Returns a list of results for each input operation including errors.<br/>
Guarantees that the size and order of the returned results matches the input list of operations.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.milestone_bulk_action import MilestoneBulkAction
from airfocus_client.models.milestone_with_embed import MilestoneWithEmbed
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
    api_instance = airfocus_client.MilestonesApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed milestones.
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    milestone_bulk_action = [airfocus_client.MilestoneBulkAction()] # List[MilestoneBulkAction] |  (optional)

    try:
        # Perform multiple operations with milestones
        api_response = api_instance.bulk_milestones(workspace_id, act_as_admin=act_as_admin, milestone_bulk_action=milestone_bulk_action)
        print("The response of MilestonesApi->bulk_milestones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MilestonesApi->bulk_milestones: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed milestones. | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **milestone_bulk_action** | [**List[MilestoneBulkAction]**](MilestoneBulkAction.md)|  | [optional] 

### Return type

[**List[MilestoneWithEmbed]**](MilestoneWithEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | If payload is invalid. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_milestone**
> MilestoneWithEmbed create_milestone(workspace_id, create_milestone_request, act_as_admin=act_as_admin)

Create a new milestone

Returns newly created milestone with its sanitised data.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.create_milestone_request import CreateMilestoneRequest
from airfocus_client.models.milestone_with_embed import MilestoneWithEmbed
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
    api_instance = airfocus_client.MilestonesApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed milestones.
    create_milestone_request = airfocus_client.CreateMilestoneRequest() # CreateMilestoneRequest | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Create a new milestone
        api_response = api_instance.create_milestone(workspace_id, create_milestone_request, act_as_admin=act_as_admin)
        print("The response of MilestonesApi->create_milestone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MilestonesApi->create_milestone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed milestones. | 
 **create_milestone_request** | [**CreateMilestoneRequest**](CreateMilestoneRequest.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**MilestoneWithEmbed**](MilestoneWithEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | If payload is invalid. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_milestone**
> delete_milestone(workspace_id, milestone_id, act_as_admin=act_as_admin)

Delete an existing milestone

Returns empty result if the milestone was successfully deleted.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
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
    api_instance = airfocus_client.MilestonesApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed milestones.
    milestone_id = 'milestone_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Delete an existing milestone
        api_instance.delete_milestone(workspace_id, milestone_id, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling MilestonesApi->delete_milestone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed milestones. | 
 **milestone_id** | **str**|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

void (empty response body)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**400** | If path parameters are invalid or resource does not exist. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_milestones**
> List[MilestoneWithEmbed] list_milestones(workspace_id, act_as_admin=act_as_admin, request_body=request_body)

Retrieve multiple milestones by their IDs

Returns a list of milestones resolved for the provided IDs.<br/>
Does not fail if any of the requested milestones is not found or not accessible - instead it returns corresponding error-object instead of an entity-object.<br/>
Guarantees that the size and order of the returned list matches the requested IDs.<br/>Requirements:<br/>- auth-client scopes: "workspace:read"<br/>- user permission: "read" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.milestone_with_embed import MilestoneWithEmbed
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
    api_instance = airfocus_client.MilestonesApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed milestones.
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Retrieve multiple milestones by their IDs
        api_response = api_instance.list_milestones(workspace_id, act_as_admin=act_as_admin, request_body=request_body)
        print("The response of MilestonesApi->list_milestones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MilestonesApi->list_milestones: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed milestones. | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **request_body** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[MilestoneWithEmbed]**](MilestoneWithEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | If payload is invalid. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_milestone**
> MilestoneWithEmbed patch_milestone(workspace_id, milestone_id, json_patch_operation, act_as_admin=act_as_admin)

Patch an existing milestone

Returns the whole updated milestone with its sanitised data.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.json_patch_operation import JsonPatchOperation
from airfocus_client.models.milestone_with_embed import MilestoneWithEmbed
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
    api_instance = airfocus_client.MilestonesApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed milestones.
    milestone_id = 'milestone_id_example' # str | 
    json_patch_operation = [airfocus_client.JsonPatchOperation()] # List[JsonPatchOperation] | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Patch an existing milestone
        api_response = api_instance.patch_milestone(workspace_id, milestone_id, json_patch_operation, act_as_admin=act_as_admin)
        print("The response of MilestonesApi->patch_milestone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MilestonesApi->patch_milestone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed milestones. | 
 **milestone_id** | **str**|  | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**MilestoneWithEmbed**](MilestoneWithEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | If path parameters are invalid or payload is invalid or resource does not exist. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_milestone**
> MilestoneWithEmbed retrieve_milestone(workspace_id, milestone_id, act_as_admin=act_as_admin)

Retrieve a single milestone by its ID

Returns found milestone.<br/>Requirements:<br/>- auth-client scopes: "workspace:read"<br/>- user permission: "read" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.milestone_with_embed import MilestoneWithEmbed
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
    api_instance = airfocus_client.MilestonesApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed milestones.
    milestone_id = 'milestone_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Retrieve a single milestone by its ID
        api_response = api_instance.retrieve_milestone(workspace_id, milestone_id, act_as_admin=act_as_admin)
        print("The response of MilestonesApi->retrieve_milestone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MilestonesApi->retrieve_milestone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed milestones. | 
 **milestone_id** | **str**|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**MilestoneWithEmbed**](MilestoneWithEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | If path parameters are invalid or payload is invalid or resource does not exist. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_milestones**
> MilestoneWithEmbedPage search_milestones(workspace_id, act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, body=body)

Retrieve or search milestones

Returns all milestones or searches milestones by query. Always returns only milestones which are accessible by the current user.<br/>Requirements:<br/>- auth-client scopes: "workspace:read"<br/>- user permission: "read" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.milestone_with_embed_page import MilestoneWithEmbedPage
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
    api_instance = airfocus_client.MilestonesApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed milestones.
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    offset = 0 # int | How many elements to skip. (optional) (default to 0)
    limit = 1000 # int | How many elements to return. (optional) (default to 1000)
    var_from = 0 # int | From which element the page should start. (optional) (default to 0)
    to = 56 # int | At which element the page should end (excluding it). (optional)
    body = None # object |  (optional)

    try:
        # Retrieve or search milestones
        api_response = api_instance.search_milestones(workspace_id, act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, body=body)
        print("The response of MilestonesApi->search_milestones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MilestonesApi->search_milestones: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed milestones. | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **offset** | **int**| How many elements to skip. | [optional] [default to 0]
 **limit** | **int**| How many elements to return. | [optional] [default to 1000]
 **var_from** | **int**| From which element the page should start. | [optional] [default to 0]
 **to** | **int**| At which element the page should end (excluding it). | [optional] 
 **body** | **object**|  | [optional] 

### Return type

[**MilestoneWithEmbedPage**](MilestoneWithEmbedPage.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | If payload is invalid. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_milestone**
> MilestoneWithEmbed update_milestone(workspace_id, milestone_id, update_milestone_request, act_as_admin=act_as_admin)

Update an existing milestone

Returns updated milestone with its sanitised data.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.milestone_with_embed import MilestoneWithEmbed
from airfocus_client.models.update_milestone_request import UpdateMilestoneRequest
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
    api_instance = airfocus_client.MilestonesApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed milestones.
    milestone_id = 'milestone_id_example' # str | 
    update_milestone_request = airfocus_client.UpdateMilestoneRequest() # UpdateMilestoneRequest | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Update an existing milestone
        api_response = api_instance.update_milestone(workspace_id, milestone_id, update_milestone_request, act_as_admin=act_as_admin)
        print("The response of MilestonesApi->update_milestone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MilestonesApi->update_milestone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed milestones. | 
 **milestone_id** | **str**|  | 
 **update_milestone_request** | [**UpdateMilestoneRequest**](UpdateMilestoneRequest.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**MilestoneWithEmbed**](MilestoneWithEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | If path parameters are invalid or payload is invalid or resource does not exist. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

