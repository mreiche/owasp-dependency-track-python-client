from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PackageMetadata")


@_attrs_define
class PackageMetadata:
    """Latest version information from configured package registries. Only present when the component has a PURL with a
    type supported by at least one configured repository, and metadata has been successfully resolved from an upstream
    repository. Metadata resolution is asynchronous and runs in the background after a component is created or updated.
    This field may be absent for recently created components until resolution completes.

        Attributes:
            resolved_at (int): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
            latest_version (None | str | Unset): Latest known version in the configured registries. Null when the resolver
                ran but returned no version.
            latest_version_published_at (int | None | Unset): When the latest version was published. May be null even when
                latest_version is non-null, as some registries do not report publication dates.
    """

    resolved_at: int
    latest_version: None | str | Unset = UNSET
    latest_version_published_at: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resolved_at = self.resolved_at

        latest_version: None | str | Unset
        if isinstance(self.latest_version, Unset):
            latest_version = UNSET
        else:
            latest_version = self.latest_version

        latest_version_published_at: int | None | Unset
        if isinstance(self.latest_version_published_at, Unset):
            latest_version_published_at = UNSET
        else:
            latest_version_published_at = self.latest_version_published_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resolved_at": resolved_at,
            }
        )
        if latest_version is not UNSET:
            field_dict["latest_version"] = latest_version
        if latest_version_published_at is not UNSET:
            field_dict["latest_version_published_at"] = latest_version_published_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        resolved_at = d.pop("resolved_at")

        def _parse_latest_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_version = _parse_latest_version(d.pop("latest_version", UNSET))

        def _parse_latest_version_published_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        latest_version_published_at = _parse_latest_version_published_at(
            d.pop("latest_version_published_at", UNSET)
        )

        package_metadata = cls(
            resolved_at=resolved_at,
            latest_version=latest_version,
            latest_version_published_at=latest_version_published_at,
        )

        package_metadata.additional_properties = d
        return package_metadata

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
