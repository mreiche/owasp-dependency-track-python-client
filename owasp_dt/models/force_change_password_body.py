from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ForceChangePasswordBody")


@_attrs_define
class ForceChangePasswordBody:
    """
    Attributes:
        confirm_password (str | Unset):
        new_password (str | Unset):
        password (str | Unset):
        username (str | Unset):
    """

    confirm_password: str | Unset = UNSET
    new_password: str | Unset = UNSET
    password: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        confirm_password = self.confirm_password

        new_password = self.new_password

        password = self.password

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if confirm_password is not UNSET:
            field_dict["confirmPassword"] = confirm_password
        if new_password is not UNSET:
            field_dict["newPassword"] = new_password
        if password is not UNSET:
            field_dict["password"] = password
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        confirm_password = d.pop("confirmPassword", UNSET)

        new_password = d.pop("newPassword", UNSET)

        password = d.pop("password", UNSET)

        username = d.pop("username", UNSET)

        force_change_password_body = cls(
            confirm_password=confirm_password,
            new_password=new_password,
            password=password,
            username=username,
        )

        force_change_password_body.additional_properties = d
        return force_change_password_body

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
