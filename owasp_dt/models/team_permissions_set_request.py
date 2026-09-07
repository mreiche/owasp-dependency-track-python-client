from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.team_permissions_set_request_permissions_item import (
    TeamPermissionsSetRequestPermissionsItem,
)

T = TypeVar("T", bound="TeamPermissionsSetRequest")


@_attrs_define
class TeamPermissionsSetRequest:
    """
    Attributes:
        permissions (list[TeamPermissionsSetRequestPermissionsItem]):
        team (str):
    """

    permissions: list[TeamPermissionsSetRequestPermissionsItem]
    team: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item = permissions_item_data.value
            permissions.append(permissions_item)

        team = self.team

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "permissions": permissions,
                "team": team,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in _permissions:
            permissions_item = TeamPermissionsSetRequestPermissionsItem(
                permissions_item_data
            )

            permissions.append(permissions_item)

        team = d.pop("team")

        team_permissions_set_request = cls(
            permissions=permissions,
            team=team,
        )

        team_permissions_set_request.additional_properties = d
        return team_permissions_set_request

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
