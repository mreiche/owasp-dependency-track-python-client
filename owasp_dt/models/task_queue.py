from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_queue_status import TaskQueueStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskQueue")


@_attrs_define
class TaskQueue:
    """
    Attributes:
        name (str):
        status (TaskQueueStatus):
        capacity (int):
        depth (int):
        created_at (int): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
        updated_at (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
    """

    name: str
    status: TaskQueueStatus
    capacity: int
    depth: int
    created_at: int
    updated_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status.value

        capacity = self.capacity

        depth = self.depth

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "capacity": capacity,
                "depth": depth,
                "created_at": created_at,
            }
        )
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        status = TaskQueueStatus(d.pop("status"))

        capacity = d.pop("capacity")

        depth = d.pop("depth")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at", UNSET)

        task_queue = cls(
            name=name,
            status=status,
            capacity=capacity,
            depth=depth,
            created_at=created_at,
            updated_at=updated_at,
        )

        task_queue.additional_properties = d
        return task_queue

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
