# WorkspaceWorkspaceMetadata

Additional metadata about this workspace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duplicated** | **bool** | Whether this workspace was duplicated from another workspace. | 
**template_id** | **str** | Id of the template used to create this workspace. | [optional] 
**template_workspace_ref** | **str** | Which specific workspace-instruction in the template was used to create this workspace. | [optional] 
**version** | **str** | Version of the server at the moment when this workspace was created. | [optional] 

## Example

```python
from airfocus_client.models.workspace_workspace_metadata import WorkspaceWorkspaceMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceWorkspaceMetadata from a JSON string
workspace_workspace_metadata_instance = WorkspaceWorkspaceMetadata.from_json(json)
# print the JSON string representation of the object
print(WorkspaceWorkspaceMetadata.to_json())

# convert the object into a dict
workspace_workspace_metadata_dict = workspace_workspace_metadata_instance.to_dict()
# create an instance of WorkspaceWorkspaceMetadata from a dict
workspace_workspace_metadata_from_dict = WorkspaceWorkspaceMetadata.from_dict(workspace_workspace_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


