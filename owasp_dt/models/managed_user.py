from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.permission import Permission
    from ..models.team import Team


T = TypeVar("T", bound="ManagedUser")


@_attrs_define
class ManagedUser:
    """
    Attributes:
        last_password_change (int): UNIX epoch timestamp in milliseconds
        username (str):
        confirm_password (str | Unset):
        email (str | Unset):
        force_password_change (bool | Unset):
        fullname (str | Unset):
        new_password (str | Unset):
        non_expiry_password (bool | Unset):
        permissions (list[Permission] | Unset):
        suspended (bool | Unset):
        teams (list[Team] | Unset):
    """

    last_password_change: int
    username: str
    confirm_password: str | Unset = UNSET
    email: str | Unset = UNSET
    force_password_change: bool | Unset = UNSET
    fullname: str | Unset = UNSET
    new_password: str | Unset = UNSET
    non_expiry_password: bool | Unset = UNSET
    permissions: list[Permission] | Unset = UNSET
    suspended: bool | Unset = UNSET
    teams: list[Team] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_password_change = self.last_password_change

        username = self.username

        confirm_password = self.confirm_password

        email = self.email

        force_password_change = self.force_password_change

        fullname = self.fullname

        new_password = self.new_password

        non_expiry_password = self.non_expiry_password

        permissions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.to_dict()
                permissions.append(permissions_item)

        suspended = self.suspended

        teams: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()
                teams.append(teams_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lastPasswordChange": last_password_change,
                "username": username,
            }
        )
        if confirm_password is not UNSET:
            field_dict["confirmPassword"] = confirm_password
        if email is not UNSET:
            field_dict["email"] = email
        if force_password_change is not UNSET:
            field_dict["forcePasswordChange"] = force_password_change
        if fullname is not UNSET:
            field_dict["fullname"] = fullname
        if new_password is not UNSET:
            field_dict["newPassword"] = new_password
        if non_expiry_password is not UNSET:
            field_dict["nonExpiryPassword"] = non_expiry_password
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if suspended is not UNSET:
            field_dict["suspended"] = suspended
        if teams is not UNSET:
            field_dict["teams"] = teams

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permission import Permission
        from ..models.team import Team

        d = dict(src_dict)
        last_password_change = d.pop("lastPasswordChange")

        username = d.pop("username")

        confirm_password = d.pop("confirmPassword", UNSET)

        email = d.pop("email", UNSET)

        force_password_change = d.pop("forcePasswordChange", UNSET)

        fullname = d.pop("fullname", UNSET)

        new_password = d.pop("newPassword", UNSET)

        non_expiry_password = d.pop("nonExpiryPassword", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: list[Permission] | Unset = UNSET
        if _permissions is not UNSET:
            permissions = []
            for permissions_item_data in _permissions:
                permissions_item = Permission.from_dict(permissions_item_data)

                permissions.append(permissions_item)

        suspended = d.pop("suspended", UNSET)

        _teams = d.pop("teams", UNSET)
        teams: list[Team] | Unset = UNSET
        if _teams is not UNSET:
            teams = []
            for teams_item_data in _teams:
                teams_item = Team.from_dict(teams_item_data)

                teams.append(teams_item)

        managed_user = cls(
            last_password_change=last_password_change,
            username=username,
            confirm_password=confirm_password,
            email=email,
            force_password_change=force_password_change,
            fullname=fullname,
            new_password=new_password,
            non_expiry_password=non_expiry_password,
            permissions=permissions,
            suspended=suspended,
            teams=teams,
        )

        managed_user.additional_properties = d
        return managed_user

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
