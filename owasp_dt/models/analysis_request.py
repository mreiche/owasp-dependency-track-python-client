from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.analysis_request_analysis_justification import (
    AnalysisRequestAnalysisJustification,
)
from ..models.analysis_request_analysis_response import AnalysisRequestAnalysisResponse
from ..models.analysis_request_analysis_state import AnalysisRequestAnalysisState
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalysisRequest")


@_attrs_define
class AnalysisRequest:
    """
    Attributes:
        component (str):
        vulnerability (str):
        analysis_details (str | Unset):
        analysis_justification (AnalysisRequestAnalysisJustification | Unset):
        analysis_response (AnalysisRequestAnalysisResponse | Unset):
        analysis_state (AnalysisRequestAnalysisState | Unset):
        comment (str | Unset):
        is_suppressed (bool | Unset):
        project (str | Unset):
        suppressed (bool | Unset):
    """

    component: str
    vulnerability: str
    analysis_details: str | Unset = UNSET
    analysis_justification: AnalysisRequestAnalysisJustification | Unset = UNSET
    analysis_response: AnalysisRequestAnalysisResponse | Unset = UNSET
    analysis_state: AnalysisRequestAnalysisState | Unset = UNSET
    comment: str | Unset = UNSET
    is_suppressed: bool | Unset = UNSET
    project: str | Unset = UNSET
    suppressed: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component = self.component

        vulnerability = self.vulnerability

        analysis_details = self.analysis_details

        analysis_justification: str | Unset = UNSET
        if not isinstance(self.analysis_justification, Unset):
            analysis_justification = self.analysis_justification.value

        analysis_response: str | Unset = UNSET
        if not isinstance(self.analysis_response, Unset):
            analysis_response = self.analysis_response.value

        analysis_state: str | Unset = UNSET
        if not isinstance(self.analysis_state, Unset):
            analysis_state = self.analysis_state.value

        comment = self.comment

        is_suppressed = self.is_suppressed

        project = self.project

        suppressed = self.suppressed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "component": component,
                "vulnerability": vulnerability,
            }
        )
        if analysis_details is not UNSET:
            field_dict["analysisDetails"] = analysis_details
        if analysis_justification is not UNSET:
            field_dict["analysisJustification"] = analysis_justification
        if analysis_response is not UNSET:
            field_dict["analysisResponse"] = analysis_response
        if analysis_state is not UNSET:
            field_dict["analysisState"] = analysis_state
        if comment is not UNSET:
            field_dict["comment"] = comment
        if is_suppressed is not UNSET:
            field_dict["isSuppressed"] = is_suppressed
        if project is not UNSET:
            field_dict["project"] = project
        if suppressed is not UNSET:
            field_dict["suppressed"] = suppressed

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        component = d.pop("component")

        vulnerability = d.pop("vulnerability")

        analysis_details = d.pop("analysisDetails", UNSET)

        _analysis_justification = d.pop("analysisJustification", UNSET)
        analysis_justification: AnalysisRequestAnalysisJustification | Unset
        if isinstance(_analysis_justification, Unset):
            analysis_justification = UNSET
        else:
            analysis_justification = AnalysisRequestAnalysisJustification(
                _analysis_justification
            )

        _analysis_response = d.pop("analysisResponse", UNSET)
        analysis_response: AnalysisRequestAnalysisResponse | Unset
        if isinstance(_analysis_response, Unset):
            analysis_response = UNSET
        else:
            analysis_response = AnalysisRequestAnalysisResponse(_analysis_response)

        _analysis_state = d.pop("analysisState", UNSET)
        analysis_state: AnalysisRequestAnalysisState | Unset
        if isinstance(_analysis_state, Unset):
            analysis_state = UNSET
        else:
            analysis_state = AnalysisRequestAnalysisState(_analysis_state)

        comment = d.pop("comment", UNSET)

        is_suppressed = d.pop("isSuppressed", UNSET)

        project = d.pop("project", UNSET)

        suppressed = d.pop("suppressed", UNSET)

        analysis_request = cls(
            component=component,
            vulnerability=vulnerability,
            analysis_details=analysis_details,
            analysis_justification=analysis_justification,
            analysis_response=analysis_response,
            analysis_state=analysis_state,
            comment=comment,
            is_suppressed=is_suppressed,
            project=project,
            suppressed=suppressed,
        )

        analysis_request.additional_properties = d
        return analysis_request

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
