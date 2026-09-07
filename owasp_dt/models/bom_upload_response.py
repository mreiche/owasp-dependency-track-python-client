from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BomUploadResponse")


@_attrs_define
class BomUploadResponse:
    """
    Attributes:
        token (UUID): Token used to check task progress
        project_uuid (UUID | Unset): UUID of the project the BOM was uploaded for
    """

    token: UUID
    project_uuid: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = str(self.token)

        project_uuid: str | Unset = UNSET
        if not isinstance(self.project_uuid, Unset):
            project_uuid = str(self.project_uuid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
            }
        )
        if project_uuid is not UNSET:
            field_dict["projectUuid"] = project_uuid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        token = UUID(d.pop("token"))

        _project_uuid = d.pop("projectUuid", UNSET)
        project_uuid: UUID | Unset
        if isinstance(_project_uuid, Unset):
            project_uuid = UNSET
        else:
            project_uuid = UUID(_project_uuid)

        bom_upload_response = cls(
            token=token,
            project_uuid=project_uuid,
        )

        bom_upload_response.additional_properties = d
        return bom_upload_response

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
