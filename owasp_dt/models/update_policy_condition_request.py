from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_policy_condition_request_operator import (
    UpdatePolicyConditionRequestOperator,
)
from ..models.update_policy_condition_request_subject import (
    UpdatePolicyConditionRequestSubject,
)
from ..models.update_policy_condition_request_violation_type import (
    UpdatePolicyConditionRequestViolationType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatePolicyConditionRequest")


@_attrs_define
class UpdatePolicyConditionRequest:
    """
    Attributes:
        operator (UpdatePolicyConditionRequestOperator): Operator used to compare the subject to the value
        subject (UpdatePolicyConditionRequestSubject): Subject the condition evaluates
        uuid (UUID): UUID of the policy condition to update
        value (str): Value the subject is compared to
        violation_type (UpdatePolicyConditionRequestViolationType | Unset): Violation type produced when the condition
            matches. Required for `EXPRESSION` subjects
    """

    operator: UpdatePolicyConditionRequestOperator
    subject: UpdatePolicyConditionRequestSubject
    uuid: UUID
    value: str
    violation_type: UpdatePolicyConditionRequestViolationType | Unset = UNSET
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
        operator = UpdatePolicyConditionRequestOperator(d.pop("operator"))

        subject = UpdatePolicyConditionRequestSubject(d.pop("subject"))

        uuid = UUID(d.pop("uuid"))

        value = d.pop("value")

        _violation_type = d.pop("violationType", UNSET)
        violation_type: UpdatePolicyConditionRequestViolationType | Unset
        if isinstance(_violation_type, Unset):
            violation_type = UNSET
        else:
            violation_type = UpdatePolicyConditionRequestViolationType(_violation_type)

        update_policy_condition_request = cls(
            operator=operator,
            subject=subject,
            uuid=uuid,
            value=value,
            violation_type=violation_type,
        )

        update_policy_condition_request.additional_properties = d
        return update_policy_condition_request

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
