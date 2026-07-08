from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationPublisher")


@_attrs_define
class NotificationPublisher:
    """
    Attributes:
        extension_name (str):
        name (str):
        template_mime_type (str):
        uuid (UUID):
        default_publisher (bool | Unset):
        description (str | Unset):
        template (str | Unset):
    """

    extension_name: str
    name: str
    template_mime_type: str
    uuid: UUID
    default_publisher: bool | Unset = UNSET
    description: str | Unset = UNSET
    template: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extension_name = self.extension_name

        name = self.name

        template_mime_type = self.template_mime_type

        uuid = str(self.uuid)

        default_publisher = self.default_publisher

        description = self.description

        template = self.template

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "extensionName": extension_name,
                "name": name,
                "templateMimeType": template_mime_type,
                "uuid": uuid,
            }
        )
        if default_publisher is not UNSET:
            field_dict["defaultPublisher"] = default_publisher
        if description is not UNSET:
            field_dict["description"] = description
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        extension_name = d.pop("extensionName")

        name = d.pop("name")

        template_mime_type = d.pop("templateMimeType")

        uuid = UUID(d.pop("uuid"))

        default_publisher = d.pop("defaultPublisher", UNSET)

        description = d.pop("description", UNSET)

        template = d.pop("template", UNSET)

        notification_publisher = cls(
            extension_name=extension_name,
            name=name,
            template_mime_type=template_mime_type,
            uuid=uuid,
            default_publisher=default_publisher,
            description=description,
            template=template,
        )

        notification_publisher.additional_properties = d
        return notification_publisher

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
