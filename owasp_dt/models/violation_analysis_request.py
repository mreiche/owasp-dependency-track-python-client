from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.violation_analysis_request_analysis_state import (
    ViolationAnalysisRequestAnalysisState,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ViolationAnalysisRequest")


@_attrs_define
class ViolationAnalysisRequest:
    """
    Attributes:
        component (str):
        policy_violation (str):
        analysis_state (ViolationAnalysisRequestAnalysisState | Unset):
        comment (str | Unset):
        is_suppressed (bool | Unset):
        suppressed (bool | Unset):
    """

    component: str
    policy_violation: str
    analysis_state: ViolationAnalysisRequestAnalysisState | Unset = UNSET
    comment: str | Unset = UNSET
    is_suppressed: bool | Unset = UNSET
    suppressed: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component = self.component

        policy_violation = self.policy_violation

        analysis_state: str | Unset = UNSET
        if not isinstance(self.analysis_state, Unset):
            analysis_state = self.analysis_state.value

        comment = self.comment

        is_suppressed = self.is_suppressed

        suppressed = self.suppressed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "component": component,
                "policyViolation": policy_violation,
            }
        )
        if analysis_state is not UNSET:
            field_dict["analysisState"] = analysis_state
        if comment is not UNSET:
            field_dict["comment"] = comment
        if is_suppressed is not UNSET:
            field_dict["isSuppressed"] = is_suppressed
        if suppressed is not UNSET:
            field_dict["suppressed"] = suppressed

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        component = d.pop("component")

        policy_violation = d.pop("policyViolation")

        _analysis_state = d.pop("analysisState", UNSET)
        analysis_state: ViolationAnalysisRequestAnalysisState | Unset
        if isinstance(_analysis_state, Unset):
            analysis_state = UNSET
        else:
            analysis_state = ViolationAnalysisRequestAnalysisState(_analysis_state)

        comment = d.pop("comment", UNSET)

        is_suppressed = d.pop("isSuppressed", UNSET)

        suppressed = d.pop("suppressed", UNSET)

        violation_analysis_request = cls(
            component=component,
            policy_violation=policy_violation,
            analysis_state=analysis_state,
            comment=comment,
            is_suppressed=is_suppressed,
            suppressed=suppressed,
        )

        violation_analysis_request.additional_properties = d
        return violation_analysis_request

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
