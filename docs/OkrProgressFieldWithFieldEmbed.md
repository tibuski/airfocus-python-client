# OkrProgressFieldWithFieldEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**FieldEmbed**](FieldEmbed.md) |  | 
**created_at** | **datetime** |  | 
**description** | **str** |  | 
**id** | **str** |  | 
**is_team_field** | **bool** |  | 
**name** | **str** |  | 
**team_id** | **str** |  | 
**type_id** | **str** |  | 

## Example

```python
from airfocus_client.models.okr_progress_field_with_field_embed import OkrProgressFieldWithFieldEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of OkrProgressFieldWithFieldEmbed from a JSON string
okr_progress_field_with_field_embed_instance = OkrProgressFieldWithFieldEmbed.from_json(json)
# print the JSON string representation of the object
print(OkrProgressFieldWithFieldEmbed.to_json())

# convert the object into a dict
okr_progress_field_with_field_embed_dict = okr_progress_field_with_field_embed_instance.to_dict()
# create an instance of OkrProgressFieldWithFieldEmbed from a dict
okr_progress_field_with_field_embed_from_dict = OkrProgressFieldWithFieldEmbed.from_dict(okr_progress_field_with_field_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


