# CreateMilestoneRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | 
**description** | **str** |  | 
**name** | **str** |  | 
**timezone** | **str** |  | [optional] 

## Example

```python
from airfocus_client.models.create_milestone_request import CreateMilestoneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMilestoneRequest from a JSON string
create_milestone_request_instance = CreateMilestoneRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMilestoneRequest.to_json())

# convert the object into a dict
create_milestone_request_dict = create_milestone_request_instance.to_dict()
# create an instance of CreateMilestoneRequest from a dict
create_milestone_request_from_dict = CreateMilestoneRequest.from_dict(create_milestone_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


