from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_rule_notification_level import (
    NotificationRuleNotificationLevel,
)
from ..models.notification_rule_notify_on_item import NotificationRuleNotifyOnItem
from ..models.notification_rule_scope import NotificationRuleScope
from ..models.notification_rule_trigger_type import NotificationRuleTriggerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_publisher import NotificationPublisher
    from ..models.project import Project
    from ..models.tag import Tag
    from ..models.team import Team


T = TypeVar("T", bound="NotificationRule")


@_attrs_define
class NotificationRule:
    """
    Attributes:
        name (str):
        scope (NotificationRuleScope):
        trigger_type (NotificationRuleTriggerType):
        uuid (UUID):
        enabled (bool | Unset):
        filter_expression (str | Unset):
        log_successful_publish (bool | Unset):
        message (str | Unset):
        notification_level (NotificationRuleNotificationLevel | Unset):
        notify_children (bool | Unset):
        notify_on (list[NotificationRuleNotifyOnItem] | Unset):
        projects (list[Project] | Unset):
        publisher (NotificationPublisher | Unset):
        publisher_config (str | Unset):
        schedule_cron (str | Unset): Schedule of this rule as cron expression. Must not be set for rules with trigger
            type EVENT.
        schedule_last_triggered_at (int | Unset): When the schedule last triggered, as UNIX epoch timestamp in
            milliseconds
        schedule_next_trigger_at (int | Unset): When the schedule triggers next, as UNIX epoch timestamp in milliseconds
        schedule_skip_unchanged (bool | Unset): Whether to skip emitting a scheduled notification if it doesn't contain
            any changes since its last emission. Must not be set for rules with trigger type EVENT.
        tags (list[Tag] | Unset):
        teams (list[Team] | Unset):
    """

    name: str
    scope: NotificationRuleScope
    trigger_type: NotificationRuleTriggerType
    uuid: UUID
    enabled: bool | Unset = UNSET
    filter_expression: str | Unset = UNSET
    log_successful_publish: bool | Unset = UNSET
    message: str | Unset = UNSET
    notification_level: NotificationRuleNotificationLevel | Unset = UNSET
    notify_children: bool | Unset = UNSET
    notify_on: list[NotificationRuleNotifyOnItem] | Unset = UNSET
    projects: list[Project] | Unset = UNSET
    publisher: NotificationPublisher | Unset = UNSET
    publisher_config: str | Unset = UNSET
    schedule_cron: str | Unset = UNSET
    schedule_last_triggered_at: int | Unset = UNSET
    schedule_next_trigger_at: int | Unset = UNSET
    schedule_skip_unchanged: bool | Unset = UNSET
    tags: list[Tag] | Unset = UNSET
    teams: list[Team] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        scope = self.scope.value

        trigger_type = self.trigger_type.value

        uuid = str(self.uuid)

        enabled = self.enabled

        filter_expression = self.filter_expression

        log_successful_publish = self.log_successful_publish

        message = self.message

        notification_level: str | Unset = UNSET
        if not isinstance(self.notification_level, Unset):
            notification_level = self.notification_level.value

        notify_children = self.notify_children

        notify_on: list[str] | Unset = UNSET
        if not isinstance(self.notify_on, Unset):
            notify_on = []
            for notify_on_item_data in self.notify_on:
                notify_on_item = notify_on_item_data.value
                notify_on.append(notify_on_item)

        projects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.projects, Unset):
            projects = []
            for projects_item_data in self.projects:
                projects_item = projects_item_data.to_dict()
                projects.append(projects_item)

        publisher: dict[str, Any] | Unset = UNSET
        if not isinstance(self.publisher, Unset):
            publisher = self.publisher.to_dict()

        publisher_config = self.publisher_config

        schedule_cron = self.schedule_cron

        schedule_last_triggered_at = self.schedule_last_triggered_at

        schedule_next_trigger_at = self.schedule_next_trigger_at

        schedule_skip_unchanged = self.schedule_skip_unchanged

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        teams: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()
                teams.append(teams_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "scope": scope,
                "triggerType": trigger_type,
                "uuid": uuid,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if filter_expression is not UNSET:
            field_dict["filterExpression"] = filter_expression
        if log_successful_publish is not UNSET:
            field_dict["logSuccessfulPublish"] = log_successful_publish
        if message is not UNSET:
            field_dict["message"] = message
        if notification_level is not UNSET:
            field_dict["notificationLevel"] = notification_level
        if notify_children is not UNSET:
            field_dict["notifyChildren"] = notify_children
        if notify_on is not UNSET:
            field_dict["notifyOn"] = notify_on
        if projects is not UNSET:
            field_dict["projects"] = projects
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if publisher_config is not UNSET:
            field_dict["publisherConfig"] = publisher_config
        if schedule_cron is not UNSET:
            field_dict["scheduleCron"] = schedule_cron
        if schedule_last_triggered_at is not UNSET:
            field_dict["scheduleLastTriggeredAt"] = schedule_last_triggered_at
        if schedule_next_trigger_at is not UNSET:
            field_dict["scheduleNextTriggerAt"] = schedule_next_trigger_at
        if schedule_skip_unchanged is not UNSET:
            field_dict["scheduleSkipUnchanged"] = schedule_skip_unchanged
        if tags is not UNSET:
            field_dict["tags"] = tags
        if teams is not UNSET:
            field_dict["teams"] = teams

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_publisher import NotificationPublisher
        from ..models.project import Project
        from ..models.tag import Tag
        from ..models.team import Team

        d = dict(src_dict)
        name = d.pop("name")

        scope = NotificationRuleScope(d.pop("scope"))

        trigger_type = NotificationRuleTriggerType(d.pop("triggerType"))

        uuid = UUID(d.pop("uuid"))

        enabled = d.pop("enabled", UNSET)

        filter_expression = d.pop("filterExpression", UNSET)

        log_successful_publish = d.pop("logSuccessfulPublish", UNSET)

        message = d.pop("message", UNSET)

        _notification_level = d.pop("notificationLevel", UNSET)
        notification_level: NotificationRuleNotificationLevel | Unset
        if isinstance(_notification_level, Unset):
            notification_level = UNSET
        else:
            notification_level = NotificationRuleNotificationLevel(_notification_level)

        notify_children = d.pop("notifyChildren", UNSET)

        _notify_on = d.pop("notifyOn", UNSET)
        notify_on: list[NotificationRuleNotifyOnItem] | Unset = UNSET
        if _notify_on is not UNSET:
            notify_on = []
            for notify_on_item_data in _notify_on:
                notify_on_item = NotificationRuleNotifyOnItem(notify_on_item_data)

                notify_on.append(notify_on_item)

        _projects = d.pop("projects", UNSET)
        projects: list[Project] | Unset = UNSET
        if _projects is not UNSET:
            projects = []
            for projects_item_data in _projects:
                projects_item = Project.from_dict(projects_item_data)

                projects.append(projects_item)

        _publisher = d.pop("publisher", UNSET)
        publisher: NotificationPublisher | Unset
        if isinstance(_publisher, Unset):
            publisher = UNSET
        else:
            publisher = NotificationPublisher.from_dict(_publisher)

        publisher_config = d.pop("publisherConfig", UNSET)

        schedule_cron = d.pop("scheduleCron", UNSET)

        schedule_last_triggered_at = d.pop("scheduleLastTriggeredAt", UNSET)

        schedule_next_trigger_at = d.pop("scheduleNextTriggerAt", UNSET)

        schedule_skip_unchanged = d.pop("scheduleSkipUnchanged", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: list[Tag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = Tag.from_dict(tags_item_data)

                tags.append(tags_item)

        _teams = d.pop("teams", UNSET)
        teams: list[Team] | Unset = UNSET
        if _teams is not UNSET:
            teams = []
            for teams_item_data in _teams:
                teams_item = Team.from_dict(teams_item_data)

                teams.append(teams_item)

        notification_rule = cls(
            name=name,
            scope=scope,
            trigger_type=trigger_type,
            uuid=uuid,
            enabled=enabled,
            filter_expression=filter_expression,
            log_successful_publish=log_successful_publish,
            message=message,
            notification_level=notification_level,
            notify_children=notify_children,
            notify_on=notify_on,
            projects=projects,
            publisher=publisher,
            publisher_config=publisher_config,
            schedule_cron=schedule_cron,
            schedule_last_triggered_at=schedule_last_triggered_at,
            schedule_next_trigger_at=schedule_next_trigger_at,
            schedule_skip_unchanged=schedule_skip_unchanged,
            tags=tags,
            teams=teams,
        )

        notification_rule.additional_properties = d
        return notification_rule

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
