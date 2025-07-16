# ItemWithItemEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**ItemEmbed**](ItemEmbed.md) |  | 
**archived** | **bool** | Whether this item is archived. | 
**color** | [**ItemColor**](ItemColor.md) | Color of this item. | 
**created_at** | **datetime** | Timestamp of when this item was created. | 
**description** | [**RichText**](RichText.md) |  | 
**fields** | **Dict[str, object]** | Values of custom fields, where each key is a custom-field ID and each value is a JSON-formatted value of the corresponding field. | 
**id** | **str** | Unique identifier of this item. | 
**last_updated_at** | **datetime** | Timestamp of when this item was last updated. | 
**name** | **str** | Name (title) of this item. | 
**order** | **int** | A order number of this item for sorting. | 
**status_id** | **str** | Id of the status of this item. | 
**workspace_id** | **str** | Id of the workspace this workspace belongs to. | 
**assignee_user_ids** | **List[str]** | Ids of users who are assigned to this item. | [optional] 
**number** | **int** | A numeric id of this item, which is used to create an alias to this item like DEV-123. The number is unique within the workspace, and defined by server on item creation. | [optional] 
**status_category_updated_at** | **datetime** | Timestamp of when the status of this item was last time switched from one category to another. | [optional] 
**status_updated_at** | **datetime** | Timestamp of when the status of this item was last updated. | [optional] 

## Example

```python
from airfocus_client.models.item_with_item_embed import ItemWithItemEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of ItemWithItemEmbed from a JSON string
item_with_item_embed_instance = ItemWithItemEmbed.from_json(json)
# print the JSON string representation of the object
print(ItemWithItemEmbed.to_json())

# convert the object into a dict
item_with_item_embed_dict = item_with_item_embed_instance.to_dict()
# create an instance of ItemWithItemEmbed from a dict
item_with_item_embed_from_dict = ItemWithItemEmbed.from_dict(item_with_item_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


