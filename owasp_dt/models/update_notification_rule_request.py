from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_notification_rule_request_level import (
    UpdateNotificationRuleRequestLevel,
)
from ..models.update_notification_rule_request_notify_on_item import (
    UpdateNotificationRuleRequestNotifyOnItem,
)
from ..models.update_notification_rule_request_scope import (
    UpdateNotificationRuleRequestScope,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tag import Tag


T = TypeVar("T", bound="UpdateNotificationRuleRequest")


@_attrs_define
class UpdateNotificationRuleRequest:
    """
    Attributes:
        level (UpdateNotificationRuleRequestLevel):
        name (str):
        scope (UpdateNotificationRuleRequestScope):
        uuid (UUID):
        enabled (bool | Unset):
        filter_expression (str | Unset):
        log_successful_publish (bool | Unset):
        notify_children (bool | Unset):
        notify_on (list[UpdateNotificationRuleRequestNotifyOnItem] | Unset):
        publisher_config (str | Unset):
        schedule_cron (str | Unset):
        schedule_skip_unchanged (bool | Unset):
        tags (list[Tag] | Unset):
    """

    level: UpdateNotificationRuleRequestLevel
    name: str
    scope: UpdateNotificationRuleRequestScope
    uuid: UUID
    enabled: bool | Unset = UNSET
    filter_expression: str | Unset = UNSET
    log_successful_publish: bool | Unset = UNSET
    notify_children: bool | Unset = UNSET
    notify_on: list[UpdateNotificationRuleRequestNotifyOnItem] | Unset = UNSET
    publisher_config: str | Unset = UNSET
    schedule_cron: str | Unset = UNSET
    schedule_skip_unchanged: bool | Unset = UNSET
    tags: list[Tag] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        level = self.level.value

        name = self.name

        scope = self.scope.value

        uuid = str(self.uuid)

        enabled = self.enabled

        filter_expression = self.filter_expression

        log_successful_publish = self.log_successful_publish

        notify_children = self.notify_children

        notify_on: list[str] | Unset = UNSET
        if not isinstance(self.notify_on, Unset):
            notify_on = []
            for notify_on_item_data in self.notify_on:
                notify_on_item = notify_on_item_data.value
                notify_on.append(notify_on_item)

        publisher_config = self.publisher_config

        schedule_cron = self.schedule_cron

        schedule_skip_unchanged = self.schedule_skip_unchanged

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "level": level,
                "name": name,
                "scope": scope,
                "uuid": uuid,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if filter_expression is not UNSET:
            field_dict["filterExpression"] = filter_expression
        if log_successful_publish is not UNSET:
            field_dict["logSuccessfulPublish"] = log_successful_publish
        if notify_children is not UNSET:
            field_dict["notifyChildren"] = notify_children
        if notify_on is not UNSET:
            field_dict["notifyOn"] = notify_on
        if publisher_config is not UNSET:
            field_dict["publisherConfig"] = publisher_config
        if schedule_cron is not UNSET:
            field_dict["scheduleCron"] = schedule_cron
        if schedule_skip_unchanged is not UNSET:
            field_dict["scheduleSkipUnchanged"] = schedule_skip_unchanged
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.tag import Tag

        d = dict(src_dict)
        level = UpdateNotificationRuleRequestLevel(d.pop("level"))

        name = d.pop("name")

        scope = UpdateNotificationRuleRequestScope(d.pop("scope"))

        uuid = UUID(d.pop("uuid"))

        enabled = d.pop("enabled", UNSET)

        filter_expression = d.pop("filterExpression", UNSET)

        log_successful_publish = d.pop("logSuccessfulPublish", UNSET)

        notify_children = d.pop("notifyChildren", UNSET)

        _notify_on = d.pop("notifyOn", UNSET)
        notify_on: list[UpdateNotificationRuleRequestNotifyOnItem] | Unset = UNSET
        if _notify_on is not UNSET:
            notify_on = []
            for notify_on_item_data in _notify_on:
                notify_on_item = UpdateNotificationRuleRequestNotifyOnItem(
                    notify_on_item_data
                )

                notify_on.append(notify_on_item)

        publisher_config = d.pop("publisherConfig", UNSET)

        schedule_cron = d.pop("scheduleCron", UNSET)

        schedule_skip_unchanged = d.pop("scheduleSkipUnchanged", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: list[Tag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = Tag.from_dict(tags_item_data)

                tags.append(tags_item)

        update_notification_rule_request = cls(
            level=level,
            name=name,
            scope=scope,
            uuid=uuid,
            enabled=enabled,
            filter_expression=filter_expression,
            log_successful_publish=log_successful_publish,
            notify_children=notify_children,
            notify_on=notify_on,
            publisher_config=publisher_config,
            schedule_cron=schedule_cron,
            schedule_skip_unchanged=schedule_skip_unchanged,
            tags=tags,
        )

        update_notification_rule_request.additional_properties = d
        return update_notification_rule_request

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
