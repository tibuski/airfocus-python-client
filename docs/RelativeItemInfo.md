# RelativeItemInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_order** | **int** |  | 
**item_id** | **str** |  | 
**parent_order** | **int** |  | 
**relation_id** | **str** |  | 
**workspace_id** | **str** |  | 
**alias** | **str** |  | [optional] 
**item** | [**Item**](Item.md) |  | [optional] 
**item_type** | [**ItemType**](ItemType.md) |  | [optional] 

## Example

```python
from airfocus_client.models.relative_item_info import RelativeItemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RelativeItemInfo from a JSON string
relative_item_info_instance = RelativeItemInfo.from_json(json)
# print the JSON string representation of the object
print(RelativeItemInfo.to_json())

# convert the object into a dict
relative_item_info_dict = relative_item_info_instance.to_dict()
# create an instance of RelativeItemInfo from a dict
relative_item_info_from_dict = RelativeItemInfo.from_dict(relative_item_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


