from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.total_count import TotalCount


T = TypeVar("T", bound="PaginatedResponse")


@_attrs_define
class PaginatedResponse:
    """
    Attributes:
        total (TotalCount):
        next_page_token (str | Unset): Token to retrieve the next page. Absent when no more items exist.
    """

    total: TotalCount
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total.to_dict()

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
            }
        )
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.total_count import TotalCount

        d = dict(src_dict)
        total = TotalCount.from_dict(d.pop("total"))

        next_page_token = d.pop("next_page_token", UNSET)

        paginated_response = cls(
            total=total,
            next_page_token=next_page_token,
        )

        paginated_response.additional_properties = d
        return paginated_response

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
