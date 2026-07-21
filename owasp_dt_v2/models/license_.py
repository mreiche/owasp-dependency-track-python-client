from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="License")


@_attrs_define
class License:
    """
    Attributes:
        name (str | Unset):
        license_id (str | Unset):
        uuid (UUID | Unset):
        osi_approved (bool | Unset):
        fsf_libre (bool | Unset):
        custom_license (bool | Unset):
    """

    name: str | Unset = UNSET
    license_id: str | Unset = UNSET
    uuid: UUID | Unset = UNSET
    osi_approved: bool | Unset = UNSET
    fsf_libre: bool | Unset = UNSET
    custom_license: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        license_id = self.license_id

        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        osi_approved = self.osi_approved

        fsf_libre = self.fsf_libre

        custom_license = self.custom_license

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if license_id is not UNSET:
            field_dict["license_id"] = license_id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if osi_approved is not UNSET:
            field_dict["osi_approved"] = osi_approved
        if fsf_libre is not UNSET:
            field_dict["fsf_libre"] = fsf_libre
        if custom_license is not UNSET:
            field_dict["custom_license"] = custom_license

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        license_id = d.pop("license_id", UNSET)

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        osi_approved = d.pop("osi_approved", UNSET)

        fsf_libre = d.pop("fsf_libre", UNSET)

        custom_license = d.pop("custom_license", UNSET)

        license_ = cls(
            name=name,
            license_id=license_id,
            uuid=uuid,
            osi_approved=osi_approved,
            fsf_libre=fsf_libre,
            custom_license=custom_license,
        )

        license_.additional_properties = d
        return license_

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
