# CreateItemRequestWithMD

Item with Markdown string description.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | [**ItemColor**](ItemColor.md) | Color of this item. | 
**description** | **str** | Rich-text as markdown string. | 
**fields** | **Dict[str, object]** | Values of custom fields, where each key is a custom-field ID and each value is a JSON-formatted value of the corresponding field. | 
**name** | **str** | Name (title) of this item. | 
**order** | **int** | A order number of this item for sorting. | 
**status_id** | **str** | Id of the status of this item. | 
**archived** | **bool** | Whether this item is archived. | [optional] [default to False]
**assignee_user_ids** | **List[str]** | Ids of users who are assigned to this item. | [optional] 

## Example

```python
from airfocus_client.models.create_item_request_with_md import CreateItemRequestWithMD

# TODO update the JSON string below
json = "{}"
# create an instance of CreateItemRequestWithMD from a JSON string
create_item_request_with_md_instance = CreateItemRequestWithMD.from_json(json)
# print the JSON string representation of the object
print(CreateItemRequestWithMD.to_json())

# convert the object into a dict
create_item_request_with_md_dict = create_item_request_with_md_instance.to_dict()
# create an instance of CreateItemRequestWithMD from a dict
create_item_request_with_md_from_dict = CreateItemRequestWithMD.from_dict(create_item_request_with_md_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


