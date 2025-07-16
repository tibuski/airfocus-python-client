# ItemRelationUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_order** | **int** |  | 
**parent_order** | **int** |  | 

## Example

```python
from airfocus_client.models.item_relation_update_request import ItemRelationUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ItemRelationUpdateRequest from a JSON string
item_relation_update_request_instance = ItemRelationUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ItemRelationUpdateRequest.to_json())

# convert the object into a dict
item_relation_update_request_dict = item_relation_update_request_instance.to_dict()
# create an instance of ItemRelationUpdateRequest from a dict
item_relation_update_request_from_dict = ItemRelationUpdateRequest.from_dict(item_relation_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


