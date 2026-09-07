from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortfolioMetrics")


@_attrs_define
class PortfolioMetrics:
    """
    Attributes:
        first_occurrence (int): UNIX epoch timestamp in milliseconds
        last_occurrence (int): UNIX epoch timestamp in milliseconds
        components (int | Unset):
        critical (int | Unset):
        findings_audited (int | Unset):
        findings_total (int | Unset):
        findings_unaudited (int | Unset):
        high (int | Unset):
        inherited_risk_score (float | Unset):
        kev (int | Unset):
        low (int | Unset):
        medium (int | Unset):
        policy_violations_audited (int | Unset):
        policy_violations_fail (int | Unset):
        policy_violations_info (int | Unset):
        policy_violations_license_audited (int | Unset):
        policy_violations_license_total (int | Unset):
        policy_violations_license_unaudited (int | Unset):
        policy_violations_operational_audited (int | Unset):
        policy_violations_operational_total (int | Unset):
        policy_violations_operational_unaudited (int | Unset):
        policy_violations_security_audited (int | Unset):
        policy_violations_security_total (int | Unset):
        policy_violations_security_unaudited (int | Unset):
        policy_violations_total (int | Unset):
        policy_violations_unaudited (int | Unset):
        policy_violations_warn (int | Unset):
        projects (int | Unset):
        suppressed (int | Unset):
        unassigned (int | Unset):
        vulnerabilities (int | Unset):
        vulnerable_components (int | Unset):
        vulnerable_projects (int | Unset):
    """

    first_occurrence: int
    last_occurrence: int
    components: int | Unset = UNSET
    critical: int | Unset = UNSET
    findings_audited: int | Unset = UNSET
    findings_total: int | Unset = UNSET
    findings_unaudited: int | Unset = UNSET
    high: int | Unset = UNSET
    inherited_risk_score: float | Unset = UNSET
    kev: int | Unset = UNSET
    low: int | Unset = UNSET
    medium: int | Unset = UNSET
    policy_violations_audited: int | Unset = UNSET
    policy_violations_fail: int | Unset = UNSET
    policy_violations_info: int | Unset = UNSET
    policy_violations_license_audited: int | Unset = UNSET
    policy_violations_license_total: int | Unset = UNSET
    policy_violations_license_unaudited: int | Unset = UNSET
    policy_violations_operational_audited: int | Unset = UNSET
    policy_violations_operational_total: int | Unset = UNSET
    policy_violations_operational_unaudited: int | Unset = UNSET
    policy_violations_security_audited: int | Unset = UNSET
    policy_violations_security_total: int | Unset = UNSET
    policy_violations_security_unaudited: int | Unset = UNSET
    policy_violations_total: int | Unset = UNSET
    policy_violations_unaudited: int | Unset = UNSET
    policy_violations_warn: int | Unset = UNSET
    projects: int | Unset = UNSET
    suppressed: int | Unset = UNSET
    unassigned: int | Unset = UNSET
    vulnerabilities: int | Unset = UNSET
    vulnerable_components: int | Unset = UNSET
    vulnerable_projects: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_occurrence = self.first_occurrence

        last_occurrence = self.last_occurrence

        components = self.components

        critical = self.critical

        findings_audited = self.findings_audited

        findings_total = self.findings_total

        findings_unaudited = self.findings_unaudited

        high = self.high

        inherited_risk_score = self.inherited_risk_score

        kev = self.kev

        low = self.low

        medium = self.medium

        policy_violations_audited = self.policy_violations_audited

        policy_violations_fail = self.policy_violations_fail

        policy_violations_info = self.policy_violations_info

        policy_violations_license_audited = self.policy_violations_license_audited

        policy_violations_license_total = self.policy_violations_license_total

        policy_violations_license_unaudited = self.policy_violations_license_unaudited

        policy_violations_operational_audited = (
            self.policy_violations_operational_audited
        )

        policy_violations_operational_total = self.policy_violations_operational_total

        policy_violations_operational_unaudited = (
            self.policy_violations_operational_unaudited
        )

        policy_violations_security_audited = self.policy_violations_security_audited

        policy_violations_security_total = self.policy_violations_security_total

        policy_violations_security_unaudited = self.policy_violations_security_unaudited

        policy_violations_total = self.policy_violations_total

        policy_violations_unaudited = self.policy_violations_unaudited

        policy_violations_warn = self.policy_violations_warn

        projects = self.projects

        suppressed = self.suppressed

        unassigned = self.unassigned

        vulnerabilities = self.vulnerabilities

        vulnerable_components = self.vulnerable_components

        vulnerable_projects = self.vulnerable_projects

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "firstOccurrence": first_occurrence,
                "lastOccurrence": last_occurrence,
            }
        )
        if components is not UNSET:
            field_dict["components"] = components
        if critical is not UNSET:
            field_dict["critical"] = critical
        if findings_audited is not UNSET:
            field_dict["findingsAudited"] = findings_audited
        if findings_total is not UNSET:
            field_dict["findingsTotal"] = findings_total
        if findings_unaudited is not UNSET:
            field_dict["findingsUnaudited"] = findings_unaudited
        if high is not UNSET:
            field_dict["high"] = high
        if inherited_risk_score is not UNSET:
            field_dict["inheritedRiskScore"] = inherited_risk_score
        if kev is not UNSET:
            field_dict["kev"] = kev
        if low is not UNSET:
            field_dict["low"] = low
        if medium is not UNSET:
            field_dict["medium"] = medium
        if policy_violations_audited is not UNSET:
            field_dict["policyViolationsAudited"] = policy_violations_audited
        if policy_violations_fail is not UNSET:
            field_dict["policyViolationsFail"] = policy_violations_fail
        if policy_violations_info is not UNSET:
            field_dict["policyViolationsInfo"] = policy_violations_info
        if policy_violations_license_audited is not UNSET:
            field_dict["policyViolationsLicenseAudited"] = (
                policy_violations_license_audited
            )
        if policy_violations_license_total is not UNSET:
            field_dict["policyViolationsLicenseTotal"] = policy_violations_license_total
        if policy_violations_license_unaudited is not UNSET:
            field_dict["policyViolationsLicenseUnaudited"] = (
                policy_violations_license_unaudited
            )
        if policy_violations_operational_audited is not UNSET:
            field_dict["policyViolationsOperationalAudited"] = (
                policy_violations_operational_audited
            )
        if policy_violations_operational_total is not UNSET:
            field_dict["policyViolationsOperationalTotal"] = (
                policy_violations_operational_total
            )
        if policy_violations_operational_unaudited is not UNSET:
            field_dict["policyViolationsOperationalUnaudited"] = (
                policy_violations_operational_unaudited
            )
        if policy_violations_security_audited is not UNSET:
            field_dict["policyViolationsSecurityAudited"] = (
                policy_violations_security_audited
            )
        if policy_violations_security_total is not UNSET:
            field_dict["policyViolationsSecurityTotal"] = (
                policy_violations_security_total
            )
        if policy_violations_security_unaudited is not UNSET:
            field_dict["policyViolationsSecurityUnaudited"] = (
                policy_violations_security_unaudited
            )
        if policy_violations_total is not UNSET:
            field_dict["policyViolationsTotal"] = policy_violations_total
        if policy_violations_unaudited is not UNSET:
            field_dict["policyViolationsUnaudited"] = policy_violations_unaudited
        if policy_violations_warn is not UNSET:
            field_dict["policyViolationsWarn"] = policy_violations_warn
        if projects is not UNSET:
            field_dict["projects"] = projects
        if suppressed is not UNSET:
            field_dict["suppressed"] = suppressed
        if unassigned is not UNSET:
            field_dict["unassigned"] = unassigned
        if vulnerabilities is not UNSET:
            field_dict["vulnerabilities"] = vulnerabilities
        if vulnerable_components is not UNSET:
            field_dict["vulnerableComponents"] = vulnerable_components
        if vulnerable_projects is not UNSET:
            field_dict["vulnerableProjects"] = vulnerable_projects

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        first_occurrence = d.pop("firstOccurrence")

        last_occurrence = d.pop("lastOccurrence")

        components = d.pop("components", UNSET)

        critical = d.pop("critical", UNSET)

        findings_audited = d.pop("findingsAudited", UNSET)

        findings_total = d.pop("findingsTotal", UNSET)

        findings_unaudited = d.pop("findingsUnaudited", UNSET)

        high = d.pop("high", UNSET)

        inherited_risk_score = d.pop("inheritedRiskScore", UNSET)

        kev = d.pop("kev", UNSET)

        low = d.pop("low", UNSET)

        medium = d.pop("medium", UNSET)

        policy_violations_audited = d.pop("policyViolationsAudited", UNSET)

        policy_violations_fail = d.pop("policyViolationsFail", UNSET)

        policy_violations_info = d.pop("policyViolationsInfo", UNSET)

        policy_violations_license_audited = d.pop(
            "policyViolationsLicenseAudited", UNSET
        )

        policy_violations_license_total = d.pop("policyViolationsLicenseTotal", UNSET)

        policy_violations_license_unaudited = d.pop(
            "policyViolationsLicenseUnaudited", UNSET
        )

        policy_violations_operational_audited = d.pop(
            "policyViolationsOperationalAudited", UNSET
        )

        policy_violations_operational_total = d.pop(
            "policyViolationsOperationalTotal", UNSET
        )

        policy_violations_operational_unaudited = d.pop(
            "policyViolationsOperationalUnaudited", UNSET
        )

        policy_violations_security_audited = d.pop(
            "policyViolationsSecurityAudited", UNSET
        )

        policy_violations_security_total = d.pop("policyViolationsSecurityTotal", UNSET)

        policy_violations_security_unaudited = d.pop(
            "policyViolationsSecurityUnaudited", UNSET
        )

        policy_violations_total = d.pop("policyViolationsTotal", UNSET)

        policy_violations_unaudited = d.pop("policyViolationsUnaudited", UNSET)

        policy_violations_warn = d.pop("policyViolationsWarn", UNSET)

        projects = d.pop("projects", UNSET)

        suppressed = d.pop("suppressed", UNSET)

        unassigned = d.pop("unassigned", UNSET)

        vulnerabilities = d.pop("vulnerabilities", UNSET)

        vulnerable_components = d.pop("vulnerableComponents", UNSET)

        vulnerable_projects = d.pop("vulnerableProjects", UNSET)

        portfolio_metrics = cls(
            first_occurrence=first_occurrence,
            last_occurrence=last_occurrence,
            components=components,
            critical=critical,
            findings_audited=findings_audited,
            findings_total=findings_total,
            findings_unaudited=findings_unaudited,
            high=high,
            inherited_risk_score=inherited_risk_score,
            kev=kev,
            low=low,
            medium=medium,
            policy_violations_audited=policy_violations_audited,
            policy_violations_fail=policy_violations_fail,
            policy_violations_info=policy_violations_info,
            policy_violations_license_audited=policy_violations_license_audited,
            policy_violations_license_total=policy_violations_license_total,
            policy_violations_license_unaudited=policy_violations_license_unaudited,
            policy_violations_operational_audited=policy_violations_operational_audited,
            policy_violations_operational_total=policy_violations_operational_total,
            policy_violations_operational_unaudited=policy_violations_operational_unaudited,
            policy_violations_security_audited=policy_violations_security_audited,
            policy_violations_security_total=policy_violations_security_total,
            policy_violations_security_unaudited=policy_violations_security_unaudited,
            policy_violations_total=policy_violations_total,
            policy_violations_unaudited=policy_violations_unaudited,
            policy_violations_warn=policy_violations_warn,
            projects=projects,
            suppressed=suppressed,
            unassigned=unassigned,
            vulnerabilities=vulnerabilities,
            vulnerable_components=vulnerable_components,
            vulnerable_projects=vulnerable_projects,
        )

        portfolio_metrics.additional_properties = d
        return portfolio_metrics

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
