from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organizational_contact import OrganizationalContact
    from ..models.organizational_entity import OrganizationalEntity
    from ..models.tools import Tools


T = TypeVar("T", bound="ProjectMetadata")


@_attrs_define
class ProjectMetadata:
    """
    Attributes:
        authors (list[OrganizationalContact] | Unset):
        supplier (OrganizationalEntity | Unset):
        tools (Tools | Unset):
    """

    authors: list[OrganizationalContact] | Unset = UNSET
    supplier: OrganizationalEntity | Unset = UNSET
    tools: Tools | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.authors, Unset):
            authors = []
            for authors_item_data in self.authors:
                authors_item = authors_item_data.to_dict()
                authors.append(authors_item)

        supplier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.supplier, Unset):
            supplier = self.supplier.to_dict()

        tools: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tools, Unset):
            tools = self.tools.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authors is not UNSET:
            field_dict["authors"] = authors
        if supplier is not UNSET:
            field_dict["supplier"] = supplier
        if tools is not UNSET:
            field_dict["tools"] = tools

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.organizational_contact import (
            OrganizationalContact,
        )
        from ..models.organizational_entity import OrganizationalEntity
        from ..models.tools import Tools

        d = dict(src_dict)
        _authors = d.pop("authors", UNSET)
        authors: list[OrganizationalContact] | Unset = UNSET
        if _authors is not UNSET:
            authors = []
            for authors_item_data in _authors:
                authors_item = OrganizationalContact.from_dict(authors_item_data)

                authors.append(authors_item)

        _supplier = d.pop("supplier", UNSET)
        supplier: OrganizationalEntity | Unset
        if isinstance(_supplier, Unset):
            supplier = UNSET
        else:
            supplier = OrganizationalEntity.from_dict(_supplier)

        _tools = d.pop("tools", UNSET)
        tools: Tools | Unset
        if isinstance(_tools, Unset):
            tools = UNSET
        else:
            tools = Tools.from_dict(_tools)

        project_metadata = cls(
            authors=authors,
            supplier=supplier,
            tools=tools,
        )

        project_metadata.additional_properties = d
        return project_metadata

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
