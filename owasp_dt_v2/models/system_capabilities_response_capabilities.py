from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.system_capabilities_response_capabilities_additional_property import (
        SystemCapabilitiesResponseCapabilitiesAdditionalProperty,
    )


T = TypeVar("T", bound="SystemCapabilitiesResponseCapabilities")


@_attrs_define
class SystemCapabilitiesResponseCapabilities:
    """Map of namespaces to capability flags."""

    additional_properties: dict[
        str, SystemCapabilitiesResponseCapabilitiesAdditionalProperty
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.system_capabilities_response_capabilities_additional_property import (
            SystemCapabilitiesResponseCapabilitiesAdditionalProperty,
        )

        d = dict(src_dict)
        system_capabilities_response_capabilities = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = (
                SystemCapabilitiesResponseCapabilitiesAdditionalProperty.from_dict(
                    prop_dict
                )
            )

            additional_properties[prop_name] = additional_property

        system_capabilities_response_capabilities.additional_properties = (
            additional_properties
        )
        return system_capabilities_response_capabilities

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> SystemCapabilitiesResponseCapabilitiesAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: SystemCapabilitiesResponseCapabilitiesAdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
