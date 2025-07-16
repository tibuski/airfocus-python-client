# InboxViewCountersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived** | **bool** | Whether archived items should be included or excluded from all the counters. | 
**count_assigned** | **bool** | Whether to also additionally return a counter of items with assigned users. | 
**filter** | [**ItemSearchQueryFilter**](ItemSearchQueryFilter.md) | Custom filter to apply to the counted items. If not specified, then the default filter from the view settings is used. | [optional] 

## Example

```python
from airfocus_client.models.inbox_view_counters_request import InboxViewCountersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InboxViewCountersRequest from a JSON string
inbox_view_counters_request_instance = InboxViewCountersRequest.from_json(json)
# print the JSON string representation of the object
print(InboxViewCountersRequest.to_json())

# convert the object into a dict
inbox_view_counters_request_dict = inbox_view_counters_request_instance.to_dict()
# create an instance of InboxViewCountersRequest from a dict
inbox_view_counters_request_from_dict = InboxViewCountersRequest.from_dict(inbox_view_counters_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


