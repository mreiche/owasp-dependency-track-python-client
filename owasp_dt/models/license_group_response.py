from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.license_ import License


T = TypeVar("T", bound="LicenseGroupResponse")


@_attrs_define
class LicenseGroupResponse:
    """
    Attributes:
        licenses (list[License]): Licenses belonging to the license group
        name (str): Name of the license group
        risk_weight (int): Risk weight assigned to violations of this group
        uuid (UUID): UUID of the license group
    """

    licenses: list[License]
    name: str
    risk_weight: int
    uuid: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        licenses = []
        for licenses_item_data in self.licenses:
            licenses_item = licenses_item_data.to_dict()
            licenses.append(licenses_item)

        name = self.name

        risk_weight = self.risk_weight

        uuid = str(self.uuid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "licenses": licenses,
                "name": name,
                "riskWeight": risk_weight,
                "uuid": uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.license_ import License

        d = dict(src_dict)
        licenses = []
        _licenses = d.pop("licenses")
        for licenses_item_data in _licenses:
            licenses_item = License.from_dict(licenses_item_data)

            licenses.append(licenses_item)

        name = d.pop("name")

        risk_weight = d.pop("riskWeight")

        uuid = UUID(d.pop("uuid"))

        license_group_response = cls(
            licenses=licenses,
            name=name,
            risk_weight=risk_weight,
            uuid=uuid,
        )

        license_group_response.additional_properties = d
        return license_group_response

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
