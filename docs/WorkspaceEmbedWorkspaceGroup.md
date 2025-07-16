# WorkspaceEmbedWorkspaceGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**order** | **int** |  | 
**parent_id** | **str** |  | [optional] 

## Example

```python
from airfocus_client.models.workspace_embed_workspace_group import WorkspaceEmbedWorkspaceGroup

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceEmbedWorkspaceGroup from a JSON string
workspace_embed_workspace_group_instance = WorkspaceEmbedWorkspaceGroup.from_json(json)
# print the JSON string representation of the object
print(WorkspaceEmbedWorkspaceGroup.to_json())

# convert the object into a dict
workspace_embed_workspace_group_dict = workspace_embed_workspace_group_instance.to_dict()
# create an instance of WorkspaceEmbedWorkspaceGroup from a dict
workspace_embed_workspace_group_from_dict = WorkspaceEmbedWorkspaceGroup.from_dict(workspace_embed_workspace_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


