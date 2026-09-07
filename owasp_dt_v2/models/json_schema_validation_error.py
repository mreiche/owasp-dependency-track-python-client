from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JsonSchemaValidationError")


@_attrs_define
class JsonSchemaValidationError:
    """A JSON Schema validation error as per
    <https://json-schema.org/draft/2020-12/json-schema-core.html#name-output-structure>.

        Attributes:
            instance_location (str): JSON Pointer to the location in the instance that failed validation Example:
                /config/port.
            message (str): Human-readable error message Example: Value must be a number.
            evaluation_path (str | Unset): JSON Pointer to the location in the schema during evaluation Example:
                /properties/config/properties/port.
            schema_location (str | Unset): Schema location that generated the error Example:
                https://example.com/schemas/config#/properties/config/properties/port.
            keyword (str | Unset): The validation keyword that failed Example: type.
    """

    instance_location: str
    message: str
    evaluation_path: str | Unset = UNSET
    schema_location: str | Unset = UNSET
    keyword: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_location = self.instance_location

        message = self.message

        evaluation_path = self.evaluation_path

        schema_location = self.schema_location

        keyword = self.keyword

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instance_location": instance_location,
                "message": message,
            }
        )
        if evaluation_path is not UNSET:
            field_dict["evaluation_path"] = evaluation_path
        if schema_location is not UNSET:
            field_dict["schema_location"] = schema_location
        if keyword is not UNSET:
            field_dict["keyword"] = keyword

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        instance_location = d.pop("instance_location")

        message = d.pop("message")

        evaluation_path = d.pop("evaluation_path", UNSET)

        schema_location = d.pop("schema_location", UNSET)

        keyword = d.pop("keyword", UNSET)

        json_schema_validation_error = cls(
            instance_location=instance_location,
            message=message,
            evaluation_path=evaluation_path,
            schema_location=schema_location,
            keyword=keyword,
        )

        json_schema_validation_error.additional_properties = d
        return json_schema_validation_error

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
