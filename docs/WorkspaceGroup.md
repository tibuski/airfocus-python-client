# WorkspaceGroup

An entity for grouping workspaces (like folders).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from airfocus_client.models.workspace_group import WorkspaceGroup

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceGroup from a JSON string
workspace_group_instance = WorkspaceGroup.from_json(json)
# print the JSON string representation of the object
print(WorkspaceGroup.to_json())

# convert the object into a dict
workspace_group_dict = workspace_group_instance.to_dict()
# create an instance of WorkspaceGroup from a dict
workspace_group_from_dict = WorkspaceGroup.from_dict(workspace_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


