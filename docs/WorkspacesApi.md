# airfocus_client.WorkspacesApi

All URIs are relative to *https://app.airfocus.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_workspaces**](WorkspacesApi.md#bulk_workspaces) | **POST** /api/workspaces/bulk | Perform multiple operations with workspaces
[**count_workspaces**](WorkspacesApi.md#count_workspaces) | **GET** /api/workspaces/count | Count workspaces in the current team.
[**create_workspace**](WorkspacesApi.md#create_workspace) | **POST** /api/workspaces | Create a new workspace
[**delete_workspace**](WorkspacesApi.md#delete_workspace) | **DELETE** /api/workspaces/{workspaceId} | Delete an existing workspace
[**duplicate_workspace**](WorkspacesApi.md#duplicate_workspace) | **POST** /api/workspaces/{workspaceId}/duplicate | Duplicate workspace with all its items and apps.
[**list_workspaces**](WorkspacesApi.md#list_workspaces) | **POST** /api/workspaces/list | Retrieve multiple workspaces by their IDs
[**patch_workspace**](WorkspacesApi.md#patch_workspace) | **PATCH** /api/workspaces/{workspaceId} | Patch an existing workspace
[**retrieve_workspace**](WorkspacesApi.md#retrieve_workspace) | **GET** /api/workspaces/{workspaceId} | Retrieve a single workspace by its ID
[**search_workspaces**](WorkspacesApi.md#search_workspaces) | **POST** /api/workspaces/search | Retrieve or search workspaces
[**set_workspace_statuses**](WorkspacesApi.md#set_workspace_statuses) | **POST** /api/workspaces/{workspaceId}/statuses | Configure workspace statuses.
[**update_workspace**](WorkspacesApi.md#update_workspace) | **PUT** /api/workspaces/{workspaceId} | Update an existing workspace
[**update_workspace_permissions**](WorkspacesApi.md#update_workspace_permissions) | **POST** /api/workspaces/{workspaceId}/permissions | Update workspace permissions.


# **bulk_workspaces**
> List[WorkspaceWithWorkspaceEmbed] bulk_workspaces(act_as_admin=act_as_admin, workspace_bulk_action=workspace_bulk_action)

Perform multiple operations with workspaces

Accepts a list of create/update/patch/delete operations (see the request model for more details).<br/>
Each operation can target a single or multiple workspaces.<br/>
Returns a list of results for each input operation including errors.<br/>
Guarantees that the size and order of the returned results matches the input list of operations.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.workspace_bulk_action import WorkspaceBulkAction
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
    api_instance = airfocus_client.WorkspacesApi(api_client)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    workspace_bulk_action = [airfocus_client.WorkspaceBulkAction()] # List[WorkspaceBulkAction] |  (optional)

    try:
        # Perform multiple operations with workspaces
        api_response = api_instance.bulk_workspaces(act_as_admin=act_as_admin, workspace_bulk_action=workspace_bulk_action)
        print("The response of WorkspacesApi->bulk_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->bulk_workspaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **workspace_bulk_action** | [**List[WorkspaceBulkAction]**](WorkspaceBulkAction.md)|  | [optional] 

### Return type

[**List[WorkspaceWithWorkspaceEmbed]**](WorkspaceWithWorkspaceEmbed.md)

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

# **count_workspaces**
> int count_workspaces(act_as_admin=act_as_admin)

Count workspaces in the current team.

Returns the total counter number.<br/>Requirements:<br/>- auth-client scopes: "workspace:read"<br/>- user permission: "read" or higher

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
    api_instance = airfocus_client.WorkspacesApi(api_client)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Count workspaces in the current team.
        api_response = api_instance.count_workspaces(act_as_admin=act_as_admin)
        print("The response of WorkspacesApi->count_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->count_workspaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

**int**

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
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workspace**
> WorkspaceWithWorkspaceEmbed create_workspace(create_workspace_request, act_as_admin=act_as_admin)

Create a new workspace

Returns newly created workspace with its sanitised data.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.create_workspace_request import CreateWorkspaceRequest
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
    api_instance = airfocus_client.WorkspacesApi(api_client)
    create_workspace_request = airfocus_client.CreateWorkspaceRequest() # CreateWorkspaceRequest | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Create a new workspace
        api_response = api_instance.create_workspace(create_workspace_request, act_as_admin=act_as_admin)
        print("The response of WorkspacesApi->create_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->create_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_workspace_request** | [**CreateWorkspaceRequest**](CreateWorkspaceRequest.md)|  | 
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
**400** | If payload is invalid. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace**
> delete_workspace(workspace_id, act_as_admin=act_as_admin)

Delete an existing workspace

Returns empty result if the workspace was successfully deleted.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

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
    api_instance = airfocus_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Delete an existing workspace
        api_instance.delete_workspace(workspace_id, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling WorkspacesApi->delete_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
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

# **duplicate_workspace**
> WorkspaceWithWorkspaceEmbed duplicate_workspace(workspace_id, workspace_duplicate_request, act_as_admin=act_as_admin)

Duplicate workspace with all its items and apps.

Returns the newly created workspace with embedded data.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.workspace_duplicate_request import WorkspaceDuplicateRequest
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
    api_instance = airfocus_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    workspace_duplicate_request = airfocus_client.WorkspaceDuplicateRequest() # WorkspaceDuplicateRequest | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Duplicate workspace with all its items and apps.
        api_response = api_instance.duplicate_workspace(workspace_id, workspace_duplicate_request, act_as_admin=act_as_admin)
        print("The response of WorkspacesApi->duplicate_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->duplicate_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **workspace_duplicate_request** | [**WorkspaceDuplicateRequest**](WorkspaceDuplicateRequest.md)|  | 
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
**400** | If path parameters are invalid or payload is invalid or resource does not exist. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workspaces**
> List[WorkspaceWithWorkspaceEmbed] list_workspaces(act_as_admin=act_as_admin, request_body=request_body)

Retrieve multiple workspaces by their IDs

Returns a list of workspaces resolved for the provided IDs.<br/>
Does not fail if any of the requested workspaces is not found or not accessible - instead it returns corresponding error-object instead of an entity-object.<br/>
Guarantees that the size and order of the returned list matches the requested IDs.<br/>Requirements:<br/>- auth-client scopes: "workspace:read"<br/>- user permission: "read" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
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
    api_instance = airfocus_client.WorkspacesApi(api_client)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Retrieve multiple workspaces by their IDs
        api_response = api_instance.list_workspaces(act_as_admin=act_as_admin, request_body=request_body)
        print("The response of WorkspacesApi->list_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->list_workspaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **request_body** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[WorkspaceWithWorkspaceEmbed]**](WorkspaceWithWorkspaceEmbed.md)

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

# **patch_workspace**
> WorkspaceWithWorkspaceEmbed patch_workspace(workspace_id, json_patch_operation, act_as_admin=act_as_admin)

Patch an existing workspace

Returns the whole updated workspace with its sanitised data.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.json_patch_operation import JsonPatchOperation
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
    api_instance = airfocus_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    json_patch_operation = [airfocus_client.JsonPatchOperation()] # List[JsonPatchOperation] | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Patch an existing workspace
        api_response = api_instance.patch_workspace(workspace_id, json_patch_operation, act_as_admin=act_as_admin)
        print("The response of WorkspacesApi->patch_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->patch_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)|  | 
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
**400** | If path parameters are invalid or payload is invalid or resource does not exist. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_workspace**
> WorkspaceWithWorkspaceEmbed retrieve_workspace(workspace_id, act_as_admin=act_as_admin)

Retrieve a single workspace by its ID

Returns found workspace.<br/>Requirements:<br/>- auth-client scopes: "workspace:read"<br/>- user permission: "read" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
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
    api_instance = airfocus_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Retrieve a single workspace by its ID
        api_response = api_instance.retrieve_workspace(workspace_id, act_as_admin=act_as_admin)
        print("The response of WorkspacesApi->retrieve_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->retrieve_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**WorkspaceWithWorkspaceEmbed**](WorkspaceWithWorkspaceEmbed.md)

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

# **search_workspaces**
> WorkspaceWithWorkspaceSearchEmbedPage search_workspaces(act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, workspace_search_query=workspace_search_query)

Retrieve or search workspaces

Returns all workspaces or searches workspaces by query. Always returns only workspaces which are accessible by the current user.<br/>Requirements:<br/>- auth-client scopes: "workspace:read"<br/>- user permission: "read" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.workspace_search_query import WorkspaceSearchQuery
from airfocus_client.models.workspace_with_workspace_search_embed_page import WorkspaceWithWorkspaceSearchEmbedPage
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
    api_instance = airfocus_client.WorkspacesApi(api_client)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    offset = 0 # int | How many elements to skip. (optional) (default to 0)
    limit = 1000 # int | How many elements to return. (optional) (default to 1000)
    var_from = 0 # int | From which element the page should start. (optional) (default to 0)
    to = 56 # int | At which element the page should end (excluding it). (optional)
    workspace_search_query = airfocus_client.WorkspaceSearchQuery() # WorkspaceSearchQuery |  (optional)

    try:
        # Retrieve or search workspaces
        api_response = api_instance.search_workspaces(act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, workspace_search_query=workspace_search_query)
        print("The response of WorkspacesApi->search_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->search_workspaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **offset** | **int**| How many elements to skip. | [optional] [default to 0]
 **limit** | **int**| How many elements to return. | [optional] [default to 1000]
 **var_from** | **int**| From which element the page should start. | [optional] [default to 0]
 **to** | **int**| At which element the page should end (excluding it). | [optional] 
 **workspace_search_query** | [**WorkspaceSearchQuery**](WorkspaceSearchQuery.md)|  | [optional] 

### Return type

[**WorkspaceWithWorkspaceSearchEmbedPage**](WorkspaceWithWorkspaceSearchEmbedPage.md)

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

# **set_workspace_statuses**
> set_workspace_statuses(workspace_id, set_workspace_statuses_request, act_as_admin=act_as_admin)

Configure workspace statuses.

Sets statuses (all at once) for the specified workspace.
New statuses in the list will be added to the database, missing statuses will be removed from the database, all other statuses will be updated.
Each workspace must have at least one status in each category: 'draft', 'active', 'closed'<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.set_workspace_statuses_request import SetWorkspaceStatusesRequest
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
    api_instance = airfocus_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    set_workspace_statuses_request = airfocus_client.SetWorkspaceStatusesRequest() # SetWorkspaceStatusesRequest | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Configure workspace statuses.
        api_instance.set_workspace_statuses(workspace_id, set_workspace_statuses_request, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling WorkspacesApi->set_workspace_statuses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **set_workspace_statuses_request** | [**SetWorkspaceStatusesRequest**](SetWorkspaceStatusesRequest.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

void (empty response body)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**400** | If path parameters are invalid or payload is invalid or resource does not exist. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workspace**
> WorkspaceWithWorkspaceEmbed update_workspace(workspace_id, update_workspace_request, act_as_admin=act_as_admin)

Update an existing workspace

Returns updated workspace with its sanitised data.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.update_workspace_request import UpdateWorkspaceRequest
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
    api_instance = airfocus_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    update_workspace_request = airfocus_client.UpdateWorkspaceRequest() # UpdateWorkspaceRequest | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Update an existing workspace
        api_response = api_instance.update_workspace(workspace_id, update_workspace_request, act_as_admin=act_as_admin)
        print("The response of WorkspacesApi->update_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->update_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **update_workspace_request** | [**UpdateWorkspaceRequest**](UpdateWorkspaceRequest.md)|  | 
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
**400** | If path parameters are invalid or payload is invalid or resource does not exist. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workspace_permissions**
> Permission update_workspace_permissions(workspace_id, workspace_permissions_update_request, act_as_admin=act_as_admin)

Update workspace permissions.

Returns effective permission for the current user.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.permission import Permission
from airfocus_client.models.workspace_permissions_update_request import WorkspacePermissionsUpdateRequest
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
    api_instance = airfocus_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    workspace_permissions_update_request = airfocus_client.WorkspacePermissionsUpdateRequest() # WorkspacePermissionsUpdateRequest | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Update workspace permissions.
        api_response = api_instance.update_workspace_permissions(workspace_id, workspace_permissions_update_request, act_as_admin=act_as_admin)
        print("The response of WorkspacesApi->update_workspace_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->update_workspace_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **workspace_permissions_update_request** | [**WorkspacePermissionsUpdateRequest**](WorkspacePermissionsUpdateRequest.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**Permission**](Permission.md)

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

