from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.repository_meta_component_repository_type import (
    RepositoryMetaComponentRepositoryType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RepositoryMetaComponent")


@_attrs_define
class RepositoryMetaComponent:
    """
    Attributes:
        last_check (int | Unset): UNIX epoch timestamp in milliseconds
        latest_version (str | Unset):
        latest_version_published_at (int | Unset): UNIX epoch timestamp in milliseconds
        name (str | Unset):
        namespace (str | Unset):
        repository_type (RepositoryMetaComponentRepositoryType | Unset):
    """

    last_check: int | Unset = UNSET
    latest_version: str | Unset = UNSET
    latest_version_published_at: int | Unset = UNSET
    name: str | Unset = UNSET
    namespace: str | Unset = UNSET
    repository_type: RepositoryMetaComponentRepositoryType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_check = self.last_check

        latest_version = self.latest_version

        latest_version_published_at = self.latest_version_published_at

        name = self.name

        namespace = self.namespace

        repository_type: str | Unset = UNSET
        if not isinstance(self.repository_type, Unset):
            repository_type = self.repository_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_check is not UNSET:
            field_dict["lastCheck"] = last_check
        if latest_version is not UNSET:
            field_dict["latestVersion"] = latest_version
        if latest_version_published_at is not UNSET:
            field_dict["latestVersionPublishedAt"] = latest_version_published_at
        if name is not UNSET:
            field_dict["name"] = name
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if repository_type is not UNSET:
            field_dict["repositoryType"] = repository_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        last_check = d.pop("lastCheck", UNSET)

        latest_version = d.pop("latestVersion", UNSET)

        latest_version_published_at = d.pop("latestVersionPublishedAt", UNSET)

        name = d.pop("name", UNSET)

        namespace = d.pop("namespace", UNSET)

        _repository_type = d.pop("repositoryType", UNSET)
        repository_type: RepositoryMetaComponentRepositoryType | Unset
        if isinstance(_repository_type, Unset):
            repository_type = UNSET
        else:
            repository_type = RepositoryMetaComponentRepositoryType(_repository_type)

        repository_meta_component = cls(
            last_check=last_check,
            latest_version=latest_version,
            latest_version_published_at=latest_version_published_at,
            name=name,
            namespace=namespace,
            repository_type=repository_type,
        )

        repository_meta_component.additional_properties = d
        return repository_meta_component

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
