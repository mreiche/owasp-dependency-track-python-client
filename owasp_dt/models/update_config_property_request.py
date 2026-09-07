from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateConfigPropertyRequest")


@_attrs_define
class UpdateConfigPropertyRequest:
    """
    Attributes:
        group_name (str): Group the property belongs to
        property_name (str): Name of the property
        property_value (str | Unset): Value of the property
    """

    group_name: str
    property_name: str
    property_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_name = self.group_name

        property_name = self.property_name

        property_value = self.property_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "groupName": group_name,
                "propertyName": property_name,
            }
        )
        if property_value is not UNSET:
            field_dict["propertyValue"] = property_value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        group_name = d.pop("groupName")

        property_name = d.pop("propertyName")

        property_value = d.pop("propertyValue", UNSET)

        update_config_property_request = cls(
            group_name=group_name,
            property_name=property_name,
            property_value=property_value,
        )

        update_config_property_request.additional_properties = d
        return update_config_property_request

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
