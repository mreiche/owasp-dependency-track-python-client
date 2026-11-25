from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceAccountApiKey")


@_attrs_define
class ServiceAccountApiKey:
    """
    Attributes:
        public_id (str): The public, non-secret portion of the key. Example: a1b2c3d4.
        comment (str | Unset):
        created_at (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
        last_used_at (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
        expires_at (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
    """

    public_id: str
    comment: str | Unset = UNSET
    created_at: int | Unset = UNSET
    last_used_at: int | Unset = UNSET
    expires_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_id = self.public_id

        comment = self.comment

        created_at = self.created_at

        last_used_at = self.last_used_at

        expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "public_id": public_id,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if last_used_at is not UNSET:
            field_dict["last_used_at"] = last_used_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        public_id = d.pop("public_id")

        comment = d.pop("comment", UNSET)

        created_at = d.pop("created_at", UNSET)

        last_used_at = d.pop("last_used_at", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        service_account_api_key = cls(
            public_id=public_id,
            comment=comment,
            created_at=created_at,
            last_used_at=last_used_at,
            expires_at=expires_at,
        )

        service_account_api_key.additional_properties = d
        return service_account_api_key

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
