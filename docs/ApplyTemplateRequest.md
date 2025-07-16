# ApplyTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**TemplateParameters**](TemplateParameters.md) |  | 
**permissions** | [**Dict[str, Permission]**](Permission.md) |  | 
**default_permission** | [**Permission**](Permission.md) |  | [optional] 
**group_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from airfocus_client.models.apply_template_request import ApplyTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyTemplateRequest from a JSON string
apply_template_request_instance = ApplyTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(ApplyTemplateRequest.to_json())

# convert the object into a dict
apply_template_request_dict = apply_template_request_instance.to_dict()
# create an instance of ApplyTemplateRequest from a dict
apply_template_request_from_dict = ApplyTemplateRequest.from_dict(apply_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


