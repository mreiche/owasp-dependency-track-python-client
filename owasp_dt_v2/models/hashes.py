from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Hashes")


@_attrs_define
class Hashes:
    """
    Attributes:
        sha1 (str | Unset):
        sha256 (str | Unset):
        sha384 (str | Unset):
        sha512 (str | Unset):
        sha3_256 (str | Unset):
        sha3_384 (str | Unset):
        sha3_512 (str | Unset):
        blake2b_256 (str | Unset):
        blake2b_384 (str | Unset):
        blake2b_512 (str | Unset):
        blake3 (str | Unset):
        streebog_256 (str | Unset):
        streebog_512 (str | Unset):
        md5 (str | Unset):
    """

    sha1: str | Unset = UNSET
    sha256: str | Unset = UNSET
    sha384: str | Unset = UNSET
    sha512: str | Unset = UNSET
    sha3_256: str | Unset = UNSET
    sha3_384: str | Unset = UNSET
    sha3_512: str | Unset = UNSET
    blake2b_256: str | Unset = UNSET
    blake2b_384: str | Unset = UNSET
    blake2b_512: str | Unset = UNSET
    blake3: str | Unset = UNSET
    streebog_256: str | Unset = UNSET
    streebog_512: str | Unset = UNSET
    md5: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sha1 = self.sha1

        sha256 = self.sha256

        sha384 = self.sha384

        sha512 = self.sha512

        sha3_256 = self.sha3_256

        sha3_384 = self.sha3_384

        sha3_512 = self.sha3_512

        blake2b_256 = self.blake2b_256

        blake2b_384 = self.blake2b_384

        blake2b_512 = self.blake2b_512

        blake3 = self.blake3

        streebog_256 = self.streebog_256

        streebog_512 = self.streebog_512

        md5 = self.md5

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sha1 is not UNSET:
            field_dict["sha1"] = sha1
        if sha256 is not UNSET:
            field_dict["sha256"] = sha256
        if sha384 is not UNSET:
            field_dict["sha384"] = sha384
        if sha512 is not UNSET:
            field_dict["sha512"] = sha512
        if sha3_256 is not UNSET:
            field_dict["sha3_256"] = sha3_256
        if sha3_384 is not UNSET:
            field_dict["sha3_384"] = sha3_384
        if sha3_512 is not UNSET:
            field_dict["sha3_512"] = sha3_512
        if blake2b_256 is not UNSET:
            field_dict["blake2b_256"] = blake2b_256
        if blake2b_384 is not UNSET:
            field_dict["blake2b_384"] = blake2b_384
        if blake2b_512 is not UNSET:
            field_dict["blake2b_512"] = blake2b_512
        if blake3 is not UNSET:
            field_dict["blake3"] = blake3
        if streebog_256 is not UNSET:
            field_dict["streebog_256"] = streebog_256
        if streebog_512 is not UNSET:
            field_dict["streebog_512"] = streebog_512
        if md5 is not UNSET:
            field_dict["md5"] = md5

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        sha1 = d.pop("sha1", UNSET)

        sha256 = d.pop("sha256", UNSET)

        sha384 = d.pop("sha384", UNSET)

        sha512 = d.pop("sha512", UNSET)

        sha3_256 = d.pop("sha3_256", UNSET)

        sha3_384 = d.pop("sha3_384", UNSET)

        sha3_512 = d.pop("sha3_512", UNSET)

        blake2b_256 = d.pop("blake2b_256", UNSET)

        blake2b_384 = d.pop("blake2b_384", UNSET)

        blake2b_512 = d.pop("blake2b_512", UNSET)

        blake3 = d.pop("blake3", UNSET)

        streebog_256 = d.pop("streebog_256", UNSET)

        streebog_512 = d.pop("streebog_512", UNSET)

        md5 = d.pop("md5", UNSET)

        hashes = cls(
            sha1=sha1,
            sha256=sha256,
            sha384=sha384,
            sha512=sha512,
            sha3_256=sha3_256,
            sha3_384=sha3_384,
            sha3_512=sha3_512,
            blake2b_256=blake2b_256,
            blake2b_384=blake2b_384,
            blake2b_512=blake2b_512,
            blake3=blake3,
            streebog_256=streebog_256,
            streebog_512=streebog_512,
            md5=md5,
        )

        hashes.additional_properties = d
        return hashes

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
