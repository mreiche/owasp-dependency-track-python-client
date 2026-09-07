from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.kev_data_source_mirror_status_status import (
    KevDataSourceMirrorStatusStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KevDataSourceMirrorStatus")


@_attrs_define
class KevDataSourceMirrorStatus:
    """
    Attributes:
        status (KevDataSourceMirrorStatusStatus): Status of the mirror run.
        started_at (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
        completed_at (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
        failure_reason (str | Unset): Reason for why the mirror run failed.
    """

    status: KevDataSourceMirrorStatusStatus
    started_at: int | Unset = UNSET
    completed_at: int | Unset = UNSET
    failure_reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        started_at = self.started_at

        completed_at = self.completed_at

        failure_reason = self.failure_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if failure_reason is not UNSET:
            field_dict["failure_reason"] = failure_reason

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = KevDataSourceMirrorStatusStatus(d.pop("status"))

        started_at = d.pop("started_at", UNSET)

        completed_at = d.pop("completed_at", UNSET)

        failure_reason = d.pop("failure_reason", UNSET)

        kev_data_source_mirror_status = cls(
            status=status,
            started_at=started_at,
            completed_at=completed_at,
            failure_reason=failure_reason,
        )

        kev_data_source_mirror_status.additional_properties = d
        return kev_data_source_mirror_status

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
