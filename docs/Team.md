# Team


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**flags** | [**TeamFlags**](TeamFlags.md) |  | 
**name** | **str** |  | 
**slug** | **str** |  | 
**state** | [**TeamState**](TeamState.md) |  | 
**team_id** | **str** |  | 
**updated_at** | **datetime** |  | 
**company_info** | [**TeamCompanyInfo**](TeamCompanyInfo.md) |  | [optional] 

## Example

```python
from airfocus_client.models.team import Team

# TODO update the JSON string below
json = "{}"
# create an instance of Team from a JSON string
team_instance = Team.from_json(json)
# print the JSON string representation of the object
print(Team.to_json())

# convert the object into a dict
team_dict = team_instance.to_dict()
# create an instance of Team from a dict
team_from_dict = Team.from_dict(team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


