# WorkspaceDuplicateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duplicate_permissions** | **bool** | Whether to also duplicate all user-permissions to the new workspace. | 

## Example

```python
from airfocus_client.models.workspace_duplicate_request import WorkspaceDuplicateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceDuplicateRequest from a JSON string
workspace_duplicate_request_instance = WorkspaceDuplicateRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceDuplicateRequest.to_json())

# convert the object into a dict
workspace_duplicate_request_dict = workspace_duplicate_request_instance.to_dict()
# create an instance of WorkspaceDuplicateRequest from a dict
workspace_duplicate_request_from_dict = WorkspaceDuplicateRequest.from_dict(workspace_duplicate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


