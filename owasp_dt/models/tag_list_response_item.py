from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TagListResponseItem")


@_attrs_define
class TagListResponseItem:
    """
    Attributes:
        collection_project_count (int): Number of collection projects assigned to this tag
        name (str): Name of the tag
        notification_rule_count (int): Number of notification rules assigned to this tag
        policy_count (int): Number of policies assigned to this tag
        project_count (int): Number of projects assigned to this tag
        vulnerability_count (int): Number of vulnerabilities assigned to this tag
    """

    collection_project_count: int
    name: str
    notification_rule_count: int
    policy_count: int
    project_count: int
    vulnerability_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_project_count = self.collection_project_count

        name = self.name

        notification_rule_count = self.notification_rule_count

        policy_count = self.policy_count

        project_count = self.project_count

        vulnerability_count = self.vulnerability_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collectionProjectCount": collection_project_count,
                "name": name,
                "notificationRuleCount": notification_rule_count,
                "policyCount": policy_count,
                "projectCount": project_count,
                "vulnerabilityCount": vulnerability_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collection_project_count = d.pop("collectionProjectCount")

        name = d.pop("name")

        notification_rule_count = d.pop("notificationRuleCount")

        policy_count = d.pop("policyCount")

        project_count = d.pop("projectCount")

        vulnerability_count = d.pop("vulnerabilityCount")

        tag_list_response_item = cls(
            collection_project_count=collection_project_count,
            name=name,
            notification_rule_count=notification_rule_count,
            policy_count=policy_count,
            project_count=project_count,
            vulnerability_count=vulnerability_count,
        )

        tag_list_response_item.additional_properties = d
        return tag_list_response_item

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
