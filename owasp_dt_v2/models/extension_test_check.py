from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.extension_test_check_status import ExtensionTestCheckStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtensionTestCheck")


@_attrs_define
class ExtensionTestCheck:
    """
    Attributes:
        name (str):  Example: connection.
        status (ExtensionTestCheckStatus):
        message (str | Unset):  Example: Connection failed.
    """

    name: str
    status: ExtensionTestCheckStatus
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status.value

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        status = ExtensionTestCheckStatus(d.pop("status"))

        message = d.pop("message", UNSET)

        extension_test_check = cls(
            name=name,
            status=status,
            message=message,
        )

        extension_test_check.additional_properties = d
        return extension_test_check

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
