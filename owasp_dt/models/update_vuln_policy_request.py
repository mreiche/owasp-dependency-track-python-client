from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vuln_policy_operation_mode import VulnPolicyOperationMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vuln_policy_analysis import VulnPolicyAnalysis
    from ..models.vuln_policy_rating import VulnPolicyRating


T = TypeVar("T", bound="UpdateVulnPolicyRequest")


@_attrs_define
class UpdateVulnPolicyRequest:
    """
    Attributes:
        name (str):
        condition (str):
        analysis (VulnPolicyAnalysis):
        description (str | Unset):
        author (str | Unset):
        ratings (list[VulnPolicyRating] | Unset):
        operation_mode (VulnPolicyOperationMode | Unset):
        priority (int | Unset):  Default: 0.
        valid_from (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
        valid_until (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
    """

    name: str
    condition: str
    analysis: VulnPolicyAnalysis
    description: str | Unset = UNSET
    author: str | Unset = UNSET
    ratings: list[VulnPolicyRating] | Unset = UNSET
    operation_mode: VulnPolicyOperationMode | Unset = UNSET
    priority: int | Unset = 0
    valid_from: int | Unset = UNSET
    valid_until: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        condition = self.condition

        analysis = self.analysis.to_dict()

        description = self.description

        author = self.author

        ratings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ratings, Unset):
            ratings = []
            for ratings_item_data in self.ratings:
                ratings_item = ratings_item_data.to_dict()
                ratings.append(ratings_item)

        operation_mode: str | Unset = UNSET
        if not isinstance(self.operation_mode, Unset):
            operation_mode = self.operation_mode.value

        priority = self.priority

        valid_from = self.valid_from

        valid_until = self.valid_until

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "condition": condition,
                "analysis": analysis,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if author is not UNSET:
            field_dict["author"] = author
        if ratings is not UNSET:
            field_dict["ratings"] = ratings
        if operation_mode is not UNSET:
            field_dict["operation_mode"] = operation_mode
        if priority is not UNSET:
            field_dict["priority"] = priority
        if valid_from is not UNSET:
            field_dict["valid_from"] = valid_from
        if valid_until is not UNSET:
            field_dict["valid_until"] = valid_until

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vuln_policy_analysis import VulnPolicyAnalysis
        from ..models.vuln_policy_rating import VulnPolicyRating

        d = dict(src_dict)
        name = d.pop("name")

        condition = d.pop("condition")

        analysis = VulnPolicyAnalysis.from_dict(d.pop("analysis"))

        description = d.pop("description", UNSET)

        author = d.pop("author", UNSET)

        _ratings = d.pop("ratings", UNSET)
        ratings: list[VulnPolicyRating] | Unset = UNSET
        if _ratings is not UNSET:
            ratings = []
            for ratings_item_data in _ratings:
                ratings_item = VulnPolicyRating.from_dict(ratings_item_data)

                ratings.append(ratings_item)

        _operation_mode = d.pop("operation_mode", UNSET)
        operation_mode: VulnPolicyOperationMode | Unset
        if isinstance(_operation_mode, Unset):
            operation_mode = UNSET
        else:
            operation_mode = VulnPolicyOperationMode(_operation_mode)

        priority = d.pop("priority", UNSET)

        valid_from = d.pop("valid_from", UNSET)

        valid_until = d.pop("valid_until", UNSET)

        update_vuln_policy_request = cls(
            name=name,
            condition=condition,
            analysis=analysis,
            description=description,
            author=author,
            ratings=ratings,
            operation_mode=operation_mode,
            priority=priority,
            valid_from=valid_from,
            valid_until=valid_until,
        )

        update_vuln_policy_request.additional_properties = d
        return update_vuln_policy_request

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
