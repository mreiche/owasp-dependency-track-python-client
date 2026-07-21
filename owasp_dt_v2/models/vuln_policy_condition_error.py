from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VulnPolicyConditionError")


@_attrs_define
class VulnPolicyConditionError:
    """
    Attributes:
        line (int): Line number where the error occurred
        column (int): Column number where the error occurred
        message (str): Description of the error
    """

    line: int
    column: int
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        line = self.line

        column = self.column

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "line": line,
                "column": column,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        line = d.pop("line")

        column = d.pop("column")

        message = d.pop("message")

        vuln_policy_condition_error = cls(
            line=line,
            column=column,
            message=message,
        )

        vuln_policy_condition_error.additional_properties = d
        return vuln_policy_condition_error

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
