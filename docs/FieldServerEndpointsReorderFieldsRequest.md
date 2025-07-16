# FieldServerEndpointsReorderFieldsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** |  | 
**field_ids** | **List[str]** |  | [optional] 

## Example

```python
from airfocus_client.models.field_server_endpoints_reorder_fields_request import FieldServerEndpointsReorderFieldsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FieldServerEndpointsReorderFieldsRequest from a JSON string
field_server_endpoints_reorder_fields_request_instance = FieldServerEndpointsReorderFieldsRequest.from_json(json)
# print the JSON string representation of the object
print(FieldServerEndpointsReorderFieldsRequest.to_json())

# convert the object into a dict
field_server_endpoints_reorder_fields_request_dict = field_server_endpoints_reorder_fields_request_instance.to_dict()
# create an instance of FieldServerEndpointsReorderFieldsRequest from a dict
field_server_endpoints_reorder_fields_request_from_dict = FieldServerEndpointsReorderFieldsRequest.from_dict(field_server_endpoints_reorder_fields_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


