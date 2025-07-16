# UpdateItemLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_item_id** | **str** |  | 
**from_order** | **int** | How this item-link is ordered in the list of links of the \&quot;fromItem\&quot;. | 
**to_item_id** | **str** |  | 
**to_order** | **int** | How this item-link is ordered in the list of links of the \&quot;toItem\&quot;. | 
**type** | [**ItemLinkType**](ItemLinkType.md) |  | 

## Example

```python
from airfocus_client.models.update_item_link_request import UpdateItemLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateItemLinkRequest from a JSON string
update_item_link_request_instance = UpdateItemLinkRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateItemLinkRequest.to_json())

# convert the object into a dict
update_item_link_request_dict = update_item_link_request_instance.to_dict()
# create an instance of UpdateItemLinkRequest from a dict
update_item_link_request_from_dict = UpdateItemLinkRequest.from_dict(update_item_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


