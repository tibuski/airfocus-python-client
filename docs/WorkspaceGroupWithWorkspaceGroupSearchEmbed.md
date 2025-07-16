# WorkspaceGroupWithWorkspaceGroupSearchEmbed

An entity for grouping workspaces (like folders).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**WorkspaceGroupSearchEmbed**](WorkspaceGroupSearchEmbed.md) |  | 
**created_at** | **datetime** | Date-time when this group was created. | 
**id** | **str** | UUID of this group. | 
**last_updated_at** | **datetime** | Date-time when this group was last updated. | 
**name** | **str** | Name of this group. | 
**order** | **int** | Order number of this group for sorting. | 
**team_id** | **str** | UUID of the team which owns this group. | 
**default_permission** | [**Permission**](Permission.md) | Default permission for all team-members to all the inner contents of this group. | [optional] 
**parent_id** | **str** | UUID of the parent group (if applicable). | [optional] 

## Example

```python
from airfocus_client.models.workspace_group_with_workspace_group_search_embed import WorkspaceGroupWithWorkspaceGroupSearchEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceGroupWithWorkspaceGroupSearchEmbed from a JSON string
workspace_group_with_workspace_group_search_embed_instance = WorkspaceGroupWithWorkspaceGroupSearchEmbed.from_json(json)
# print the JSON string representation of the object
print(WorkspaceGroupWithWorkspaceGroupSearchEmbed.to_json())

# convert the object into a dict
workspace_group_with_workspace_group_search_embed_dict = workspace_group_with_workspace_group_search_embed_instance.to_dict()
# create an instance of WorkspaceGroupWithWorkspaceGroupSearchEmbed from a dict
workspace_group_with_workspace_group_search_embed_from_dict = WorkspaceGroupWithWorkspaceGroupSearchEmbed.from_dict(workspace_group_with_workspace_group_search_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


