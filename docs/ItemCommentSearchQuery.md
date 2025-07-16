# ItemCommentSearchQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** |  | [optional] 

## Example

```python
from airfocus_client.models.item_comment_search_query import ItemCommentSearchQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ItemCommentSearchQuery from a JSON string
item_comment_search_query_instance = ItemCommentSearchQuery.from_json(json)
# print the JSON string representation of the object
print(ItemCommentSearchQuery.to_json())

# convert the object into a dict
item_comment_search_query_dict = item_comment_search_query_instance.to_dict()
# create an instance of ItemCommentSearchQuery from a dict
item_comment_search_query_from_dict = ItemCommentSearchQuery.from_dict(item_comment_search_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


