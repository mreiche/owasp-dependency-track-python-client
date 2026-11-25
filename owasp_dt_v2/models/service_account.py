from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceAccount")


@_attrs_define
class ServiceAccount:
    """
    Attributes:
        name (str): The name of the service account, without the reserved `svc:` prefix. Example: ci-pipeline.
        username (str): The full username of the service account, i.e. the name with the reserved `svc:` prefix.
            Example: svc:ci-pipeline.
        suspended (bool): Whether the service account is suspended.
        email (str | Unset):
    """

    name: str
    username: str
    suspended: bool
    email: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        username = self.username

        suspended = self.suspended

        email = self.email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "username": username,
                "suspended": suspended,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        username = d.pop("username")

        suspended = d.pop("suspended")

        email = d.pop("email", UNSET)

        service_account = cls(
            name=name,
            username=username,
            suspended=suspended,
            email=email,
        )

        service_account.additional_properties = d
        return service_account

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
