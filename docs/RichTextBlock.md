# RichTextBlock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment_id** | **str** |  | 
**content_type** | **str** |  | 
**content** | [**List[RichTextInline]**](RichTextInline.md) |  | 
**id** | **str** |  | 
**raw** | **str** |  | 
**url** | **str** |  | 
**level** | **int** |  | 
**ordered** | **bool** |  | 
**color_hex** | **str** |  | 
**caption** | **str** |  | [optional] 
**meta** | **object** |  | [optional] 
**width** | **int** |  | [optional] 
**language** | **str** |  | [optional] 
**height** | **int** |  | [optional] 
**bullet_list_marker** | **str** |  | [optional] 
**items** | [**List[RichTextListItem]**](RichTextListItem.md) |  | [optional] 
**ordered_list_delimiter** | **str** |  | [optional] 
**ordered_list_starts_at** | **int** |  | [optional] 

## Example

```python
from airfocus_client.models.rich_text_block import RichTextBlock

# TODO update the JSON string below
json = "{}"
# create an instance of RichTextBlock from a JSON string
rich_text_block_instance = RichTextBlock.from_json(json)
# print the JSON string representation of the object
print(RichTextBlock.to_json())

# convert the object into a dict
rich_text_block_dict = rich_text_block_instance.to_dict()
# create an instance of RichTextBlock from a dict
rich_text_block_from_dict = RichTextBlock.from_dict(rich_text_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


