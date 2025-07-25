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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from airfocus_client.models.item_color import ItemColor
from airfocus_client.models.item_embed import ItemEmbed
from typing import Optional, Set
from typing_extensions import Self

class ItemWithMDWithItemEmbed(BaseModel):
    """
    Item with Markdown string description.
    """ # noqa: E501
    embedded: ItemEmbed = Field(alias="_embedded")
    archived: StrictBool = Field(description="Whether this item is archived.")
    color: ItemColor = Field(description="Color of this item.")
    created_at: datetime = Field(description="Timestamp of when this item was created.", alias="createdAt")
    description: StrictStr = Field(description="Rich-text as markdown string.")
    fields: Dict[str, Any] = Field(description="Values of custom fields, where each key is a custom-field ID and each value is a JSON-formatted value of the corresponding field.")
    id: StrictStr = Field(description="Unique identifier of this item.")
    last_updated_at: datetime = Field(description="Timestamp of when this item was last updated.", alias="lastUpdatedAt")
    name: StrictStr = Field(description="Name (title) of this item.")
    order: StrictInt = Field(description="A order number of this item for sorting.")
    status_id: StrictStr = Field(description="Id of the status of this item.", alias="statusId")
    workspace_id: StrictStr = Field(description="Id of the workspace this workspace belongs to.", alias="workspaceId")
    assignee_user_ids: Optional[List[StrictStr]] = Field(default=None, description="Ids of users who are assigned to this item.", alias="assigneeUserIds")
    number: Optional[StrictInt] = Field(default=None, description="A numeric id of this item, which is used to create an alias to this item like DEV-123. The number is unique within the workspace, and defined by server on item creation.")
    status_category_updated_at: Optional[datetime] = Field(default=None, description="Timestamp of when the status of this item was last time switched from one category to another.", alias="statusCategoryUpdatedAt")
    status_updated_at: Optional[datetime] = Field(default=None, description="Timestamp of when the status of this item was last updated.", alias="statusUpdatedAt")
    __properties: ClassVar[List[str]] = ["_embedded", "archived", "color", "createdAt", "description", "fields", "id", "lastUpdatedAt", "name", "order", "statusId", "workspaceId", "assigneeUserIds", "number", "statusCategoryUpdatedAt", "statusUpdatedAt"]

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
        """Create an instance of ItemWithMDWithItemEmbed from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of embedded
        if self.embedded:
            _dict['_embedded'] = self.embedded.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ItemWithMDWithItemEmbed from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_embedded": ItemEmbed.from_dict(obj["_embedded"]) if obj.get("_embedded") is not None else None,
            "archived": obj.get("archived"),
            "color": obj.get("color"),
            "createdAt": obj.get("createdAt"),
            "description": obj.get("description"),
            "fields": obj.get("fields"),
            "id": obj.get("id"),
            "lastUpdatedAt": obj.get("lastUpdatedAt"),
            "name": obj.get("name"),
            "order": obj.get("order"),
            "statusId": obj.get("statusId"),
            "workspaceId": obj.get("workspaceId"),
            "assigneeUserIds": obj.get("assigneeUserIds"),
            "number": obj.get("number"),
            "statusCategoryUpdatedAt": obj.get("statusCategoryUpdatedAt"),
            "statusUpdatedAt": obj.get("statusUpdatedAt")
        })
        return _obj


