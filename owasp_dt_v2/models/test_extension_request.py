from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_extension_request_config import TestExtensionRequestConfig


T = TypeVar("T", bound="TestExtensionRequest")


@_attrs_define
class TestExtensionRequest:
    """
    Attributes:
        config (TestExtensionRequestConfig | Unset):
    """

    config: TestExtensionRequestConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.test_extension_request_config import (
            TestExtensionRequestConfig,
        )

        d = dict(src_dict)
        _config = d.pop("config", UNSET)
        config: TestExtensionRequestConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = TestExtensionRequestConfig.from_dict(_config)

        test_extension_request = cls(
            config=config,
        )

        test_extension_request.additional_properties = d
        return test_extension_request

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
