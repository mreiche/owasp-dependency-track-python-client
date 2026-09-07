from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hashes import Hashes


T = TypeVar("T", bound="PackageArtifactMetadata")


@_attrs_define
class PackageArtifactMetadata:
    """Artifact-level metadata for the component's exact version from configured package repositories. Only present when
    the component has a PURL with a version, the PURL type is supported by at least one configured repository, and
    artifact metadata has been successfully resolved from an upstream repository. Metadata resolution is asynchronous
    and runs in the background after a component is created or updated. This field may be absent for recently created
    components until resolution completes.

        Attributes:
            hashes (Hashes | Unset):
            published_at (int | None | Unset): When this artifact was published to the repository.
            resolved_from (None | str | Unset): Identifier of the repository from which artifact metadata was fetched.
            resolved_at (int | None | Unset): When artifact metadata was last resolved from the upstream repository.
    """

    hashes: Hashes | Unset = UNSET
    published_at: int | None | Unset = UNSET
    resolved_from: None | str | Unset = UNSET
    resolved_at: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hashes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hashes, Unset):
            hashes = self.hashes.to_dict()

        published_at: int | None | Unset
        if isinstance(self.published_at, Unset):
            published_at = UNSET
        else:
            published_at = self.published_at

        resolved_from: None | str | Unset
        if isinstance(self.resolved_from, Unset):
            resolved_from = UNSET
        else:
            resolved_from = self.resolved_from

        resolved_at: int | None | Unset
        if isinstance(self.resolved_at, Unset):
            resolved_at = UNSET
        else:
            resolved_at = self.resolved_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hashes is not UNSET:
            field_dict["hashes"] = hashes
        if published_at is not UNSET:
            field_dict["published_at"] = published_at
        if resolved_from is not UNSET:
            field_dict["resolved_from"] = resolved_from
        if resolved_at is not UNSET:
            field_dict["resolved_at"] = resolved_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.hashes import Hashes

        d = dict(src_dict)
        _hashes = d.pop("hashes", UNSET)
        hashes: Hashes | Unset
        if isinstance(_hashes, Unset):
            hashes = UNSET
        else:
            hashes = Hashes.from_dict(_hashes)

        def _parse_published_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        published_at = _parse_published_at(d.pop("published_at", UNSET))

        def _parse_resolved_from(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolved_from = _parse_resolved_from(d.pop("resolved_from", UNSET))

        def _parse_resolved_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        resolved_at = _parse_resolved_at(d.pop("resolved_at", UNSET))

        package_artifact_metadata = cls(
            hashes=hashes,
            published_at=published_at,
            resolved_from=resolved_from,
            resolved_at=resolved_at,
        )

        package_artifact_metadata.additional_properties = d
        return package_artifact_metadata

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
