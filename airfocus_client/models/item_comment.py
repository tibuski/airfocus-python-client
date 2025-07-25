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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from airfocus_client.models.item_comment_reaction import ItemCommentReaction
from airfocus_client.models.rich_text import RichText
from typing import Optional, Set
from typing_extensions import Self

class ItemComment(BaseModel):
    """
    ItemComment
    """ # noqa: E501
    content: RichText
    created_at: datetime = Field(alias="createdAt")
    id: StrictStr
    item_id: StrictStr = Field(alias="itemId")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    user_id: StrictStr = Field(alias="userId")
    reactions: Optional[List[ItemCommentReaction]] = None
    __properties: ClassVar[List[str]] = ["content", "createdAt", "id", "itemId", "lastUpdatedAt", "userId", "reactions"]

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
        """Create an instance of ItemComment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of content
        if self.content:
            _dict['content'] = self.content.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in reactions (list)
        _items = []
        if self.reactions:
            for _item_reactions in self.reactions:
                if _item_reactions:
                    _items.append(_item_reactions.to_dict())
            _dict['reactions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ItemComment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "content": RichText.from_dict(obj["content"]) if obj.get("content") is not None else None,
            "createdAt": obj.get("createdAt"),
            "id": obj.get("id"),
            "itemId": obj.get("itemId"),
            "lastUpdatedAt": obj.get("lastUpdatedAt"),
            "userId": obj.get("userId"),
            "reactions": [ItemCommentReaction.from_dict(_item) for _item in obj["reactions"]] if obj.get("reactions") is not None else None
        })
        return _obj


