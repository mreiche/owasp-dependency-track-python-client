from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vuln_policy_rating_method import VulnPolicyRatingMethod
from ..models.vuln_policy_rating_severity import VulnPolicyRatingSeverity
from ..types import UNSET, Unset

T = TypeVar("T", bound="VulnPolicyRating")


@_attrs_define
class VulnPolicyRating:
    """
    Attributes:
        method (VulnPolicyRatingMethod):
        severity (VulnPolicyRatingSeverity):
        vector (str | Unset):
        score (float | Unset):
    """

    method: VulnPolicyRatingMethod
    severity: VulnPolicyRatingSeverity
    vector: str | Unset = UNSET
    score: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        severity = self.severity.value

        vector = self.vector

        score = self.score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "severity": severity,
            }
        )
        if vector is not UNSET:
            field_dict["vector"] = vector
        if score is not UNSET:
            field_dict["score"] = score

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        method = VulnPolicyRatingMethod(d.pop("method"))

        severity = VulnPolicyRatingSeverity(d.pop("severity"))

        vector = d.pop("vector", UNSET)

        score = d.pop("score", UNSET)

        vuln_policy_rating = cls(
            method=method,
            severity=severity,
            vector=vector,
            score=score,
        )

        vuln_policy_rating.additional_properties = d
        return vuln_policy_rating

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
