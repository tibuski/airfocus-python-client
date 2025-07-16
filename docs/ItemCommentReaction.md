# ItemCommentReaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emoji** | [**Emoji**](Emoji.md) |  | 
**user_ids** | **List[str]** |  | [optional] 

## Example

```python
from airfocus_client.models.item_comment_reaction import ItemCommentReaction

# TODO update the JSON string below
json = "{}"
# create an instance of ItemCommentReaction from a JSON string
item_comment_reaction_instance = ItemCommentReaction.from_json(json)
# print the JSON string representation of the object
print(ItemCommentReaction.to_json())

# convert the object into a dict
item_comment_reaction_dict = item_comment_reaction_instance.to_dict()
# create an instance of ItemCommentReaction from a dict
item_comment_reaction_from_dict = ItemCommentReaction.from_dict(item_comment_reaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


