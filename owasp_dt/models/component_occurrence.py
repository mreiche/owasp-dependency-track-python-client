from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComponentOccurrence")


@_attrs_define
class ComponentOccurrence:
    """
    Attributes:
        created_at (int | Unset): UNIX epoch timestamp in milliseconds
        id (UUID | Unset):
        line (int | Unset):
        location (str | Unset):
        offset (int | Unset):
        symbol (str | Unset):
    """

    created_at: int | Unset = UNSET
    id: UUID | Unset = UNSET
    line: int | Unset = UNSET
    location: str | Unset = UNSET
    offset: int | Unset = UNSET
    symbol: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        line = self.line

        location = self.location

        offset = self.offset

        symbol = self.symbol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if line is not UNSET:
            field_dict["line"] = line
        if location is not UNSET:
            field_dict["location"] = location
        if offset is not UNSET:
            field_dict["offset"] = offset
        if symbol is not UNSET:
            field_dict["symbol"] = symbol

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("createdAt", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        line = d.pop("line", UNSET)

        location = d.pop("location", UNSET)

        offset = d.pop("offset", UNSET)

        symbol = d.pop("symbol", UNSET)

        component_occurrence = cls(
            created_at=created_at,
            id=id,
            line=line,
            location=location,
            offset=offset,
            symbol=symbol,
        )

        component_occurrence.additional_properties = d
        return component_occurrence

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
