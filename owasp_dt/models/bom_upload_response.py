from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BomUploadResponse")


@_attrs_define
class BomUploadResponse:
    """
    Attributes:
        project_uuid (UUID): UUID of the project the BOM was uploaded for
        token (UUID): Token used to check task progress
    """

    project_uuid: UUID
    token: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_uuid = str(self.project_uuid)

        token = str(self.token)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectUuid": project_uuid,
                "token": token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        project_uuid = UUID(d.pop("projectUuid"))

        token = UUID(d.pop("token"))

        bom_upload_response = cls(
            project_uuid=project_uuid,
            token=token,
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
