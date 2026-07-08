from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.policy_violation_type import PolicyViolationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.component import Component
    from ..models.policy_condition import PolicyCondition
    from ..models.project import Project
    from ..models.violation_analysis import ViolationAnalysis


T = TypeVar("T", bound="PolicyViolation")


@_attrs_define
class PolicyViolation:
    """
    Attributes:
        timestamp (int): UNIX epoch timestamp in milliseconds
        uuid (UUID):
        analysis (ViolationAnalysis | Unset):
        component (Component | Unset):
        policy_condition (PolicyCondition | Unset):
        project (Project | Unset):
        text (str | Unset):
        type_ (PolicyViolationType | Unset):
    """

    timestamp: int
    uuid: UUID
    analysis: ViolationAnalysis | Unset = UNSET
    component: Component | Unset = UNSET
    policy_condition: PolicyCondition | Unset = UNSET
    project: Project | Unset = UNSET
    text: str | Unset = UNSET
    type_: PolicyViolationType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        uuid = str(self.uuid)

        analysis: dict[str, Any] | Unset = UNSET
        if not isinstance(self.analysis, Unset):
            analysis = self.analysis.to_dict()

        component: dict[str, Any] | Unset = UNSET
        if not isinstance(self.component, Unset):
            component = self.component.to_dict()

        policy_condition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.policy_condition, Unset):
            policy_condition = self.policy_condition.to_dict()

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        text = self.text

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "uuid": uuid,
            }
        )
        if analysis is not UNSET:
            field_dict["analysis"] = analysis
        if component is not UNSET:
            field_dict["component"] = component
        if policy_condition is not UNSET:
            field_dict["policyCondition"] = policy_condition
        if project is not UNSET:
            field_dict["project"] = project
        if text is not UNSET:
            field_dict["text"] = text
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.component import Component
        from ..models.policy_condition import PolicyCondition
        from ..models.project import Project
        from ..models.violation_analysis import ViolationAnalysis

        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        uuid = UUID(d.pop("uuid"))

        _analysis = d.pop("analysis", UNSET)
        analysis: ViolationAnalysis | Unset
        if isinstance(_analysis, Unset):
            analysis = UNSET
        else:
            analysis = ViolationAnalysis.from_dict(_analysis)

        _component = d.pop("component", UNSET)
        component: Component | Unset
        if isinstance(_component, Unset):
            component = UNSET
        else:
            component = Component.from_dict(_component)

        _policy_condition = d.pop("policyCondition", UNSET)
        policy_condition: PolicyCondition | Unset
        if isinstance(_policy_condition, Unset):
            policy_condition = UNSET
        else:
            policy_condition = PolicyCondition.from_dict(_policy_condition)

        _project = d.pop("project", UNSET)
        project: Project | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = Project.from_dict(_project)

        text = d.pop("text", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: PolicyViolationType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PolicyViolationType(_type_)

        policy_violation = cls(
            timestamp=timestamp,
            uuid=uuid,
            analysis=analysis,
            component=component,
            policy_condition=policy_condition,
            project=project,
            text=text,
            type_=type_,
        )

        policy_violation.additional_properties = d
        return policy_violation

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
