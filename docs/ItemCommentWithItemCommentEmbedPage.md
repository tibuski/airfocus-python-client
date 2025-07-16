# ItemCommentWithItemCommentEmbedPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_items** | **int** |  | 
**items** | [**List[ItemCommentWithItemCommentEmbed]**](ItemCommentWithItemCommentEmbed.md) |  | [optional] 

## Example

```python
from airfocus_client.models.item_comment_with_item_comment_embed_page import ItemCommentWithItemCommentEmbedPage

# TODO update the JSON string below
json = "{}"
# create an instance of ItemCommentWithItemCommentEmbedPage from a JSON string
item_comment_with_item_comment_embed_page_instance = ItemCommentWithItemCommentEmbedPage.from_json(json)
# print the JSON string representation of the object
print(ItemCommentWithItemCommentEmbedPage.to_json())

# convert the object into a dict
item_comment_with_item_comment_embed_page_dict = item_comment_with_item_comment_embed_page_instance.to_dict()
# create an instance of ItemCommentWithItemCommentEmbedPage from a dict
item_comment_with_item_comment_embed_page_from_dict = ItemCommentWithItemCommentEmbedPage.from_dict(item_comment_with_item_comment_embed_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


