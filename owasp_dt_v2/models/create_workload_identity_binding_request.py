from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWorkloadIdentityBindingRequest")


@_attrs_define
class CreateWorkloadIdentityBindingRequest:
    """
    Attributes:
        provider_name (str): The name of the workload identity provider to trust the subject of. The provider must
            exist. Example: github-actions.
        subject (str): The `sub` claim to match. A trailing `*` makes it a prefix match, whose prefix must not be empty
            and must end with `:` or `/`. Example: repo:acme/app:*.
        condition (str | Unset): An optional CEL expression over the token's claims that must evaluate to `true`. The
            claims are available as the `claims` map, for example `claims.ref == "refs/heads/main"`. Use it when the subject
            alone cannot express the rule. Example: claims.ref == "refs/heads/main".
    """

    provider_name: str
    subject: str
    condition: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider_name = self.provider_name

        subject = self.subject

        condition = self.condition

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider_name": provider_name,
                "subject": subject,
            }
        )
        if condition is not UNSET:
            field_dict["condition"] = condition

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        provider_name = d.pop("provider_name")

        subject = d.pop("subject")

        condition = d.pop("condition", UNSET)

        create_workload_identity_binding_request = cls(
            provider_name=provider_name,
            subject=subject,
            condition=condition,
        )

        create_workload_identity_binding_request.additional_properties = d
        return create_workload_identity_binding_request

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
