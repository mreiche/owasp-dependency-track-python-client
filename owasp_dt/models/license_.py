from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.license_group import LicenseGroup


T = TypeVar("T", bound="License")


@_attrs_define
class License:
    """
    Attributes:
        license_id (str):
        name (str):
        uuid (UUID):
        is_custom_license (bool | Unset):
        is_deprecated_license_id (bool | Unset):
        is_fsf_libre (bool | Unset):
        is_osi_approved (bool | Unset):
        license_comments (str | Unset):
        license_groups (list[LicenseGroup] | Unset):
        license_text (str | Unset):
        see_also (list[str] | Unset):
        standard_license_header (str | Unset):
        standard_license_template (str | Unset):
    """

    license_id: str
    name: str
    uuid: UUID
    is_custom_license: bool | Unset = UNSET
    is_deprecated_license_id: bool | Unset = UNSET
    is_fsf_libre: bool | Unset = UNSET
    is_osi_approved: bool | Unset = UNSET
    license_comments: str | Unset = UNSET
    license_groups: list[LicenseGroup] | Unset = UNSET
    license_text: str | Unset = UNSET
    see_also: list[str] | Unset = UNSET
    standard_license_header: str | Unset = UNSET
    standard_license_template: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        license_id = self.license_id

        name = self.name

        uuid = str(self.uuid)

        is_custom_license = self.is_custom_license

        is_deprecated_license_id = self.is_deprecated_license_id

        is_fsf_libre = self.is_fsf_libre

        is_osi_approved = self.is_osi_approved

        license_comments = self.license_comments

        license_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.license_groups, Unset):
            license_groups = []
            for license_groups_item_data in self.license_groups:
                license_groups_item = license_groups_item_data.to_dict()
                license_groups.append(license_groups_item)

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
                "licenseId": license_id,
                "name": name,
                "uuid": uuid,
            }
        )
        if is_custom_license is not UNSET:
            field_dict["isCustomLicense"] = is_custom_license
        if is_deprecated_license_id is not UNSET:
            field_dict["isDeprecatedLicenseId"] = is_deprecated_license_id
        if is_fsf_libre is not UNSET:
            field_dict["isFsfLibre"] = is_fsf_libre
        if is_osi_approved is not UNSET:
            field_dict["isOsiApproved"] = is_osi_approved
        if license_comments is not UNSET:
            field_dict["licenseComments"] = license_comments
        if license_groups is not UNSET:
            field_dict["licenseGroups"] = license_groups
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.license_group import LicenseGroup

        d = dict(src_dict)
        license_id = d.pop("licenseId")

        name = d.pop("name")

        uuid = UUID(d.pop("uuid"))

        is_custom_license = d.pop("isCustomLicense", UNSET)

        is_deprecated_license_id = d.pop("isDeprecatedLicenseId", UNSET)

        is_fsf_libre = d.pop("isFsfLibre", UNSET)

        is_osi_approved = d.pop("isOsiApproved", UNSET)

        license_comments = d.pop("licenseComments", UNSET)

        _license_groups = d.pop("licenseGroups", UNSET)
        license_groups: list[LicenseGroup] | Unset = UNSET
        if _license_groups is not UNSET:
            license_groups = []
            for license_groups_item_data in _license_groups:
                license_groups_item = LicenseGroup.from_dict(license_groups_item_data)

                license_groups.append(license_groups_item)

        license_text = d.pop("licenseText", UNSET)

        see_also = cast(list[str], d.pop("seeAlso", UNSET))

        standard_license_header = d.pop("standardLicenseHeader", UNSET)

        standard_license_template = d.pop("standardLicenseTemplate", UNSET)

        license_ = cls(
            license_id=license_id,
            name=name,
            uuid=uuid,
            is_custom_license=is_custom_license,
            is_deprecated_license_id=is_deprecated_license_id,
            is_fsf_libre=is_fsf_libre,
            is_osi_approved=is_osi_approved,
            license_comments=license_comments,
            license_groups=license_groups,
            license_text=license_text,
            see_also=see_also,
            standard_license_header=standard_license_header,
            standard_license_template=standard_license_template,
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
