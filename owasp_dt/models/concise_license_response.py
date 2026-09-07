from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConciseLicenseResponse")


@_attrs_define
class ConciseLicenseResponse:
    """
    Attributes:
        is_custom_license (bool): Whether the license is a custom license created by a user
        is_deprecated_license_id (bool): Whether the licenseId has been deprecated by SPDX
        is_fsf_libre (bool): Whether the license is FSF libre
        is_osi_approved (bool): Whether the license is approved by the OSI
        license_id (str): Identifier of the license
        name (str): Display name of the license
        uuid (UUID): UUID of the license
    """

    is_custom_license: bool
    is_deprecated_license_id: bool
    is_fsf_libre: bool
    is_osi_approved: bool
    license_id: str
    name: str
    uuid: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_custom_license = self.is_custom_license

        is_deprecated_license_id = self.is_deprecated_license_id

        is_fsf_libre = self.is_fsf_libre

        is_osi_approved = self.is_osi_approved

        license_id = self.license_id

        name = self.name

        uuid = str(self.uuid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isCustomLicense": is_custom_license,
                "isDeprecatedLicenseId": is_deprecated_license_id,
                "isFsfLibre": is_fsf_libre,
                "isOsiApproved": is_osi_approved,
                "licenseId": license_id,
                "name": name,
                "uuid": uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        is_custom_license = d.pop("isCustomLicense")

        is_deprecated_license_id = d.pop("isDeprecatedLicenseId")

        is_fsf_libre = d.pop("isFsfLibre")

        is_osi_approved = d.pop("isOsiApproved")

        license_id = d.pop("licenseId")

        name = d.pop("name")

        uuid = UUID(d.pop("uuid"))

        concise_license_response = cls(
            is_custom_license=is_custom_license,
            is_deprecated_license_id=is_deprecated_license_id,
            is_fsf_libre=is_fsf_libre,
            is_osi_approved=is_osi_approved,
            license_id=license_id,
            name=name,
            uuid=uuid,
        )

        concise_license_response.additional_properties = d
        return concise_license_response

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
