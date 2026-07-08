from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListVulnPolicyBundlesResponseItem")


@_attrs_define
class ListVulnPolicyBundlesResponseItem:
    """
    Attributes:
        uuid (UUID):
        url (str):
        hash_ (str | Unset):
        last_successful_sync (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example:
            1752209050377.
        created (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
        updated (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
    """

    uuid: UUID
    url: str
    hash_: str | Unset = UNSET
    last_successful_sync: int | Unset = UNSET
    created: int | Unset = UNSET
    updated: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        url = self.url

        hash_ = self.hash_

        last_successful_sync = self.last_successful_sync

        created = self.created

        updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "url": url,
            }
        )
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if last_successful_sync is not UNSET:
            field_dict["last_successful_sync"] = last_successful_sync
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        url = d.pop("url")

        hash_ = d.pop("hash", UNSET)

        last_successful_sync = d.pop("last_successful_sync", UNSET)

        created = d.pop("created", UNSET)

        updated = d.pop("updated", UNSET)

        list_vuln_policy_bundles_response_item = cls(
            uuid=uuid,
            url=url,
            hash_=hash_,
            last_successful_sync=last_successful_sync,
            created=created,
            updated=updated,
        )

        list_vuln_policy_bundles_response_item.additional_properties = d
        return list_vuln_policy_bundles_response_item

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
