# UpdateWorkspaceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**RichText**](RichText.md) | Description of this workspace. | 
**name** | **str** | Name of this workspace. | 
**order** | **int** | Order number of this workspace for sorting. | 
**alias** | **str** | A custom code of this workspace (e.g. PROD, DEV, etc), which is used to create aliases for items (e.g. DEV-123). Alias should consist of 1-10 uppercase letters, and should be unique within the team. | [optional] 
**default_permission** | [**Permission**](Permission.md) | Default permission for all the team members in this workspace. Note: the final permission can be adjusted corresponding to each user&#39;s role, e.g. contributors can&#39;t have more than Comment permission. | [optional] 
**item_color** | [**ItemColor**](ItemColor.md) | Default color applied to newly created items in this workspace. If not defined - a random color will be assigned to each new item. | [optional] 
**item_type** | [**ItemType**](ItemType.md) | Type of items in this workspace. | [optional] 
**progress_mode** | [**WorkspaceProgressMode**](WorkspaceProgressMode.md) |  | [optional] 

## Example

```python
from airfocus_client.models.update_workspace_request import UpdateWorkspaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkspaceRequest from a JSON string
update_workspace_request_instance = UpdateWorkspaceRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWorkspaceRequest.to_json())

# convert the object into a dict
update_workspace_request_dict = update_workspace_request_instance.to_dict()
# create an instance of UpdateWorkspaceRequest from a dict
update_workspace_request_from_dict = UpdateWorkspaceRequest.from_dict(update_workspace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


