# ItemRelationCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_id** | **str** |  | 
**parent_id** | **str** |  | 
**child_order** | **int** |  | [optional] 
**parent_order** | **int** |  | [optional] 

## Example

```python
from airfocus_client.models.item_relation_create_request import ItemRelationCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ItemRelationCreateRequest from a JSON string
item_relation_create_request_instance = ItemRelationCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ItemRelationCreateRequest.to_json())

# convert the object into a dict
item_relation_create_request_dict = item_relation_create_request_instance.to_dict()
# create an instance of ItemRelationCreateRequest from a dict
item_relation_create_request_from_dict = ItemRelationCreateRequest.from_dict(item_relation_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


