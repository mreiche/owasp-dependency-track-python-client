from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organizational_contact import OrganizationalContact


T = TypeVar("T", bound="OrganizationalEntity")


@_attrs_define
class OrganizationalEntity:
    """
    Attributes:
        contacts (list[OrganizationalContact] | Unset):
        name (str | Unset):
        urls (list[str] | Unset):
    """

    contacts: list[OrganizationalContact] | Unset = UNSET
    name: str | Unset = UNSET
    urls: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contacts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()
                contacts.append(contacts_item)

        name = self.name

        urls: list[str] | Unset = UNSET
        if not isinstance(self.urls, Unset):
            urls = self.urls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if name is not UNSET:
            field_dict["name"] = name
        if urls is not UNSET:
            field_dict["urls"] = urls

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.organizational_contact import (
            OrganizationalContact,
        )

        d = dict(src_dict)
        _contacts = d.pop("contacts", UNSET)
        contacts: list[OrganizationalContact] | Unset = UNSET
        if _contacts is not UNSET:
            contacts = []
            for contacts_item_data in _contacts:
                contacts_item = OrganizationalContact.from_dict(contacts_item_data)

                contacts.append(contacts_item)

        name = d.pop("name", UNSET)

        urls = cast(list[str], d.pop("urls", UNSET))

        organizational_entity = cls(
            contacts=contacts,
            name=name,
            urls=urls,
        )

        organizational_entity.additional_properties = d
        return organizational_entity

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
