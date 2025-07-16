# TimePeriodFieldSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_id** | **str** |  | 
**multi** | **bool** |  | 
**time_periods** | [**List[TimePeriod]**](TimePeriod.md) |  | [optional] 

## Example

```python
from airfocus_client.models.time_period_field_settings import TimePeriodFieldSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TimePeriodFieldSettings from a JSON string
time_period_field_settings_instance = TimePeriodFieldSettings.from_json(json)
# print the JSON string representation of the object
print(TimePeriodFieldSettings.to_json())

# convert the object into a dict
time_period_field_settings_dict = time_period_field_settings_instance.to_dict()
# create an instance of TimePeriodFieldSettings from a dict
time_period_field_settings_from_dict = TimePeriodFieldSettings.from_dict(time_period_field_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


