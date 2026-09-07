from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_workflow_run_events_response_item_event import (
        ListWorkflowRunEventsResponseItemEvent,
    )


T = TypeVar("T", bound="ListWorkflowRunEventsResponseItem")


@_attrs_define
class ListWorkflowRunEventsResponseItem:
    """
    Attributes:
        sequence_number (int):
        event (ListWorkflowRunEventsResponseItemEvent):
    """

    sequence_number: int
    event: ListWorkflowRunEventsResponseItemEvent
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sequence_number = self.sequence_number

        event = self.event.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sequence_number": sequence_number,
                "event": event,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_workflow_run_events_response_item_event import (
            ListWorkflowRunEventsResponseItemEvent,
        )

        d = dict(src_dict)
        sequence_number = d.pop("sequence_number")

        event = ListWorkflowRunEventsResponseItemEvent.from_dict(d.pop("event"))

        list_workflow_run_events_response_item = cls(
            sequence_number=sequence_number,
            event=event,
        )

        list_workflow_run_events_response_item.additional_properties = d
        return list_workflow_run_events_response_item

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
