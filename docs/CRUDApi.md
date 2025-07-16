# airfocus_client.CRUDApi

All URIs are relative to *https://app.airfocus.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_comments**](CRUDApi.md#bulk_comments) | **POST** /api/workspaces/{workspaceId}/comments/bulk | Perform multiple operations with comments
[**bulk_item_attachments**](CRUDApi.md#bulk_item_attachments) | **POST** /api/workspaces/{workspaceId}/attachments/bulk | Perform multiple operations with attachments
[**bulk_item_links**](CRUDApi.md#bulk_item_links) | **POST** /api/workspaces/{workspaceId}/links/bulk | Perform multiple operations with item-links
[**bulk_item_relations**](CRUDApi.md#bulk_item_relations) | **POST** /api/workspaces/item-relations/bulk | Perform multiple operations with item-relations
[**bulk_items**](CRUDApi.md#bulk_items) | **POST** /api/workspaces/{workspaceId}/items/bulk | Perform multiple operations with items
[**bulk_milestones**](CRUDApi.md#bulk_milestones) | **POST** /api/workspaces/{workspaceId}/milestones/bulk | Perform multiple operations with milestones
[**bulk_workspace_groups**](CRUDApi.md#bulk_workspace_groups) | **POST** /api/workspaces/groups/bulk | Perform multiple operations with workspace groups
[**bulk_workspace_relations**](CRUDApi.md#bulk_workspace_relations) | **POST** /api/workspaces/workspace-relations/bulk | Perform multiple operations with workspace relations
[**bulk_workspaces**](CRUDApi.md#bulk_workspaces) | **POST** /api/workspaces/bulk | Perform multiple operations with workspaces
[**create_comment**](CRUDApi.md#create_comment) | **POST** /api/workspaces/{workspaceId}/comments | Create a new comment
[**create_item**](CRUDApi.md#create_item) | **POST** /api/workspaces/{workspaceId}/items | Create a new item
[**create_item_attachment**](CRUDApi.md#create_item_attachment) | **POST** /api/workspaces/{workspaceId}/attachments | Create a new attachment
[**create_item_link**](CRUDApi.md#create_item_link) | **POST** /api/workspaces/{workspaceId}/links | Create a new item-link
[**create_item_relation**](CRUDApi.md#create_item_relation) | **POST** /api/workspaces/item-relations | Create a new item-relation
[**create_milestone**](CRUDApi.md#create_milestone) | **POST** /api/workspaces/{workspaceId}/milestones | Create a new milestone
[**create_workspace**](CRUDApi.md#create_workspace) | **POST** /api/workspaces | Create a new workspace
[**create_workspace_group**](CRUDApi.md#create_workspace_group) | **POST** /api/workspaces/groups | Create a new workspace group
[**create_workspace_relation**](CRUDApi.md#create_workspace_relation) | **POST** /api/workspaces/workspace-relations | Create a new workspace relation
[**delete_comment**](CRUDApi.md#delete_comment) | **DELETE** /api/workspaces/{workspaceId}/comments/{commentId} | Delete an existing comment
[**delete_item**](CRUDApi.md#delete_item) | **DELETE** /api/workspaces/{workspaceId}/items/{itemId} | Delete an existing item
[**delete_item_attachment**](CRUDApi.md#delete_item_attachment) | **DELETE** /api/workspaces/{workspaceId}/attachments/{itemAttachmentId} | Delete an existing attachment
[**delete_item_link**](CRUDApi.md#delete_item_link) | **DELETE** /api/workspaces/{workspaceId}/links/{itemLinkId} | Delete an existing item-link
[**delete_item_relation**](CRUDApi.md#delete_item_relation) | **DELETE** /api/workspaces/item-relations/{itemRelationId} | Delete an existing item-relation
[**delete_milestone**](CRUDApi.md#delete_milestone) | **DELETE** /api/workspaces/{workspaceId}/milestones/{milestoneId} | Delete an existing milestone
[**delete_workspace**](CRUDApi.md#delete_workspace) | **DELETE** /api/workspaces/{workspaceId} | Delete an existing workspace
[**delete_workspace_group**](CRUDApi.md#delete_workspace_group) | **DELETE** /api/workspaces/groups/{workspaceGroupId} | Delete an existing workspace group
[**delete_workspace_relation**](CRUDApi.md#delete_workspace_relation) | **DELETE** /api/workspaces/workspace-relations/{workspaceRelationId} | Delete an existing workspace relation
[**list_comments**](CRUDApi.md#list_comments) | **POST** /api/workspaces/{workspaceId}/comments/list | Retrieve multiple comments by their IDs
[**list_item_attachments**](CRUDApi.md#list_item_attachments) | **POST** /api/workspaces/{workspaceId}/attachments/list | Retrieve multiple attachments by their IDs
[**list_item_links**](CRUDApi.md#list_item_links) | **POST** /api/workspaces/{workspaceId}/links/list | Retrieve multiple item-links by their IDs
[**list_item_relations**](CRUDApi.md#list_item_relations) | **POST** /api/workspaces/item-relations/list | Retrieve multiple item-relations by their IDs
[**list_items**](CRUDApi.md#list_items) | **POST** /api/workspaces/{workspaceId}/items/list | Retrieve multiple items by their IDs
[**list_milestones**](CRUDApi.md#list_milestones) | **POST** /api/workspaces/{workspaceId}/milestones/list | Retrieve multiple milestones by their IDs
[**list_workspace_groups**](CRUDApi.md#list_workspace_groups) | **POST** /api/workspaces/groups/list | Retrieve multiple workspace groups by their IDs
[**list_workspace_relations**](CRUDApi.md#list_workspace_relations) | **POST** /api/workspaces/workspace-relations/list | Retrieve multiple workspace relations by their IDs
[**list_workspaces**](CRUDApi.md#list_workspaces) | **POST** /api/workspaces/list | Retrieve multiple workspaces by their IDs
[**patch_comment**](CRUDApi.md#patch_comment) | **PATCH** /api/workspaces/{workspaceId}/comments/{commentId} | Patch an existing comment
[**patch_item**](CRUDApi.md#patch_item) | **PATCH** /api/workspaces/{workspaceId}/items/{itemId} | Patch an existing item
[**patch_item_attachment**](CRUDApi.md#patch_item_attachment) | **PATCH** /api/workspaces/{workspaceId}/attachments/{itemAttachmentId} | Patch an existing attachment
[**patch_item_link**](CRUDApi.md#patch_item_link) | **PATCH** /api/workspaces/{workspaceId}/links/{itemLinkId} | Patch an existing item-link
[**patch_item_relation**](CRUDApi.md#patch_item_relation) | **PATCH** /api/workspaces/item-relations/{itemRelationId} | Patch an existing item-relation
[**patch_milestone**](CRUDApi.md#patch_milestone) | **PATCH** /api/workspaces/{workspaceId}/milestones/{milestoneId} | Patch an existing milestone
[**patch_workspace**](CRUDApi.md#patch_workspace) | **PATCH** /api/workspaces/{workspaceId} | Patch an existing workspace
[**patch_workspace_group**](CRUDApi.md#patch_workspace_group) | **PATCH** /api/workspaces/groups/{workspaceGroupId} | Patch an existing workspace group
[**patch_workspace_relation**](CRUDApi.md#patch_workspace_relation) | **PATCH** /api/workspaces/workspace-relations/{workspaceRelationId} | Patch an existing workspace relation
[**retrieve_comment**](CRUDApi.md#retrieve_comment) | **GET** /api/workspaces/{workspaceId}/comments/{commentId} | Retrieve a single comment by its ID
[**retrieve_item**](CRUDApi.md#retrieve_item) | **GET** /api/workspaces/{workspaceId}/items/{itemId} | Retrieve a single item by its ID
[**retrieve_item_attachment**](CRUDApi.md#retrieve_item_attachment) | **GET** /api/workspaces/{workspaceId}/attachments/{itemAttachmentId} | Retrieve a single attachment by its ID
[**retrieve_item_link**](CRUDApi.md#retrieve_item_link) | **GET** /api/workspaces/{workspaceId}/links/{itemLinkId} | Retrieve a single item-link by its ID
[**retrieve_item_relation**](CRUDApi.md#retrieve_item_relation) | **GET** /api/workspaces/item-relations/{itemRelationId} | Retrieve a single item-relation by its ID
[**retrieve_milestone**](CRUDApi.md#retrieve_milestone) | **GET** /api/workspaces/{workspaceId}/milestones/{milestoneId} | Retrieve a single milestone by its ID
[**retrieve_workspace**](CRUDApi.md#retrieve_workspace) | **GET** /api/workspaces/{workspaceId} | Retrieve a single workspace by its ID
[**retrieve_workspace_group**](CRUDApi.md#retrieve_workspace_group) | **GET** /api/workspaces/groups/{workspaceGroupId} | Retrieve a single workspace group by its ID
[**retrieve_workspace_relation**](CRUDApi.md#retrieve_workspace_relation) | **GET** /api/workspaces/workspace-relations/{workspaceRelationId} | Retrieve a single workspace relation by its ID
[**search_comments**](CRUDApi.md#search_comments) | **POST** /api/workspaces/{workspaceId}/comments/search | Retrieve or search comments
[**search_item_attachments**](CRUDApi.md#search_item_attachments) | **POST** /api/workspaces/{workspaceId}/attachments/search | Retrieve or search attachments
[**search_item_links**](CRUDApi.md#search_item_links) | **POST** /api/workspaces/{workspaceId}/links/search | Retrieve or search item-links
[**search_item_relations**](CRUDApi.md#search_item_relations) | **POST** /api/workspaces/item-relations/search | Retrieve or search item-relations
[**search_items**](CRUDApi.md#search_items) | **POST** /api/workspaces/{workspaceId}/items/search | Retrieve or search items
[**search_milestones**](CRUDApi.md#search_milestones) | **POST** /api/workspaces/{workspaceId}/milestones/search | Retrieve or search milestones
[**search_workspace_groups**](CRUDApi.md#search_workspace_groups) | **POST** /api/workspaces/groups/search | Retrieve or search workspace groups
[**search_workspace_relations**](CRUDApi.md#search_workspace_relations) | **POST** /api/workspaces/workspace-relations/search | Retrieve or search workspace relations
[**search_workspaces**](CRUDApi.md#search_workspaces) | **POST** /api/workspaces/search | Retrieve or search workspaces
[**update_comment**](CRUDApi.md#update_comment) | **PUT** /api/workspaces/{workspaceId}/comments/{commentId} | Update an existing comment
[**update_item**](CRUDApi.md#update_item) | **PUT** /api/workspaces/{workspaceId}/items/{itemId} | Update an existing item
[**update_item_attachment**](CRUDApi.md#update_item_attachment) | **PUT** /api/workspaces/{workspaceId}/attachments/{itemAttachmentId} | Update an existing attachment
[**update_item_link**](CRUDApi.md#update_item_link) | **PUT** /api/workspaces/{workspaceId}/links/{itemLinkId} | Update an existing item-link
[**update_item_relation**](CRUDApi.md#update_item_relation) | **PUT** /api/workspaces/item-relations/{itemRelationId} | Update an existing item-relation
[**update_milestone**](CRUDApi.md#update_milestone) | **PUT** /api/workspaces/{workspaceId}/milestones/{milestoneId} | Update an existing milestone
[**update_workspace**](CRUDApi.md#update_workspace) | **PUT** /api/workspaces/{workspaceId} | Update an existing workspace
[**update_workspace_group**](CRUDApi.md#update_workspace_group) | **PUT** /api/workspaces/groups/{workspaceGroupId} | Update an existing workspace group
[**update_workspace_relation**](CRUDApi.md#update_workspace_relation) | **PUT** /api/workspaces/workspace-relations/{workspaceRelationId} | Update an existing workspace relation


# **bulk_comments**
> List[ItemCommentWithItemCommentEmbed] bulk_comments(workspace_id, act_as_admin=act_as_admin, comment_bulk_action=comment_bulk_action)

Perform multiple operations with comments

Accepts a list of create/update/patch/delete operations (see the request model for more details).<br/>
Each operations can target a single or multiple comments.<br/>
Returns a list of results for each input operation including errors.<br/>
Guarantees that the size and order of the returned results matches the input list of operations.<br/>Requirements:<br/>  - auth-client scopes: "workspace"<br/>  - user permission: "write" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.comment_bulk_action import CommentBulkAction
from airfocus_client.models.item_comment_with_item_comment_embed import ItemCommentWithItemCommentEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    comment_bulk_action = [airfocus_client.CommentBulkAction()] # List[CommentBulkAction] |  (optional)

    try:
        # Perform multiple operations with comments
        api_response = api_instance.bulk_comments(workspace_id, act_as_admin=act_as_admin, comment_bulk_action=comment_bulk_action)
        print("The response of CRUDApi->bulk_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->bulk_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **comment_bulk_action** | [**List[CommentBulkAction]**](CommentBulkAction.md)|  | [optional] 

### Return type

[**List[ItemCommentWithItemCommentEmbed]**](ItemCommentWithItemCommentEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/json+markdown
 - **Accept**: application/json, application/json+markdown

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_item_attachments**
> List[ItemAttachmentWithEmbed] bulk_item_attachments(workspace_id, act_as_admin=act_as_admin, item_attachment_bulk_action=item_attachment_bulk_action)

Perform multiple operations with attachments

Accepts a list of create/update/patch/delete operations (see the request model for more details).<br/>
Each operations can target a single or multiple attachments.<br/>
Returns a list of results for each input operation including errors.<br/>
Guarantees that the size and order of the returned results matches the input list of operations.<br/>Requirements:<br/>  - auth-client scopes: "workspace"<br/>  - user permission: "write" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_attachment_bulk_action import ItemAttachmentBulkAction
from airfocus_client.models.item_attachment_with_embed import ItemAttachmentWithEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed attachments.
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    item_attachment_bulk_action = [airfocus_client.ItemAttachmentBulkAction()] # List[ItemAttachmentBulkAction] |  (optional)

    try:
        # Perform multiple operations with attachments
        api_response = api_instance.bulk_item_attachments(workspace_id, act_as_admin=act_as_admin, item_attachment_bulk_action=item_attachment_bulk_action)
        print("The response of CRUDApi->bulk_item_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->bulk_item_attachments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed attachments. | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **item_attachment_bulk_action** | [**List[ItemAttachmentBulkAction]**](ItemAttachmentBulkAction.md)|  | [optional] 

### Return type

[**List[ItemAttachmentWithEmbed]**](ItemAttachmentWithEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_item_links**
> List[ItemLinkWithItemLinkEmbed] bulk_item_links(workspace_id, act_as_admin=act_as_admin, item_link_bulk_action=item_link_bulk_action)

Perform multiple operations with item-links

Accepts a list of create/update/patch/delete operations (see the request model for more details).<br/>
Each operation can target a single or multiple item-links.<br/>
Returns a list of results for each input operation including errors.<br/>
Guarantees that the size and order of the returned results matches the input list of operations.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_link_bulk_action import ItemLinkBulkAction
from airfocus_client.models.item_link_with_item_link_embed import ItemLinkWithItemLinkEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed item-links.
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    item_link_bulk_action = [airfocus_client.ItemLinkBulkAction()] # List[ItemLinkBulkAction] |  (optional)

    try:
        # Perform multiple operations with item-links
        api_response = api_instance.bulk_item_links(workspace_id, act_as_admin=act_as_admin, item_link_bulk_action=item_link_bulk_action)
        print("The response of CRUDApi->bulk_item_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->bulk_item_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed item-links. | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **item_link_bulk_action** | [**List[ItemLinkBulkAction]**](ItemLinkBulkAction.md)|  | [optional] 

### Return type

[**List[ItemLinkWithItemLinkEmbed]**](ItemLinkWithItemLinkEmbed.md)

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
    api_instance = airfocus_client.CRUDApi(api_client)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    item_relation_bulk_action = [airfocus_client.ItemRelationBulkAction()] # List[ItemRelationBulkAction] |  (optional)

    try:
        # Perform multiple operations with item-relations
        api_response = api_instance.bulk_item_relations(act_as_admin=act_as_admin, item_relation_bulk_action=item_relation_bulk_action)
        print("The response of CRUDApi->bulk_item_relations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->bulk_item_relations: %s\n" % e)
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed items.
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    item_bulk_action = [airfocus_client.ItemBulkAction()] # List[ItemBulkAction] |  (optional)

    try:
        # Perform multiple operations with items
        api_response = api_instance.bulk_items(workspace_id, act_as_admin=act_as_admin, item_bulk_action=item_bulk_action)
        print("The response of CRUDApi->bulk_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->bulk_items: %s\n" % e)
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed milestones.
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    milestone_bulk_action = [airfocus_client.MilestoneBulkAction()] # List[MilestoneBulkAction] |  (optional)

    try:
        # Perform multiple operations with milestones
        api_response = api_instance.bulk_milestones(workspace_id, act_as_admin=act_as_admin, milestone_bulk_action=milestone_bulk_action)
        print("The response of CRUDApi->bulk_milestones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->bulk_milestones: %s\n" % e)
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

# **bulk_workspace_groups**
> List[WorkspaceGroupWithWorkspaceGroupEmbed] bulk_workspace_groups(act_as_admin=act_as_admin, workspace_group_bulk_action=workspace_group_bulk_action)

Perform multiple operations with workspace groups

Accepts a list of create/update/patch/delete operations (see the request model for more details).<br/>
Each operations can target a single or multiple workspace groups.<br/>
Returns a list of results for each input operation including errors.<br/>
Guarantees that the size and order of the returned results matches the input list of operations.<br/>Requirements:<br/>  - auth-client scopes: "workspace"<br/>  - user permission: "write" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.workspace_group_bulk_action import WorkspaceGroupBulkAction
from airfocus_client.models.workspace_group_with_workspace_group_embed import WorkspaceGroupWithWorkspaceGroupEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    workspace_group_bulk_action = [airfocus_client.WorkspaceGroupBulkAction()] # List[WorkspaceGroupBulkAction] |  (optional)

    try:
        # Perform multiple operations with workspace groups
        api_response = api_instance.bulk_workspace_groups(act_as_admin=act_as_admin, workspace_group_bulk_action=workspace_group_bulk_action)
        print("The response of CRUDApi->bulk_workspace_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->bulk_workspace_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **workspace_group_bulk_action** | [**List[WorkspaceGroupBulkAction]**](WorkspaceGroupBulkAction.md)|  | [optional] 

### Return type

[**List[WorkspaceGroupWithWorkspaceGroupEmbed]**](WorkspaceGroupWithWorkspaceGroupEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_workspace_relations**
> List[WorkspaceRelationWithEmbed] bulk_workspace_relations(act_as_admin=act_as_admin, workspace_relation_bulk_action=workspace_relation_bulk_action)

Perform multiple operations with workspace relations

Accepts a list of create/update/patch/delete operations (see the request model for more details).<br/>
Each operations can target a single or multiple workspace relations.<br/>
Returns a list of results for each input operation including errors.<br/>
Guarantees that the size and order of the returned results matches the input list of operations.<br/>Requirements:<br/>  - auth-client scopes: "workspace"<br/>  - user permission: "write" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.workspace_relation_bulk_action import WorkspaceRelationBulkAction
from airfocus_client.models.workspace_relation_with_embed import WorkspaceRelationWithEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    workspace_relation_bulk_action = [airfocus_client.WorkspaceRelationBulkAction()] # List[WorkspaceRelationBulkAction] |  (optional)

    try:
        # Perform multiple operations with workspace relations
        api_response = api_instance.bulk_workspace_relations(act_as_admin=act_as_admin, workspace_relation_bulk_action=workspace_relation_bulk_action)
        print("The response of CRUDApi->bulk_workspace_relations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->bulk_workspace_relations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **workspace_relation_bulk_action** | [**List[WorkspaceRelationBulkAction]**](WorkspaceRelationBulkAction.md)|  | [optional] 

### Return type

[**List[WorkspaceRelationWithEmbed]**](WorkspaceRelationWithEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    api_instance = airfocus_client.CRUDApi(api_client)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    workspace_bulk_action = [airfocus_client.WorkspaceBulkAction()] # List[WorkspaceBulkAction] |  (optional)

    try:
        # Perform multiple operations with workspaces
        api_response = api_instance.bulk_workspaces(act_as_admin=act_as_admin, workspace_bulk_action=workspace_bulk_action)
        print("The response of CRUDApi->bulk_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->bulk_workspaces: %s\n" % e)
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

# **create_comment**
> ItemCommentWithItemCommentEmbed create_comment(workspace_id, item_comment, act_as_admin=act_as_admin)

Create a new comment

Returns newly created comment with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: "workspace"<br/>  - user permission: "write" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_comment import ItemComment
from airfocus_client.models.item_comment_with_item_comment_embed import ItemCommentWithItemCommentEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    item_comment = airfocus_client.ItemComment() # ItemComment | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Create a new comment
        api_response = api_instance.create_comment(workspace_id, item_comment, act_as_admin=act_as_admin)
        print("The response of CRUDApi->create_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->create_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **item_comment** | [**ItemComment**](ItemComment.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemCommentWithItemCommentEmbed**](ItemCommentWithItemCommentEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/json+markdown
 - **Accept**: application/json, application/json+markdown

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed items.
    create_item_request = airfocus_client.CreateItemRequest() # CreateItemRequest | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Create a new item
        api_response = api_instance.create_item(workspace_id, create_item_request, act_as_admin=act_as_admin)
        print("The response of CRUDApi->create_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->create_item: %s\n" % e)
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

# **create_item_attachment**
> ItemAttachmentWithEmbed create_item_attachment(workspace_id, item_attachment, act_as_admin=act_as_admin)

Create a new attachment

Returns newly created attachment with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: "workspace"<br/>  - user permission: "write" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_attachment import ItemAttachment
from airfocus_client.models.item_attachment_with_embed import ItemAttachmentWithEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed attachments.
    item_attachment = airfocus_client.ItemAttachment() # ItemAttachment | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Create a new attachment
        api_response = api_instance.create_item_attachment(workspace_id, item_attachment, act_as_admin=act_as_admin)
        print("The response of CRUDApi->create_item_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->create_item_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed attachments. | 
 **item_attachment** | [**ItemAttachment**](ItemAttachment.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemAttachmentWithEmbed**](ItemAttachmentWithEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_item_link**
> ItemLinkWithItemLinkEmbed create_item_link(workspace_id, create_item_link_request, act_as_admin=act_as_admin)

Create a new item-link

Returns newly created item-link with its sanitised data.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.create_item_link_request import CreateItemLinkRequest
from airfocus_client.models.item_link_with_item_link_embed import ItemLinkWithItemLinkEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed item-links.
    create_item_link_request = airfocus_client.CreateItemLinkRequest() # CreateItemLinkRequest | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Create a new item-link
        api_response = api_instance.create_item_link(workspace_id, create_item_link_request, act_as_admin=act_as_admin)
        print("The response of CRUDApi->create_item_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->create_item_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed item-links. | 
 **create_item_link_request** | [**CreateItemLinkRequest**](CreateItemLinkRequest.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemLinkWithItemLinkEmbed**](ItemLinkWithItemLinkEmbed.md)

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
    api_instance = airfocus_client.CRUDApi(api_client)
    item_relation_create_request = airfocus_client.ItemRelationCreateRequest() # ItemRelationCreateRequest | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Create a new item-relation
        api_response = api_instance.create_item_relation(item_relation_create_request, act_as_admin=act_as_admin)
        print("The response of CRUDApi->create_item_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->create_item_relation: %s\n" % e)
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed milestones.
    create_milestone_request = airfocus_client.CreateMilestoneRequest() # CreateMilestoneRequest | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Create a new milestone
        api_response = api_instance.create_milestone(workspace_id, create_milestone_request, act_as_admin=act_as_admin)
        print("The response of CRUDApi->create_milestone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->create_milestone: %s\n" % e)
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
    api_instance = airfocus_client.CRUDApi(api_client)
    create_workspace_request = airfocus_client.CreateWorkspaceRequest() # CreateWorkspaceRequest | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Create a new workspace
        api_response = api_instance.create_workspace(create_workspace_request, act_as_admin=act_as_admin)
        print("The response of CRUDApi->create_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->create_workspace: %s\n" % e)
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

# **create_workspace_group**
> WorkspaceGroupWithWorkspaceGroupEmbed create_workspace_group(workspace_group, act_as_admin=act_as_admin)

Create a new workspace group

Returns newly created workspace group with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: "workspace"<br/>  - user permission: "write" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.workspace_group import WorkspaceGroup
from airfocus_client.models.workspace_group_with_workspace_group_embed import WorkspaceGroupWithWorkspaceGroupEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_group = airfocus_client.WorkspaceGroup() # WorkspaceGroup | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Create a new workspace group
        api_response = api_instance.create_workspace_group(workspace_group, act_as_admin=act_as_admin)
        print("The response of CRUDApi->create_workspace_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->create_workspace_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_group** | [**WorkspaceGroup**](WorkspaceGroup.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**WorkspaceGroupWithWorkspaceGroupEmbed**](WorkspaceGroupWithWorkspaceGroupEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workspace_relation**
> WorkspaceRelationWithEmbed create_workspace_relation(workspace_relation, act_as_admin=act_as_admin)

Create a new workspace relation

Returns newly created workspace relation with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: "workspace"<br/>  - user permission: "write" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.workspace_relation import WorkspaceRelation
from airfocus_client.models.workspace_relation_with_embed import WorkspaceRelationWithEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_relation = airfocus_client.WorkspaceRelation() # WorkspaceRelation | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Create a new workspace relation
        api_response = api_instance.create_workspace_relation(workspace_relation, act_as_admin=act_as_admin)
        print("The response of CRUDApi->create_workspace_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->create_workspace_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_relation** | [**WorkspaceRelation**](WorkspaceRelation.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**WorkspaceRelationWithEmbed**](WorkspaceRelationWithEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comment**
> delete_comment(workspace_id, comment_id, act_as_admin=act_as_admin)

Delete an existing comment

Returns empty result if the comment was successfully deleted.<br/>Requirements:<br/>  - auth-client scopes: "workspace"<br/>  - user permission: "write" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Delete an existing comment
        api_instance.delete_comment(workspace_id, comment_id, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling CRUDApi->delete_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **comment_id** | **str**|  | 
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
**0** |  |  -  |

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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed items.
    item_id = 'item_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Delete an existing item
        api_instance.delete_item(workspace_id, item_id, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling CRUDApi->delete_item: %s\n" % e)
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

# **delete_item_attachment**
> delete_item_attachment(workspace_id, item_attachment_id, act_as_admin=act_as_admin)

Delete an existing attachment

Returns empty result if the attachment was successfully deleted.<br/>Requirements:<br/>  - auth-client scopes: "workspace"<br/>  - user permission: "write" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed attachments.
    item_attachment_id = 'item_attachment_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Delete an existing attachment
        api_instance.delete_item_attachment(workspace_id, item_attachment_id, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling CRUDApi->delete_item_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed attachments. | 
 **item_attachment_id** | **str**|  | 
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
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_link**
> delete_item_link(workspace_id, item_link_id, act_as_admin=act_as_admin)

Delete an existing item-link

Returns empty result if the item-link was successfully deleted.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed item-links.
    item_link_id = 'item_link_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Delete an existing item-link
        api_instance.delete_item_link(workspace_id, item_link_id, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling CRUDApi->delete_item_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed item-links. | 
 **item_link_id** | **str**|  | 
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
    api_instance = airfocus_client.CRUDApi(api_client)
    item_relation_id = 'item_relation_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Delete an existing item-relation
        api_instance.delete_item_relation(item_relation_id, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling CRUDApi->delete_item_relation: %s\n" % e)
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed milestones.
    milestone_id = 'milestone_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Delete an existing milestone
        api_instance.delete_milestone(workspace_id, milestone_id, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling CRUDApi->delete_milestone: %s\n" % e)
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Delete an existing workspace
        api_instance.delete_workspace(workspace_id, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling CRUDApi->delete_workspace: %s\n" % e)
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

# **delete_workspace_group**
> delete_workspace_group(workspace_group_id, act_as_admin=act_as_admin)

Delete an existing workspace group

Returns empty result if the workspace group was successfully deleted.<br/>Requirements:<br/>  - auth-client scopes: "workspace"<br/>  - user permission: "write" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_group_id = 'workspace_group_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Delete an existing workspace group
        api_instance.delete_workspace_group(workspace_group_id, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling CRUDApi->delete_workspace_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_group_id** | **str**|  | 
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
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace_relation**
> delete_workspace_relation(workspace_relation_id, act_as_admin=act_as_admin)

Delete an existing workspace relation

Returns empty result if the workspace relation was successfully deleted.<br/>Requirements:<br/>  - auth-client scopes: "workspace"<br/>  - user permission: "write" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_relation_id = 'workspace_relation_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Delete an existing workspace relation
        api_instance.delete_workspace_relation(workspace_relation_id, act_as_admin=act_as_admin)
    except Exception as e:
        print("Exception when calling CRUDApi->delete_workspace_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_relation_id** | **str**|  | 
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
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_comments**
> List[ItemCommentWithItemCommentEmbed] list_comments(workspace_id, act_as_admin=act_as_admin, request_body=request_body)

Retrieve multiple comments by their IDs

Returns a list of comments.<br/>
Returns null for those comments which are not found or not accessible.<br/>
Guarantees that the size and order of the returned list matches the requested IDs.<br/>Requirements:<br/>  - auth-client scopes: "workspace:read"<br/>  - user permission: "read" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_comment_with_item_comment_embed import ItemCommentWithItemCommentEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Retrieve multiple comments by their IDs
        api_response = api_instance.list_comments(workspace_id, act_as_admin=act_as_admin, request_body=request_body)
        print("The response of CRUDApi->list_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->list_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **request_body** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[ItemCommentWithItemCommentEmbed]**](ItemCommentWithItemCommentEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json+markdown

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_item_attachments**
> List[ItemAttachmentWithEmbed] list_item_attachments(workspace_id, act_as_admin=act_as_admin, request_body=request_body)

Retrieve multiple attachments by their IDs

Returns a list of attachments.<br/>
Returns null for those attachments which are not found or not accessible.<br/>
Guarantees that the size and order of the returned list matches the requested IDs.<br/>Requirements:<br/>  - auth-client scopes: "workspace:read"<br/>  - user permission: "read" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_attachment_with_embed import ItemAttachmentWithEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed attachments.
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Retrieve multiple attachments by their IDs
        api_response = api_instance.list_item_attachments(workspace_id, act_as_admin=act_as_admin, request_body=request_body)
        print("The response of CRUDApi->list_item_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->list_item_attachments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed attachments. | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **request_body** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[ItemAttachmentWithEmbed]**](ItemAttachmentWithEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_item_links**
> List[ItemLinkWithItemLinkEmbed] list_item_links(workspace_id, act_as_admin=act_as_admin, request_body=request_body)

Retrieve multiple item-links by their IDs

Returns a list of item-links resolved for the provided IDs.<br/>
Does not fail if any of the requested item-links is not found or not accessible - instead it returns corresponding error-object instead of an entity-object.<br/>
Guarantees that the size and order of the returned list matches the requested IDs.<br/>Requirements:<br/>- auth-client scopes: "workspace:read"<br/>- user permission: "read" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_link_with_item_link_embed import ItemLinkWithItemLinkEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed item-links.
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Retrieve multiple item-links by their IDs
        api_response = api_instance.list_item_links(workspace_id, act_as_admin=act_as_admin, request_body=request_body)
        print("The response of CRUDApi->list_item_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->list_item_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed item-links. | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **request_body** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[ItemLinkWithItemLinkEmbed]**](ItemLinkWithItemLinkEmbed.md)

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
    api_instance = airfocus_client.CRUDApi(api_client)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Retrieve multiple item-relations by their IDs
        api_response = api_instance.list_item_relations(act_as_admin=act_as_admin, request_body=request_body)
        print("The response of CRUDApi->list_item_relations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->list_item_relations: %s\n" % e)
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed items.
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Retrieve multiple items by their IDs
        api_response = api_instance.list_items(workspace_id, act_as_admin=act_as_admin, request_body=request_body)
        print("The response of CRUDApi->list_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->list_items: %s\n" % e)
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed milestones.
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Retrieve multiple milestones by their IDs
        api_response = api_instance.list_milestones(workspace_id, act_as_admin=act_as_admin, request_body=request_body)
        print("The response of CRUDApi->list_milestones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->list_milestones: %s\n" % e)
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

# **list_workspace_groups**
> List[WorkspaceGroupWithWorkspaceGroupEmbed] list_workspace_groups(act_as_admin=act_as_admin, request_body=request_body)

Retrieve multiple workspace groups by their IDs

Returns a list of workspace groups.<br/>
Returns null for those workspace groups which are not found or not accessible.<br/>
Guarantees that the size and order of the returned list matches the requested IDs.<br/>Requirements:<br/>  - auth-client scopes: "workspace:read"<br/>  - user permission: "read" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.workspace_group_with_workspace_group_embed import WorkspaceGroupWithWorkspaceGroupEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Retrieve multiple workspace groups by their IDs
        api_response = api_instance.list_workspace_groups(act_as_admin=act_as_admin, request_body=request_body)
        print("The response of CRUDApi->list_workspace_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->list_workspace_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **request_body** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[WorkspaceGroupWithWorkspaceGroupEmbed]**](WorkspaceGroupWithWorkspaceGroupEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workspace_relations**
> List[WorkspaceRelationWithEmbed] list_workspace_relations(act_as_admin=act_as_admin, request_body=request_body)

Retrieve multiple workspace relations by their IDs

Returns a list of workspace relations.<br/>
Returns null for those workspace relations which are not found or not accessible.<br/>
Guarantees that the size and order of the returned list matches the requested IDs.<br/>Requirements:<br/>  - auth-client scopes: "workspace:read"<br/>  - user permission: "read" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.workspace_relation_with_embed import WorkspaceRelationWithEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Retrieve multiple workspace relations by their IDs
        api_response = api_instance.list_workspace_relations(act_as_admin=act_as_admin, request_body=request_body)
        print("The response of CRUDApi->list_workspace_relations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->list_workspace_relations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **request_body** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[WorkspaceRelationWithEmbed]**](WorkspaceRelationWithEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

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
    api_instance = airfocus_client.CRUDApi(api_client)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Retrieve multiple workspaces by their IDs
        api_response = api_instance.list_workspaces(act_as_admin=act_as_admin, request_body=request_body)
        print("The response of CRUDApi->list_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->list_workspaces: %s\n" % e)
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

# **patch_comment**
> ItemCommentWithItemCommentEmbed patch_comment(workspace_id, comment_id, json_patch_operation, act_as_admin=act_as_admin)

Patch an existing comment

Returns the whole updated comment with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: "workspace"<br/>  - user permission: "write" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_comment_with_item_comment_embed import ItemCommentWithItemCommentEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    json_patch_operation = [airfocus_client.JsonPatchOperation()] # List[JsonPatchOperation] | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Patch an existing comment
        api_response = api_instance.patch_comment(workspace_id, comment_id, json_patch_operation, act_as_admin=act_as_admin)
        print("The response of CRUDApi->patch_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->patch_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemCommentWithItemCommentEmbed**](ItemCommentWithItemCommentEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json+markdown

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed items.
    item_id = 'item_id_example' # str | 
    json_patch_operation = [airfocus_client.JsonPatchOperation()] # List[JsonPatchOperation] | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Patch an existing item
        api_response = api_instance.patch_item(workspace_id, item_id, json_patch_operation, act_as_admin=act_as_admin)
        print("The response of CRUDApi->patch_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->patch_item: %s\n" % e)
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

# **patch_item_attachment**
> ItemAttachmentWithEmbed patch_item_attachment(workspace_id, item_attachment_id, json_patch_operation, act_as_admin=act_as_admin)

Patch an existing attachment

Returns the whole updated attachment with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: "workspace"<br/>  - user permission: "write" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_attachment_with_embed import ItemAttachmentWithEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed attachments.
    item_attachment_id = 'item_attachment_id_example' # str | 
    json_patch_operation = [airfocus_client.JsonPatchOperation()] # List[JsonPatchOperation] | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Patch an existing attachment
        api_response = api_instance.patch_item_attachment(workspace_id, item_attachment_id, json_patch_operation, act_as_admin=act_as_admin)
        print("The response of CRUDApi->patch_item_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->patch_item_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed attachments. | 
 **item_attachment_id** | **str**|  | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemAttachmentWithEmbed**](ItemAttachmentWithEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_item_link**
> ItemLinkWithItemLinkEmbed patch_item_link(workspace_id, item_link_id, json_patch_operation, act_as_admin=act_as_admin)

Patch an existing item-link

Returns the whole updated item-link with its sanitised data.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_link_with_item_link_embed import ItemLinkWithItemLinkEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed item-links.
    item_link_id = 'item_link_id_example' # str | 
    json_patch_operation = [airfocus_client.JsonPatchOperation()] # List[JsonPatchOperation] | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Patch an existing item-link
        api_response = api_instance.patch_item_link(workspace_id, item_link_id, json_patch_operation, act_as_admin=act_as_admin)
        print("The response of CRUDApi->patch_item_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->patch_item_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed item-links. | 
 **item_link_id** | **str**|  | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemLinkWithItemLinkEmbed**](ItemLinkWithItemLinkEmbed.md)

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
    api_instance = airfocus_client.CRUDApi(api_client)
    item_relation_id = 'item_relation_id_example' # str | 
    json_patch_operation = [airfocus_client.JsonPatchOperation()] # List[JsonPatchOperation] | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Patch an existing item-relation
        api_response = api_instance.patch_item_relation(item_relation_id, json_patch_operation, act_as_admin=act_as_admin)
        print("The response of CRUDApi->patch_item_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->patch_item_relation: %s\n" % e)
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed milestones.
    milestone_id = 'milestone_id_example' # str | 
    json_patch_operation = [airfocus_client.JsonPatchOperation()] # List[JsonPatchOperation] | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Patch an existing milestone
        api_response = api_instance.patch_milestone(workspace_id, milestone_id, json_patch_operation, act_as_admin=act_as_admin)
        print("The response of CRUDApi->patch_milestone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->patch_milestone: %s\n" % e)
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    json_patch_operation = [airfocus_client.JsonPatchOperation()] # List[JsonPatchOperation] | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Patch an existing workspace
        api_response = api_instance.patch_workspace(workspace_id, json_patch_operation, act_as_admin=act_as_admin)
        print("The response of CRUDApi->patch_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->patch_workspace: %s\n" % e)
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

# **patch_workspace_group**
> WorkspaceGroupWithWorkspaceGroupEmbed patch_workspace_group(workspace_group_id, json_patch_operation, act_as_admin=act_as_admin)

Patch an existing workspace group

Returns the whole updated workspace group with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: "workspace"<br/>  - user permission: "write" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.json_patch_operation import JsonPatchOperation
from airfocus_client.models.workspace_group_with_workspace_group_embed import WorkspaceGroupWithWorkspaceGroupEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_group_id = 'workspace_group_id_example' # str | 
    json_patch_operation = [airfocus_client.JsonPatchOperation()] # List[JsonPatchOperation] | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Patch an existing workspace group
        api_response = api_instance.patch_workspace_group(workspace_group_id, json_patch_operation, act_as_admin=act_as_admin)
        print("The response of CRUDApi->patch_workspace_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->patch_workspace_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_group_id** | **str**|  | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**WorkspaceGroupWithWorkspaceGroupEmbed**](WorkspaceGroupWithWorkspaceGroupEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_workspace_relation**
> WorkspaceRelationWithEmbed patch_workspace_relation(workspace_relation_id, json_patch_operation, act_as_admin=act_as_admin)

Patch an existing workspace relation

Returns the whole updated workspace relation with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: "workspace"<br/>  - user permission: "write" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.json_patch_operation import JsonPatchOperation
from airfocus_client.models.workspace_relation_with_embed import WorkspaceRelationWithEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_relation_id = 'workspace_relation_id_example' # str | 
    json_patch_operation = [airfocus_client.JsonPatchOperation()] # List[JsonPatchOperation] | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Patch an existing workspace relation
        api_response = api_instance.patch_workspace_relation(workspace_relation_id, json_patch_operation, act_as_admin=act_as_admin)
        print("The response of CRUDApi->patch_workspace_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->patch_workspace_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_relation_id** | **str**|  | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**WorkspaceRelationWithEmbed**](WorkspaceRelationWithEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_comment**
> ItemCommentWithItemCommentEmbed retrieve_comment(workspace_id, comment_id, act_as_admin=act_as_admin)

Retrieve a single comment by its ID

Returns found comment.<br/>Requirements:<br/>  - auth-client scopes: "workspace:read"<br/>  - user permission: "read" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_comment_with_item_comment_embed import ItemCommentWithItemCommentEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Retrieve a single comment by its ID
        api_response = api_instance.retrieve_comment(workspace_id, comment_id, act_as_admin=act_as_admin)
        print("The response of CRUDApi->retrieve_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->retrieve_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemCommentWithItemCommentEmbed**](ItemCommentWithItemCommentEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+markdown

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed items.
    item_id = 'item_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Retrieve a single item by its ID
        api_response = api_instance.retrieve_item(workspace_id, item_id, act_as_admin=act_as_admin)
        print("The response of CRUDApi->retrieve_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->retrieve_item: %s\n" % e)
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

# **retrieve_item_attachment**
> ItemAttachmentWithEmbed retrieve_item_attachment(workspace_id, item_attachment_id, act_as_admin=act_as_admin)

Retrieve a single attachment by its ID

Returns found attachment.<br/>Requirements:<br/>  - auth-client scopes: "workspace:read"<br/>  - user permission: "read" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_attachment_with_embed import ItemAttachmentWithEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed attachments.
    item_attachment_id = 'item_attachment_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Retrieve a single attachment by its ID
        api_response = api_instance.retrieve_item_attachment(workspace_id, item_attachment_id, act_as_admin=act_as_admin)
        print("The response of CRUDApi->retrieve_item_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->retrieve_item_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed attachments. | 
 **item_attachment_id** | **str**|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemAttachmentWithEmbed**](ItemAttachmentWithEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_item_link**
> ItemLinkWithItemLinkEmbed retrieve_item_link(workspace_id, item_link_id, act_as_admin=act_as_admin)

Retrieve a single item-link by its ID

Returns found item-link.<br/>Requirements:<br/>- auth-client scopes: "workspace:read"<br/>- user permission: "read" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_link_with_item_link_embed import ItemLinkWithItemLinkEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed item-links.
    item_link_id = 'item_link_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Retrieve a single item-link by its ID
        api_response = api_instance.retrieve_item_link(workspace_id, item_link_id, act_as_admin=act_as_admin)
        print("The response of CRUDApi->retrieve_item_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->retrieve_item_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed item-links. | 
 **item_link_id** | **str**|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemLinkWithItemLinkEmbed**](ItemLinkWithItemLinkEmbed.md)

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
    api_instance = airfocus_client.CRUDApi(api_client)
    item_relation_id = 'item_relation_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Retrieve a single item-relation by its ID
        api_response = api_instance.retrieve_item_relation(item_relation_id, act_as_admin=act_as_admin)
        print("The response of CRUDApi->retrieve_item_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->retrieve_item_relation: %s\n" % e)
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed milestones.
    milestone_id = 'milestone_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Retrieve a single milestone by its ID
        api_response = api_instance.retrieve_milestone(workspace_id, milestone_id, act_as_admin=act_as_admin)
        print("The response of CRUDApi->retrieve_milestone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->retrieve_milestone: %s\n" % e)
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Retrieve a single workspace by its ID
        api_response = api_instance.retrieve_workspace(workspace_id, act_as_admin=act_as_admin)
        print("The response of CRUDApi->retrieve_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->retrieve_workspace: %s\n" % e)
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

# **retrieve_workspace_group**
> WorkspaceGroupWithWorkspaceGroupEmbed retrieve_workspace_group(workspace_group_id, act_as_admin=act_as_admin)

Retrieve a single workspace group by its ID

Returns found workspace group.<br/>Requirements:<br/>  - auth-client scopes: "workspace:read"<br/>  - user permission: "read" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.workspace_group_with_workspace_group_embed import WorkspaceGroupWithWorkspaceGroupEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_group_id = 'workspace_group_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Retrieve a single workspace group by its ID
        api_response = api_instance.retrieve_workspace_group(workspace_group_id, act_as_admin=act_as_admin)
        print("The response of CRUDApi->retrieve_workspace_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->retrieve_workspace_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_group_id** | **str**|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**WorkspaceGroupWithWorkspaceGroupEmbed**](WorkspaceGroupWithWorkspaceGroupEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_workspace_relation**
> WorkspaceRelationWithEmbed retrieve_workspace_relation(workspace_relation_id, act_as_admin=act_as_admin)

Retrieve a single workspace relation by its ID

Returns found workspace relation.<br/>Requirements:<br/>  - auth-client scopes: "workspace:read"<br/>  - user permission: "read" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.workspace_relation_with_embed import WorkspaceRelationWithEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_relation_id = 'workspace_relation_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Retrieve a single workspace relation by its ID
        api_response = api_instance.retrieve_workspace_relation(workspace_relation_id, act_as_admin=act_as_admin)
        print("The response of CRUDApi->retrieve_workspace_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->retrieve_workspace_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_relation_id** | **str**|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**WorkspaceRelationWithEmbed**](WorkspaceRelationWithEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_comments**
> ItemCommentWithItemCommentEmbedPage search_comments(workspace_id, act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, item_comment_search_query=item_comment_search_query)

Retrieve or search comments

Returns all comments or searches comments by query. Always returns only comments which are accessible by the current user.<br/>Requirements:<br/>  - auth-client scopes: "workspace:read"<br/>  - user permission: "read" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_comment_search_query import ItemCommentSearchQuery
from airfocus_client.models.item_comment_with_item_comment_embed_page import ItemCommentWithItemCommentEmbedPage
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    offset = 0 # int | How many elements to skip. (optional) (default to 0)
    limit = 1000 # int | How many elements to return. (optional) (default to 1000)
    var_from = 0 # int | From which element the page should start. (optional) (default to 0)
    to = 56 # int | At which element the page should end (excluding it). (optional)
    item_comment_search_query = airfocus_client.ItemCommentSearchQuery() # ItemCommentSearchQuery |  (optional)

    try:
        # Retrieve or search comments
        api_response = api_instance.search_comments(workspace_id, act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, item_comment_search_query=item_comment_search_query)
        print("The response of CRUDApi->search_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->search_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **offset** | **int**| How many elements to skip. | [optional] [default to 0]
 **limit** | **int**| How many elements to return. | [optional] [default to 1000]
 **var_from** | **int**| From which element the page should start. | [optional] [default to 0]
 **to** | **int**| At which element the page should end (excluding it). | [optional] 
 **item_comment_search_query** | [**ItemCommentSearchQuery**](ItemCommentSearchQuery.md)|  | [optional] 

### Return type

[**ItemCommentWithItemCommentEmbedPage**](ItemCommentWithItemCommentEmbedPage.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json+markdown

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_item_attachments**
> ItemAttachmentWithEmbedPage search_item_attachments(workspace_id, act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, attachment_search_query=attachment_search_query)

Retrieve or search attachments

Returns all attachments or searches attachments by query. Always returns only attachments which are accessible by the current user.<br/>Requirements:<br/>  - auth-client scopes: "workspace:read"<br/>  - user permission: "read" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.attachment_search_query import AttachmentSearchQuery
from airfocus_client.models.item_attachment_with_embed_page import ItemAttachmentWithEmbedPage
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed attachments.
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    offset = 0 # int | How many elements to skip. (optional) (default to 0)
    limit = 1000 # int | How many elements to return. (optional) (default to 1000)
    var_from = 0 # int | From which element the page should start. (optional) (default to 0)
    to = 56 # int | At which element the page should end (excluding it). (optional)
    attachment_search_query = airfocus_client.AttachmentSearchQuery() # AttachmentSearchQuery |  (optional)

    try:
        # Retrieve or search attachments
        api_response = api_instance.search_item_attachments(workspace_id, act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, attachment_search_query=attachment_search_query)
        print("The response of CRUDApi->search_item_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->search_item_attachments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed attachments. | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **offset** | **int**| How many elements to skip. | [optional] [default to 0]
 **limit** | **int**| How many elements to return. | [optional] [default to 1000]
 **var_from** | **int**| From which element the page should start. | [optional] [default to 0]
 **to** | **int**| At which element the page should end (excluding it). | [optional] 
 **attachment_search_query** | [**AttachmentSearchQuery**](AttachmentSearchQuery.md)|  | [optional] 

### Return type

[**ItemAttachmentWithEmbedPage**](ItemAttachmentWithEmbedPage.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_item_links**
> ItemLinkWithItemLinkEmbedPage search_item_links(workspace_id, act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, item_link_search_query=item_link_search_query)

Retrieve or search item-links

Returns all item-links or searches item-links by query. Always returns only item-links which are accessible by the current user.<br/>Requirements:<br/>- auth-client scopes: "workspace:read"<br/>- user permission: "read" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_link_search_query import ItemLinkSearchQuery
from airfocus_client.models.item_link_with_item_link_embed_page import ItemLinkWithItemLinkEmbedPage
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed item-links.
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    offset = 0 # int | How many elements to skip. (optional) (default to 0)
    limit = 1000 # int | How many elements to return. (optional) (default to 1000)
    var_from = 0 # int | From which element the page should start. (optional) (default to 0)
    to = 56 # int | At which element the page should end (excluding it). (optional)
    item_link_search_query = airfocus_client.ItemLinkSearchQuery() # ItemLinkSearchQuery |  (optional)

    try:
        # Retrieve or search item-links
        api_response = api_instance.search_item_links(workspace_id, act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, item_link_search_query=item_link_search_query)
        print("The response of CRUDApi->search_item_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->search_item_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed item-links. | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **offset** | **int**| How many elements to skip. | [optional] [default to 0]
 **limit** | **int**| How many elements to return. | [optional] [default to 1000]
 **var_from** | **int**| From which element the page should start. | [optional] [default to 0]
 **to** | **int**| At which element the page should end (excluding it). | [optional] 
 **item_link_search_query** | [**ItemLinkSearchQuery**](ItemLinkSearchQuery.md)|  | [optional] 

### Return type

[**ItemLinkWithItemLinkEmbedPage**](ItemLinkWithItemLinkEmbedPage.md)

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
    api_instance = airfocus_client.CRUDApi(api_client)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    offset = 0 # int | How many elements to skip. (optional) (default to 0)
    limit = 1000 # int | How many elements to return. (optional) (default to 1000)
    var_from = 0 # int | From which element the page should start. (optional) (default to 0)
    to = 56 # int | At which element the page should end (excluding it). (optional)
    item_relation_search_query = airfocus_client.ItemRelationSearchQuery() # ItemRelationSearchQuery |  (optional)

    try:
        # Retrieve or search item-relations
        api_response = api_instance.search_item_relations(act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, item_relation_search_query=item_relation_search_query)
        print("The response of CRUDApi->search_item_relations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->search_item_relations: %s\n" % e)
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
    api_instance = airfocus_client.CRUDApi(api_client)
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
        print("The response of CRUDApi->search_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->search_items: %s\n" % e)
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
    api_instance = airfocus_client.CRUDApi(api_client)
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
        print("The response of CRUDApi->search_milestones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->search_milestones: %s\n" % e)
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

# **search_workspace_groups**
> WorkspaceGroupWithWorkspaceGroupSearchEmbedPage search_workspace_groups(act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, body=body)

Retrieve or search workspace groups

Returns all workspace groups or searches workspace groups by query. Always returns only workspace groups which are accessible by the current user.<br/>Requirements:<br/>  - auth-client scopes: "workspace:read"<br/>  - user permission: "read" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.workspace_group_with_workspace_group_search_embed_page import WorkspaceGroupWithWorkspaceGroupSearchEmbedPage
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
    api_instance = airfocus_client.CRUDApi(api_client)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    offset = 0 # int | How many elements to skip. (optional) (default to 0)
    limit = 1000 # int | How many elements to return. (optional) (default to 1000)
    var_from = 0 # int | From which element the page should start. (optional) (default to 0)
    to = 56 # int | At which element the page should end (excluding it). (optional)
    body = None # object |  (optional)

    try:
        # Retrieve or search workspace groups
        api_response = api_instance.search_workspace_groups(act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, body=body)
        print("The response of CRUDApi->search_workspace_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->search_workspace_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **offset** | **int**| How many elements to skip. | [optional] [default to 0]
 **limit** | **int**| How many elements to return. | [optional] [default to 1000]
 **var_from** | **int**| From which element the page should start. | [optional] [default to 0]
 **to** | **int**| At which element the page should end (excluding it). | [optional] 
 **body** | **object**|  | [optional] 

### Return type

[**WorkspaceGroupWithWorkspaceGroupSearchEmbedPage**](WorkspaceGroupWithWorkspaceGroupSearchEmbedPage.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_workspace_relations**
> WorkspaceRelationWithEmbedPage search_workspace_relations(act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, workspace_relation_search_query=workspace_relation_search_query)

Retrieve or search workspace relations

Returns all workspace relations or searches workspace relations by query. Always returns only workspace relations which are accessible by the current user.<br/>Requirements:<br/>  - auth-client scopes: "workspace:read"<br/>  - user permission: "read" or higher<br/>Returns:<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.workspace_relation_search_query import WorkspaceRelationSearchQuery
from airfocus_client.models.workspace_relation_with_embed_page import WorkspaceRelationWithEmbedPage
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
    api_instance = airfocus_client.CRUDApi(api_client)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    offset = 0 # int | How many elements to skip. (optional) (default to 0)
    limit = 1000 # int | How many elements to return. (optional) (default to 1000)
    var_from = 0 # int | From which element the page should start. (optional) (default to 0)
    to = 56 # int | At which element the page should end (excluding it). (optional)
    workspace_relation_search_query = airfocus_client.WorkspaceRelationSearchQuery() # WorkspaceRelationSearchQuery |  (optional)

    try:
        # Retrieve or search workspace relations
        api_response = api_instance.search_workspace_relations(act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, workspace_relation_search_query=workspace_relation_search_query)
        print("The response of CRUDApi->search_workspace_relations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->search_workspace_relations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 
 **offset** | **int**| How many elements to skip. | [optional] [default to 0]
 **limit** | **int**| How many elements to return. | [optional] [default to 1000]
 **var_from** | **int**| From which element the page should start. | [optional] [default to 0]
 **to** | **int**| At which element the page should end (excluding it). | [optional] 
 **workspace_relation_search_query** | [**WorkspaceRelationSearchQuery**](WorkspaceRelationSearchQuery.md)|  | [optional] 

### Return type

[**WorkspaceRelationWithEmbedPage**](WorkspaceRelationWithEmbedPage.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

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
    api_instance = airfocus_client.CRUDApi(api_client)
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)
    offset = 0 # int | How many elements to skip. (optional) (default to 0)
    limit = 1000 # int | How many elements to return. (optional) (default to 1000)
    var_from = 0 # int | From which element the page should start. (optional) (default to 0)
    to = 56 # int | At which element the page should end (excluding it). (optional)
    workspace_search_query = airfocus_client.WorkspaceSearchQuery() # WorkspaceSearchQuery |  (optional)

    try:
        # Retrieve or search workspaces
        api_response = api_instance.search_workspaces(act_as_admin=act_as_admin, offset=offset, limit=limit, var_from=var_from, to=to, workspace_search_query=workspace_search_query)
        print("The response of CRUDApi->search_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->search_workspaces: %s\n" % e)
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

# **update_comment**
> ItemCommentWithItemCommentEmbed update_comment(workspace_id, comment_id, item_comment, act_as_admin=act_as_admin)

Update an existing comment

Returns updated comment with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: "workspace"<br/>  - user permission: "write" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_comment import ItemComment
from airfocus_client.models.item_comment_with_item_comment_embed import ItemCommentWithItemCommentEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    item_comment = airfocus_client.ItemComment() # ItemComment | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Update an existing comment
        api_response = api_instance.update_comment(workspace_id, comment_id, item_comment, act_as_admin=act_as_admin)
        print("The response of CRUDApi->update_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->update_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **item_comment** | [**ItemComment**](ItemComment.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemCommentWithItemCommentEmbed**](ItemCommentWithItemCommentEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/json+markdown
 - **Accept**: application/json, application/json+markdown

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed items.
    item_id = 'item_id_example' # str | 
    update_item_request = airfocus_client.UpdateItemRequest() # UpdateItemRequest | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Update an existing item
        api_response = api_instance.update_item(workspace_id, item_id, update_item_request, act_as_admin=act_as_admin)
        print("The response of CRUDApi->update_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->update_item: %s\n" % e)
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

# **update_item_attachment**
> ItemAttachmentWithEmbed update_item_attachment(workspace_id, item_attachment_id, item_attachment, act_as_admin=act_as_admin)

Update an existing attachment

Returns updated attachment with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: "workspace"<br/>  - user permission: "write" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_attachment import ItemAttachment
from airfocus_client.models.item_attachment_with_embed import ItemAttachmentWithEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed attachments.
    item_attachment_id = 'item_attachment_id_example' # str | 
    item_attachment = airfocus_client.ItemAttachment() # ItemAttachment | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Update an existing attachment
        api_response = api_instance.update_item_attachment(workspace_id, item_attachment_id, item_attachment, act_as_admin=act_as_admin)
        print("The response of CRUDApi->update_item_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->update_item_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed attachments. | 
 **item_attachment_id** | **str**|  | 
 **item_attachment** | [**ItemAttachment**](ItemAttachment.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemAttachmentWithEmbed**](ItemAttachmentWithEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_link**
> ItemLinkWithItemLinkEmbed update_item_link(workspace_id, item_link_id, update_item_link_request, act_as_admin=act_as_admin)

Update an existing item-link

Returns updated item-link with its sanitised data.<br/>Requirements:<br/>- auth-client scopes: "workspace"<br/>- user permission: "write" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.item_link_with_item_link_embed import ItemLinkWithItemLinkEmbed
from airfocus_client.models.update_item_link_request import UpdateItemLinkRequest
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed item-links.
    item_link_id = 'item_link_id_example' # str | 
    update_item_link_request = airfocus_client.UpdateItemLinkRequest() # UpdateItemLinkRequest | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Update an existing item-link
        api_response = api_instance.update_item_link(workspace_id, item_link_id, update_item_link_request, act_as_admin=act_as_admin)
        print("The response of CRUDApi->update_item_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->update_item_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| ID of the workspace which contains the managed item-links. | 
 **item_link_id** | **str**|  | 
 **update_item_link_request** | [**UpdateItemLinkRequest**](UpdateItemLinkRequest.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**ItemLinkWithItemLinkEmbed**](ItemLinkWithItemLinkEmbed.md)

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
    api_instance = airfocus_client.CRUDApi(api_client)
    item_relation_id = 'item_relation_id_example' # str | 
    item_relation_update_request = airfocus_client.ItemRelationUpdateRequest() # ItemRelationUpdateRequest | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Update an existing item-relation
        api_response = api_instance.update_item_relation(item_relation_id, item_relation_update_request, act_as_admin=act_as_admin)
        print("The response of CRUDApi->update_item_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->update_item_relation: %s\n" % e)
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | ID of the workspace which contains the managed milestones.
    milestone_id = 'milestone_id_example' # str | 
    update_milestone_request = airfocus_client.UpdateMilestoneRequest() # UpdateMilestoneRequest | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Update an existing milestone
        api_response = api_instance.update_milestone(workspace_id, milestone_id, update_milestone_request, act_as_admin=act_as_admin)
        print("The response of CRUDApi->update_milestone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->update_milestone: %s\n" % e)
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    update_workspace_request = airfocus_client.UpdateWorkspaceRequest() # UpdateWorkspaceRequest | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Update an existing workspace
        api_response = api_instance.update_workspace(workspace_id, update_workspace_request, act_as_admin=act_as_admin)
        print("The response of CRUDApi->update_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->update_workspace: %s\n" % e)
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

# **update_workspace_group**
> WorkspaceGroupWithWorkspaceGroupEmbed update_workspace_group(workspace_group_id, workspace_group, act_as_admin=act_as_admin)

Update an existing workspace group

Returns updated workspace group with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: "workspace"<br/>  - user permission: "write" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.workspace_group import WorkspaceGroup
from airfocus_client.models.workspace_group_with_workspace_group_embed import WorkspaceGroupWithWorkspaceGroupEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_group_id = 'workspace_group_id_example' # str | 
    workspace_group = airfocus_client.WorkspaceGroup() # WorkspaceGroup | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Update an existing workspace group
        api_response = api_instance.update_workspace_group(workspace_group_id, workspace_group, act_as_admin=act_as_admin)
        print("The response of CRUDApi->update_workspace_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->update_workspace_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_group_id** | **str**|  | 
 **workspace_group** | [**WorkspaceGroup**](WorkspaceGroup.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**WorkspaceGroupWithWorkspaceGroupEmbed**](WorkspaceGroupWithWorkspaceGroupEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workspace_relation**
> WorkspaceRelationWithEmbed update_workspace_relation(workspace_relation_id, workspace_relation, act_as_admin=act_as_admin)

Update an existing workspace relation

Returns updated workspace relation with its sanitised data.<br/>Requirements:<br/>  - auth-client scopes: "workspace"<br/>  - user permission: "write" or higher<br/>Returns:<br/>400 if the resource is not found<br/>403 if user does not have the required permission

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.workspace_relation import WorkspaceRelation
from airfocus_client.models.workspace_relation_with_embed import WorkspaceRelationWithEmbed
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
    api_instance = airfocus_client.CRUDApi(api_client)
    workspace_relation_id = 'workspace_relation_id_example' # str | 
    workspace_relation = airfocus_client.WorkspaceRelation() # WorkspaceRelation | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Update an existing workspace relation
        api_response = api_instance.update_workspace_relation(workspace_relation_id, workspace_relation, act_as_admin=act_as_admin)
        print("The response of CRUDApi->update_workspace_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRUDApi->update_workspace_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_relation_id** | **str**|  | 
 **workspace_relation** | [**WorkspaceRelation**](WorkspaceRelation.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**WorkspaceRelationWithEmbed**](WorkspaceRelationWithEmbed.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

