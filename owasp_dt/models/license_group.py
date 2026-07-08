from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.license_ import License


T = TypeVar("T", bound="LicenseGroup")


@_attrs_define
class LicenseGroup:
    """
    Attributes:
        name (str):
        uuid (UUID):
        licenses (list[License] | Unset):
        risk_weight (int | Unset):
    """

    name: str
    uuid: UUID
    licenses: list[License] | Unset = UNSET
    risk_weight: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        uuid = str(self.uuid)

        licenses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.licenses, Unset):
            licenses = []
            for licenses_item_data in self.licenses:
                licenses_item = licenses_item_data.to_dict()
                licenses.append(licenses_item)

        risk_weight = self.risk_weight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "uuid": uuid,
            }
        )
        if licenses is not UNSET:
            field_dict["licenses"] = licenses
        if risk_weight is not UNSET:
            field_dict["riskWeight"] = risk_weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.license_ import License

        d = dict(src_dict)
        name = d.pop("name")

        uuid = UUID(d.pop("uuid"))

        _licenses = d.pop("licenses", UNSET)
        licenses: list[License] | Unset = UNSET
        if _licenses is not UNSET:
            licenses = []
            for licenses_item_data in _licenses:
                licenses_item = License.from_dict(licenses_item_data)

                licenses.append(licenses_item)

        risk_weight = d.pop("riskWeight", UNSET)

        license_group = cls(
            name=name,
            uuid=uuid,
            licenses=licenses,
            risk_weight=risk_weight,
        )

        license_group.additional_properties = d
        return license_group

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
