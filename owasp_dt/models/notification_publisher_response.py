from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationPublisherResponse")


@_attrs_define
class NotificationPublisherResponse:
    """
    Attributes:
        default_publisher (bool): Whether the publisher is one of the built-in defaults
        extension_name (str): Name of the publisher extension that handles delivery
        name (str): Name of the notification publisher
        template_mime_type (str): MIME type of the rendered template
        uuid (UUID): UUID of the notification publisher
        description (str | Unset): Description of the notification publisher
        template (str | Unset): Template used to render the notification payload
    """

    default_publisher: bool
    extension_name: str
    name: str
    template_mime_type: str
    uuid: UUID
    description: str | Unset = UNSET
    template: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_publisher = self.default_publisher

        extension_name = self.extension_name

        name = self.name

        template_mime_type = self.template_mime_type

        uuid = str(self.uuid)

        description = self.description

        template = self.template

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "defaultPublisher": default_publisher,
                "extensionName": extension_name,
                "name": name,
                "templateMimeType": template_mime_type,
                "uuid": uuid,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        default_publisher = d.pop("defaultPublisher")

        extension_name = d.pop("extensionName")

        name = d.pop("name")

        template_mime_type = d.pop("templateMimeType")

        uuid = UUID(d.pop("uuid"))

        description = d.pop("description", UNSET)

        template = d.pop("template", UNSET)

        notification_publisher_response = cls(
            default_publisher=default_publisher,
            extension_name=extension_name,
            name=name,
            template_mime_type=template_mime_type,
            uuid=uuid,
            description=description,
            template=template,
        )

        notification_publisher_response.additional_properties = d
        return notification_publisher_response

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
