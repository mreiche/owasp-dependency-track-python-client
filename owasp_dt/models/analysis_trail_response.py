from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.analysis_trail_response_analysis_justification import (
    AnalysisTrailResponseAnalysisJustification,
)
from ..models.analysis_trail_response_analysis_response import (
    AnalysisTrailResponseAnalysisResponse,
)
from ..models.analysis_trail_response_analysis_state import (
    AnalysisTrailResponseAnalysisState,
)
from ..models.analysis_trail_response_severity import AnalysisTrailResponseSeverity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comment import Comment


T = TypeVar("T", bound="AnalysisTrailResponse")


@_attrs_define
class AnalysisTrailResponse:
    """
    Attributes:
        analysis_comments (list[Comment]): Audit trail of analysis comments
        analysis_state (AnalysisTrailResponseAnalysisState): The state of the analysis decision
        is_suppressed (bool): Whether the finding is suppressed
        analysis_details (str | Unset): Free-form details of the analysis decision
        analysis_justification (AnalysisTrailResponseAnalysisJustification | Unset): The justification of the analysis
            decision
        analysis_response (AnalysisTrailResponseAnalysisResponse | Unset): The vendor response to the vulnerability
        cvss_v2_score (float | Unset): CVSS v2 score assigned by the analysis
        cvss_v2_vector (str | Unset): CVSS v2 vector assigned by the analysis
        cvss_v3_score (float | Unset): CVSS v3 score assigned by the analysis
        cvss_v3_vector (str | Unset): CVSS v3 vector assigned by the analysis
        cvss_v4_score (float | Unset): CVSS v4 score assigned by the analysis
        cvss_v4_vector (str | Unset): CVSS v4 vector assigned by the analysis
        owasp_score (float | Unset): OWASP Risk Rating score assigned by the analysis
        owasp_vector (str | Unset): OWASP Risk Rating vector assigned by the analysis
        severity (AnalysisTrailResponseSeverity | Unset): Severity assigned by the analysis
    """

    analysis_comments: list[Comment]
    analysis_state: AnalysisTrailResponseAnalysisState
    is_suppressed: bool
    analysis_details: str | Unset = UNSET
    analysis_justification: AnalysisTrailResponseAnalysisJustification | Unset = UNSET
    analysis_response: AnalysisTrailResponseAnalysisResponse | Unset = UNSET
    cvss_v2_score: float | Unset = UNSET
    cvss_v2_vector: str | Unset = UNSET
    cvss_v3_score: float | Unset = UNSET
    cvss_v3_vector: str | Unset = UNSET
    cvss_v4_score: float | Unset = UNSET
    cvss_v4_vector: str | Unset = UNSET
    owasp_score: float | Unset = UNSET
    owasp_vector: str | Unset = UNSET
    severity: AnalysisTrailResponseSeverity | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        analysis_comments = []
        for analysis_comments_item_data in self.analysis_comments:
            analysis_comments_item = analysis_comments_item_data.to_dict()
            analysis_comments.append(analysis_comments_item)

        analysis_state = self.analysis_state.value

        is_suppressed = self.is_suppressed

        analysis_details = self.analysis_details

        analysis_justification: str | Unset = UNSET
        if not isinstance(self.analysis_justification, Unset):
            analysis_justification = self.analysis_justification.value

        analysis_response: str | Unset = UNSET
        if not isinstance(self.analysis_response, Unset):
            analysis_response = self.analysis_response.value

        cvss_v2_score = self.cvss_v2_score

        cvss_v2_vector = self.cvss_v2_vector

        cvss_v3_score = self.cvss_v3_score

        cvss_v3_vector = self.cvss_v3_vector

        cvss_v4_score = self.cvss_v4_score

        cvss_v4_vector = self.cvss_v4_vector

        owasp_score = self.owasp_score

        owasp_vector = self.owasp_vector

        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "analysisComments": analysis_comments,
                "analysisState": analysis_state,
                "isSuppressed": is_suppressed,
            }
        )
        if analysis_details is not UNSET:
            field_dict["analysisDetails"] = analysis_details
        if analysis_justification is not UNSET:
            field_dict["analysisJustification"] = analysis_justification
        if analysis_response is not UNSET:
            field_dict["analysisResponse"] = analysis_response
        if cvss_v2_score is not UNSET:
            field_dict["cvssV2Score"] = cvss_v2_score
        if cvss_v2_vector is not UNSET:
            field_dict["cvssV2Vector"] = cvss_v2_vector
        if cvss_v3_score is not UNSET:
            field_dict["cvssV3Score"] = cvss_v3_score
        if cvss_v3_vector is not UNSET:
            field_dict["cvssV3Vector"] = cvss_v3_vector
        if cvss_v4_score is not UNSET:
            field_dict["cvssV4Score"] = cvss_v4_score
        if cvss_v4_vector is not UNSET:
            field_dict["cvssV4Vector"] = cvss_v4_vector
        if owasp_score is not UNSET:
            field_dict["owaspScore"] = owasp_score
        if owasp_vector is not UNSET:
            field_dict["owaspVector"] = owasp_vector
        if severity is not UNSET:
            field_dict["severity"] = severity

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.comment import Comment

        d = dict(src_dict)
        analysis_comments = []
        _analysis_comments = d.pop("analysisComments")
        for analysis_comments_item_data in _analysis_comments:
            analysis_comments_item = Comment.from_dict(analysis_comments_item_data)

            analysis_comments.append(analysis_comments_item)

        analysis_state = AnalysisTrailResponseAnalysisState(d.pop("analysisState"))

        is_suppressed = d.pop("isSuppressed")

        analysis_details = d.pop("analysisDetails", UNSET)

        _analysis_justification = d.pop("analysisJustification", UNSET)
        analysis_justification: AnalysisTrailResponseAnalysisJustification | Unset
        if isinstance(_analysis_justification, Unset):
            analysis_justification = UNSET
        else:
            analysis_justification = AnalysisTrailResponseAnalysisJustification(
                _analysis_justification
            )

        _analysis_response = d.pop("analysisResponse", UNSET)
        analysis_response: AnalysisTrailResponseAnalysisResponse | Unset
        if isinstance(_analysis_response, Unset):
            analysis_response = UNSET
        else:
            analysis_response = AnalysisTrailResponseAnalysisResponse(
                _analysis_response
            )

        cvss_v2_score = d.pop("cvssV2Score", UNSET)

        cvss_v2_vector = d.pop("cvssV2Vector", UNSET)

        cvss_v3_score = d.pop("cvssV3Score", UNSET)

        cvss_v3_vector = d.pop("cvssV3Vector", UNSET)

        cvss_v4_score = d.pop("cvssV4Score", UNSET)

        cvss_v4_vector = d.pop("cvssV4Vector", UNSET)

        owasp_score = d.pop("owaspScore", UNSET)

        owasp_vector = d.pop("owaspVector", UNSET)

        _severity = d.pop("severity", UNSET)
        severity: AnalysisTrailResponseSeverity | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = AnalysisTrailResponseSeverity(_severity)

        analysis_trail_response = cls(
            analysis_comments=analysis_comments,
            analysis_state=analysis_state,
            is_suppressed=is_suppressed,
            analysis_details=analysis_details,
            analysis_justification=analysis_justification,
            analysis_response=analysis_response,
            cvss_v2_score=cvss_v2_score,
            cvss_v2_vector=cvss_v2_vector,
            cvss_v3_score=cvss_v3_score,
            cvss_v3_vector=cvss_v3_vector,
            cvss_v4_score=cvss_v4_score,
            cvss_v4_vector=cvss_v4_vector,
            owasp_score=owasp_score,
            owasp_vector=owasp_vector,
            severity=severity,
        )

        analysis_trail_response.additional_properties = d
        return analysis_trail_response

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
