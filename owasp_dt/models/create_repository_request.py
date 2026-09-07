from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_repository_request_type import CreateRepositoryRequestType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateRepositoryRequest")


@_attrs_define
class CreateRepositoryRequest:
    """
    Attributes:
        authentication_required (bool): Whether the repository requires authentication
        enabled (bool): Whether the repository is enabled
        identifier (str): Unique identifier of the repository within its type
        type_ (CreateRepositoryRequestType): Type of the repository
        url (str): URL of the repository
        internal (bool | Unset): Whether the repository is internal to the organization
        password (str | Unset): Name of the secret holding the password or token
        username (str | Unset): Username to authenticate with
    """

    authentication_required: bool
    enabled: bool
    identifier: str
    type_: CreateRepositoryRequestType
    url: str
    internal: bool | Unset = UNSET
    password: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authentication_required = self.authentication_required

        enabled = self.enabled

        identifier = self.identifier

        type_ = self.type_.value

        url = self.url

        internal = self.internal

        password = self.password

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authenticationRequired": authentication_required,
                "enabled": enabled,
                "identifier": identifier,
                "type": type_,
                "url": url,
            }
        )
        if internal is not UNSET:
            field_dict["internal"] = internal
        if password is not UNSET:
            field_dict["password"] = password
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        authentication_required = d.pop("authenticationRequired")

        enabled = d.pop("enabled")

        identifier = d.pop("identifier")

        type_ = CreateRepositoryRequestType(d.pop("type"))

        url = d.pop("url")

        internal = d.pop("internal", UNSET)

        password = d.pop("password", UNSET)

        username = d.pop("username", UNSET)

        create_repository_request = cls(
            authentication_required=authentication_required,
            enabled=enabled,
            identifier=identifier,
            type_=type_,
            url=url,
            internal=internal,
            password=password,
            username=username,
        )

        create_repository_request.additional_properties = d
        return create_repository_request

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
