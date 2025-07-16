# WorkspaceSearchQueryFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inner** | [**WorkspaceSearchQueryFilter**](WorkspaceSearchQueryFilter.md) |  | 
**ids** | **List[str]** |  | [optional] 
**values** | [**List[WorkspaceNamespace]**](WorkspaceNamespace.md) |  | [optional] 

## Example

```python
from airfocus_client.models.workspace_search_query_filter import WorkspaceSearchQueryFilter

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceSearchQueryFilter from a JSON string
workspace_search_query_filter_instance = WorkspaceSearchQueryFilter.from_json(json)
# print the JSON string representation of the object
print(WorkspaceSearchQueryFilter.to_json())

# convert the object into a dict
workspace_search_query_filter_dict = workspace_search_query_filter_instance.to_dict()
# create an instance of WorkspaceSearchQueryFilter from a dict
workspace_search_query_filter_from_dict = WorkspaceSearchQueryFilter.from_dict(workspace_search_query_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


