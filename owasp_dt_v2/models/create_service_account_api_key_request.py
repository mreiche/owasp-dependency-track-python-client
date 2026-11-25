from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateServiceAccountApiKeyRequest")


@_attrs_define
class CreateServiceAccountApiKeyRequest:
    """
    Attributes:
        comment (str | Unset):
        expires_in_days (int | Unset): Number of days from now after which the key expires. Must not exceed the maximum
            lifetime configured with `dt.api-key.max-lifetime-days` (366 days by default). Defaults to 30 days, or the
            maximum lifetime if that is shorter.
    """

    comment: str | Unset = UNSET
    expires_in_days: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        expires_in_days = self.expires_in_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if expires_in_days is not UNSET:
            field_dict["expires_in_days"] = expires_in_days

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        comment = d.pop("comment", UNSET)

        expires_in_days = d.pop("expires_in_days", UNSET)

        create_service_account_api_key_request = cls(
            comment=comment,
            expires_in_days=expires_in_days,
        )

        create_service_account_api_key_request.additional_properties = d
        return create_service_account_api_key_request

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
