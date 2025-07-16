# SetWorkspaceStatusesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replacements** | **Dict[str, str]** | A map of status replacements, where key is and OLD status-id and value is a NEW status-id. Replacements must be specified for each status being deleted from the workspace.This mapping will be used to migrate all items in the workspace to new statuses before deleting the old ones. | 
**statuses** | [**List[Status]**](Status.md) | Statuses to be set for the specified workspace. New statuses will be added to database, missing statuses will be removed from database. | [optional] 

## Example

```python
from airfocus_client.models.set_workspace_statuses_request import SetWorkspaceStatusesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetWorkspaceStatusesRequest from a JSON string
set_workspace_statuses_request_instance = SetWorkspaceStatusesRequest.from_json(json)
# print the JSON string representation of the object
print(SetWorkspaceStatusesRequest.to_json())

# convert the object into a dict
set_workspace_statuses_request_dict = set_workspace_statuses_request_instance.to_dict()
# create an instance of SetWorkspaceStatusesRequest from a dict
set_workspace_statuses_request_from_dict = SetWorkspaceStatusesRequest.from_dict(set_workspace_statuses_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


