# CreateItemLinkRequest


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
from airfocus_client.models.create_item_link_request import CreateItemLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateItemLinkRequest from a JSON string
create_item_link_request_instance = CreateItemLinkRequest.from_json(json)
# print the JSON string representation of the object
print(CreateItemLinkRequest.to_json())

# convert the object into a dict
create_item_link_request_dict = create_item_link_request_instance.to_dict()
# create an instance of CreateItemLinkRequest from a dict
create_item_link_request_from_dict = CreateItemLinkRequest.from_dict(create_item_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


