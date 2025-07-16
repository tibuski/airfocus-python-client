# ItemRelationBulkPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**transform** | [**List[JsonPatchOperation]**](JsonPatchOperation.md) | A JSON Patch document. See https://jsonpatch.com/ for more information. | 
**type** | **str** |  | 

## Example

```python
from airfocus_client.models.item_relation_bulk_patch import ItemRelationBulkPatch

# TODO update the JSON string below
json = "{}"
# create an instance of ItemRelationBulkPatch from a JSON string
item_relation_bulk_patch_instance = ItemRelationBulkPatch.from_json(json)
# print the JSON string representation of the object
print(ItemRelationBulkPatch.to_json())

# convert the object into a dict
item_relation_bulk_patch_dict = item_relation_bulk_patch_instance.to_dict()
# create an instance of ItemRelationBulkPatch from a dict
item_relation_bulk_patch_from_dict = ItemRelationBulkPatch.from_dict(item_relation_bulk_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


