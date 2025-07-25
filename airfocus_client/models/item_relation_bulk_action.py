# coding: utf-8

"""
    airfocus API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0-beta.37.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from airfocus_client.models.item_relation_bulk_create import ItemRelationBulkCreate
from airfocus_client.models.item_relation_bulk_delete import ItemRelationBulkDelete
from airfocus_client.models.item_relation_bulk_patch import ItemRelationBulkPatch
from airfocus_client.models.item_relation_bulk_update import ItemRelationBulkUpdate
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

ITEMRELATIONBULKACTION_ONE_OF_SCHEMAS = ["ItemRelationBulkCreate", "ItemRelationBulkDelete", "ItemRelationBulkPatch", "ItemRelationBulkUpdate"]

class ItemRelationBulkAction(BaseModel):
    """
    ItemRelationBulkAction
    """
    # data type: ItemRelationBulkCreate
    oneof_schema_1_validator: Optional[ItemRelationBulkCreate] = None
    # data type: ItemRelationBulkDelete
    oneof_schema_2_validator: Optional[ItemRelationBulkDelete] = None
    # data type: ItemRelationBulkPatch
    oneof_schema_3_validator: Optional[ItemRelationBulkPatch] = None
    # data type: ItemRelationBulkUpdate
    oneof_schema_4_validator: Optional[ItemRelationBulkUpdate] = None
    actual_instance: Optional[Union[ItemRelationBulkCreate, ItemRelationBulkDelete, ItemRelationBulkPatch, ItemRelationBulkUpdate]] = None
    one_of_schemas: Set[str] = { "ItemRelationBulkCreate", "ItemRelationBulkDelete", "ItemRelationBulkPatch", "ItemRelationBulkUpdate" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = ItemRelationBulkAction.model_construct()
        error_messages = []
        match = 0
        # validate data type: ItemRelationBulkCreate
        if not isinstance(v, ItemRelationBulkCreate):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ItemRelationBulkCreate`")
        else:
            match += 1
        # validate data type: ItemRelationBulkDelete
        if not isinstance(v, ItemRelationBulkDelete):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ItemRelationBulkDelete`")
        else:
            match += 1
        # validate data type: ItemRelationBulkPatch
        if not isinstance(v, ItemRelationBulkPatch):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ItemRelationBulkPatch`")
        else:
            match += 1
        # validate data type: ItemRelationBulkUpdate
        if not isinstance(v, ItemRelationBulkUpdate):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ItemRelationBulkUpdate`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ItemRelationBulkAction with oneOf schemas: ItemRelationBulkCreate, ItemRelationBulkDelete, ItemRelationBulkPatch, ItemRelationBulkUpdate. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ItemRelationBulkAction with oneOf schemas: ItemRelationBulkCreate, ItemRelationBulkDelete, ItemRelationBulkPatch, ItemRelationBulkUpdate. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into ItemRelationBulkCreate
        try:
            instance.actual_instance = ItemRelationBulkCreate.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ItemRelationBulkDelete
        try:
            instance.actual_instance = ItemRelationBulkDelete.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ItemRelationBulkPatch
        try:
            instance.actual_instance = ItemRelationBulkPatch.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ItemRelationBulkUpdate
        try:
            instance.actual_instance = ItemRelationBulkUpdate.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ItemRelationBulkAction with oneOf schemas: ItemRelationBulkCreate, ItemRelationBulkDelete, ItemRelationBulkPatch, ItemRelationBulkUpdate. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ItemRelationBulkAction with oneOf schemas: ItemRelationBulkCreate, ItemRelationBulkDelete, ItemRelationBulkPatch, ItemRelationBulkUpdate. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], ItemRelationBulkCreate, ItemRelationBulkDelete, ItemRelationBulkPatch, ItemRelationBulkUpdate]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


