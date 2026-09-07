from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vuln_policy_analysis_justification import VulnPolicyAnalysisJustification
from ..models.vuln_policy_analysis_state import VulnPolicyAnalysisState
from ..models.vuln_policy_analysis_vendor_response import (
    VulnPolicyAnalysisVendorResponse,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="VulnPolicyAnalysis")


@_attrs_define
class VulnPolicyAnalysis:
    """
    Attributes:
        state (VulnPolicyAnalysisState):
        justification (VulnPolicyAnalysisJustification | Unset):
        vendor_response (VulnPolicyAnalysisVendorResponse | Unset):
        details (str | Unset):
        suppress (bool | Unset):  Default: False.
    """

    state: VulnPolicyAnalysisState
    justification: VulnPolicyAnalysisJustification | Unset = UNSET
    vendor_response: VulnPolicyAnalysisVendorResponse | Unset = UNSET
    details: str | Unset = UNSET
    suppress: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state.value

        justification: str | Unset = UNSET
        if not isinstance(self.justification, Unset):
            justification = self.justification.value

        vendor_response: str | Unset = UNSET
        if not isinstance(self.vendor_response, Unset):
            vendor_response = self.vendor_response.value

        details = self.details

        suppress = self.suppress

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
            }
        )
        if justification is not UNSET:
            field_dict["justification"] = justification
        if vendor_response is not UNSET:
            field_dict["vendor_response"] = vendor_response
        if details is not UNSET:
            field_dict["details"] = details
        if suppress is not UNSET:
            field_dict["suppress"] = suppress

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        state = VulnPolicyAnalysisState(d.pop("state"))

        _justification = d.pop("justification", UNSET)
        justification: VulnPolicyAnalysisJustification | Unset
        if isinstance(_justification, Unset):
            justification = UNSET
        else:
            justification = VulnPolicyAnalysisJustification(_justification)

        _vendor_response = d.pop("vendor_response", UNSET)
        vendor_response: VulnPolicyAnalysisVendorResponse | Unset
        if isinstance(_vendor_response, Unset):
            vendor_response = UNSET
        else:
            vendor_response = VulnPolicyAnalysisVendorResponse(_vendor_response)

        details = d.pop("details", UNSET)

        suppress = d.pop("suppress", UNSET)

        vuln_policy_analysis = cls(
            state=state,
            justification=justification,
            vendor_response=vendor_response,
            details=details,
            suppress=suppress,
        )

        vuln_policy_analysis.additional_properties = d
        return vuln_policy_analysis

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
