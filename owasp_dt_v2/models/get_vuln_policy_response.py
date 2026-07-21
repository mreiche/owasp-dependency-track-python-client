from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vuln_policy_operation_mode import VulnPolicyOperationMode
from ..models.vuln_policy_source import VulnPolicySource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vuln_policy_analysis import VulnPolicyAnalysis
    from ..models.vuln_policy_rating import VulnPolicyRating


T = TypeVar("T", bound="GetVulnPolicyResponse")


@_attrs_define
class GetVulnPolicyResponse:
    """
    Attributes:
        uuid (UUID):
        name (str):
        condition (str):
        analysis (VulnPolicyAnalysis):
        operation_mode (VulnPolicyOperationMode):
        priority (int):
        source (VulnPolicySource):
        description (str | Unset):
        author (str | Unset):
        ratings (list[VulnPolicyRating] | Unset):
        valid_from (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
        valid_until (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
        created (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
        updated (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
    """

    uuid: UUID
    name: str
    condition: str
    analysis: VulnPolicyAnalysis
    operation_mode: VulnPolicyOperationMode
    priority: int
    source: VulnPolicySource
    description: str | Unset = UNSET
    author: str | Unset = UNSET
    ratings: list[VulnPolicyRating] | Unset = UNSET
    valid_from: int | Unset = UNSET
    valid_until: int | Unset = UNSET
    created: int | Unset = UNSET
    updated: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        condition = self.condition

        analysis = self.analysis.to_dict()

        operation_mode = self.operation_mode.value

        priority = self.priority

        source = self.source.value

        description = self.description

        author = self.author

        ratings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ratings, Unset):
            ratings = []
            for ratings_item_data in self.ratings:
                ratings_item = ratings_item_data.to_dict()
                ratings.append(ratings_item)

        valid_from = self.valid_from

        valid_until = self.valid_until

        created = self.created

        updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "condition": condition,
                "analysis": analysis,
                "operation_mode": operation_mode,
                "priority": priority,
                "source": source,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if author is not UNSET:
            field_dict["author"] = author
        if ratings is not UNSET:
            field_dict["ratings"] = ratings
        if valid_from is not UNSET:
            field_dict["valid_from"] = valid_from
        if valid_until is not UNSET:
            field_dict["valid_until"] = valid_until
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vuln_policy_analysis import VulnPolicyAnalysis
        from ..models.vuln_policy_rating import VulnPolicyRating

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        condition = d.pop("condition")

        analysis = VulnPolicyAnalysis.from_dict(d.pop("analysis"))

        operation_mode = VulnPolicyOperationMode(d.pop("operation_mode"))

        priority = d.pop("priority")

        source = VulnPolicySource(d.pop("source"))

        description = d.pop("description", UNSET)

        author = d.pop("author", UNSET)

        _ratings = d.pop("ratings", UNSET)
        ratings: list[VulnPolicyRating] | Unset = UNSET
        if _ratings is not UNSET:
            ratings = []
            for ratings_item_data in _ratings:
                ratings_item = VulnPolicyRating.from_dict(ratings_item_data)

                ratings.append(ratings_item)

        valid_from = d.pop("valid_from", UNSET)

        valid_until = d.pop("valid_until", UNSET)

        created = d.pop("created", UNSET)

        updated = d.pop("updated", UNSET)

        get_vuln_policy_response = cls(
            uuid=uuid,
            name=name,
            condition=condition,
            analysis=analysis,
            operation_mode=operation_mode,
            priority=priority,
            source=source,
            description=description,
            author=author,
            ratings=ratings,
            valid_from=valid_from,
            valid_until=valid_until,
            created=created,
            updated=updated,
        )

        get_vuln_policy_response.additional_properties = d
        return get_vuln_policy_response

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
