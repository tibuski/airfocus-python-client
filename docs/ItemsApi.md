# airfocus_client.ItemsApi

All URIs are relative to *https://app.airfocus.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_items**](ItemsApi.md#bulk_items) | **POST** /api/workspaces/{workspaceId}/items/bulk | Perform multiple operations with items
[**copy_items**](ItemsApi.md#copy_items) | **POST** /api/workspaces/items/copy | Copy specified items.
[**create_item**](ItemsApi.md#create_item) | **POST** /api/workspaces/{workspaceId}/items | Create a new item
[**delete_item**](ItemsApi.md#delete_item) | **DELETE** /api/workspaces/{workspaceId}/items/{itemId} | Delete an existing item
[**list_items**](ItemsApi.md#list_items) | **POST** /api/workspaces/{workspaceId}/items/list | Retrieve multiple items by their IDs
[**list_items_global**](ItemsApi.md#list_items_global) | **POST** /api/workspaces/items/list | Retrieve items from any workspace by specified IDs.
[**move_items**](ItemsApi.md#move_items) | **POST** /api/workspaces/items/move | Move specified items from one workspace to another.
[**patch_item**](ItemsApi.md#patch_item) | **PATCH** /api/workspaces/{workspaceId}/items/{itemId} | Patch an existing item
[**reset_item_colors**](ItemsApi.md#reset_item_colors) | **POST** /api/workspaces/{workspaceId}/items/reset-colors | Reset colors of all items in the specified workspace.
[**retrieve_item**](ItemsApi.md#retrieve_item) | **GET** /api/workspaces/{workspaceId}/items/{itemId} | Retrieve a single item by its ID
[**retrieve_item_by_alias**](ItemsApi.md#retrieve_item_by_alias) | **GET** /api/workspaces/items/alias/{aliasValue} | Retrieve a single item by its alias (e.g. &#39;DEV-123&#39;).
[**search_items**](ItemsApi.md#search_items) | **POST** /api/workspaces/{workspaceId}/items/search | Retrieve or search items
[**unwatch_items**](ItemsApi.md#unwatch_items) | **POST** /api/workspaces/{workspaceId}/items/unwatch | Remove watching status of the current user for the specified items.
[**update_item**](ItemsApi.md#update_item) | **PUT** /api/workspaces/{workspaceId}/items/{itemId} | Update an existing item
[**watch_items**](ItemsApi.md#watch_items) | **POST** /api/workspaces/{workspaceId}/items/watch | Set current user as a watcher of the specified items.


# **bulk_items**
> List[ItemWithItemEmbed] bulk_items(workspace_id, act_as_admin=act_as_admin, item_bulk_action=item_bulk_action)

Perform multiple operations with items

Accepts a list of create/update/patch/delete operations (see the request model for more details).<br/>
Each operation can target a single or multiple items.<br/>
Returns a list of results for each input operation including errors.<br/>
Guarantees that the size and order of the returned results matches the input list of operations.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_bulk_action import ItemBulkAction
from airfocus_client.models.item_with_item_embed import ItemWithItemEmbed
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
    api_instance = airfocus_client.ItemsApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed items.
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    item_bulk_action = [airfocus_client.ItemBulkAction()] # List[ItemBulkAction] |  (optional)

    try:
        # Perform multiple operations with items
        api_response = api_instance.bulk_items(workspace_id, act_as_admin=act_as_admin, item_bulk_action=item_bulk_action)
        print("The response of ItemsApi->bulk_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->bulk_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed items. | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **item_bulk_action** | [**List[ItemBulkAction]**](ItemBulkAction.md)|  | [optional] 

### Return type

[**List[ItemWithItemEmbed]**](ItemWithItemEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/json+markdown
 - **Accept**: application/json, application/json+markdown

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | If payload is invalid. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_items**
> List[str] copy_items(source_workspace_id, target_workspace_id, act_as_admin=act_as_admin, request_body=request_body)

Copy specified items.

Returns ids of newly copied items, with order of the returned ids matching the order of requested source items. Returns Not Found if either of the specified source items does not exist.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

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
    api_instance = airfocus_client.ItemsApi(api_client)
    source_workspace_id = 'source_workspace_id_example' # str | Workspace of the source items to be copied.
    target_workspace_id = 'target_workspace_id_example' # str | Target workspace for the newly copied items.
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    request_body = ['request_body_example'] # List[str] | List of item IDs to be copied. (optional)

    try:
        # Copy specified items.
        api_response = api_instance.copy_items(source_workspace_id, target_workspace_id, act_as_admin=act_as_admin, request_body=request_body)
        print("The response of ItemsApi->copy_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->copy_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_workspace_id** | **str**| Workspace of the source items to be copied. | 
 **target_workspace_id** | **str**| Target workspace for the newly copied items. | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **request_body** | [**List[str]**](str.md)| List of item IDs to be copied. | [optional] 

### Return type

**List[str]**

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of newly created item IDs. |  -  |
**400** | If payload is invalid or one of the specified source items or the target workspace does not exist. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_item**
> ItemWithItemEmbed create_item(workspace_id, create_item_request, act_as_admin=act_as_admin)

Create a new item

Returns newly created item with its sanitised data.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.create_item_request import CreateItemRequest
from airfocus_client.models.item_with_item_embed import ItemWithItemEmbed
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
    api_instance = airfocus_client.ItemsApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed items.
    create_item_request = airfocus_client.CreateItemRequest() # CreateItemRequest | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Create a new item
        api_response = api_instance.create_item(workspace_id, create_item_request, act_as_admin=act_as_admin)
        print("The response of ItemsApi->create_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->create_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed items. | 
 **create_item_request** | [**CreateItemRequest**](CreateItemRequest.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemWithItemEmbed**](ItemWithItemEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/json+markdown
 - **Accept**: application/json, application/json+markdown

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | If payload is invalid. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item**
> delete_item(workspace_id, item_id, act_as_admin=act_as_admin)

Delete an existing item

Returns empty result if the item was successfully deleted.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

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
    api_instance = airfocus_client.ItemsApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed items.
    item_id = 'item_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Delete an existing item
        api_instance.delete_item(workspace_id, item_id, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling ItemsApi->delete_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed items. | 
 **item_id** | **str**|  | 
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

# **list_items**
> List[ItemWithItemEmbed] list_items(workspace_id, act_as_admin=act_as_admin, request_body=request_body)

Retrieve multiple items by their IDs

Returns a list of items resolved for the provided IDs.<br/>
Does not fail if any of the requested items is not found or not accessible - instead it returns corresponding error-object instead of an entity-object.<br/>
Guarantees that the size and order of the returned list matches the requested IDs.<br/>Requirements:<br/>- auth-client scopes: "workspace:read"<br/>- user permission: "read" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_with_item_embed import ItemWithItemEmbed
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
    api_instance = airfocus_client.ItemsApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed items.
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Retrieve multiple items by their IDs
        api_response = api_instance.list_items(workspace_id, act_as_admin=act_as_admin, request_body=request_body)
        print("The response of ItemsApi->list_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->list_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed items. | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **request_body** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[ItemWithItemEmbed]**](ItemWithItemEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json+markdown

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | If payload is invalid. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_items_global**
> List[ItemWithItemEmbed] list_items_global(act_as_admin=act_as_admin, request_body=request_body)

Retrieve items from any workspace by specified IDs.

Returns an array of results, where each element is either a found item with its embeddings, or null if there no item with such ID.<br/>Requirements:<br/>- auth-client scopes: "workspace:read"<br/>- user permission: "read" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_with_item_embed import ItemWithItemEmbed
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
    api_instance = airfocus_client.ItemsApi(api_client)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    request_body = ['request_body_example'] # List[str] | List of item IDs to be retrieve from any workspace in the team. (optional)

    try:
        # Retrieve items from any workspace by specified IDs.
        api_response = api_instance.list_items_global(act_as_admin=act_as_admin, request_body=request_body)
        print("The response of ItemsApi->list_items_global:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->list_items_global: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **request_body** | [**List[str]**](str.md)| List of item IDs to be retrieve from any workspace in the team. | [optional] 

### Return type

[**List[ItemWithItemEmbed]**](ItemWithItemEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json+markdown

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | If payload is invalid or resource does not exist. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_items**
> List[str] move_items(source_workspace_id, target_workspace_id, act_as_admin=act_as_admin, request_body=request_body)

Move specified items from one workspace to another.

Returns ids of newly created items in the target workspace, with order of the returned ids matching the order of requested source items. Returns Not Found if either of the specified source items does not exist.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

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
    api_instance = airfocus_client.ItemsApi(api_client)
    source_workspace_id = 'source_workspace_id_example' # str | Workspace of the source items to be moved.
    target_workspace_id = 'target_workspace_id_example' # str | New target workspace for the moved items.
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    request_body = ['request_body_example'] # List[str] | List of item IDs to be moved. (optional)

    try:
        # Move specified items from one workspace to another.
        api_response = api_instance.move_items(source_workspace_id, target_workspace_id, act_as_admin=act_as_admin, request_body=request_body)
        print("The response of ItemsApi->move_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->move_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_workspace_id** | **str**| Workspace of the source items to be moved. | 
 **target_workspace_id** | **str**| New target workspace for the moved items. | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **request_body** | [**List[str]**](str.md)| List of item IDs to be moved. | [optional] 

### Return type

**List[str]**

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of newly created item IDs. |  -  |
**400** | If payload is invalid or one of the specified source items or the target workspace does not exist. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_item**
> ItemWithItemEmbed patch_item(workspace_id, item_id, json_patch_operation, act_as_admin=act_as_admin)

Patch an existing item

Returns the whole updated item with its sanitised data.<br>Note: also supports patching description as a Markdown string.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_with_item_embed import ItemWithItemEmbed
from airfocus_client.models.json_patch_operation import JsonPatchOperation
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
    api_instance = airfocus_client.ItemsApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed items.
    item_id = 'item_id_example' # str | 
    json_patch_operation = [airfocus_client.JsonPatchOperation()] # List[JsonPatchOperation] | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Patch an existing item
        api_response = api_instance.patch_item(workspace_id, item_id, json_patch_operation, act_as_admin=act_as_admin)
        print("The response of ItemsApi->patch_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->patch_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed items. | 
 **item_id** | **str**|  | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemWithItemEmbed**](ItemWithItemEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json+markdown

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | If path parameters are invalid or payload is invalid or resource does not exist. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_item_colors**
> reset_item_colors(workspace_id, act_as_admin=act_as_admin)

Reset colors of all items in the specified workspace.

Sets all items to match the color configured in the workspace settings if it's configured, otherwise resets each item with a randomly generated color from the available color palette.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

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
    api_instance = airfocus_client.ItemsApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed items.
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Reset colors of all items in the specified workspace.
        api_instance.reset_item_colors(workspace_id, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling ItemsApi->reset_item_colors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed items. | 
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
**400** | If target workspace does not exist. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_item**
> ItemWithItemEmbed retrieve_item(workspace_id, item_id, act_as_admin=act_as_admin)

Retrieve a single item by its ID

Returns found item.<br/>Requirements:<br/>- auth-client scopes: "workspace:read"<br/>- user permission: "read" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_with_item_embed import ItemWithItemEmbed
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
    api_instance = airfocus_client.ItemsApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed items.
    item_id = 'item_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Retrieve a single item by its ID
        api_response = api_instance.retrieve_item(workspace_id, item_id, act_as_admin=act_as_admin)
        print("The response of ItemsApi->retrieve_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->retrieve_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed items. | 
 **item_id** | **str**|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemWithItemEmbed**](ItemWithItemEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+markdown

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | If path parameters are invalid or payload is invalid or resource does not exist. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_item_by_alias**
> ItemWithItemEmbed retrieve_item_by_alias(alias_value, act_as_admin=act_as_admin)

Retrieve a single item by its alias (e.g. 'DEV-123').

Returns found item.<br/>Requirements:<br/>- auth-client scopes: "workspace:read"<br/>- user permission: "read" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_with_item_embed import ItemWithItemEmbed
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
    api_instance = airfocus_client.ItemsApi(api_client)
    alias_value = 'DEV-123' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Retrieve a single item by its alias (e.g. 'DEV-123').
        api_response = api_instance.retrieve_item_by_alias(alias_value, act_as_admin=act_as_admin)
        print("The response of ItemsApi->retrieve_item_by_alias:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->retrieve_item_by_alias: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias_value** | **str**|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemWithItemEmbed**](ItemWithItemEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+markdown

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | If path parameters are invalid or resource does not exist. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_items**
> ItemWithItemEmbedPage search_items(workspace_id, act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, item_search_query=item_search_query)

Retrieve or search items

Returns all items or searches items by query. Always returns only items which are accessible by the current user.<br/>Requirements:<br/>- auth-client scopes: "workspace:read"<br/>- user permission: "read" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_search_query import ItemSearchQuery
from airfocus_client.models.item_with_item_embed_page import ItemWithItemEmbedPage
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
    api_instance = airfocus_client.ItemsApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed items.
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    offset = 0 # int | How many elements to skip. (optional) (default to 0)
    limit = 1000 # int | How many elements to return. (optional) (default to 1000)
    var_from = 0 # int | From which element the page should start. (optional) (default to 0)
    to = 56 # int | At which element the page should end (excluding it). (optional)
    item_search_query = airfocus_client.ItemSearchQuery() # ItemSearchQuery |  (optional)

    try:
        # Retrieve or search items
        api_response = api_instance.search_items(workspace_id, act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, item_search_query=item_search_query)
        print("The response of ItemsApi->search_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->search_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed items. | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **offset** | **int**| How many elements to skip. | [optional] [default to 0]
 **limit** | **int**| How many elements to return. | [optional] [default to 1000]
 **var_from** | **int**| From which element the page should start. | [optional] [default to 0]
 **to** | **int**| At which element the page should end (excluding it). | [optional] 
 **item_search_query** | [**ItemSearchQuery**](ItemSearchQuery.md)|  | [optional] 

### Return type

[**ItemWithItemEmbedPage**](ItemWithItemEmbedPage.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json+markdown

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | If payload is invalid. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unwatch_items**
> unwatch_items(workspace_id, act_as_admin=act_as_admin, request_body=request_body)

Remove watching status of the current user for the specified items.

Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

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
    api_instance = airfocus_client.ItemsApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed items.
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    request_body = ['request_body_example'] # List[str] | List of item IDs to unwatch. (optional)

    try:
        # Remove watching status of the current user for the specified items.
        api_instance.unwatch_items(workspace_id, act_as_admin=act_as_admin, request_body=request_body)
    except Exception as e:
        print("Exception when calling ItemsApi->unwatch_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed items. | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **request_body** | [**List[str]**](str.md)| List of item IDs to unwatch. | [optional] 

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
**400** | If payload is invalid or resource does not exist. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item**
> ItemWithItemEmbed update_item(workspace_id, item_id, update_item_request, act_as_admin=act_as_admin)

Update an existing item

Returns updated item with its sanitised data.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_with_item_embed import ItemWithItemEmbed
from airfocus_client.models.update_item_request import UpdateItemRequest
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
    api_instance = airfocus_client.ItemsApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed items.
    item_id = 'item_id_example' # str | 
    update_item_request = airfocus_client.UpdateItemRequest() # UpdateItemRequest | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Update an existing item
        api_response = api_instance.update_item(workspace_id, item_id, update_item_request, act_as_admin=act_as_admin)
        print("The response of ItemsApi->update_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->update_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed items. | 
 **item_id** | **str**|  | 
 **update_item_request** | [**UpdateItemRequest**](UpdateItemRequest.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemWithItemEmbed**](ItemWithItemEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/json+markdown
 - **Accept**: application/json, application/json+markdown

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | If path parameters are invalid or payload is invalid or resource does not exist. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_items**
> watch_items(workspace_id, act_as_admin=act_as_admin, request_body=request_body)

Set current user as a watcher of the specified items.

Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

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
    api_instance = airfocus_client.ItemsApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed items.
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    request_body = ['request_body_example'] # List[str] | List of item IDs to watch. (optional)

    try:
        # Set current user as a watcher of the specified items.
        api_instance.watch_items(workspace_id, act_as_admin=act_as_admin, request_body=request_body)
    except Exception as e:
        print("Exception when calling ItemsApi->watch_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed items. | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **request_body** | [**List[str]**](str.md)| List of item IDs to watch. | [optional] 

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
**400** | If payload is invalid or resource does not exist. |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not have the required permission, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

