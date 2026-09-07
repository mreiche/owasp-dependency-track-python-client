from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DependencyGraphResponse")


@_attrs_define
class DependencyGraphResponse:
    """
    Attributes:
        direct_dependencies (str | Unset):
        latest_version (str | Unset):
        name (str | Unset):
        purl (str | Unset):
        uuid (UUID | Unset):
        version (str | Unset):
    """

    direct_dependencies: str | Unset = UNSET
    latest_version: str | Unset = UNSET
    name: str | Unset = UNSET
    purl: str | Unset = UNSET
    uuid: UUID | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        direct_dependencies = self.direct_dependencies

        latest_version = self.latest_version

        name = self.name

        purl = self.purl

        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if direct_dependencies is not UNSET:
            field_dict["directDependencies"] = direct_dependencies
        if latest_version is not UNSET:
            field_dict["latestVersion"] = latest_version
        if name is not UNSET:
            field_dict["name"] = name
        if purl is not UNSET:
            field_dict["purl"] = purl
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        direct_dependencies = d.pop("directDependencies", UNSET)

        latest_version = d.pop("latestVersion", UNSET)

        name = d.pop("name", UNSET)

        purl = d.pop("purl", UNSET)

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        version = d.pop("version", UNSET)

        dependency_graph_response = cls(
            direct_dependencies=direct_dependencies,
            latest_version=latest_version,
            name=name,
            purl=purl,
            uuid=uuid,
            version=version,
        )

        dependency_graph_response.additional_properties = d
        return dependency_graph_response

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
