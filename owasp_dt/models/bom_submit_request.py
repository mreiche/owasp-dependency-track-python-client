from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tag import Tag


T = TypeVar("T", bound="BomSubmitRequest")


@_attrs_define
class BomSubmitRequest:
    """
    Attributes:
        bom (str): Base64 encoded BOM Example: ewogICJib21Gb3JtYXQiOiAiQ3ljbG9uZURYIiwKICAic3BlY1ZlcnNpb24iOiAiMS40IiwKI
            CAiY29tcG9uZW50cyI6IFsKICAgIHsKICAgICAgInR5cGUiOiAibGlicmFyeSIsCiAgICAgICJuYW1lIjogImFjbWUtbGliIiwKICAgICAgInZlc
            nNpb24iOiAiMS4wLjAiCiAgICB9CiAgXQp9.
        project (str):  Example: 38640b33-4ba9-4733-bdab-cbfc40c6f8aa.
        project_name (str):  Example: Example Application.
        project_version (str):  Example: 1.0.0.
        auto_create (bool | Unset):
        is_active (bool | Unset):
        is_latest (bool | Unset):
        parent_name (str | Unset):  Example: Example Application Parent.
        parent_uuid (str | Unset):  Example: 5341f53c-611b-4388-9d9c-731026dc5eec.
        parent_version (str | Unset):  Example: 1.0.0.
        project_tags (list[Tag] | Unset):  Example: tag1, tag2.
    """

    bom: str
    project: str
    project_name: str
    project_version: str
    auto_create: bool | Unset = UNSET
    is_active: bool | Unset = UNSET
    is_latest: bool | Unset = UNSET
    parent_name: str | Unset = UNSET
    parent_uuid: str | Unset = UNSET
    parent_version: str | Unset = UNSET
    project_tags: list[Tag] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bom = self.bom

        project = self.project

        project_name = self.project_name

        project_version = self.project_version

        auto_create = self.auto_create

        is_active = self.is_active

        is_latest = self.is_latest

        parent_name = self.parent_name

        parent_uuid = self.parent_uuid

        parent_version = self.parent_version

        project_tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.project_tags, Unset):
            project_tags = []
            for project_tags_item_data in self.project_tags:
                project_tags_item = project_tags_item_data.to_dict()
                project_tags.append(project_tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bom": bom,
                "project": project,
                "projectName": project_name,
                "projectVersion": project_version,
            }
        )
        if auto_create is not UNSET:
            field_dict["autoCreate"] = auto_create
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if is_latest is not UNSET:
            field_dict["isLatest"] = is_latest
        if parent_name is not UNSET:
            field_dict["parentName"] = parent_name
        if parent_uuid is not UNSET:
            field_dict["parentUUID"] = parent_uuid
        if parent_version is not UNSET:
            field_dict["parentVersion"] = parent_version
        if project_tags is not UNSET:
            field_dict["projectTags"] = project_tags

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.tag import Tag

        d = dict(src_dict)
        bom = d.pop("bom")

        project = d.pop("project")

        project_name = d.pop("projectName")

        project_version = d.pop("projectVersion")

        auto_create = d.pop("autoCreate", UNSET)

        is_active = d.pop("isActive", UNSET)

        is_latest = d.pop("isLatest", UNSET)

        parent_name = d.pop("parentName", UNSET)

        parent_uuid = d.pop("parentUUID", UNSET)

        parent_version = d.pop("parentVersion", UNSET)

        _project_tags = d.pop("projectTags", UNSET)
        project_tags: list[Tag] | Unset = UNSET
        if _project_tags is not UNSET:
            project_tags = []
            for project_tags_item_data in _project_tags:
                project_tags_item = Tag.from_dict(project_tags_item_data)

                project_tags.append(project_tags_item)

        bom_submit_request = cls(
            bom=bom,
            project=project,
            project_name=project_name,
            project_version=project_version,
            auto_create=auto_create,
            is_active=is_active,
            is_latest=is_latest,
            parent_name=parent_name,
            parent_uuid=parent_uuid,
            parent_version=parent_version,
            project_tags=project_tags,
        )

        bom_submit_request.additional_properties = d
        return bom_submit_request

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
