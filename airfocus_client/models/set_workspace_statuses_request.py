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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from airfocus_client.models.status import Status
from typing import Optional, Set
from typing_extensions import Self

class SetWorkspaceStatusesRequest(BaseModel):
    """
    SetWorkspaceStatusesRequest
    """ # noqa: E501
    replacements: Dict[str, StrictStr] = Field(description="A map of status replacements, where key is and OLD status-id and value is a NEW status-id. Replacements must be specified for each status being deleted from the workspace.This mapping will be used to migrate all items in the workspace to new statuses before deleting the old ones.")
    statuses: Optional[List[Status]] = Field(default=None, description="Statuses to be set for the specified workspace. New statuses will be added to database, missing statuses will be removed from database.")
    __properties: ClassVar[List[str]] = ["replacements", "statuses"]

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
        """Create an instance of SetWorkspaceStatusesRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in statuses (list)
        _items = []
        if self.statuses:
            for _item_statuses in self.statuses:
                if _item_statuses:
                    _items.append(_item_statuses.to_dict())
            _dict['statuses'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SetWorkspaceStatusesRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "replacements": obj.get("replacements"),
            "statuses": [Status.from_dict(_item) for _item in obj["statuses"]] if obj.get("statuses") is not None else None
        })
        return _obj


