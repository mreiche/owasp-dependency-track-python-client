from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.finding_analysis_state import FindingAnalysisState
from ..types import UNSET, Unset

T = TypeVar("T", bound="FindingAnalysis")


@_attrs_define
class FindingAnalysis:
    """
    Attributes:
        state (FindingAnalysisState | Unset):
        is_suppressed (bool | Unset):
    """

    state: FindingAnalysisState | Unset = UNSET
    is_suppressed: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        is_suppressed = self.is_suppressed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if is_suppressed is not UNSET:
            field_dict["isSuppressed"] = is_suppressed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: FindingAnalysisState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = FindingAnalysisState(_state)

        is_suppressed = d.pop("isSuppressed", UNSET)

        finding_analysis = cls(
            state=state,
            is_suppressed=is_suppressed,
        )

        finding_analysis.additional_properties = d
        return finding_analysis

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
