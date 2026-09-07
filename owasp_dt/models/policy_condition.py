from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.policy_condition_operator import PolicyConditionOperator
from ..models.policy_condition_subject import PolicyConditionSubject
from ..models.policy_condition_violation_type import PolicyConditionViolationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.policy import Policy


T = TypeVar("T", bound="PolicyCondition")


@_attrs_define
class PolicyCondition:
    """
    Attributes:
        operator (PolicyConditionOperator):
        subject (PolicyConditionSubject):
        uuid (UUID):
        value (str):
        policy (Policy | Unset):
        violation_type (PolicyConditionViolationType | Unset):
    """

    operator: PolicyConditionOperator
    subject: PolicyConditionSubject
    uuid: UUID
    value: str
    policy: Policy | Unset = UNSET
    violation_type: PolicyConditionViolationType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operator = self.operator.value

        subject = self.subject.value

        uuid = str(self.uuid)

        value = self.value

        policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict()

        violation_type: str | Unset = UNSET
        if not isinstance(self.violation_type, Unset):
            violation_type = self.violation_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operator": operator,
                "subject": subject,
                "uuid": uuid,
                "value": value,
            }
        )
        if policy is not UNSET:
            field_dict["policy"] = policy
        if violation_type is not UNSET:
            field_dict["violationType"] = violation_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.policy import Policy

        d = dict(src_dict)
        operator = PolicyConditionOperator(d.pop("operator"))

        subject = PolicyConditionSubject(d.pop("subject"))

        uuid = UUID(d.pop("uuid"))

        value = d.pop("value")

        _policy = d.pop("policy", UNSET)
        policy: Policy | Unset
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = Policy.from_dict(_policy)

        _violation_type = d.pop("violationType", UNSET)
        violation_type: PolicyConditionViolationType | Unset
        if isinstance(_violation_type, Unset):
            violation_type = UNSET
        else:
            violation_type = PolicyConditionViolationType(_violation_type)

        policy_condition = cls(
            operator=operator,
            subject=subject,
            uuid=uuid,
            value=value,
            policy=policy,
            violation_type=violation_type,
        )

        policy_condition.additional_properties = d
        return policy_condition

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
