# airfocus_client.ProfileApi

All URIs are relative to *https://app.airfocus.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_password**](ProfileApi.md#change_password) | **POST** /api/profile/change-password | 
[**create_api_key**](ProfileApi.md#create_api_key) | **POST** /api/profile/api-keys | 
[**delete_api_key**](ProfileApi.md#delete_api_key) | **DELETE** /api/profile/api-keys/{apiKeyId} | 
[**get_client_settings**](ProfileApi.md#get_client_settings) | **GET** /api/profile/client-settings | 
[**list_api_keys**](ProfileApi.md#list_api_keys) | **GET** /api/profile/api-keys | 
[**retrieve_profile**](ProfileApi.md#retrieve_profile) | **GET** /api/profile | 
[**set_client_settings**](ProfileApi.md#set_client_settings) | **PUT** /api/profile/client-settings | 
[**update_profile**](ProfileApi.md#update_profile) | **PUT** /api/profile | 


# **change_password**
> change_password(change_password_request)

Requirements:<br/>- auth-client scopes: "profile"

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.change_password_request import ChangePasswordRequest
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
    api_instance = airfocus_client.ProfileApi(api_client)
    change_password_request = airfocus_client.ChangePasswordRequest() # ChangePasswordRequest | 

    try:
        api_instance.change_password(change_password_request)
    except Exception as e:
        print("Exception when calling ProfileApi->change_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_password_request** | [**ChangePasswordRequest**](ChangePasswordRequest.md)|  | 

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
**403** | If authenticated client does not have the required access scopes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_api_key**
> CreateApiKeyResponse create_api_key(create_api_key_request)

Requirements:<br/>- auth-client scopes: "profile"<br/>- team features: "api-keys"

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.create_api_key_request import CreateApiKeyRequest
from airfocus_client.models.create_api_key_response import CreateApiKeyResponse
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
    api_instance = airfocus_client.ProfileApi(api_client)
    create_api_key_request = airfocus_client.CreateApiKeyRequest() # CreateApiKeyRequest | 

    try:
        api_response = api_instance.create_api_key(create_api_key_request)
        print("The response of ProfileApi->create_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->create_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_api_key_request** | [**CreateApiKeyRequest**](CreateApiKeyRequest.md)|  | 

### Return type

[**CreateApiKeyResponse**](CreateApiKeyResponse.md)

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
**403** | If user&#39;s team does not have access to the required features, or authenticated client does not have the required access scopes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key**
> delete_api_key(api_key_id)

Requirements:<br/>- auth-client scopes: "profile"<br/>- team features: "api-keys"

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
    api_instance = airfocus_client.ProfileApi(api_client)
    api_key_id = 'api_key_id_example' # str | 

    try:
        api_instance.delete_api_key(api_key_id)
    except Exception as e:
        print("Exception when calling ProfileApi->delete_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **str**|  | 

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
**200** |  |  -  |
**401** | If missing authentication token. |  -  |
**403** | If user&#39;s team does not have access to the required features, or authenticated client does not have the required access scopes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_settings**
> object get_client_settings(path=path)

Requirements:<br/>- auth-client scopes: "profile:read"

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
    api_instance = airfocus_client.ProfileApi(api_client)
    path = 'path_example' # str |  (optional)

    try:
        api_response = api_instance.get_client_settings(path=path)
        print("The response of ProfileApi->get_client_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->get_client_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | [optional] 

### Return type

**object**

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

# **list_api_keys**
> List[ApiKey] list_api_keys()

Requirements:<br/>- auth-client scopes: "profile"<br/>- team features: "api-keys"

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.api_key import ApiKey
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
    api_instance = airfocus_client.ProfileApi(api_client)

    try:
        api_response = api_instance.list_api_keys()
        print("The response of ProfileApi->list_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->list_api_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApiKey]**](ApiKey.md)

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
**403** | If user&#39;s team does not have access to the required features, or authenticated client does not have the required access scopes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_profile**
> User retrieve_profile()

Requirements:<br/>- auth-client scopes: "profile:read"

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
    api_instance = airfocus_client.ProfileApi(api_client)

    try:
        api_response = api_instance.retrieve_profile()
        print("The response of ProfileApi->retrieve_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->retrieve_profile: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**User**](User.md)

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

# **set_client_settings**
> set_client_settings(set_client_settings_request)

Requirements:<br/>- auth-client scopes: "profile"

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.set_client_settings_request import SetClientSettingsRequest
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
    api_instance = airfocus_client.ProfileApi(api_client)
    set_client_settings_request = airfocus_client.SetClientSettingsRequest() # SetClientSettingsRequest | 

    try:
        api_instance.set_client_settings(set_client_settings_request)
    except Exception as e:
        print("Exception when calling ProfileApi->set_client_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_client_settings_request** | [**SetClientSettingsRequest**](SetClientSettingsRequest.md)|  | 

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
**403** | If authenticated client does not have the required access scopes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile**
> User update_profile(update_user_request)

Requirements:<br/>- auth-client scopes: "profile"

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.update_user_request import UpdateUserRequest
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
    api_instance = airfocus_client.ProfileApi(api_client)
    update_user_request = airfocus_client.UpdateUserRequest() # UpdateUserRequest | 

    try:
        api_response = api_instance.update_profile(update_user_request)
        print("The response of ProfileApi->update_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->update_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_user_request** | [**UpdateUserRequest**](UpdateUserRequest.md)|  | 

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
**403** | If authenticated client does not have the required access scopes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

