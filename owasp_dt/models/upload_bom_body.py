from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadBomBody")


@_attrs_define
class UploadBomBody:
    """
    Attributes:
        auto_create (bool | Unset):  Default: False.
        bom (str | Unset):
        is_latest (bool | Unset):  Default: False.
        parent_name (str | Unset):
        parent_uuid (str | Unset):
        parent_version (str | Unset):
        project (str | Unset):
        project_name (str | Unset):
        project_tags (str | Unset):
        project_version (str | Unset):
    """

    auto_create: bool | Unset = False
    bom: str | Unset = UNSET
    is_latest: bool | Unset = False
    parent_name: str | Unset = UNSET
    parent_uuid: str | Unset = UNSET
    parent_version: str | Unset = UNSET
    project: str | Unset = UNSET
    project_name: str | Unset = UNSET
    project_tags: str | Unset = UNSET
    project_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_create = self.auto_create

        bom = self.bom

        is_latest = self.is_latest

        parent_name = self.parent_name

        parent_uuid = self.parent_uuid

        parent_version = self.parent_version

        project = self.project

        project_name = self.project_name

        project_tags = self.project_tags

        project_version = self.project_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_create is not UNSET:
            field_dict["autoCreate"] = auto_create
        if bom is not UNSET:
            field_dict["bom"] = bom
        if is_latest is not UNSET:
            field_dict["isLatest"] = is_latest
        if parent_name is not UNSET:
            field_dict["parentName"] = parent_name
        if parent_uuid is not UNSET:
            field_dict["parentUUID"] = parent_uuid
        if parent_version is not UNSET:
            field_dict["parentVersion"] = parent_version
        if project is not UNSET:
            field_dict["project"] = project
        if project_name is not UNSET:
            field_dict["projectName"] = project_name
        if project_tags is not UNSET:
            field_dict["projectTags"] = project_tags
        if project_version is not UNSET:
            field_dict["projectVersion"] = project_version

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.auto_create, Unset):
            files.append(
                ("autoCreate", (None, str(self.auto_create).encode(), "text/plain"))
            )

        if not isinstance(self.bom, Unset):
            files.append(("bom", (None, str(self.bom).encode(), "text/plain")))

        if not isinstance(self.is_latest, Unset):
            files.append(
                ("isLatest", (None, str(self.is_latest).encode(), "text/plain"))
            )

        if not isinstance(self.parent_name, Unset):
            files.append(
                ("parentName", (None, str(self.parent_name).encode(), "text/plain"))
            )

        if not isinstance(self.parent_uuid, Unset):
            files.append(
                ("parentUUID", (None, str(self.parent_uuid).encode(), "text/plain"))
            )

        if not isinstance(self.parent_version, Unset):
            files.append(
                (
                    "parentVersion",
                    (None, str(self.parent_version).encode(), "text/plain"),
                )
            )

        if not isinstance(self.project, Unset):
            files.append(("project", (None, str(self.project).encode(), "text/plain")))

        if not isinstance(self.project_name, Unset):
            files.append(
                ("projectName", (None, str(self.project_name).encode(), "text/plain"))
            )

        if not isinstance(self.project_tags, Unset):
            files.append(
                ("projectTags", (None, str(self.project_tags).encode(), "text/plain"))
            )

        if not isinstance(self.project_version, Unset):
            files.append(
                (
                    "projectVersion",
                    (None, str(self.project_version).encode(), "text/plain"),
                )
            )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_create = d.pop("autoCreate", UNSET)

        bom = d.pop("bom", UNSET)

        is_latest = d.pop("isLatest", UNSET)

        parent_name = d.pop("parentName", UNSET)

        parent_uuid = d.pop("parentUUID", UNSET)

        parent_version = d.pop("parentVersion", UNSET)

        project = d.pop("project", UNSET)

        project_name = d.pop("projectName", UNSET)

        project_tags = d.pop("projectTags", UNSET)

        project_version = d.pop("projectVersion", UNSET)

        upload_bom_body = cls(
            auto_create=auto_create,
            bom=bom,
            is_latest=is_latest,
            parent_name=parent_name,
            parent_uuid=parent_uuid,
            parent_version=parent_version,
            project=project,
            project_name=project_name,
            project_tags=project_tags,
            project_version=project_version,
        )

        upload_bom_body.additional_properties = d
        return upload_bom_body

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
