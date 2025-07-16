# WorkspaceGroupSearchEmbed

An object embedded into each workspace-group when searching workspaces.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**Dict[str, Permission]**](Permission.md) | All explicitly defined permissions for all users for this workspace-group. | 
**current_permission** | [**Permission**](Permission.md) | Actual permission of the current user for this workspace-group. | [optional] 
**workspace_ids** | **List[str]** | List of workspace-ids which belongs to this workspace-group. | [optional] 
**workspaces** | [**List[Workspace]**](Workspace.md) | Deprecated and will be removed. Use &#39;workspaceIds&#39; instead, and a followup workspace-search request. | [optional] 

## Example

```python
from airfocus_client.models.workspace_group_search_embed import WorkspaceGroupSearchEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceGroupSearchEmbed from a JSON string
workspace_group_search_embed_instance = WorkspaceGroupSearchEmbed.from_json(json)
# print the JSON string representation of the object
print(WorkspaceGroupSearchEmbed.to_json())

# convert the object into a dict
workspace_group_search_embed_dict = workspace_group_search_embed_instance.to_dict()
# create an instance of WorkspaceGroupSearchEmbed from a dict
workspace_group_search_embed_from_dict = WorkspaceGroupSearchEmbed.from_dict(workspace_group_search_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


