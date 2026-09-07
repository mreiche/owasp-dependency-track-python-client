from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_queue_status import TaskQueueStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTaskQueueRequest")


@_attrs_define
class UpdateTaskQueueRequest:
    """
    Attributes:
        status (TaskQueueStatus | Unset):
        capacity (int | Unset):
    """

    status: TaskQueueStatus | Unset = UNSET
    capacity: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        capacity = self.capacity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if capacity is not UNSET:
            field_dict["capacity"] = capacity

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: TaskQueueStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TaskQueueStatus(_status)

        capacity = d.pop("capacity", UNSET)

        update_task_queue_request = cls(
            status=status,
            capacity=capacity,
        )

        update_task_queue_request.additional_properties = d
        return update_task_queue_request

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
