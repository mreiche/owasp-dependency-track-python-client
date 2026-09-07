from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.framework import Framework


T = TypeVar("T", bound="About")


@_attrs_define
class About:
    """
    Attributes:
        application (str | Unset):
        framework (Framework | Unset):
        timestamp (str | Unset):
        uuid (str | Unset):
        version (str | Unset):
    """

    application: str | Unset = UNSET
    framework: Framework | Unset = UNSET
    timestamp: str | Unset = UNSET
    uuid: str | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application = self.application

        framework: dict[str, Any] | Unset = UNSET
        if not isinstance(self.framework, Unset):
            framework = self.framework.to_dict()

        timestamp = self.timestamp

        uuid = self.uuid

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application is not UNSET:
            field_dict["application"] = application
        if framework is not UNSET:
            field_dict["framework"] = framework
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.framework import Framework

        d = dict(src_dict)
        application = d.pop("application", UNSET)

        _framework = d.pop("framework", UNSET)
        framework: Framework | Unset
        if isinstance(_framework, Unset):
            framework = UNSET
        else:
            framework = Framework.from_dict(_framework)

        timestamp = d.pop("timestamp", UNSET)

        uuid = d.pop("uuid", UNSET)

        version = d.pop("version", UNSET)

        about = cls(
            application=application,
            framework=framework,
            timestamp=timestamp,
            uuid=uuid,
            version=version,
        )

        about.additional_properties = d
        return about

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
