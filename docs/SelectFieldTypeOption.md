# SelectFieldTypeOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **bool** |  | 
**description** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**color** | [**SelectFieldOptionColor**](SelectFieldOptionColor.md) |  | [optional] 
**numeric_value** | **float** |  | [optional] 

## Example

```python
from airfocus_client.models.select_field_type_option import SelectFieldTypeOption

# TODO update the JSON string below
json = "{}"
# create an instance of SelectFieldTypeOption from a JSON string
select_field_type_option_instance = SelectFieldTypeOption.from_json(json)
# print the JSON string representation of the object
print(SelectFieldTypeOption.to_json())

# convert the object into a dict
select_field_type_option_dict = select_field_type_option_instance.to_dict()
# create an instance of SelectFieldTypeOption from a dict
select_field_type_option_from_dict = SelectFieldTypeOption.from_dict(select_field_type_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


