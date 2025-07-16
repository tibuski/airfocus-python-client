# WorkspaceSearchQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived** | **bool** |  | 
**sort** | [**WorkspaceSearchQuerySort**](WorkspaceSearchQuerySort.md) |  | 
**filter** | [**WorkspaceSearchQueryFilter**](WorkspaceSearchQueryFilter.md) |  | [optional] 

## Example

```python
from airfocus_client.models.workspace_search_query import WorkspaceSearchQuery

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceSearchQuery from a JSON string
workspace_search_query_instance = WorkspaceSearchQuery.from_json(json)
# print the JSON string representation of the object
print(WorkspaceSearchQuery.to_json())

# convert the object into a dict
workspace_search_query_dict = workspace_search_query_instance.to_dict()
# create an instance of WorkspaceSearchQuery from a dict
workspace_search_query_from_dict = WorkspaceSearchQuery.from_dict(workspace_search_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


