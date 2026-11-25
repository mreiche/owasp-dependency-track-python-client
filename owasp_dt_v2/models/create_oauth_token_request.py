from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateOauthTokenRequest")


@_attrs_define
class CreateOauthTokenRequest:
    """
    Attributes:
        grant_type (str): The grant type. Only `urn:ietf:params:oauth:grant-type:token-exchange` is supported. Example:
            urn:ietf:params:oauth:grant-type:token-exchange.
        subject_token (str | Unset): The token to exchange. Required for the token exchange grant. At most 16 KiB.
        subject_token_type (str | Unset): The type of the subject token. Required for the token exchange grant.
            `urn:ietf:params:oauth:token-type:jwt` for all workload identity providers, or `urn:ietf:params:oauth:token-
            type:id_token` for `OIDC` providers. Example: urn:ietf:params:oauth:token-type:jwt.
        requested_token_type (str | Unset): The type of token to issue. Optional. Only `urn:ietf:params:oauth:token-
            type:access_token` is supported. Example: urn:ietf:params:oauth:token-type:access_token.
        workload_identity_provider (str | Unset): The name of the workload identity provider. Example: github-actions.
        service_account (str | Unset): The name of the service account, without the reserved `svc:` prefix. Example: ci-
            pipeline.
    """

    grant_type: str
    subject_token: str | Unset = UNSET
    subject_token_type: str | Unset = UNSET
    requested_token_type: str | Unset = UNSET
    workload_identity_provider: str | Unset = UNSET
    service_account: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grant_type = self.grant_type

        subject_token = self.subject_token

        subject_token_type = self.subject_token_type

        requested_token_type = self.requested_token_type

        workload_identity_provider = self.workload_identity_provider

        service_account = self.service_account

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grant_type": grant_type,
            }
        )
        if subject_token is not UNSET:
            field_dict["subject_token"] = subject_token
        if subject_token_type is not UNSET:
            field_dict["subject_token_type"] = subject_token_type
        if requested_token_type is not UNSET:
            field_dict["requested_token_type"] = requested_token_type
        if workload_identity_provider is not UNSET:
            field_dict["workload_identity_provider"] = workload_identity_provider
        if service_account is not UNSET:
            field_dict["service_account"] = service_account

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        grant_type = d.pop("grant_type")

        subject_token = d.pop("subject_token", UNSET)

        subject_token_type = d.pop("subject_token_type", UNSET)

        requested_token_type = d.pop("requested_token_type", UNSET)

        workload_identity_provider = d.pop("workload_identity_provider", UNSET)

        service_account = d.pop("service_account", UNSET)

        create_oauth_token_request = cls(
            grant_type=grant_type,
            subject_token=subject_token,
            subject_token_type=subject_token_type,
            requested_token_type=requested_token_type,
            workload_identity_provider=workload_identity_provider,
            service_account=service_account,
        )

        create_oauth_token_request.additional_properties = d
        return create_oauth_token_request

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
