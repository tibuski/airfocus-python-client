# Status


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**StatusCategory**](StatusCategory.md) |  | 
**default** | **bool** | Whether this status should be applied by default to newly created items. There can be only one default status in each workspace. | 
**id** | **str** |  | 
**name** | **str** | Name of this status in UI. | 
**order** | **int** | Order of this status comparing to other statuses in the same workspace. | 
**workspace_id** | **str** |  | 
**color** | [**StatusColor**](StatusColor.md) |  | [optional] 

## Example

```python
from airfocus_client.models.status import Status

# TODO update the JSON string below
json = "{}"
# create an instance of Status from a JSON string
status_instance = Status.from_json(json)
# print the JSON string representation of the object
print(Status.to_json())

# convert the object into a dict
status_dict = status_instance.to_dict()
# create an instance of Status from a dict
status_from_dict = Status.from_dict(status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


