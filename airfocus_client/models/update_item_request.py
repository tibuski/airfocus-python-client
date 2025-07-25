# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.37.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from airfocus_client.models.item_color import ItemColor
from airfocus_client.models.rich_text import RichText
from typing import Optional, Set
from typing_extensions import Self

class UpdateItemRequest(BaseModel):
    """
    UpdateItemRequest
    """ # noqa: E501
    color: ItemColor = Field(description="Color of this item.")
    description: RichText
    fields: Dict[str, Any] = Field(description="Values of custom fields, where each key is a custom-field ID and each value is a JSON-formatted value of the corresponding field.")
    name: StrictStr = Field(description="Name (title) of this item.")
    order: StrictInt = Field(description="A order number of this item for sorting.")
    status_id: StrictStr = Field(description="Id of the status of this item.", alias="statusId")
    archived: Optional[StrictBool] = Field(default=False, description="Whether this item is archived.")
    assignee_user_ids: Optional[List[StrictStr]] = Field(default=None, description="Ids of users who are assigned to this item.", alias="assigneeUserIds")
    __properties: ClassVar[List[str]] = ["color", "description", "fields", "name", "order", "statusId", "archived", "assigneeUserIds"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UpdateItemRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['description'] = self.description.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateItemRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "color": obj.get("color"),
            "description": RichText.from_dict(obj["description"]) if obj.get("description") is not None else None,
            "fields": obj.get("fields"),
            "name": obj.get("name"),
            "order": obj.get("order"),
            "statusId": obj.get("statusId"),
            "archived": obj.get("archived") if obj.get("archived") is not None else False,
            "assigneeUserIds": obj.get("assigneeUserIds")
        })
        return _obj


