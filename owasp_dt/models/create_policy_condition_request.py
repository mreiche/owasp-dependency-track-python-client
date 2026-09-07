from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_policy_condition_request_operator import (
    CreatePolicyConditionRequestOperator,
)
from ..models.create_policy_condition_request_subject import (
    CreatePolicyConditionRequestSubject,
)
from ..models.create_policy_condition_request_violation_type import (
    CreatePolicyConditionRequestViolationType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePolicyConditionRequest")


@_attrs_define
class CreatePolicyConditionRequest:
    """
    Attributes:
        operator (CreatePolicyConditionRequestOperator): Operator used to compare the subject to the value
        subject (CreatePolicyConditionRequestSubject): Subject the condition evaluates
        value (str): Value the subject is compared to
        violation_type (CreatePolicyConditionRequestViolationType | Unset): Violation type produced when the condition
            matches. Required for `EXPRESSION` subjects
    """

    operator: CreatePolicyConditionRequestOperator
    subject: CreatePolicyConditionRequestSubject
    value: str
    violation_type: CreatePolicyConditionRequestViolationType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operator = self.operator.value

        subject = self.subject.value

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
                "value": value,
            }
        )
        if violation_type is not UNSET:
            field_dict["violationType"] = violation_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        operator = CreatePolicyConditionRequestOperator(d.pop("operator"))

        subject = CreatePolicyConditionRequestSubject(d.pop("subject"))

        value = d.pop("value")

        _violation_type = d.pop("violationType", UNSET)
        violation_type: CreatePolicyConditionRequestViolationType | Unset
        if isinstance(_violation_type, Unset):
            violation_type = UNSET
        else:
            violation_type = CreatePolicyConditionRequestViolationType(_violation_type)

        create_policy_condition_request = cls(
            operator=operator,
            subject=subject,
            value=value,
            violation_type=violation_type,
        )

        create_policy_condition_request.additional_properties = d
        return create_policy_condition_request

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
