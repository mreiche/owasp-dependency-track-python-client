from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ldap_user import LdapUser
    from ..models.managed_user import ManagedUser
    from ..models.oidc_user import OidcUser


T = TypeVar("T", bound="Permission")


@_attrs_define
class Permission:
    """
    Attributes:
        name (str):
        description (str | Unset):
        ldap_users (list[LdapUser] | Unset):
        managed_users (list[ManagedUser] | Unset):
        oidc_users (list[OidcUser] | Unset):
    """

    name: str
    description: str | Unset = UNSET
    ldap_users: list[LdapUser] | Unset = UNSET
    managed_users: list[ManagedUser] | Unset = UNSET
    oidc_users: list[OidcUser] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        ldap_users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ldap_users, Unset):
            ldap_users = []
            for ldap_users_item_data in self.ldap_users:
                ldap_users_item = ldap_users_item_data.to_dict()
                ldap_users.append(ldap_users_item)

        managed_users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.managed_users, Unset):
            managed_users = []
            for managed_users_item_data in self.managed_users:
                managed_users_item = managed_users_item_data.to_dict()
                managed_users.append(managed_users_item)

        oidc_users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.oidc_users, Unset):
            oidc_users = []
            for oidc_users_item_data in self.oidc_users:
                oidc_users_item = oidc_users_item_data.to_dict()
                oidc_users.append(oidc_users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if ldap_users is not UNSET:
            field_dict["ldapUsers"] = ldap_users
        if managed_users is not UNSET:
            field_dict["managedUsers"] = managed_users
        if oidc_users is not UNSET:
            field_dict["oidcUsers"] = oidc_users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ldap_user import LdapUser
        from ..models.managed_user import ManagedUser
        from ..models.oidc_user import OidcUser

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        _ldap_users = d.pop("ldapUsers", UNSET)
        ldap_users: list[LdapUser] | Unset = UNSET
        if _ldap_users is not UNSET:
            ldap_users = []
            for ldap_users_item_data in _ldap_users:
                ldap_users_item = LdapUser.from_dict(ldap_users_item_data)

                ldap_users.append(ldap_users_item)

        _managed_users = d.pop("managedUsers", UNSET)
        managed_users: list[ManagedUser] | Unset = UNSET
        if _managed_users is not UNSET:
            managed_users = []
            for managed_users_item_data in _managed_users:
                managed_users_item = ManagedUser.from_dict(managed_users_item_data)

                managed_users.append(managed_users_item)

        _oidc_users = d.pop("oidcUsers", UNSET)
        oidc_users: list[OidcUser] | Unset = UNSET
        if _oidc_users is not UNSET:
            oidc_users = []
            for oidc_users_item_data in _oidc_users:
                oidc_users_item = OidcUser.from_dict(oidc_users_item_data)

                oidc_users.append(oidc_users_item)

        permission = cls(
            name=name,
            description=description,
            ldap_users=ldap_users,
            managed_users=managed_users,
            oidc_users=oidc_users,
        )

        permission.additional_properties = d
        return permission

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
