from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vuln_policy_operation_mode import VulnPolicyOperationMode
from ..models.vuln_policy_source import VulnPolicySource
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListVulnPoliciesResponseItem")


@_attrs_define
class ListVulnPoliciesResponseItem:
    """
    Attributes:
        uuid (UUID):
        name (str):
        priority (int):
        operation_mode (VulnPolicyOperationMode):
        source (VulnPolicySource):
        description (str | Unset):
        author (str | Unset):
    """

    uuid: UUID
    name: str
    priority: int
    operation_mode: VulnPolicyOperationMode
    source: VulnPolicySource
    description: str | Unset = UNSET
    author: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        priority = self.priority

        operation_mode = self.operation_mode.value

        source = self.source.value

        description = self.description

        author = self.author

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "priority": priority,
                "operation_mode": operation_mode,
                "source": source,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if author is not UNSET:
            field_dict["author"] = author

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        priority = d.pop("priority")

        operation_mode = VulnPolicyOperationMode(d.pop("operation_mode"))

        source = VulnPolicySource(d.pop("source"))

        description = d.pop("description", UNSET)

        author = d.pop("author", UNSET)

        list_vuln_policies_response_item = cls(
            uuid=uuid,
            name=name,
            priority=priority,
            operation_mode=operation_mode,
            source=source,
            description=description,
            author=author,
        )

        list_vuln_policies_response_item.additional_properties = d
        return list_vuln_policies_response_item

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
