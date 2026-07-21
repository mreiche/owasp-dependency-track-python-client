from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.affected_component_identity_type import AffectedComponentIdentityType
from ..models.affected_component_version_type import AffectedComponentVersionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.affected_version_attribution import AffectedVersionAttribution


T = TypeVar("T", bound="AffectedComponent")


@_attrs_define
class AffectedComponent:
    """
    Attributes:
        affected_version_attributions (list[AffectedVersionAttribution] | Unset):
        identity (str | Unset):
        identity_type (AffectedComponentIdentityType | Unset):
        uuid (UUID | Unset):
        version (str | Unset):
        version_end_excluding (str | Unset):
        version_end_including (str | Unset):
        version_start_excluding (str | Unset):
        version_start_including (str | Unset):
        version_type (AffectedComponentVersionType | Unset):
    """

    affected_version_attributions: list[AffectedVersionAttribution] | Unset = UNSET
    identity: str | Unset = UNSET
    identity_type: AffectedComponentIdentityType | Unset = UNSET
    uuid: UUID | Unset = UNSET
    version: str | Unset = UNSET
    version_end_excluding: str | Unset = UNSET
    version_end_including: str | Unset = UNSET
    version_start_excluding: str | Unset = UNSET
    version_start_including: str | Unset = UNSET
    version_type: AffectedComponentVersionType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_version_attributions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.affected_version_attributions, Unset):
            affected_version_attributions = []
            for (
                affected_version_attributions_item_data
            ) in self.affected_version_attributions:
                affected_version_attributions_item = (
                    affected_version_attributions_item_data.to_dict()
                )
                affected_version_attributions.append(affected_version_attributions_item)

        identity = self.identity

        identity_type: str | Unset = UNSET
        if not isinstance(self.identity_type, Unset):
            identity_type = self.identity_type.value

        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        version = self.version

        version_end_excluding = self.version_end_excluding

        version_end_including = self.version_end_including

        version_start_excluding = self.version_start_excluding

        version_start_including = self.version_start_including

        version_type: str | Unset = UNSET
        if not isinstance(self.version_type, Unset):
            version_type = self.version_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_version_attributions is not UNSET:
            field_dict["affectedVersionAttributions"] = affected_version_attributions
        if identity is not UNSET:
            field_dict["identity"] = identity
        if identity_type is not UNSET:
            field_dict["identityType"] = identity_type
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if version is not UNSET:
            field_dict["version"] = version
        if version_end_excluding is not UNSET:
            field_dict["versionEndExcluding"] = version_end_excluding
        if version_end_including is not UNSET:
            field_dict["versionEndIncluding"] = version_end_including
        if version_start_excluding is not UNSET:
            field_dict["versionStartExcluding"] = version_start_excluding
        if version_start_including is not UNSET:
            field_dict["versionStartIncluding"] = version_start_including
        if version_type is not UNSET:
            field_dict["versionType"] = version_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.affected_version_attribution import AffectedVersionAttribution

        d = dict(src_dict)
        _affected_version_attributions = d.pop("affectedVersionAttributions", UNSET)
        affected_version_attributions: list[AffectedVersionAttribution] | Unset = UNSET
        if _affected_version_attributions is not UNSET:
            affected_version_attributions = []
            for (
                affected_version_attributions_item_data
            ) in _affected_version_attributions:
                affected_version_attributions_item = (
                    AffectedVersionAttribution.from_dict(
                        affected_version_attributions_item_data
                    )
                )

                affected_version_attributions.append(affected_version_attributions_item)

        identity = d.pop("identity", UNSET)

        _identity_type = d.pop("identityType", UNSET)
        identity_type: AffectedComponentIdentityType | Unset
        if isinstance(_identity_type, Unset):
            identity_type = UNSET
        else:
            identity_type = AffectedComponentIdentityType(_identity_type)

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        version = d.pop("version", UNSET)

        version_end_excluding = d.pop("versionEndExcluding", UNSET)

        version_end_including = d.pop("versionEndIncluding", UNSET)

        version_start_excluding = d.pop("versionStartExcluding", UNSET)

        version_start_including = d.pop("versionStartIncluding", UNSET)

        _version_type = d.pop("versionType", UNSET)
        version_type: AffectedComponentVersionType | Unset
        if isinstance(_version_type, Unset):
            version_type = UNSET
        else:
            version_type = AffectedComponentVersionType(_version_type)

        affected_component = cls(
            affected_version_attributions=affected_version_attributions,
            identity=identity,
            identity_type=identity_type,
            uuid=uuid,
            version=version,
            version_end_excluding=version_end_excluding,
            version_end_including=version_end_including,
            version_start_excluding=version_start_excluding,
            version_start_including=version_start_including,
            version_type=version_type,
        )

        affected_component.additional_properties = d
        return affected_component

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
