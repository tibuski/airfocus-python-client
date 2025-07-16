# ItemEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apps** | [**Dict[str, ItemEmbedApp]**](ItemEmbedApp.md) |  | 
**attachment_count** | **int** |  | 
**comment_count** | **int** |  | 
**link_count** | **int** |  | 
**progress** | [**ItemEmbedProgress**](ItemEmbedProgress.md) |  | 
**watched** | **bool** |  | 
**alias** | **str** |  | [optional] 
**children** | [**List[RelativeItemInfo]**](RelativeItemInfo.md) |  | [optional] 
**constraints** | [**List[ItemConstraint]**](ItemConstraint.md) |  | [optional] 
**integration** | [**ItemEmbedIntegration**](ItemEmbedIntegration.md) |  | [optional] 
**parents** | [**List[RelativeItemInfo]**](RelativeItemInfo.md) |  | [optional] 
**workspace_item_type** | [**ItemType**](ItemType.md) |  | [optional] 

## Example

```python
from airfocus_client.models.item_embed import ItemEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of ItemEmbed from a JSON string
item_embed_instance = ItemEmbed.from_json(json)
# print the JSON string representation of the object
print(ItemEmbed.to_json())

# convert the object into a dict
item_embed_dict = item_embed_instance.to_dict()
# create an instance of ItemEmbed from a dict
item_embed_from_dict = ItemEmbed.from_dict(item_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


