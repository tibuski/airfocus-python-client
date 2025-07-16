# InboxViewCounter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of items in the counter. | 
**id** | **str** | Machine-readable ID of the counter. | 
**name** | **str** | Human-readable name of the counter. | 

## Example

```python
from airfocus_client.models.inbox_view_counter import InboxViewCounter

# TODO update the JSON string below
json = "{}"
# create an instance of InboxViewCounter from a JSON string
inbox_view_counter_instance = InboxViewCounter.from_json(json)
# print the JSON string representation of the object
print(InboxViewCounter.to_json())

# convert the object into a dict
inbox_view_counter_dict = inbox_view_counter_instance.to_dict()
# create an instance of InboxViewCounter from a dict
inbox_view_counter_from_dict = InboxViewCounter.from_dict(inbox_view_counter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


