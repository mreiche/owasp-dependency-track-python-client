from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.clone_project_include import CloneProjectInclude
from ..types import UNSET, Unset

T = TypeVar("T", bound="CloneProjectRequest")


@_attrs_define
class CloneProjectRequest:
    """
    Attributes:
        version (str): Version of the cloned project.
        version_is_latest (bool | Unset): Whether to mark the cloned project version as latest. If another version is
            already marked as latest, it will be atomically un-unmarked as part of the cloning operation. Default: False.
        includes (list[CloneProjectInclude] | Unset): List of items to include in the clone:

              * `ACL`: Include portfolio ACL definitions.
              * `COMPONENTS`: Include components.
              * `FINDINGS`: Include findings.
                  * Has no effect unless `COMPONENTS` is also included.
              * `FINDINGS_AUDIT_HISTORY`: Include audit history of findings.
                  * Has no effect unless `FINDINGS` is also included.
              * `POLICY_VIOLATIONS`: Include policy violations.
                  * Has no effect unless `COMPONENTS` is also included.
              * `POLICY_VIOLATIONS_AUDIT_HISTORY`: Include audit history of policy violations.
                  * Has no effect unless `POLICY_VIOLATIONS` is also included.
              * `PROPERTIES`: Include project properties.
              * `SERVICES`: Include services.
              * `TAGS`: Include project tags.
    """

    version: str
    version_is_latest: bool | Unset = False
    includes: list[CloneProjectInclude] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        version_is_latest = self.version_is_latest

        includes: list[str] | Unset = UNSET
        if not isinstance(self.includes, Unset):
            includes = []
            for includes_item_data in self.includes:
                includes_item = includes_item_data.value
                includes.append(includes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
            }
        )
        if version_is_latest is not UNSET:
            field_dict["version_is_latest"] = version_is_latest
        if includes is not UNSET:
            field_dict["includes"] = includes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        version = d.pop("version")

        version_is_latest = d.pop("version_is_latest", UNSET)

        _includes = d.pop("includes", UNSET)
        includes: list[CloneProjectInclude] | Unset = UNSET
        if _includes is not UNSET:
            includes = []
            for includes_item_data in _includes:
                includes_item = CloneProjectInclude(includes_item_data)

                includes.append(includes_item)

        clone_project_request = cls(
            version=version,
            version_is_latest=version_is_latest,
            includes=includes,
        )

        clone_project_request.additional_properties = d
        return clone_project_request

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
