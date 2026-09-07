from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AffectedProject")


@_attrs_define
class AffectedProject:
    """
    Attributes:
        active (bool | Unset):
        affected_component_uuids (list[UUID] | Unset):
        dependency_graph_available (bool | Unset):
        name (str | Unset):
        uuid (UUID | Unset):
        version (str | Unset):
    """

    active: bool | Unset = UNSET
    affected_component_uuids: list[UUID] | Unset = UNSET
    dependency_graph_available: bool | Unset = UNSET
    name: str | Unset = UNSET
    uuid: UUID | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        affected_component_uuids: list[str] | Unset = UNSET
        if not isinstance(self.affected_component_uuids, Unset):
            affected_component_uuids = []
            for affected_component_uuids_item_data in self.affected_component_uuids:
                affected_component_uuids_item = str(affected_component_uuids_item_data)
                affected_component_uuids.append(affected_component_uuids_item)

        dependency_graph_available = self.dependency_graph_available

        name = self.name

        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if affected_component_uuids is not UNSET:
            field_dict["affectedComponentUuids"] = affected_component_uuids
        if dependency_graph_available is not UNSET:
            field_dict["dependencyGraphAvailable"] = dependency_graph_available
        if name is not UNSET:
            field_dict["name"] = name
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        active = d.pop("active", UNSET)

        _affected_component_uuids = d.pop("affectedComponentUuids", UNSET)
        affected_component_uuids: list[UUID] | Unset = UNSET
        if _affected_component_uuids is not UNSET:
            affected_component_uuids = []
            for affected_component_uuids_item_data in _affected_component_uuids:
                affected_component_uuids_item = UUID(affected_component_uuids_item_data)

                affected_component_uuids.append(affected_component_uuids_item)

        dependency_graph_available = d.pop("dependencyGraphAvailable", UNSET)

        name = d.pop("name", UNSET)

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        version = d.pop("version", UNSET)

        affected_project = cls(
            active=active,
            affected_component_uuids=affected_component_uuids,
            dependency_graph_available=dependency_graph_available,
            name=name,
            uuid=uuid,
            version=version,
        )

        affected_project.additional_properties = d
        return affected_project

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
