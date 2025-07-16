# WorkspaceSearchQueryFilterName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_sensitive** | **bool** |  | 
**text** | **str** |  | 

## Example

```python
from airfocus_client.models.workspace_search_query_filter_name import WorkspaceSearchQueryFilterName

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceSearchQueryFilterName from a JSON string
workspace_search_query_filter_name_instance = WorkspaceSearchQueryFilterName.from_json(json)
# print the JSON string representation of the object
print(WorkspaceSearchQueryFilterName.to_json())

# convert the object into a dict
workspace_search_query_filter_name_dict = workspace_search_query_filter_name_instance.to_dict()
# create an instance of WorkspaceSearchQueryFilterName from a dict
workspace_search_query_filter_name_from_dict = WorkspaceSearchQueryFilterName.from_dict(workspace_search_query_filter_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


