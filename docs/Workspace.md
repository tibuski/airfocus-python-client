# Workspace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Timestamp of when this workspace was created. | 
**description** | [**RichText**](RichText.md) | Description of this workspace. | 
**id** | **str** | Unique identifier of this workspace. | 
**last_updated_at** | **datetime** | Timestamp of when this workspace was last updated. | 
**name** | **str** | Name of this workspace. | 
**namespace** | [**WorkspaceNamespace**](WorkspaceNamespace.md) | The system namespace of this workspace. | 
**order** | **int** | Order number of this workspace for sorting. | 
**progress_mode** | [**WorkspaceProgressMode**](WorkspaceProgressMode.md) |  | 
**team_id** | **str** | Id of the team this workspace belongs to. | 
**alias** | **str** | A custom code of this workspace (e.g. PROD, DEV, etc), which is used to create aliases for items (e.g. DEV-123). Alias should consist of 1-10 uppercase letters, and should be unique within the team. | [optional] 
**default_permission** | [**Permission**](Permission.md) | Default permission for all the team members in this workspace. Note: the final permission can be adjusted corresponding to each user&#39;s role, e.g. contributors can&#39;t have more than Comment permission. | [optional] 
**item_color** | [**ItemColor**](ItemColor.md) | Default color applied to newly created items in this workspace. If not defined - a random color will be assigned to each new item. | [optional] 
**item_type** | [**ItemType**](ItemType.md) | Type of items in this workspace. | [optional] 
**metadata** | [**WorkspaceWorkspaceMetadata**](WorkspaceWorkspaceMetadata.md) |  | [optional] 

## Example

```python
from airfocus_client.models.workspace import Workspace

# TODO update the JSON string below
json = "{}"
# create an instance of Workspace from a JSON string
workspace_instance = Workspace.from_json(json)
# print the JSON string representation of the object
print(Workspace.to_json())

# convert the object into a dict
workspace_dict = workspace_instance.to_dict()
# create an instance of Workspace from a dict
workspace_from_dict = Workspace.from_dict(workspace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


