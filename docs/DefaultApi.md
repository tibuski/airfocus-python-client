# airfocus_client.DefaultApi

All URIs are relative to *https://app.airfocus.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_inbox_view_counters**](DefaultApi.md#retrieve_inbox_view_counters) | **POST** /api/workspaces/extensions/views/inbox/{viewId}/counters | Retrieve counters of items in each tab of the view.


# **retrieve_inbox_view_counters**
> List[InboxViewCounter] retrieve_inbox_view_counters(view_id, inbox_view_counters_request, act_as_admin=act_as_admin)

Retrieve counters of items in each tab of the view.

Requirements:<br/>- auth-client scopes: "workspace:read"<br/>- team features: "view:inbox"<br/>- user permission: "read" or higher

### Example

* Bearer Authentication (httpAuth):

```python
import airfocus_client
from airfocus_client.models.inbox_view_counter import InboxViewCounter
from airfocus_client.models.inbox_view_counters_request import InboxViewCountersRequest
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
    api_instance = airfocus_client.DefaultApi(api_client)
    view_id = 'view_id_example' # str | 
    inbox_view_counters_request = airfocus_client.InboxViewCountersRequest() # InboxViewCountersRequest | 
    act_as_admin = True # bool | Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. (optional)

    try:
        # Retrieve counters of items in each tab of the view.
        api_response = api_instance.retrieve_inbox_view_counters(view_id, inbox_view_counters_request, act_as_admin=act_as_admin)
        print("The response of DefaultApi->retrieve_inbox_view_counters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->retrieve_inbox_view_counters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**|  | 
 **inbox_view_counters_request** | [**InboxViewCountersRequest**](InboxViewCountersRequest.md)|  | 
 **act_as_admin** | **bool**| Enable sudo-mode for admins for a single request, which gives full permission to all workspaces in the team. | [optional] 

### Return type

[**List[InboxViewCounter]**](InboxViewCounter.md)

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
**403** | If user does not have the required permission, or user&#39;s team does not have access to the required features, or authenticated client does not have the required access scopes. |  -  |
**0** | If any other error happens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

