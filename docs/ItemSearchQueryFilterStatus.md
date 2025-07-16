# ItemSearchQueryFilterStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**ItemSearchQueryTimeAnchor**](ItemSearchQueryTimeAnchor.md) |  | 
**status_ids** | **List[str]** |  | [optional] 

## Example

```python
from airfocus_client.models.item_search_query_filter_status import ItemSearchQueryFilterStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ItemSearchQueryFilterStatus from a JSON string
item_search_query_filter_status_instance = ItemSearchQueryFilterStatus.from_json(json)
# print the JSON string representation of the object
print(ItemSearchQueryFilterStatus.to_json())

# convert the object into a dict
item_search_query_filter_status_dict = item_search_query_filter_status_instance.to_dict()
# create an instance of ItemSearchQueryFilterStatus from a dict
item_search_query_filter_status_from_dict = ItemSearchQueryFilterStatus.from_dict(item_search_query_filter_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


