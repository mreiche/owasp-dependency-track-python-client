from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_workload_identity_provider_request_jwks import (
        UpdateWorkloadIdentityProviderRequestJwks,
    )


T = TypeVar("T", bound="UpdateWorkloadIdentityProviderRequest")


@_attrs_define
class UpdateWorkloadIdentityProviderRequest:
    """
    Attributes:
        issuer (str | Unset): The expected `iss` claim for `OIDC` providers, or the SPIFFE trust domain for `SPIFFE`
            providers, such as `example.org`. Example: https://token.actions.githubusercontent.com.
        audience (str | Unset): The value that the token's `aud` claim must contain. Example: https://dependency-
            track.example.com.
        jwks_url (str | Unset): The URL to fetch the signing keys from. Must be `https`. Example:
            https://example.org/keys.
        jwks (UpdateWorkloadIdentityProviderRequestJwks | Unset): An RFC 7517 JSON Web Key Set holding the issuer's
            public signing keys.
        session_lifetime_seconds (int | Unset): The lifetime of sessions created through this provider, unless a binding
            sets its own. Example: 3600.
    """

    issuer: str | Unset = UNSET
    audience: str | Unset = UNSET
    jwks_url: str | Unset = UNSET
    jwks: UpdateWorkloadIdentityProviderRequestJwks | Unset = UNSET
    session_lifetime_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issuer = self.issuer

        audience = self.audience

        jwks_url = self.jwks_url

        jwks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.jwks, Unset):
            jwks = self.jwks.to_dict()

        session_lifetime_seconds = self.session_lifetime_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if audience is not UNSET:
            field_dict["audience"] = audience
        if jwks_url is not UNSET:
            field_dict["jwks_url"] = jwks_url
        if jwks is not UNSET:
            field_dict["jwks"] = jwks
        if session_lifetime_seconds is not UNSET:
            field_dict["session_lifetime_seconds"] = session_lifetime_seconds

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.update_workload_identity_provider_request_jwks import (
            UpdateWorkloadIdentityProviderRequestJwks,
        )

        d = dict(src_dict)
        issuer = d.pop("issuer", UNSET)

        audience = d.pop("audience", UNSET)

        jwks_url = d.pop("jwks_url", UNSET)

        _jwks = d.pop("jwks", UNSET)
        jwks: UpdateWorkloadIdentityProviderRequestJwks | Unset
        if isinstance(_jwks, Unset):
            jwks = UNSET
        else:
            jwks = UpdateWorkloadIdentityProviderRequestJwks.from_dict(_jwks)

        session_lifetime_seconds = d.pop("session_lifetime_seconds", UNSET)

        update_workload_identity_provider_request = cls(
            issuer=issuer,
            audience=audience,
            jwks_url=jwks_url,
            jwks=jwks,
            session_lifetime_seconds=session_lifetime_seconds,
        )

        update_workload_identity_provider_request.additional_properties = d
        return update_workload_identity_provider_request

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
