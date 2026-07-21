from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConciseProjectMetrics")


@_attrs_define
class ConciseProjectMetrics:
    """A concise representation of a project's metrics

    Attributes:
        components (int): Total number of components
        critical (int): Number of vulnerabilities with critical severity
        high (int): Number of vulnerabilities with high severity
        inherited_risk_score (float): The inherited risk score
        low (int): Number of vulnerabilities with low severity
        medium (int): Number of vulnerabilities with medium severity
        policy_violations_fail (int): Number of policy violations with status FAIL
        policy_violations_info (int): Number of policy violations with status WARN
        policy_violations_license_total (int): Number of license policy violations
        policy_violations_operational_total (int): Number of operational policy violations
        policy_violations_security_total (int): Number of security policy violations
        policy_violations_total (int): Total number of policy violations
        policy_violations_warn (int): Number of policy violations with status WARN
        unassigned (int): Number of vulnerabilities with unassigned severity
        vulnerabilities (int): Total number of vulnerabilities
    """

    components: int
    critical: int
    high: int
    inherited_risk_score: float
    low: int
    medium: int
    policy_violations_fail: int
    policy_violations_info: int
    policy_violations_license_total: int
    policy_violations_operational_total: int
    policy_violations_security_total: int
    policy_violations_total: int
    policy_violations_warn: int
    unassigned: int
    vulnerabilities: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        components = self.components

        critical = self.critical

        high = self.high

        inherited_risk_score = self.inherited_risk_score

        low = self.low

        medium = self.medium

        policy_violations_fail = self.policy_violations_fail

        policy_violations_info = self.policy_violations_info

        policy_violations_license_total = self.policy_violations_license_total

        policy_violations_operational_total = self.policy_violations_operational_total

        policy_violations_security_total = self.policy_violations_security_total

        policy_violations_total = self.policy_violations_total

        policy_violations_warn = self.policy_violations_warn

        unassigned = self.unassigned

        vulnerabilities = self.vulnerabilities

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "components": components,
                "critical": critical,
                "high": high,
                "inheritedRiskScore": inherited_risk_score,
                "low": low,
                "medium": medium,
                "policyViolationsFail": policy_violations_fail,
                "policyViolationsInfo": policy_violations_info,
                "policyViolationsLicenseTotal": policy_violations_license_total,
                "policyViolationsOperationalTotal": policy_violations_operational_total,
                "policyViolationsSecurityTotal": policy_violations_security_total,
                "policyViolationsTotal": policy_violations_total,
                "policyViolationsWarn": policy_violations_warn,
                "unassigned": unassigned,
                "vulnerabilities": vulnerabilities,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        components = d.pop("components")

        critical = d.pop("critical")

        high = d.pop("high")

        inherited_risk_score = d.pop("inheritedRiskScore")

        low = d.pop("low")

        medium = d.pop("medium")

        policy_violations_fail = d.pop("policyViolationsFail")

        policy_violations_info = d.pop("policyViolationsInfo")

        policy_violations_license_total = d.pop("policyViolationsLicenseTotal")

        policy_violations_operational_total = d.pop("policyViolationsOperationalTotal")

        policy_violations_security_total = d.pop("policyViolationsSecurityTotal")

        policy_violations_total = d.pop("policyViolationsTotal")

        policy_violations_warn = d.pop("policyViolationsWarn")

        unassigned = d.pop("unassigned")

        vulnerabilities = d.pop("vulnerabilities")

        concise_project_metrics = cls(
            components=components,
            critical=critical,
            high=high,
            inherited_risk_score=inherited_risk_score,
            low=low,
            medium=medium,
            policy_violations_fail=policy_violations_fail,
            policy_violations_info=policy_violations_info,
            policy_violations_license_total=policy_violations_license_total,
            policy_violations_operational_total=policy_violations_operational_total,
            policy_violations_security_total=policy_violations_security_total,
            policy_violations_total=policy_violations_total,
            policy_violations_warn=policy_violations_warn,
            unassigned=unassigned,
            vulnerabilities=vulnerabilities,
        )

        concise_project_metrics.additional_properties = d
        return concise_project_metrics

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
