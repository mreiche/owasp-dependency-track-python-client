from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateOauthTokenResponse")


@_attrs_define
class CreateOauthTokenResponse:
    """
    Attributes:
        access_token (str): An access token.
        issued_token_type (str): Always `urn:ietf:params:oauth:token-type:access_token`. Example:
            urn:ietf:params:oauth:token-type:access_token.
        token_type (str): Always `Bearer`. Example: Bearer.
        expires_in (int): How many seconds the access token is valid for. For token exchange, this is the workload
            identity provider's `session_lifetime_seconds`. Example: 3600.
    """

    access_token: str
    issued_token_type: str
    token_type: str
    expires_in: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        issued_token_type = self.issued_token_type

        token_type = self.token_type

        expires_in = self.expires_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_token": access_token,
                "issued_token_type": issued_token_type,
                "token_type": token_type,
                "expires_in": expires_in,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        access_token = d.pop("access_token")

        issued_token_type = d.pop("issued_token_type")

        token_type = d.pop("token_type")

        expires_in = d.pop("expires_in")

        create_oauth_token_response = cls(
            access_token=access_token,
            issued_token_type=issued_token_type,
            token_type=token_type,
            expires_in=expires_in,
        )

        create_oauth_token_response.additional_properties = d
        return create_oauth_token_response

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
