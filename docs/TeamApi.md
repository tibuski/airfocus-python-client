# airfocus_client.TeamApi

All URIs are relative to *https://app.airfocus.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_terms_of_service**](TeamApi.md#accept_terms_of_service) | **POST** /api/team/tos | 
[**change_user_disabled**](TeamApi.md#change_user_disabled) | **POST** /api/team/users/disabled | 
[**change_user_role**](TeamApi.md#change_user_role) | **POST** /api/team/users/role | 
[**create_user_invite**](TeamApi.md#create_user_invite) | **POST** /api/team/users/invite/create | 
[**kick_user**](TeamApi.md#kick_user) | **POST** /api/team/users/kick | 
[**list_users**](TeamApi.md#list_users) | **GET** /api/team/users | 
[**resend_user_invite**](TeamApi.md#resend_user_invite) | **POST** /api/team/users/invite/resend | 
[**retrieve_team**](TeamApi.md#retrieve_team) | **GET** /api/team | 
[**send_bulk_user_invites**](TeamApi.md#send_bulk_user_invites) | **POST** /api/team/users/invite/bulk | 
[**send_user_invite**](TeamApi.md#send_user_invite) | **POST** /api/team/users/invite | 
[**update_team_flags**](TeamApi.md#update_team_flags) | **PATCH** /api/team/flags | 


# **accept_terms_of_service**
> accept_terms_of_service(store_accepted_tos_request)

Requirements:<br/>- auth-client scopes: "team"<br/>- user role: "admin"

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.store_accepted_tos_request import StoreAcceptedTosRequest
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
    api_instance = airfocus_client.TeamApi(api_client)
    store_accepted_tos_request = airfocus_client.StoreAcceptedTosRequest() # StoreAcceptedTosRequest | 

    try:
        api_instance.accept_terms_of_service(store_accepted_tos_request)
    except Exception as e:
        print("Exception when calling TeamApi->accept_terms_of_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_accepted_tos_request** | [**StoreAcceptedTosRequest**](StoreAcceptedTosRequest.md)|  | 

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
**200** |  |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not match the required role, or authenticated client does not have the required access scopes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user_disabled**
> change_user_disabled(change_user_disabled_request)

Requirements:<br/>- auth-client scopes: "team"<br/>- user role: "admin"

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.change_user_disabled_request import ChangeUserDisabledRequest
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
    api_instance = airfocus_client.TeamApi(api_client)
    change_user_disabled_request = airfocus_client.ChangeUserDisabledRequest() # ChangeUserDisabledRequest | 

    try:
        api_instance.change_user_disabled(change_user_disabled_request)
    except Exception as e:
        print("Exception when calling TeamApi->change_user_disabled: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_user_disabled_request** | [**ChangeUserDisabledRequest**](ChangeUserDisabledRequest.md)|  | 

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
**200** |  |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not match the required role, or authenticated client does not have the required access scopes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user_role**
> change_user_role(change_user_role_request)

Requirements:<br/>- auth-client scopes: "team"<br/>- user role: "admin"

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.change_user_role_request import ChangeUserRoleRequest
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
    api_instance = airfocus_client.TeamApi(api_client)
    change_user_role_request = airfocus_client.ChangeUserRoleRequest() # ChangeUserRoleRequest | 

    try:
        api_instance.change_user_role(change_user_role_request)
    except Exception as e:
        print("Exception when calling TeamApi->change_user_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_user_role_request** | [**ChangeUserRoleRequest**](ChangeUserRoleRequest.md)|  | 

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
**200** |  |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not match the required role, or authenticated client does not have the required access scopes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_invite**
> str create_user_invite(create_user_invite_request)

Requirements:<br/>- auth-client scopes: "team"<br/>- user role: "admin"

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.create_user_invite_request import CreateUserInviteRequest
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
    api_instance = airfocus_client.TeamApi(api_client)
    create_user_invite_request = airfocus_client.CreateUserInviteRequest() # CreateUserInviteRequest | 

    try:
        api_response = api_instance.create_user_invite(create_user_invite_request)
        print("The response of TeamApi->create_user_invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->create_user_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_invite_request** | [**CreateUserInviteRequest**](CreateUserInviteRequest.md)|  | 

### Return type

**str**

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
**403** | If user does not match the required role, or authenticated client does not have the required access scopes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kick_user**
> kick_user(kick_user_request)

Requirements:<br/>- auth-client scopes: "team"<br/>- user role: "admin"

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.kick_user_request import KickUserRequest
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
    api_instance = airfocus_client.TeamApi(api_client)
    kick_user_request = airfocus_client.KickUserRequest() # KickUserRequest | 

    try:
        api_instance.kick_user(kick_user_request)
    except Exception as e:
        print("Exception when calling TeamApi->kick_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kick_user_request** | [**KickUserRequest**](KickUserRequest.md)|  | 

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
**200** |  |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not match the required role, or authenticated client does not have the required access scopes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> List[User] list_users(query=query)

List team users.<br/>Requirements:<br/>- auth-client scopes: "team:read"

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.user import User
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
    api_instance = airfocus_client.TeamApi(api_client)
    query = 'query_example' # str |  (optional)

    try:
        api_response = api_instance.list_users(query=query)
        print("The response of TeamApi->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 

### Return type

[**List[User]**](User.md)

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

# **resend_user_invite**
> resend_user_invite(resend_user_invite_request)

Requirements:<br/>- auth-client scopes: "team"<br/>- user role: "admin"

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.resend_user_invite_request import ResendUserInviteRequest
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
    api_instance = airfocus_client.TeamApi(api_client)
    resend_user_invite_request = airfocus_client.ResendUserInviteRequest() # ResendUserInviteRequest | 

    try:
        api_instance.resend_user_invite(resend_user_invite_request)
    except Exception as e:
        print("Exception when calling TeamApi->resend_user_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resend_user_invite_request** | [**ResendUserInviteRequest**](ResendUserInviteRequest.md)|  | 

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
**200** |  |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user does not match the required role, or authenticated client does not have the required access scopes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_team**
> Team retrieve_team()

Requirements:<br/>- auth-client scopes: "team:read"

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.team import Team
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
    api_instance = airfocus_client.TeamApi(api_client)

    try:
        api_response = api_instance.retrieve_team()
        print("The response of TeamApi->retrieve_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->retrieve_team: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Team**](Team.md)

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

# **send_bulk_user_invites**
> List[User] send_bulk_user_invites(bulk_invite_users_request)

Requirements:<br/>- auth-client scopes: "team"<br/>- user role: "admin"

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.bulk_invite_users_request import BulkInviteUsersRequest
from airfocus_client.models.user import User
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
    api_instance = airfocus_client.TeamApi(api_client)
    bulk_invite_users_request = airfocus_client.BulkInviteUsersRequest() # BulkInviteUsersRequest | 

    try:
        api_response = api_instance.send_bulk_user_invites(bulk_invite_users_request)
        print("The response of TeamApi->send_bulk_user_invites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->send_bulk_user_invites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_invite_users_request** | [**BulkInviteUsersRequest**](BulkInviteUsersRequest.md)|  | 

### Return type

[**List[User]**](User.md)

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
**403** | If user does not match the required role, or authenticated client does not have the required access scopes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_user_invite**
> User send_user_invite(invite_user_request)

Requirements:<br/>- auth-client scopes: "team"<br/>- user role: "admin"

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.invite_user_request import InviteUserRequest
from airfocus_client.models.user import User
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
    api_instance = airfocus_client.TeamApi(api_client)
    invite_user_request = airfocus_client.InviteUserRequest() # InviteUserRequest | 

    try:
        api_response = api_instance.send_user_invite(invite_user_request)
        print("The response of TeamApi->send_user_invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->send_user_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_user_request** | [**InviteUserRequest**](InviteUserRequest.md)|  | 

### Return type

[**User**](User.md)

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
**403** | If user does not match the required role, or authenticated client does not have the required access scopes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team_flags**
> TeamFlags update_team_flags(update_team_flags_request)

Requirements:<br/>- auth-client scopes: "team"<br/>- user role: "admin"

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.team_flags import TeamFlags
from airfocus_client.models.update_team_flags_request import UpdateTeamFlagsRequest
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
    api_instance = airfocus_client.TeamApi(api_client)
    update_team_flags_request = airfocus_client.UpdateTeamFlagsRequest() # UpdateTeamFlagsRequest | 

    try:
        api_response = api_instance.update_team_flags(update_team_flags_request)
        print("The response of TeamApi->update_team_flags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->update_team_flags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_team_flags_request** | [**UpdateTeamFlagsRequest**](UpdateTeamFlagsRequest.md)|  | 

### Return type

[**TeamFlags**](TeamFlags.md)

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
**403** | If user does not match the required role, or authenticated client does not have the required access scopes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

