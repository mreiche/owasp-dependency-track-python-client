from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.permission import Permission
    from ..models.team import Team


T = TypeVar("T", bound="OidcUser")


@_attrs_define
class OidcUser:
    """
    Attributes:
        username (str):
        email (str | Unset):
        permissions (list[Permission] | Unset):
        subject_identifier (str | Unset):
        teams (list[Team] | Unset):
    """

    username: str
    email: str | Unset = UNSET
    permissions: list[Permission] | Unset = UNSET
    subject_identifier: str | Unset = UNSET
    teams: list[Team] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        email = self.email

        permissions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.to_dict()
                permissions.append(permissions_item)

        subject_identifier = self.subject_identifier

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
                "username": username,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if subject_identifier is not UNSET:
            field_dict["subjectIdentifier"] = subject_identifier
        if teams is not UNSET:
            field_dict["teams"] = teams

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.permission import Permission
        from ..models.team import Team

        d = dict(src_dict)
        username = d.pop("username")

        email = d.pop("email", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: list[Permission] | Unset = UNSET
        if _permissions is not UNSET:
            permissions = []
            for permissions_item_data in _permissions:
                permissions_item = Permission.from_dict(permissions_item_data)

                permissions.append(permissions_item)

        subject_identifier = d.pop("subjectIdentifier", UNSET)

        _teams = d.pop("teams", UNSET)
        teams: list[Team] | Unset = UNSET
        if _teams is not UNSET:
            teams = []
            for teams_item_data in _teams:
                teams_item = Team.from_dict(teams_item_data)

                teams.append(teams_item)

        oidc_user = cls(
            username=username,
            email=email,
            permissions=permissions,
            subject_identifier=subject_identifier,
            teams=teams,
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
