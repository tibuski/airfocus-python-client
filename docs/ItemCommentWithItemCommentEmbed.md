# ItemCommentWithItemCommentEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | **object** |  | 
**content** | [**RichText**](RichText.md) |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**item_id** | **str** |  | 
**last_updated_at** | **datetime** |  | 
**user_id** | **str** |  | 
**reactions** | [**List[ItemCommentReaction]**](ItemCommentReaction.md) |  | [optional] 

## Example

```python
from airfocus_client.models.item_comment_with_item_comment_embed import ItemCommentWithItemCommentEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of ItemCommentWithItemCommentEmbed from a JSON string
item_comment_with_item_comment_embed_instance = ItemCommentWithItemCommentEmbed.from_json(json)
# print the JSON string representation of the object
print(ItemCommentWithItemCommentEmbed.to_json())

# convert the object into a dict
item_comment_with_item_comment_embed_dict = item_comment_with_item_comment_embed_instance.to_dict()
# create an instance of ItemCommentWithItemCommentEmbed from a dict
item_comment_with_item_comment_embed_from_dict = ItemCommentWithItemCommentEmbed.from_dict(item_comment_with_item_comment_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


