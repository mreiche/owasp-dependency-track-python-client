from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectVersion")


@_attrs_define
class ProjectVersion:
    """
    Attributes:
        active (bool | Unset):
        is_latest (bool | Unset):
        uuid (UUID | Unset):
        version (str | Unset):
    """

    active: bool | Unset = UNSET
    is_latest: bool | Unset = UNSET
    uuid: UUID | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        is_latest = self.is_latest

        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if is_latest is not UNSET:
            field_dict["isLatest"] = is_latest
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        active = d.pop("active", UNSET)

        is_latest = d.pop("isLatest", UNSET)

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        version = d.pop("version", UNSET)

        project_version = cls(
            active=active,
            is_latest=is_latest,
            uuid=uuid,
            version=version,
        )

        project_version.additional_properties = d
        return project_version

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
