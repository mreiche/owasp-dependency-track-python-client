from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_classification import DataClassification
    from ..models.external_reference import ExternalReference
    from ..models.organizational_entity import OrganizationalEntity
    from ..models.project import Project
    from ..models.vulnerability import Vulnerability


T = TypeVar("T", bound="ServiceComponent")


@_attrs_define
class ServiceComponent:
    """
    Attributes:
        name (str):
        project (Project):
        uuid (UUID):
        authenticated (bool | Unset):
        bom_ref (str | Unset):
        children (list[ServiceComponent] | Unset):
        crosses_trust_boundary (bool | Unset):
        data (list[DataClassification] | Unset):
        description (str | Unset):
        endpoints (list[str] | Unset):
        external_references (list[ExternalReference] | Unset):
        group (str | Unset):
        last_inherited_risk_score (float | Unset):
        notes (str | Unset):
        parent (ServiceComponent | Unset):
        provider (OrganizationalEntity | Unset):
        version (str | Unset):
        vulnerabilities (list[Vulnerability] | Unset):
    """

    name: str
    project: Project
    uuid: UUID
    authenticated: bool | Unset = UNSET
    bom_ref: str | Unset = UNSET
    children: list[ServiceComponent] | Unset = UNSET
    crosses_trust_boundary: bool | Unset = UNSET
    data: list[DataClassification] | Unset = UNSET
    description: str | Unset = UNSET
    endpoints: list[str] | Unset = UNSET
    external_references: list[ExternalReference] | Unset = UNSET
    group: str | Unset = UNSET
    last_inherited_risk_score: float | Unset = UNSET
    notes: str | Unset = UNSET
    parent: ServiceComponent | Unset = UNSET
    provider: OrganizationalEntity | Unset = UNSET
    version: str | Unset = UNSET
    vulnerabilities: list[Vulnerability] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        project = self.project.to_dict()

        uuid = str(self.uuid)

        authenticated = self.authenticated

        bom_ref = self.bom_ref

        children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        crosses_trust_boundary = self.crosses_trust_boundary

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        description = self.description

        endpoints: list[str] | Unset = UNSET
        if not isinstance(self.endpoints, Unset):
            endpoints = self.endpoints

        external_references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.external_references, Unset):
            external_references = []
            for external_references_item_data in self.external_references:
                external_references_item = external_references_item_data.to_dict()
                external_references.append(external_references_item)

        group = self.group

        last_inherited_risk_score = self.last_inherited_risk_score

        notes = self.notes

        parent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        provider: dict[str, Any] | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.to_dict()

        version = self.version

        vulnerabilities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.vulnerabilities, Unset):
            vulnerabilities = []
            for vulnerabilities_item_data in self.vulnerabilities:
                vulnerabilities_item = vulnerabilities_item_data.to_dict()
                vulnerabilities.append(vulnerabilities_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "project": project,
                "uuid": uuid,
            }
        )
        if authenticated is not UNSET:
            field_dict["authenticated"] = authenticated
        if bom_ref is not UNSET:
            field_dict["bomRef"] = bom_ref
        if children is not UNSET:
            field_dict["children"] = children
        if crosses_trust_boundary is not UNSET:
            field_dict["crossesTrustBoundary"] = crosses_trust_boundary
        if data is not UNSET:
            field_dict["data"] = data
        if description is not UNSET:
            field_dict["description"] = description
        if endpoints is not UNSET:
            field_dict["endpoints"] = endpoints
        if external_references is not UNSET:
            field_dict["externalReferences"] = external_references
        if group is not UNSET:
            field_dict["group"] = group
        if last_inherited_risk_score is not UNSET:
            field_dict["lastInheritedRiskScore"] = last_inherited_risk_score
        if notes is not UNSET:
            field_dict["notes"] = notes
        if parent is not UNSET:
            field_dict["parent"] = parent
        if provider is not UNSET:
            field_dict["provider"] = provider
        if version is not UNSET:
            field_dict["version"] = version
        if vulnerabilities is not UNSET:
            field_dict["vulnerabilities"] = vulnerabilities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_classification import DataClassification
        from ..models.external_reference import ExternalReference
        from ..models.organizational_entity import OrganizationalEntity
        from ..models.project import Project
        from ..models.vulnerability import Vulnerability

        d = dict(src_dict)
        name = d.pop("name")

        project = Project.from_dict(d.pop("project"))

        uuid = UUID(d.pop("uuid"))

        authenticated = d.pop("authenticated", UNSET)

        bom_ref = d.pop("bomRef", UNSET)

        _children = d.pop("children", UNSET)
        children: list[ServiceComponent] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = ServiceComponent.from_dict(children_item_data)

                children.append(children_item)

        crosses_trust_boundary = d.pop("crossesTrustBoundary", UNSET)

        _data = d.pop("data", UNSET)
        data: list[DataClassification] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = DataClassification.from_dict(data_item_data)

                data.append(data_item)

        description = d.pop("description", UNSET)

        endpoints = cast(list[str], d.pop("endpoints", UNSET))

        _external_references = d.pop("externalReferences", UNSET)
        external_references: list[ExternalReference] | Unset = UNSET
        if _external_references is not UNSET:
            external_references = []
            for external_references_item_data in _external_references:
                external_references_item = ExternalReference.from_dict(
                    external_references_item_data
                )

                external_references.append(external_references_item)

        group = d.pop("group", UNSET)

        last_inherited_risk_score = d.pop("lastInheritedRiskScore", UNSET)

        notes = d.pop("notes", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: ServiceComponent | Unset
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = ServiceComponent.from_dict(_parent)

        _provider = d.pop("provider", UNSET)
        provider: OrganizationalEntity | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = OrganizationalEntity.from_dict(_provider)

        version = d.pop("version", UNSET)

        _vulnerabilities = d.pop("vulnerabilities", UNSET)
        vulnerabilities: list[Vulnerability] | Unset = UNSET
        if _vulnerabilities is not UNSET:
            vulnerabilities = []
            for vulnerabilities_item_data in _vulnerabilities:
                vulnerabilities_item = Vulnerability.from_dict(
                    vulnerabilities_item_data
                )

                vulnerabilities.append(vulnerabilities_item)

        service_component = cls(
            name=name,
            project=project,
            uuid=uuid,
            authenticated=authenticated,
            bom_ref=bom_ref,
            children=children,
            crosses_trust_boundary=crosses_trust_boundary,
            data=data,
            description=description,
            endpoints=endpoints,
            external_references=external_references,
            group=group,
            last_inherited_risk_score=last_inherited_risk_score,
            notes=notes,
            parent=parent,
            provider=provider,
            version=version,
            vulnerabilities=vulnerabilities,
        )

        service_component.additional_properties = d
        return service_component

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
