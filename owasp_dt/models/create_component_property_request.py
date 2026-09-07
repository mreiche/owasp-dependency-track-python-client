from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_component_property_request_property_type import (
    CreateComponentPropertyRequestPropertyType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateComponentPropertyRequest")


@_attrs_define
class CreateComponentPropertyRequest:
    """
    Attributes:
        property_name (str): Name of the property
        property_type (CreateComponentPropertyRequestPropertyType): Type of the property
        description (str | Unset): Description of the property
        group_name (str | Unset): Group the property belongs to
        property_value (str | Unset): Value of the property
    """

    property_name: str
    property_type: CreateComponentPropertyRequestPropertyType
    description: str | Unset = UNSET
    group_name: str | Unset = UNSET
    property_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        property_name = self.property_name

        property_type = self.property_type.value

        description = self.description

        group_name = self.group_name

        property_value = self.property_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "propertyName": property_name,
                "propertyType": property_type,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if group_name is not UNSET:
            field_dict["groupName"] = group_name
        if property_value is not UNSET:
            field_dict["propertyValue"] = property_value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        property_name = d.pop("propertyName")

        property_type = CreateComponentPropertyRequestPropertyType(
            d.pop("propertyType")
        )

        description = d.pop("description", UNSET)

        group_name = d.pop("groupName", UNSET)

        property_value = d.pop("propertyValue", UNSET)

        create_component_property_request = cls(
            property_name=property_name,
            property_type=property_type,
            description=description,
            group_name=group_name,
            property_value=property_value,
        )

        create_component_property_request.additional_properties = d
        return create_component_property_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
