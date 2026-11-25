from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateServiceAccountApiKeyResponse")


@_attrs_define
class CreateServiceAccountApiKeyResponse:
    """
    Attributes:
        public_id (str):  Example: a1b2c3d4.
        key (str): The full, plain text key. It is returned exactly once, at creation time, and cannot be retrieved
            again.
        expires_at (int): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
    """

    public_id: str
    key: str
    expires_at: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_id = self.public_id

        key = self.key

        expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "public_id": public_id,
                "key": key,
                "expires_at": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        public_id = d.pop("public_id")

        key = d.pop("key")

        expires_at = d.pop("expires_at")

        create_service_account_api_key_response = cls(
            public_id=public_id,
            key=key,
            expires_at=expires_at,
        )

        create_service_account_api_key_response.additional_properties = d
        return create_service_account_api_key_response

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
