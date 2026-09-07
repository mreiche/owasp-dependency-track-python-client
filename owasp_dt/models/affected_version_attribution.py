from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.affected_version_attribution_source import (
    AffectedVersionAttributionSource,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AffectedVersionAttribution")


@_attrs_define
class AffectedVersionAttribution:
    """
    Attributes:
        first_seen (int): UNIX epoch timestamp in milliseconds
        last_seen (int): Deprecated; always equal to firstSeen
        source (AffectedVersionAttributionSource | Unset):
    """

    first_seen: int
    last_seen: int
    source: AffectedVersionAttributionSource | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_seen = self.first_seen

        last_seen = self.last_seen

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "firstSeen": first_seen,
                "lastSeen": last_seen,
            }
        )
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        first_seen = d.pop("firstSeen")

        last_seen = d.pop("lastSeen")

        _source = d.pop("source", UNSET)
        source: AffectedVersionAttributionSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = AffectedVersionAttributionSource(_source)

        affected_version_attribution = cls(
            first_seen=first_seen,
            last_seen=last_seen,
            source=source,
        )

        affected_version_attribution.additional_properties = d
        return affected_version_attribution

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
