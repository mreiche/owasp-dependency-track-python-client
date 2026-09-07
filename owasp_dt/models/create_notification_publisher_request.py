from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateNotificationPublisherRequest")


@_attrs_define
class CreateNotificationPublisherRequest:
    """
    Attributes:
        extension_name (str):
        name (str):
        description (str | Unset):
        template (str | Unset):
        template_mime_type (str | Unset):
    """

    extension_name: str
    name: str
    description: str | Unset = UNSET
    template: str | Unset = UNSET
    template_mime_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extension_name = self.extension_name

        name = self.name

        description = self.description

        template = self.template

        template_mime_type = self.template_mime_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "extensionName": extension_name,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if template is not UNSET:
            field_dict["template"] = template
        if template_mime_type is not UNSET:
            field_dict["templateMimeType"] = template_mime_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        extension_name = d.pop("extensionName")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        template = d.pop("template", UNSET)

        template_mime_type = d.pop("templateMimeType", UNSET)

        create_notification_publisher_request = cls(
            extension_name=extension_name,
            name=name,
            description=description,
            template=template,
            template_mime_type=template_mime_type,
        )

        create_notification_publisher_request.additional_properties = d
        return create_notification_publisher_request

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
