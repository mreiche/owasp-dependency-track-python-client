from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiKey")


@_attrs_define
class ApiKey:
    """
    Attributes:
        comment (str | Unset):
        created (int | Unset): UNIX epoch timestamp in milliseconds
        key (str | Unset):
        last_used (int | Unset): UNIX epoch timestamp in milliseconds
        legacy (bool | Unset):
        masked_key (str | Unset):
        public_id (str | Unset):
    """

    comment: str | Unset = UNSET
    created: int | Unset = UNSET
    key: str | Unset = UNSET
    last_used: int | Unset = UNSET
    legacy: bool | Unset = UNSET
    masked_key: str | Unset = UNSET
    public_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        created = self.created

        key = self.key

        last_used = self.last_used

        legacy = self.legacy

        masked_key = self.masked_key

        public_id = self.public_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if created is not UNSET:
            field_dict["created"] = created
        if key is not UNSET:
            field_dict["key"] = key
        if last_used is not UNSET:
            field_dict["lastUsed"] = last_used
        if legacy is not UNSET:
            field_dict["legacy"] = legacy
        if masked_key is not UNSET:
            field_dict["maskedKey"] = masked_key
        if public_id is not UNSET:
            field_dict["publicId"] = public_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        comment = d.pop("comment", UNSET)

        created = d.pop("created", UNSET)

        key = d.pop("key", UNSET)

        last_used = d.pop("lastUsed", UNSET)

        legacy = d.pop("legacy", UNSET)

        masked_key = d.pop("maskedKey", UNSET)

        public_id = d.pop("publicId", UNSET)

        api_key = cls(
            comment=comment,
            created=created,
            key=key,
            last_used=last_used,
            legacy=legacy,
            masked_key=masked_key,
            public_id=public_id,
        )

        api_key.additional_properties = d
        return api_key

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
