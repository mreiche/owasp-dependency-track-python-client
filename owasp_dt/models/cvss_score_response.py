from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CvssScoreResponse")


@_attrs_define
class CvssScoreResponse:
    """
    Attributes:
        base_score (float | Unset):
        environmental_score (float | Unset):
        exploitability_sub_score (float | Unset):
        impact_sub_score (float | Unset):
        modified_impact_sub_score (float | Unset):
        temporal_score (float | Unset):
    """

    base_score: float | Unset = UNSET
    environmental_score: float | Unset = UNSET
    exploitability_sub_score: float | Unset = UNSET
    impact_sub_score: float | Unset = UNSET
    modified_impact_sub_score: float | Unset = UNSET
    temporal_score: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_score = self.base_score

        environmental_score = self.environmental_score

        exploitability_sub_score = self.exploitability_sub_score

        impact_sub_score = self.impact_sub_score

        modified_impact_sub_score = self.modified_impact_sub_score

        temporal_score = self.temporal_score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_score is not UNSET:
            field_dict["baseScore"] = base_score
        if environmental_score is not UNSET:
            field_dict["environmentalScore"] = environmental_score
        if exploitability_sub_score is not UNSET:
            field_dict["exploitabilitySubScore"] = exploitability_sub_score
        if impact_sub_score is not UNSET:
            field_dict["impactSubScore"] = impact_sub_score
        if modified_impact_sub_score is not UNSET:
            field_dict["modifiedImpactSubScore"] = modified_impact_sub_score
        if temporal_score is not UNSET:
            field_dict["temporalScore"] = temporal_score

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        base_score = d.pop("baseScore", UNSET)

        environmental_score = d.pop("environmentalScore", UNSET)

        exploitability_sub_score = d.pop("exploitabilitySubScore", UNSET)

        impact_sub_score = d.pop("impactSubScore", UNSET)

        modified_impact_sub_score = d.pop("modifiedImpactSubScore", UNSET)

        temporal_score = d.pop("temporalScore", UNSET)

        cvss_score_response = cls(
            base_score=base_score,
            environmental_score=environmental_score,
            exploitability_sub_score=exploitability_sub_score,
            impact_sub_score=impact_sub_score,
            modified_impact_sub_score=modified_impact_sub_score,
            temporal_score=temporal_score,
        )

        cvss_score_response.additional_properties = d
        return cvss_score_response

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
