from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workload_identity_provider_type import WorkloadIdentityProviderType
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkloadIdentityProvider")


@_attrs_define
class WorkloadIdentityProvider:
    """
    Attributes:
        name (str): The name of the workload identity provider. Example: github-actions.
        type_ (WorkloadIdentityProviderType): The type of issuer the provider trusts.

            * `OIDC`: an OpenID Connect issuer. Tokens must carry an `iss` claim equal to the provider's issuer.
            * `SPIFFE`: a SPIFFE trust domain. The `iss` claim is ignored, and `sub` must be a SPIFFE ID of that trust
            domain. Example: OIDC.
        issuer (str): The expected `iss` claim for `OIDC` providers, or the SPIFFE trust domain for `SPIFFE` providers.
            Example: https://token.actions.githubusercontent.com.
        audience (str): The value that the token's `aud` claim must contain. Example: https://dependency-
            track.example.com.
        session_lifetime_seconds (int): The lifetime of sessions created through this provider, unless a binding sets
            its own. Example: 3600.
        created_at (int): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
        jwks_url (str | Unset): The URL the signing keys are fetched from. For `OIDC` providers, this is the `jwks_uri`
            resolved from the issuer's discovery document. Absent when the keys were provided inline.
        jwks_key_ids (list[str] | Unset): The key IDs of the inline key set. Absent when the keys are fetched from a
            URL.
    """

    name: str
    type_: WorkloadIdentityProviderType
    issuer: str
    audience: str
    session_lifetime_seconds: int
    created_at: int
    jwks_url: str | Unset = UNSET
    jwks_key_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        issuer = self.issuer

        audience = self.audience

        session_lifetime_seconds = self.session_lifetime_seconds

        created_at = self.created_at

        jwks_url = self.jwks_url

        jwks_key_ids: list[str] | Unset = UNSET
        if not isinstance(self.jwks_key_ids, Unset):
            jwks_key_ids = self.jwks_key_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "issuer": issuer,
                "audience": audience,
                "session_lifetime_seconds": session_lifetime_seconds,
                "created_at": created_at,
            }
        )
        if jwks_url is not UNSET:
            field_dict["jwks_url"] = jwks_url
        if jwks_key_ids is not UNSET:
            field_dict["jwks_key_ids"] = jwks_key_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = WorkloadIdentityProviderType(d.pop("type"))

        issuer = d.pop("issuer")

        audience = d.pop("audience")

        session_lifetime_seconds = d.pop("session_lifetime_seconds")

        created_at = d.pop("created_at")

        jwks_url = d.pop("jwks_url", UNSET)

        jwks_key_ids = cast(list[str], d.pop("jwks_key_ids", UNSET))

        workload_identity_provider = cls(
            name=name,
            type_=type_,
            issuer=issuer,
            audience=audience,
            session_lifetime_seconds=session_lifetime_seconds,
            created_at=created_at,
            jwks_url=jwks_url,
            jwks_key_ids=jwks_key_ids,
        )

        workload_identity_provider.additional_properties = d
        return workload_identity_provider

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
