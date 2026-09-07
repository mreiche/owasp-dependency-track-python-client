from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_scheduled_notification_rule_request_level import (
    CreateScheduledNotificationRuleRequestLevel,
)
from ..models.create_scheduled_notification_rule_request_scope import (
    CreateScheduledNotificationRuleRequestScope,
)

if TYPE_CHECKING:
    from ..models.publisher import Publisher


T = TypeVar("T", bound="CreateScheduledNotificationRuleRequest")


@_attrs_define
class CreateScheduledNotificationRuleRequest:
    """
    Attributes:
        level (CreateScheduledNotificationRuleRequestLevel):
        name (str):
        publisher (Publisher):
        scope (CreateScheduledNotificationRuleRequestScope):
    """

    level: CreateScheduledNotificationRuleRequestLevel
    name: str
    publisher: Publisher
    scope: CreateScheduledNotificationRuleRequestScope
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        level = self.level.value

        name = self.name

        publisher = self.publisher.to_dict()

        scope = self.scope.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "level": level,
                "name": name,
                "publisher": publisher,
                "scope": scope,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.publisher import Publisher

        d = dict(src_dict)
        level = CreateScheduledNotificationRuleRequestLevel(d.pop("level"))

        name = d.pop("name")

        publisher = Publisher.from_dict(d.pop("publisher"))

        scope = CreateScheduledNotificationRuleRequestScope(d.pop("scope"))

        create_scheduled_notification_rule_request = cls(
            level=level,
            name=name,
            publisher=publisher,
            scope=scope,
        )

        create_scheduled_notification_rule_request.additional_properties = d
        return create_scheduled_notification_rule_request

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
