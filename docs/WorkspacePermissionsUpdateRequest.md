# WorkspacePermissionsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**Dict[str, Permission]**](Permission.md) | Explicit permissions for specific users in the team. | 
**default_permission** | [**Permission**](Permission.md) |  | [optional] 

## Example

```python
from airfocus_client.models.workspace_permissions_update_request import WorkspacePermissionsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspacePermissionsUpdateRequest from a JSON string
workspace_permissions_update_request_instance = WorkspacePermissionsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspacePermissionsUpdateRequest.to_json())

# convert the object into a dict
workspace_permissions_update_request_dict = workspace_permissions_update_request_instance.to_dict()
# create an instance of WorkspacePermissionsUpdateRequest from a dict
workspace_permissions_update_request_from_dict = WorkspacePermissionsUpdateRequest.from_dict(workspace_permissions_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


