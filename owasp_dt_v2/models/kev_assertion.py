from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KevAssertion")


@_attrs_define
class KevAssertion:
    """A single assertion that a vulnerability is known to be exploited.

    Attributes:
        asserter (str): The entity that asserted the vulnerability is known to be exploited (e.g. `cisa`, `enisa`).
        asserter_display_name (str): Human-readable name of the asserting entity (e.g. `CISA KEV`).
        vuln_source (str): Source of the asserted vulnerability identifier (e.g. `NVD`).
        vuln_id (str): The asserted vulnerability identifier (e.g. `CVE-2021-44228`).
        created_at (int): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
        updated_at (int): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
        published_at (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC. Example: 1752209050377.
        required_action (str | Unset): Free-form remediation guidance provided by the source, if any.
        known_ransomware (bool | Unset): Whether the vulnerability is known to be used in ransomware campaigns. Absent
            when the source does not report this signal, which is distinct from an explicit `false`.
        description (str | Unset): Short description provided by the source, if any.
    """

    asserter: str
    asserter_display_name: str
    vuln_source: str
    vuln_id: str
    created_at: int
    updated_at: int
    published_at: int | Unset = UNSET
    required_action: str | Unset = UNSET
    known_ransomware: bool | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asserter = self.asserter

        asserter_display_name = self.asserter_display_name

        vuln_source = self.vuln_source

        vuln_id = self.vuln_id

        created_at = self.created_at

        updated_at = self.updated_at

        published_at = self.published_at

        required_action = self.required_action

        known_ransomware = self.known_ransomware

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asserter": asserter,
                "asserter_display_name": asserter_display_name,
                "vuln_source": vuln_source,
                "vuln_id": vuln_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if published_at is not UNSET:
            field_dict["published_at"] = published_at
        if required_action is not UNSET:
            field_dict["required_action"] = required_action
        if known_ransomware is not UNSET:
            field_dict["known_ransomware"] = known_ransomware
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        asserter = d.pop("asserter")

        asserter_display_name = d.pop("asserter_display_name")

        vuln_source = d.pop("vuln_source")

        vuln_id = d.pop("vuln_id")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        published_at = d.pop("published_at", UNSET)

        required_action = d.pop("required_action", UNSET)

        known_ransomware = d.pop("known_ransomware", UNSET)

        description = d.pop("description", UNSET)

        kev_assertion = cls(
            asserter=asserter,
            asserter_display_name=asserter_display_name,
            vuln_source=vuln_source,
            vuln_id=vuln_id,
            created_at=created_at,
            updated_at=updated_at,
            published_at=published_at,
            required_action=required_action,
            known_ransomware=known_ransomware,
            description=description,
        )

        kev_assertion.additional_properties = d
        return kev_assertion

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
