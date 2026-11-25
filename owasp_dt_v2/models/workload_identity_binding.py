from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkloadIdentityBinding")


@_attrs_define
class WorkloadIdentityBinding:
    """
    Attributes:
        uuid (UUID): The identifier of the binding.
        provider_name (str): The name of the workload identity provider the binding belongs to. Example: github-actions.
        subject (str): The `sub` claim the binding matches. A trailing `*` makes it a prefix match. Example:
            repo:acme/app:*.
        created_at (int): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
        condition (str | Unset): A CEL expression over the token's claims that must evaluate to `true`. Absent when the
            binding matches on the subject alone. Example: claims.ref == "refs/heads/main".
        last_used_at (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
    """

    uuid: UUID
    provider_name: str
    subject: str
    created_at: int
    condition: str | Unset = UNSET
    last_used_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        provider_name = self.provider_name

        subject = self.subject

        created_at = self.created_at

        condition = self.condition

        last_used_at = self.last_used_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "provider_name": provider_name,
                "subject": subject,
                "created_at": created_at,
            }
        )
        if condition is not UNSET:
            field_dict["condition"] = condition
        if last_used_at is not UNSET:
            field_dict["last_used_at"] = last_used_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        provider_name = d.pop("provider_name")

        subject = d.pop("subject")

        created_at = d.pop("created_at")

        condition = d.pop("condition", UNSET)

        last_used_at = d.pop("last_used_at", UNSET)

        workload_identity_binding = cls(
            uuid=uuid,
            provider_name=provider_name,
            subject=subject,
            created_at=created_at,
            condition=condition,
            last_used_at=last_used_at,
        )

        workload_identity_binding.additional_properties = d
        return workload_identity_binding

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
