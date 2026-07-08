from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DependencyMetrics")


@_attrs_define
class DependencyMetrics:
    """
    Attributes:
        critical (int | Unset):
        high (int | Unset):
        medium (int | Unset):
        low (int | Unset):
        unassigned (int | Unset):
        vulnerabilities (int | Unset):
        suppressed (int | Unset):
        inherited_risk_score (float | Unset):
        findings_total (int | Unset):
        findings_audited (int | Unset):
        findings_unaudited (int | Unset):
        policy_violations_fail (int | Unset):
        policy_violations_warn (int | Unset):
        policy_violations_info (int | Unset):
        policy_violations_total (int | Unset):
        policy_violations_audited (int | Unset):
        policy_violations_unaudited (int | Unset):
        policy_violations_security_total (int | Unset):
        policy_violations_security_audited (int | Unset):
        policy_violations_security_unaudited (int | Unset):
        policy_violations_license_total (int | Unset):
        policy_violations_license_audited (int | Unset):
        policy_violations_license_unaudited (int | Unset):
        policy_violations_operational_total (int | Unset):
        policy_violations_operational_audited (int | Unset):
        policy_violations_operational_unaudited (int | Unset):
    """

    critical: int | Unset = UNSET
    high: int | Unset = UNSET
    medium: int | Unset = UNSET
    low: int | Unset = UNSET
    unassigned: int | Unset = UNSET
    vulnerabilities: int | Unset = UNSET
    suppressed: int | Unset = UNSET
    inherited_risk_score: float | Unset = UNSET
    findings_total: int | Unset = UNSET
    findings_audited: int | Unset = UNSET
    findings_unaudited: int | Unset = UNSET
    policy_violations_fail: int | Unset = UNSET
    policy_violations_warn: int | Unset = UNSET
    policy_violations_info: int | Unset = UNSET
    policy_violations_total: int | Unset = UNSET
    policy_violations_audited: int | Unset = UNSET
    policy_violations_unaudited: int | Unset = UNSET
    policy_violations_security_total: int | Unset = UNSET
    policy_violations_security_audited: int | Unset = UNSET
    policy_violations_security_unaudited: int | Unset = UNSET
    policy_violations_license_total: int | Unset = UNSET
    policy_violations_license_audited: int | Unset = UNSET
    policy_violations_license_unaudited: int | Unset = UNSET
    policy_violations_operational_total: int | Unset = UNSET
    policy_violations_operational_audited: int | Unset = UNSET
    policy_violations_operational_unaudited: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        critical = self.critical

        high = self.high

        medium = self.medium

        low = self.low

        unassigned = self.unassigned

        vulnerabilities = self.vulnerabilities

        suppressed = self.suppressed

        inherited_risk_score = self.inherited_risk_score

        findings_total = self.findings_total

        findings_audited = self.findings_audited

        findings_unaudited = self.findings_unaudited

        policy_violations_fail = self.policy_violations_fail

        policy_violations_warn = self.policy_violations_warn

        policy_violations_info = self.policy_violations_info

        policy_violations_total = self.policy_violations_total

        policy_violations_audited = self.policy_violations_audited

        policy_violations_unaudited = self.policy_violations_unaudited

        policy_violations_security_total = self.policy_violations_security_total

        policy_violations_security_audited = self.policy_violations_security_audited

        policy_violations_security_unaudited = self.policy_violations_security_unaudited

        policy_violations_license_total = self.policy_violations_license_total

        policy_violations_license_audited = self.policy_violations_license_audited

        policy_violations_license_unaudited = self.policy_violations_license_unaudited

        policy_violations_operational_total = self.policy_violations_operational_total

        policy_violations_operational_audited = (
            self.policy_violations_operational_audited
        )

        policy_violations_operational_unaudited = (
            self.policy_violations_operational_unaudited
        )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if critical is not UNSET:
            field_dict["critical"] = critical
        if high is not UNSET:
            field_dict["high"] = high
        if medium is not UNSET:
            field_dict["medium"] = medium
        if low is not UNSET:
            field_dict["low"] = low
        if unassigned is not UNSET:
            field_dict["unassigned"] = unassigned
        if vulnerabilities is not UNSET:
            field_dict["vulnerabilities"] = vulnerabilities
        if suppressed is not UNSET:
            field_dict["suppressed"] = suppressed
        if inherited_risk_score is not UNSET:
            field_dict["inherited_risk_score"] = inherited_risk_score
        if findings_total is not UNSET:
            field_dict["findings_total"] = findings_total
        if findings_audited is not UNSET:
            field_dict["findings_audited"] = findings_audited
        if findings_unaudited is not UNSET:
            field_dict["findings_unaudited"] = findings_unaudited
        if policy_violations_fail is not UNSET:
            field_dict["policy_violations_fail"] = policy_violations_fail
        if policy_violations_warn is not UNSET:
            field_dict["policy_violations_warn"] = policy_violations_warn
        if policy_violations_info is not UNSET:
            field_dict["policy_violations_info"] = policy_violations_info
        if policy_violations_total is not UNSET:
            field_dict["policy_violations_total"] = policy_violations_total
        if policy_violations_audited is not UNSET:
            field_dict["policy_violations_audited"] = policy_violations_audited
        if policy_violations_unaudited is not UNSET:
            field_dict["policy_violations_unaudited"] = policy_violations_unaudited
        if policy_violations_security_total is not UNSET:
            field_dict["policy_violations_security_total"] = (
                policy_violations_security_total
            )
        if policy_violations_security_audited is not UNSET:
            field_dict["policy_violations_security_audited"] = (
                policy_violations_security_audited
            )
        if policy_violations_security_unaudited is not UNSET:
            field_dict["policy_violations_security_unaudited"] = (
                policy_violations_security_unaudited
            )
        if policy_violations_license_total is not UNSET:
            field_dict["policy_violations_license_total"] = (
                policy_violations_license_total
            )
        if policy_violations_license_audited is not UNSET:
            field_dict["policy_violations_license_audited"] = (
                policy_violations_license_audited
            )
        if policy_violations_license_unaudited is not UNSET:
            field_dict["policy_violations_license_unaudited"] = (
                policy_violations_license_unaudited
            )
        if policy_violations_operational_total is not UNSET:
            field_dict["policy_violations_operational_total"] = (
                policy_violations_operational_total
            )
        if policy_violations_operational_audited is not UNSET:
            field_dict["policy_violations_operational_audited"] = (
                policy_violations_operational_audited
            )
        if policy_violations_operational_unaudited is not UNSET:
            field_dict["policy_violations_operational_unaudited"] = (
                policy_violations_operational_unaudited
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        critical = d.pop("critical", UNSET)

        high = d.pop("high", UNSET)

        medium = d.pop("medium", UNSET)

        low = d.pop("low", UNSET)

        unassigned = d.pop("unassigned", UNSET)

        vulnerabilities = d.pop("vulnerabilities", UNSET)

        suppressed = d.pop("suppressed", UNSET)

        inherited_risk_score = d.pop("inherited_risk_score", UNSET)

        findings_total = d.pop("findings_total", UNSET)

        findings_audited = d.pop("findings_audited", UNSET)

        findings_unaudited = d.pop("findings_unaudited", UNSET)

        policy_violations_fail = d.pop("policy_violations_fail", UNSET)

        policy_violations_warn = d.pop("policy_violations_warn", UNSET)

        policy_violations_info = d.pop("policy_violations_info", UNSET)

        policy_violations_total = d.pop("policy_violations_total", UNSET)

        policy_violations_audited = d.pop("policy_violations_audited", UNSET)

        policy_violations_unaudited = d.pop("policy_violations_unaudited", UNSET)

        policy_violations_security_total = d.pop(
            "policy_violations_security_total", UNSET
        )

        policy_violations_security_audited = d.pop(
            "policy_violations_security_audited", UNSET
        )

        policy_violations_security_unaudited = d.pop(
            "policy_violations_security_unaudited", UNSET
        )

        policy_violations_license_total = d.pop(
            "policy_violations_license_total", UNSET
        )

        policy_violations_license_audited = d.pop(
            "policy_violations_license_audited", UNSET
        )

        policy_violations_license_unaudited = d.pop(
            "policy_violations_license_unaudited", UNSET
        )

        policy_violations_operational_total = d.pop(
            "policy_violations_operational_total", UNSET
        )

        policy_violations_operational_audited = d.pop(
            "policy_violations_operational_audited", UNSET
        )

        policy_violations_operational_unaudited = d.pop(
            "policy_violations_operational_unaudited", UNSET
        )

        dependency_metrics = cls(
            critical=critical,
            high=high,
            medium=medium,
            low=low,
            unassigned=unassigned,
            vulnerabilities=vulnerabilities,
            suppressed=suppressed,
            inherited_risk_score=inherited_risk_score,
            findings_total=findings_total,
            findings_audited=findings_audited,
            findings_unaudited=findings_unaudited,
            policy_violations_fail=policy_violations_fail,
            policy_violations_warn=policy_violations_warn,
            policy_violations_info=policy_violations_info,
            policy_violations_total=policy_violations_total,
            policy_violations_audited=policy_violations_audited,
            policy_violations_unaudited=policy_violations_unaudited,
            policy_violations_security_total=policy_violations_security_total,
            policy_violations_security_audited=policy_violations_security_audited,
            policy_violations_security_unaudited=policy_violations_security_unaudited,
            policy_violations_license_total=policy_violations_license_total,
            policy_violations_license_audited=policy_violations_license_audited,
            policy_violations_license_unaudited=policy_violations_license_unaudited,
            policy_violations_operational_total=policy_violations_operational_total,
            policy_violations_operational_audited=policy_violations_operational_audited,
            policy_violations_operational_unaudited=policy_violations_operational_unaudited,
        )

        dependency_metrics.additional_properties = d
        return dependency_metrics

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
