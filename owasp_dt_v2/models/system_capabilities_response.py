from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.system_capabilities_response_capabilities import (
        SystemCapabilitiesResponseCapabilities,
    )


T = TypeVar("T", bound="SystemCapabilitiesResponse")


@_attrs_define
class SystemCapabilitiesResponse:
    """
    Example:
        {'capabilities': {'secret_management': {'read_only': False}}}

    Attributes:
        capabilities (SystemCapabilitiesResponseCapabilities): Map of namespaces to capability flags.
    """

    capabilities: SystemCapabilitiesResponseCapabilities
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        capabilities = self.capabilities.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "capabilities": capabilities,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.system_capabilities_response_capabilities import (
            SystemCapabilitiesResponseCapabilities,
        )

        d = dict(src_dict)
        capabilities = SystemCapabilitiesResponseCapabilities.from_dict(
            d.pop("capabilities")
        )

        system_capabilities_response = cls(
            capabilities=capabilities,
        )

        system_capabilities_response.additional_properties = d
        return system_capabilities_response

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
