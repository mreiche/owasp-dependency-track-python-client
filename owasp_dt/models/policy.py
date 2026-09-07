from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.policy_operator import PolicyOperator
from ..models.policy_violation_state import PolicyViolationState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.policy_condition import PolicyCondition
    from ..models.project import Project
    from ..models.tag import Tag


T = TypeVar("T", bound="Policy")


@_attrs_define
class Policy:
    """
    Attributes:
        name (str):
        operator (PolicyOperator):
        uuid (UUID):
        violation_state (PolicyViolationState):
        global_ (bool | Unset):
        include_children (bool | Unset):
        only_latest_project_version (bool | Unset):
        policy_conditions (list[PolicyCondition] | Unset):
        projects (list[Project] | Unset):
        tags (list[Tag] | Unset):
    """

    name: str
    operator: PolicyOperator
    uuid: UUID
    violation_state: PolicyViolationState
    global_: bool | Unset = UNSET
    include_children: bool | Unset = UNSET
    only_latest_project_version: bool | Unset = UNSET
    policy_conditions: list[PolicyCondition] | Unset = UNSET
    projects: list[Project] | Unset = UNSET
    tags: list[Tag] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        operator = self.operator.value

        uuid = str(self.uuid)

        violation_state = self.violation_state.value

        global_ = self.global_

        include_children = self.include_children

        only_latest_project_version = self.only_latest_project_version

        policy_conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.policy_conditions, Unset):
            policy_conditions = []
            for policy_conditions_item_data in self.policy_conditions:
                policy_conditions_item = policy_conditions_item_data.to_dict()
                policy_conditions.append(policy_conditions_item)

        projects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.projects, Unset):
            projects = []
            for projects_item_data in self.projects:
                projects_item = projects_item_data.to_dict()
                projects.append(projects_item)

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "operator": operator,
                "uuid": uuid,
                "violationState": violation_state,
            }
        )
        if global_ is not UNSET:
            field_dict["global"] = global_
        if include_children is not UNSET:
            field_dict["includeChildren"] = include_children
        if only_latest_project_version is not UNSET:
            field_dict["onlyLatestProjectVersion"] = only_latest_project_version
        if policy_conditions is not UNSET:
            field_dict["policyConditions"] = policy_conditions
        if projects is not UNSET:
            field_dict["projects"] = projects
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.policy_condition import PolicyCondition
        from ..models.project import Project
        from ..models.tag import Tag

        d = dict(src_dict)
        name = d.pop("name")

        operator = PolicyOperator(d.pop("operator"))

        uuid = UUID(d.pop("uuid"))

        violation_state = PolicyViolationState(d.pop("violationState"))

        global_ = d.pop("global", UNSET)

        include_children = d.pop("includeChildren", UNSET)

        only_latest_project_version = d.pop("onlyLatestProjectVersion", UNSET)

        _policy_conditions = d.pop("policyConditions", UNSET)
        policy_conditions: list[PolicyCondition] | Unset = UNSET
        if _policy_conditions is not UNSET:
            policy_conditions = []
            for policy_conditions_item_data in _policy_conditions:
                policy_conditions_item = PolicyCondition.from_dict(
                    policy_conditions_item_data
                )

                policy_conditions.append(policy_conditions_item)

        _projects = d.pop("projects", UNSET)
        projects: list[Project] | Unset = UNSET
        if _projects is not UNSET:
            projects = []
            for projects_item_data in _projects:
                projects_item = Project.from_dict(projects_item_data)

                projects.append(projects_item)

        _tags = d.pop("tags", UNSET)
        tags: list[Tag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = Tag.from_dict(tags_item_data)

                tags.append(tags_item)

        policy = cls(
            name=name,
            operator=operator,
            uuid=uuid,
            violation_state=violation_state,
            global_=global_,
            include_children=include_children,
            only_latest_project_version=only_latest_project_version,
            policy_conditions=policy_conditions,
            projects=projects,
            tags=tags,
        )

        policy.additional_properties = d
        return policy

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
