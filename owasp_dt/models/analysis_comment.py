from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalysisComment")


@_attrs_define
class AnalysisComment:
    """
    Attributes:
        comment (str):
        timestamp (int): UNIX epoch timestamp in milliseconds
        commenter (str | Unset):
    """

    comment: str
    timestamp: int
    commenter: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        timestamp = self.timestamp

        commenter = self.commenter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comment": comment,
                "timestamp": timestamp,
            }
        )
        if commenter is not UNSET:
            field_dict["commenter"] = commenter

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        comment = d.pop("comment")

        timestamp = d.pop("timestamp")

        commenter = d.pop("commenter", UNSET)

        analysis_comment = cls(
            comment=comment,
            timestamp=timestamp,
            commenter=commenter,
        )

        analysis_comment.additional_properties = d
        return analysis_comment

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
