from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.repository_type import RepositoryType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Repository")


@_attrs_define
class Repository:
    """
    Attributes:
        authentication_required (bool):
        enabled (bool):
        identifier (str):
        internal (bool):
        resolution_order (int):
        type_ (RepositoryType):
        url (str):
        uuid (UUID):
        password (str | Unset):
        username (str | Unset):
    """

    authentication_required: bool
    enabled: bool
    identifier: str
    internal: bool
    resolution_order: int
    type_: RepositoryType
    url: str
    uuid: UUID
    password: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authentication_required = self.authentication_required

        enabled = self.enabled

        identifier = self.identifier

        internal = self.internal

        resolution_order = self.resolution_order

        type_ = self.type_.value

        url = self.url

        uuid = str(self.uuid)

        password = self.password

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authenticationRequired": authentication_required,
                "enabled": enabled,
                "identifier": identifier,
                "internal": internal,
                "resolutionOrder": resolution_order,
                "type": type_,
                "url": url,
                "uuid": uuid,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        authentication_required = d.pop("authenticationRequired")

        enabled = d.pop("enabled")

        identifier = d.pop("identifier")

        internal = d.pop("internal")

        resolution_order = d.pop("resolutionOrder")

        type_ = RepositoryType(d.pop("type"))

        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        password = d.pop("password", UNSET)

        username = d.pop("username", UNSET)

        repository = cls(
            authentication_required=authentication_required,
            enabled=enabled,
            identifier=identifier,
            internal=internal,
            resolution_order=resolution_order,
            type_=type_,
            url=url,
            uuid=uuid,
            password=password,
            username=username,
        )

        repository.additional_properties = d
        return repository

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
