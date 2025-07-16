# ItemAttachmentBulkPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**transform** | [**List[JsonPatchOperation]**](JsonPatchOperation.md) | A JSON Patch document. See https://jsonpatch.com/ for more information. | 
**type** | **str** |  | 

## Example

```python
from airfocus_client.models.item_attachment_bulk_patch import ItemAttachmentBulkPatch

# TODO update the JSON string below
json = "{}"
# create an instance of ItemAttachmentBulkPatch from a JSON string
item_attachment_bulk_patch_instance = ItemAttachmentBulkPatch.from_json(json)
# print the JSON string representation of the object
print(ItemAttachmentBulkPatch.to_json())

# convert the object into a dict
item_attachment_bulk_patch_dict = item_attachment_bulk_patch_instance.to_dict()
# create an instance of ItemAttachmentBulkPatch from a dict
item_attachment_bulk_patch_from_dict = ItemAttachmentBulkPatch.from_dict(item_attachment_bulk_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


