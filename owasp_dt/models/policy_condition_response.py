from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.policy_condition_response_operator import PolicyConditionResponseOperator
from ..models.policy_condition_response_subject import PolicyConditionResponseSubject
from ..models.policy_condition_response_violation_type import (
    PolicyConditionResponseViolationType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PolicyConditionResponse")


@_attrs_define
class PolicyConditionResponse:
    """
    Attributes:
        operator (PolicyConditionResponseOperator): Operator used to compare the subject to the value
        subject (PolicyConditionResponseSubject): Subject the condition evaluates
        uuid (UUID): UUID of the policy condition
        value (str): Value the subject is compared to
        violation_type (PolicyConditionResponseViolationType | Unset): Violation type produced when the condition
            matches
    """

    operator: PolicyConditionResponseOperator
    subject: PolicyConditionResponseSubject
    uuid: UUID
    value: str
    violation_type: PolicyConditionResponseViolationType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operator = self.operator.value

        subject = self.subject.value

        uuid = str(self.uuid)

        value = self.value

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
        if violation_type is not UNSET:
            field_dict["violationType"] = violation_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        operator = PolicyConditionResponseOperator(d.pop("operator"))

        subject = PolicyConditionResponseSubject(d.pop("subject"))

        uuid = UUID(d.pop("uuid"))

        value = d.pop("value")

        _violation_type = d.pop("violationType", UNSET)
        violation_type: PolicyConditionResponseViolationType | Unset
        if isinstance(_violation_type, Unset):
            violation_type = UNSET
        else:
            violation_type = PolicyConditionResponseViolationType(_violation_type)

        policy_condition_response = cls(
            operator=operator,
            subject=subject,
            uuid=uuid,
            value=value,
            violation_type=violation_type,
        )

        policy_condition_response.additional_properties = d
        return policy_condition_response

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
