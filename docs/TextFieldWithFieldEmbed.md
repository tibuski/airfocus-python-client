# TextFieldWithFieldEmbed


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
from airfocus_client.models.text_field_with_field_embed import TextFieldWithFieldEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of TextFieldWithFieldEmbed from a JSON string
text_field_with_field_embed_instance = TextFieldWithFieldEmbed.from_json(json)
# print the JSON string representation of the object
print(TextFieldWithFieldEmbed.to_json())

# convert the object into a dict
text_field_with_field_embed_dict = text_field_with_field_embed_instance.to_dict()
# create an instance of TextFieldWithFieldEmbed from a dict
text_field_with_field_embed_from_dict = TextFieldWithFieldEmbed.from_dict(text_field_with_field_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


