from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateRepositoryRequest")


@_attrs_define
class UpdateRepositoryRequest:
    """
    Attributes:
        authentication_required (bool): Whether the repository requires authentication
        enabled (bool): Whether the repository is enabled
        url (str): URL of the repository
        uuid (UUID): UUID of the repository to update
        internal (bool | Unset): Whether the repository is internal to the organization
        password (str | Unset): Name of the secret holding the password or token
        username (str | Unset): Username to authenticate with
    """

    authentication_required: bool
    enabled: bool
    url: str
    uuid: UUID
    internal: bool | Unset = UNSET
    password: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authentication_required = self.authentication_required

        enabled = self.enabled

        url = self.url

        uuid = str(self.uuid)

        internal = self.internal

        password = self.password

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authenticationRequired": authentication_required,
                "enabled": enabled,
                "url": url,
                "uuid": uuid,
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

        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        internal = d.pop("internal", UNSET)

        password = d.pop("password", UNSET)

        username = d.pop("username", UNSET)

        update_repository_request = cls(
            authentication_required=authentication_required,
            enabled=enabled,
            url=url,
            uuid=uuid,
            internal=internal,
            password=password,
            username=username,
        )

        update_repository_request.additional_properties = d
        return update_repository_request

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
