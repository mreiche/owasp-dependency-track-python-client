from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_run_status import WorkflowRunStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_run_metadata_labels import WorkflowRunMetadataLabels


T = TypeVar("T", bound="WorkflowRunMetadata")


@_attrs_define
class WorkflowRunMetadata:
    """
    Attributes:
        id (UUID):
        workflow_name (str):
        workflow_version (int):
        task_queue_name (str):
        status (WorkflowRunStatus):
        priority (int):
        created_at (int): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
        parent_id (UUID | Unset):
        workflow_instance_id (str | Unset):
        concurrency_key (str | Unset):
        labels (WorkflowRunMetadataLabels | Unset):
        updated_at (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
        started_at (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
        completed_at (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
    """

    id: UUID
    workflow_name: str
    workflow_version: int
    task_queue_name: str
    status: WorkflowRunStatus
    priority: int
    created_at: int
    parent_id: UUID | Unset = UNSET
    workflow_instance_id: str | Unset = UNSET
    concurrency_key: str | Unset = UNSET
    labels: WorkflowRunMetadataLabels | Unset = UNSET
    updated_at: int | Unset = UNSET
    started_at: int | Unset = UNSET
    completed_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        workflow_name = self.workflow_name

        workflow_version = self.workflow_version

        task_queue_name = self.task_queue_name

        status = self.status.value

        priority = self.priority

        created_at = self.created_at

        parent_id: str | Unset = UNSET
        if not isinstance(self.parent_id, Unset):
            parent_id = str(self.parent_id)

        workflow_instance_id = self.workflow_instance_id

        concurrency_key = self.concurrency_key

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        updated_at = self.updated_at

        started_at = self.started_at

        completed_at = self.completed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "workflow_name": workflow_name,
                "workflow_version": workflow_version,
                "task_queue_name": task_queue_name,
                "status": status,
                "priority": priority,
                "created_at": created_at,
            }
        )
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if workflow_instance_id is not UNSET:
            field_dict["workflow_instance_id"] = workflow_instance_id
        if concurrency_key is not UNSET:
            field_dict["concurrency_key"] = concurrency_key
        if labels is not UNSET:
            field_dict["labels"] = labels
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_run_metadata_labels import WorkflowRunMetadataLabels

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        workflow_name = d.pop("workflow_name")

        workflow_version = d.pop("workflow_version")

        task_queue_name = d.pop("task_queue_name")

        status = WorkflowRunStatus(d.pop("status"))

        priority = d.pop("priority")

        created_at = d.pop("created_at")

        _parent_id = d.pop("parent_id", UNSET)
        parent_id: UUID | Unset
        if isinstance(_parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = UUID(_parent_id)

        workflow_instance_id = d.pop("workflow_instance_id", UNSET)

        concurrency_key = d.pop("concurrency_key", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: WorkflowRunMetadataLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = WorkflowRunMetadataLabels.from_dict(_labels)

        updated_at = d.pop("updated_at", UNSET)

        started_at = d.pop("started_at", UNSET)

        completed_at = d.pop("completed_at", UNSET)

        workflow_run_metadata = cls(
            id=id,
            workflow_name=workflow_name,
            workflow_version=workflow_version,
            task_queue_name=task_queue_name,
            status=status,
            priority=priority,
            created_at=created_at,
            parent_id=parent_id,
            workflow_instance_id=workflow_instance_id,
            concurrency_key=concurrency_key,
            labels=labels,
            updated_at=updated_at,
            started_at=started_at,
            completed_at=completed_at,
        )

        workflow_run_metadata.additional_properties = d
        return workflow_run_metadata

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
