# airfocus_client.ItemsRelationsApi

All URIs are relative to *https://app.airfocus.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_item_relations**](ItemsRelationsApi.md#bulk_item_relations) | **POST** /api/workspaces/item-relations/bulk | Perform multiple operations with item-relations
[**create_item_relation**](ItemsRelationsApi.md#create_item_relation) | **POST** /api/workspaces/item-relations | Create a new item-relation
[**delete_item_relation**](ItemsRelationsApi.md#delete_item_relation) | **DELETE** /api/workspaces/item-relations/{itemRelationId} | Delete an existing item-relation
[**list_item_relations**](ItemsRelationsApi.md#list_item_relations) | **POST** /api/workspaces/item-relations/list | Retrieve multiple item-relations by their IDs
[**patch_item_relation**](ItemsRelationsApi.md#patch_item_relation) | **PATCH** /api/workspaces/item-relations/{itemRelationId} | Patch an existing item-relation
[**retrieve_item_relation**](ItemsRelationsApi.md#retrieve_item_relation) | **GET** /api/workspaces/item-relations/{itemRelationId} | Retrieve a single item-relation by its ID
[**search_item_relations**](ItemsRelationsApi.md#search_item_relations) | **POST** /api/workspaces/item-relations/search | Retrieve or search item-relations
[**update_item_relation**](ItemsRelationsApi.md#update_item_relation) | **PUT** /api/workspaces/item-relations/{itemRelationId} | Update an existing item-relation


# **bulk_item_relations**
> List[ItemRelationWithEmbed] bulk_item_relations(act_as_admin=act_as_admin, item_relation_bulk_action=item_relation_bulk_action)

Perform multiple operations with item-relations

Accepts a list of create/update/patch/delete operations (see the request model for more details).<br/>
Each operation can target a single or multiple item-relations.<br/>
Returns a list of results for each input operation including errors.<br/>
Guarantees that the size and order of the returned results matches the input list of operations.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_relation_bulk_action import ItemRelationBulkAction
from airfocus_client.models.item_relation_with_embed import ItemRelationWithEmbed
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
    api_instance = airfocus_client.ItemsRelationsApi(api_client)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    item_relation_bulk_action = [airfocus_client.ItemRelationBulkAction()] # List[ItemRelationBulkAction] |  (optional)

    try:
        # Perform multiple operations with item-relations
        api_response = api_instance.bulk_item_relations(act_as_admin=act_as_admin, item_relation_bulk_action=item_relation_bulk_action)
        print("The response of ItemsRelationsApi->bulk_item_relations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsRelationsApi->bulk_item_relations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **item_relation_bulk_action** | [**List[ItemRelationBulkAction]**](ItemRelationBulkAction.md)|  | [optional] 

### Return type

[**List[ItemRelationWithEmbed]**](ItemRelationWithEmbed.md)

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

# **create_item_relation**
> ItemRelationWithEmbed create_item_relation(item_relation_create_request, act_as_admin=act_as_admin)

Create a new item-relation

Returns newly created item-relation with its sanitised data.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_relation_create_request import ItemRelationCreateRequest
from airfocus_client.models.item_relation_with_embed import ItemRelationWithEmbed
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
    api_instance = airfocus_client.ItemsRelationsApi(api_client)
    item_relation_create_request = airfocus_client.ItemRelationCreateRequest() # ItemRelationCreateRequest | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Create a new item-relation
        api_response = api_instance.create_item_relation(item_relation_create_request, act_as_admin=act_as_admin)
        print("The response of ItemsRelationsApi->create_item_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsRelationsApi->create_item_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_relation_create_request** | [**ItemRelationCreateRequest**](ItemRelationCreateRequest.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemRelationWithEmbed**](ItemRelationWithEmbed.md)

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

# **delete_item_relation**
> delete_item_relation(item_relation_id, act_as_admin=act_as_admin)

Delete an existing item-relation

Returns empty result if the item-relation was successfully deleted.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

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
    api_instance = airfocus_client.ItemsRelationsApi(api_client)
    item_relation_id = 'item_relation_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Delete an existing item-relation
        api_instance.delete_item_relation(item_relation_id, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling ItemsRelationsApi->delete_item_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_relation_id** | **str**|  | 
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

# **list_item_relations**
> List[ItemRelationWithEmbed] list_item_relations(act_as_admin=act_as_admin, request_body=request_body)

Retrieve multiple item-relations by their IDs

Returns a list of item-relations resolved for the provided IDs.<br/>
Does not fail if any of the requested item-relations is not found or not accessible - instead it returns corresponding error-object instead of an entity-object.<br/>
Guarantees that the size and order of the returned list matches the requested IDs.<br/>Requirements:<br/>- auth-client scopes: "workspace:read"<br/>- user permission: "read" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_relation_with_embed import ItemRelationWithEmbed
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
    api_instance = airfocus_client.ItemsRelationsApi(api_client)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Retrieve multiple item-relations by their IDs
        api_response = api_instance.list_item_relations(act_as_admin=act_as_admin, request_body=request_body)
        print("The response of ItemsRelationsApi->list_item_relations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsRelationsApi->list_item_relations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **request_body** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[ItemRelationWithEmbed]**](ItemRelationWithEmbed.md)

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

# **patch_item_relation**
> ItemRelationWithEmbed patch_item_relation(item_relation_id, json_patch_operation, act_as_admin=act_as_admin)

Patch an existing item-relation

Returns the whole updated item-relation with its sanitised data.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_relation_with_embed import ItemRelationWithEmbed
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
    api_instance = airfocus_client.ItemsRelationsApi(api_client)
    item_relation_id = 'item_relation_id_example' # str | 
    json_patch_operation = [airfocus_client.JsonPatchOperation()] # List[JsonPatchOperation] | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Patch an existing item-relation
        api_response = api_instance.patch_item_relation(item_relation_id, json_patch_operation, act_as_admin=act_as_admin)
        print("The response of ItemsRelationsApi->patch_item_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsRelationsApi->patch_item_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_relation_id** | **str**|  | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemRelationWithEmbed**](ItemRelationWithEmbed.md)

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

# **retrieve_item_relation**
> ItemRelationWithEmbed retrieve_item_relation(item_relation_id, act_as_admin=act_as_admin)

Retrieve a single item-relation by its ID

Returns found item-relation.<br/>Requirements:<br/>- auth-client scopes: "workspace:read"<br/>- user permission: "read" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_relation_with_embed import ItemRelationWithEmbed
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
    api_instance = airfocus_client.ItemsRelationsApi(api_client)
    item_relation_id = 'item_relation_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Retrieve a single item-relation by its ID
        api_response = api_instance.retrieve_item_relation(item_relation_id, act_as_admin=act_as_admin)
        print("The response of ItemsRelationsApi->retrieve_item_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsRelationsApi->retrieve_item_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_relation_id** | **str**|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemRelationWithEmbed**](ItemRelationWithEmbed.md)

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

# **search_item_relations**
> ItemRelationWithEmbedPage search_item_relations(act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, item_relation_search_query=item_relation_search_query)

Retrieve or search item-relations

Returns all item-relations or searches item-relations by query. Always returns only item-relations which are accessible by the current user.<br/>Requirements:<br/>- auth-client scopes: "workspace:read"<br/>- user permission: "read" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_relation_search_query import ItemRelationSearchQuery
from airfocus_client.models.item_relation_with_embed_page import ItemRelationWithEmbedPage
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
    api_instance = airfocus_client.ItemsRelationsApi(api_client)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    offset = 0 # int | How many elements to skip. (optional) (default to 0)
    limit = 1000 # int | How many elements to return. (optional) (default to 1000)
    var_from = 0 # int | From which element the page should start. (optional) (default to 0)
    to = 56 # int | At which element the page should end (excluding it). (optional)
    item_relation_search_query = airfocus_client.ItemRelationSearchQuery() # ItemRelationSearchQuery |  (optional)

    try:
        # Retrieve or search item-relations
        api_response = api_instance.search_item_relations(act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, item_relation_search_query=item_relation_search_query)
        print("The response of ItemsRelationsApi->search_item_relations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsRelationsApi->search_item_relations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **offset** | **int**| How many elements to skip. | [optional] [default to 0]
 **limit** | **int**| How many elements to return. | [optional] [default to 1000]
 **var_from** | **int**| From which element the page should start. | [optional] [default to 0]
 **to** | **int**| At which element the page should end (excluding it). | [optional] 
 **item_relation_search_query** | [**ItemRelationSearchQuery**](ItemRelationSearchQuery.md)|  | [optional] 

### Return type

[**ItemRelationWithEmbedPage**](ItemRelationWithEmbedPage.md)

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

# **update_item_relation**
> ItemRelationWithEmbed update_item_relation(item_relation_id, item_relation_update_request, act_as_admin=act_as_admin)

Update an existing item-relation

Returns updated item-relation with its sanitised data.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_relation_update_request import ItemRelationUpdateRequest
from airfocus_client.models.item_relation_with_embed import ItemRelationWithEmbed
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
    api_instance = airfocus_client.ItemsRelationsApi(api_client)
    item_relation_id = 'item_relation_id_example' # str | 
    item_relation_update_request = airfocus_client.ItemRelationUpdateRequest() # ItemRelationUpdateRequest | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Update an existing item-relation
        api_response = api_instance.update_item_relation(item_relation_id, item_relation_update_request, act_as_admin=act_as_admin)
        print("The response of ItemsRelationsApi->update_item_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsRelationsApi->update_item_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_relation_id** | **str**|  | 
 **item_relation_update_request** | [**ItemRelationUpdateRequest**](ItemRelationUpdateRequest.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemRelationWithEmbed**](ItemRelationWithEmbed.md)

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

