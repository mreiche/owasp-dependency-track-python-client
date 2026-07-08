from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.total_count_type import TotalCountType

T = TypeVar("T", bound="TotalCount")


@_attrs_define
class TotalCount:
    """
    Attributes:
        count (int): The total number of records across all pages. Might be an exact count, or a lower bound. Refer to
            the `type` field for the applicable semantics.
        type_ (TotalCountType):
    """

    count: int
    type_: TotalCountType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        type_ = TotalCountType(d.pop("type"))

        total_count = cls(
            count=count,
            type_=type_,
        )

        total_count.additional_properties = d
        return total_count

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
