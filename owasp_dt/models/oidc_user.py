from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OidcUser")


@_attrs_define
class OidcUser:
    """
    Attributes:
        username (str):
        email (str | Unset):
        subject_identifier (str | Unset):
    """

    username: str
    email: str | Unset = UNSET
    subject_identifier: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        email = self.email

        subject_identifier = self.subject_identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if subject_identifier is not UNSET:
            field_dict["subjectIdentifier"] = subject_identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        email = d.pop("email", UNSET)

        subject_identifier = d.pop("subjectIdentifier", UNSET)

        oidc_user = cls(
            username=username,
            email=email,
            subject_identifier=subject_identifier,
        )

        oidc_user.additional_properties = d
        return oidc_user

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
