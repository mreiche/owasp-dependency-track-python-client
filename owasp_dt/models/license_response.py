from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.license_group import LicenseGroup


T = TypeVar("T", bound="LicenseResponse")


@_attrs_define
class LicenseResponse:
    """
    Attributes:
        is_custom_license (bool): Whether the license is a custom license created by a user
        is_deprecated_license_id (bool): Whether the licenseId has been deprecated by SPDX
        is_fsf_libre (bool): Whether the license is FSF libre
        is_osi_approved (bool): Whether the license is approved by the OSI
        license_groups (list[LicenseGroup]): License groups the license belongs to
        license_id (str): Identifier of the license
        name (str): Display name of the license
        uuid (UUID): UUID of the license
        license_comments (str | Unset): Comments about the license
        license_text (str | Unset): Full license text
        see_also (list[str] | Unset): Additional URLs with information about the license
        standard_license_header (str | Unset): Standard license header typically added to the top of source code
        standard_license_template (str | Unset): Standard license template used to derive the license text
    """

    is_custom_license: bool
    is_deprecated_license_id: bool
    is_fsf_libre: bool
    is_osi_approved: bool
    license_groups: list[LicenseGroup]
    license_id: str
    name: str
    uuid: UUID
    license_comments: str | Unset = UNSET
    license_text: str | Unset = UNSET
    see_also: list[str] | Unset = UNSET
    standard_license_header: str | Unset = UNSET
    standard_license_template: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_custom_license = self.is_custom_license

        is_deprecated_license_id = self.is_deprecated_license_id

        is_fsf_libre = self.is_fsf_libre

        is_osi_approved = self.is_osi_approved

        license_groups = []
        for license_groups_item_data in self.license_groups:
            license_groups_item = license_groups_item_data.to_dict()
            license_groups.append(license_groups_item)

        license_id = self.license_id

        name = self.name

        uuid = str(self.uuid)

        license_comments = self.license_comments

        license_text = self.license_text

        see_also: list[str] | Unset = UNSET
        if not isinstance(self.see_also, Unset):
            see_also = self.see_also

        standard_license_header = self.standard_license_header

        standard_license_template = self.standard_license_template

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isCustomLicense": is_custom_license,
                "isDeprecatedLicenseId": is_deprecated_license_id,
                "isFsfLibre": is_fsf_libre,
                "isOsiApproved": is_osi_approved,
                "licenseGroups": license_groups,
                "licenseId": license_id,
                "name": name,
                "uuid": uuid,
            }
        )
        if license_comments is not UNSET:
            field_dict["licenseComments"] = license_comments
        if license_text is not UNSET:
            field_dict["licenseText"] = license_text
        if see_also is not UNSET:
            field_dict["seeAlso"] = see_also
        if standard_license_header is not UNSET:
            field_dict["standardLicenseHeader"] = standard_license_header
        if standard_license_template is not UNSET:
            field_dict["standardLicenseTemplate"] = standard_license_template

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.license_group import LicenseGroup

        d = dict(src_dict)
        is_custom_license = d.pop("isCustomLicense")

        is_deprecated_license_id = d.pop("isDeprecatedLicenseId")

        is_fsf_libre = d.pop("isFsfLibre")

        is_osi_approved = d.pop("isOsiApproved")

        license_groups = []
        _license_groups = d.pop("licenseGroups")
        for license_groups_item_data in _license_groups:
            license_groups_item = LicenseGroup.from_dict(license_groups_item_data)

            license_groups.append(license_groups_item)

        license_id = d.pop("licenseId")

        name = d.pop("name")

        uuid = UUID(d.pop("uuid"))

        license_comments = d.pop("licenseComments", UNSET)

        license_text = d.pop("licenseText", UNSET)

        see_also = cast(list[str], d.pop("seeAlso", UNSET))

        standard_license_header = d.pop("standardLicenseHeader", UNSET)

        standard_license_template = d.pop("standardLicenseTemplate", UNSET)

        license_response = cls(
            is_custom_license=is_custom_license,
            is_deprecated_license_id=is_deprecated_license_id,
            is_fsf_libre=is_fsf_libre,
            is_osi_approved=is_osi_approved,
            license_groups=license_groups,
            license_id=license_id,
            name=name,
            uuid=uuid,
            license_comments=license_comments,
            license_text=license_text,
            see_also=see_also,
            standard_license_header=standard_license_header,
            standard_license_template=standard_license_template,
        )

        license_response.additional_properties = d
        return license_response

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
