from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.violation_analysis_response_analysis_state import (
    ViolationAnalysisResponseAnalysisState,
)

if TYPE_CHECKING:
    from ..models.comment import Comment


T = TypeVar("T", bound="ViolationAnalysisResponse")


@_attrs_define
class ViolationAnalysisResponse:
    """
    Attributes:
        analysis_comments (list[Comment]): Audit trail of analysis comments
        analysis_state (ViolationAnalysisResponseAnalysisState): The state of the analysis decision
        is_suppressed (bool): Whether the policy violation is suppressed
    """

    analysis_comments: list[Comment]
    analysis_state: ViolationAnalysisResponseAnalysisState
    is_suppressed: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        analysis_comments = []
        for analysis_comments_item_data in self.analysis_comments:
            analysis_comments_item = analysis_comments_item_data.to_dict()
            analysis_comments.append(analysis_comments_item)

        analysis_state = self.analysis_state.value

        is_suppressed = self.is_suppressed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "analysisComments": analysis_comments,
                "analysisState": analysis_state,
                "isSuppressed": is_suppressed,
            }
        )

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

        analysis_state = ViolationAnalysisResponseAnalysisState(d.pop("analysisState"))

        is_suppressed = d.pop("isSuppressed")

        violation_analysis_response = cls(
            analysis_comments=analysis_comments,
            analysis_state=analysis_state,
            is_suppressed=is_suppressed,
        )

        violation_analysis_response.additional_properties = d
        return violation_analysis_response

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
