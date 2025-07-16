# ItemComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**RichText**](RichText.md) |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**item_id** | **str** |  | 
**last_updated_at** | **datetime** |  | 
**user_id** | **str** |  | 
**reactions** | [**List[ItemCommentReaction]**](ItemCommentReaction.md) |  | [optional] 

## Example

```python
from airfocus_client.models.item_comment import ItemComment

# TODO update the JSON string below
json = "{}"
# create an instance of ItemComment from a JSON string
item_comment_instance = ItemComment.from_json(json)
# print the JSON string representation of the object
print(ItemComment.to_json())

# convert the object into a dict
item_comment_dict = item_comment_instance.to_dict()
# create an instance of ItemComment from a dict
item_comment_from_dict = ItemComment.from_dict(item_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


