from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.analysis_analysis_justification import AnalysisAnalysisJustification
from ..models.analysis_analysis_response import AnalysisAnalysisResponse
from ..models.analysis_analysis_state import AnalysisAnalysisState
from ..models.analysis_severity import AnalysisSeverity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analysis_comment import AnalysisComment


T = TypeVar("T", bound="Analysis")


@_attrs_define
class Analysis:
    """
    Attributes:
        analysis_details (str):
        analysis_justification (AnalysisAnalysisJustification):
        analysis_response (AnalysisAnalysisResponse):
        analysis_state (AnalysisAnalysisState):
        analysis_comments (list[AnalysisComment] | Unset):
        cvss_v2_score (float | Unset):
        cvss_v2_vector (str | Unset):
        cvss_v3_score (float | Unset):
        cvss_v3_vector (str | Unset):
        cvss_v4_score (float | Unset):
        cvss_v4_vector (str | Unset):
        is_suppressed (bool | Unset):
        owasp_score (float | Unset):
        owasp_vector (str | Unset):
        severity (AnalysisSeverity | Unset):
    """

    analysis_details: str
    analysis_justification: AnalysisAnalysisJustification
    analysis_response: AnalysisAnalysisResponse
    analysis_state: AnalysisAnalysisState
    analysis_comments: list[AnalysisComment] | Unset = UNSET
    cvss_v2_score: float | Unset = UNSET
    cvss_v2_vector: str | Unset = UNSET
    cvss_v3_score: float | Unset = UNSET
    cvss_v3_vector: str | Unset = UNSET
    cvss_v4_score: float | Unset = UNSET
    cvss_v4_vector: str | Unset = UNSET
    is_suppressed: bool | Unset = UNSET
    owasp_score: float | Unset = UNSET
    owasp_vector: str | Unset = UNSET
    severity: AnalysisSeverity | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        analysis_details = self.analysis_details

        analysis_justification = self.analysis_justification.value

        analysis_response = self.analysis_response.value

        analysis_state = self.analysis_state.value

        analysis_comments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.analysis_comments, Unset):
            analysis_comments = []
            for analysis_comments_item_data in self.analysis_comments:
                analysis_comments_item = analysis_comments_item_data.to_dict()
                analysis_comments.append(analysis_comments_item)

        cvss_v2_score = self.cvss_v2_score

        cvss_v2_vector = self.cvss_v2_vector

        cvss_v3_score = self.cvss_v3_score

        cvss_v3_vector = self.cvss_v3_vector

        cvss_v4_score = self.cvss_v4_score

        cvss_v4_vector = self.cvss_v4_vector

        is_suppressed = self.is_suppressed

        owasp_score = self.owasp_score

        owasp_vector = self.owasp_vector

        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "analysisDetails": analysis_details,
                "analysisJustification": analysis_justification,
                "analysisResponse": analysis_response,
                "analysisState": analysis_state,
            }
        )
        if analysis_comments is not UNSET:
            field_dict["analysisComments"] = analysis_comments
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
        if is_suppressed is not UNSET:
            field_dict["isSuppressed"] = is_suppressed
        if owasp_score is not UNSET:
            field_dict["owaspScore"] = owasp_score
        if owasp_vector is not UNSET:
            field_dict["owaspVector"] = owasp_vector
        if severity is not UNSET:
            field_dict["severity"] = severity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analysis_comment import AnalysisComment

        d = dict(src_dict)
        analysis_details = d.pop("analysisDetails")

        analysis_justification = AnalysisAnalysisJustification(
            d.pop("analysisJustification")
        )

        analysis_response = AnalysisAnalysisResponse(d.pop("analysisResponse"))

        analysis_state = AnalysisAnalysisState(d.pop("analysisState"))

        _analysis_comments = d.pop("analysisComments", UNSET)
        analysis_comments: list[AnalysisComment] | Unset = UNSET
        if _analysis_comments is not UNSET:
            analysis_comments = []
            for analysis_comments_item_data in _analysis_comments:
                analysis_comments_item = AnalysisComment.from_dict(
                    analysis_comments_item_data
                )

                analysis_comments.append(analysis_comments_item)

        cvss_v2_score = d.pop("cvssV2Score", UNSET)

        cvss_v2_vector = d.pop("cvssV2Vector", UNSET)

        cvss_v3_score = d.pop("cvssV3Score", UNSET)

        cvss_v3_vector = d.pop("cvssV3Vector", UNSET)

        cvss_v4_score = d.pop("cvssV4Score", UNSET)

        cvss_v4_vector = d.pop("cvssV4Vector", UNSET)

        is_suppressed = d.pop("isSuppressed", UNSET)

        owasp_score = d.pop("owaspScore", UNSET)

        owasp_vector = d.pop("owaspVector", UNSET)

        _severity = d.pop("severity", UNSET)
        severity: AnalysisSeverity | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = AnalysisSeverity(_severity)

        analysis = cls(
            analysis_details=analysis_details,
            analysis_justification=analysis_justification,
            analysis_response=analysis_response,
            analysis_state=analysis_state,
            analysis_comments=analysis_comments,
            cvss_v2_score=cvss_v2_score,
            cvss_v2_vector=cvss_v2_vector,
            cvss_v3_score=cvss_v3_score,
            cvss_v3_vector=cvss_v3_vector,
            cvss_v4_score=cvss_v4_score,
            cvss_v4_vector=cvss_v4_vector,
            is_suppressed=is_suppressed,
            owasp_score=owasp_score,
            owasp_vector=owasp_vector,
            severity=severity,
        )

        analysis.additional_properties = d
        return analysis

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
