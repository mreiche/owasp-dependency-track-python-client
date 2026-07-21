from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.component_classifier import ComponentClassifier
from ..models.component_scope import ComponentScope
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.component_property import ComponentProperty
    from ..models.dependency_metrics import DependencyMetrics
    from ..models.external_reference import ExternalReference
    from ..models.license_ import License
    from ..models.organizational_contact import OrganizationalContact
    from ..models.organizational_entity import OrganizationalEntity
    from ..models.project import Project
    from ..models.repository_meta_component import RepositoryMetaComponent
    from ..models.vulnerability import Vulnerability


T = TypeVar("T", bound="Component")


@_attrs_define
class Component:
    """
    Attributes:
        project (Project):
        uuid (UUID):
        author (str | Unset):
        authors (list[OrganizationalContact] | Unset):
        blake2b_256 (str | Unset):
        blake2b_384 (str | Unset):
        blake2b_512 (str | Unset):
        blake3 (str | Unset):
        children (list[Component] | Unset):
        classifier (ComponentClassifier | Unset):
        copyright_ (str | Unset):
        cpe (str | Unset):
        dependency_graph (list[str] | Unset):
        description (str | Unset):
        direct_dependencies (str | Unset):
        expand_dependency_graph (bool | Unset):
        extension (str | Unset):
        external_references (list[ExternalReference] | Unset):
        filename (str | Unset):
        group (str | Unset):
        is_internal (bool | Unset):
        last_inherited_risk_score (float | Unset):
        license_ (str | Unset):
        license_expression (str | Unset):
        license_url (str | Unset):
        md5 (str | Unset):
        metrics (DependencyMetrics | Unset):
        name (str | Unset):
        notes (str | Unset):
        occurrence_count (int | Unset):
        parent (Component | Unset):
        properties (list[ComponentProperty] | Unset):
        publisher (str | Unset):
        purl (str | Unset):
        purl_coordinates (str | Unset):
        repository_meta (RepositoryMetaComponent | Unset):
        resolved_license (License | Unset):
        scope (ComponentScope | Unset):
        sha1 (str | Unset):
        sha256 (str | Unset):
        sha384 (str | Unset):
        sha3_256 (str | Unset):
        sha3_384 (str | Unset):
        sha3_512 (str | Unset):
        sha512 (str | Unset):
        supplier (OrganizationalEntity | Unset):
        swid_tag_id (str | Unset):
        version (str | Unset):
        vulnerabilities (list[Vulnerability] | Unset):
    """

    project: Project
    uuid: UUID
    author: str | Unset = UNSET
    authors: list[OrganizationalContact] | Unset = UNSET
    blake2b_256: str | Unset = UNSET
    blake2b_384: str | Unset = UNSET
    blake2b_512: str | Unset = UNSET
    blake3: str | Unset = UNSET
    children: list[Component] | Unset = UNSET
    classifier: ComponentClassifier | Unset = UNSET
    copyright_: str | Unset = UNSET
    cpe: str | Unset = UNSET
    dependency_graph: list[str] | Unset = UNSET
    description: str | Unset = UNSET
    direct_dependencies: str | Unset = UNSET
    expand_dependency_graph: bool | Unset = UNSET
    extension: str | Unset = UNSET
    external_references: list[ExternalReference] | Unset = UNSET
    filename: str | Unset = UNSET
    group: str | Unset = UNSET
    is_internal: bool | Unset = UNSET
    last_inherited_risk_score: float | Unset = UNSET
    license_: str | Unset = UNSET
    license_expression: str | Unset = UNSET
    license_url: str | Unset = UNSET
    md5: str | Unset = UNSET
    metrics: DependencyMetrics | Unset = UNSET
    name: str | Unset = UNSET
    notes: str | Unset = UNSET
    occurrence_count: int | Unset = UNSET
    parent: Component | Unset = UNSET
    properties: list[ComponentProperty] | Unset = UNSET
    publisher: str | Unset = UNSET
    purl: str | Unset = UNSET
    purl_coordinates: str | Unset = UNSET
    repository_meta: RepositoryMetaComponent | Unset = UNSET
    resolved_license: License | Unset = UNSET
    scope: ComponentScope | Unset = UNSET
    sha1: str | Unset = UNSET
    sha256: str | Unset = UNSET
    sha384: str | Unset = UNSET
    sha3_256: str | Unset = UNSET
    sha3_384: str | Unset = UNSET
    sha3_512: str | Unset = UNSET
    sha512: str | Unset = UNSET
    supplier: OrganizationalEntity | Unset = UNSET
    swid_tag_id: str | Unset = UNSET
    version: str | Unset = UNSET
    vulnerabilities: list[Vulnerability] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project = self.project.to_dict()

        uuid = str(self.uuid)

        author = self.author

        authors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.authors, Unset):
            authors = []
            for authors_item_data in self.authors:
                authors_item = authors_item_data.to_dict()
                authors.append(authors_item)

        blake2b_256 = self.blake2b_256

        blake2b_384 = self.blake2b_384

        blake2b_512 = self.blake2b_512

        blake3 = self.blake3

        children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        classifier: str | Unset = UNSET
        if not isinstance(self.classifier, Unset):
            classifier = self.classifier.value

        copyright_ = self.copyright_

        cpe = self.cpe

        dependency_graph: list[str] | Unset = UNSET
        if not isinstance(self.dependency_graph, Unset):
            dependency_graph = self.dependency_graph

        description = self.description

        direct_dependencies = self.direct_dependencies

        expand_dependency_graph = self.expand_dependency_graph

        extension = self.extension

        external_references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.external_references, Unset):
            external_references = []
            for external_references_item_data in self.external_references:
                external_references_item = external_references_item_data.to_dict()
                external_references.append(external_references_item)

        filename = self.filename

        group = self.group

        is_internal = self.is_internal

        last_inherited_risk_score = self.last_inherited_risk_score

        license_ = self.license_

        license_expression = self.license_expression

        license_url = self.license_url

        md5 = self.md5

        metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics.to_dict()

        name = self.name

        notes = self.notes

        occurrence_count = self.occurrence_count

        parent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        publisher = self.publisher

        purl = self.purl

        purl_coordinates = self.purl_coordinates

        repository_meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository_meta, Unset):
            repository_meta = self.repository_meta.to_dict()

        resolved_license: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resolved_license, Unset):
            resolved_license = self.resolved_license.to_dict()

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        sha1 = self.sha1

        sha256 = self.sha256

        sha384 = self.sha384

        sha3_256 = self.sha3_256

        sha3_384 = self.sha3_384

        sha3_512 = self.sha3_512

        sha512 = self.sha512

        supplier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.supplier, Unset):
            supplier = self.supplier.to_dict()

        swid_tag_id = self.swid_tag_id

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
                "project": project,
                "uuid": uuid,
            }
        )
        if author is not UNSET:
            field_dict["author"] = author
        if authors is not UNSET:
            field_dict["authors"] = authors
        if blake2b_256 is not UNSET:
            field_dict["blake2b_256"] = blake2b_256
        if blake2b_384 is not UNSET:
            field_dict["blake2b_384"] = blake2b_384
        if blake2b_512 is not UNSET:
            field_dict["blake2b_512"] = blake2b_512
        if blake3 is not UNSET:
            field_dict["blake3"] = blake3
        if children is not UNSET:
            field_dict["children"] = children
        if classifier is not UNSET:
            field_dict["classifier"] = classifier
        if copyright_ is not UNSET:
            field_dict["copyright"] = copyright_
        if cpe is not UNSET:
            field_dict["cpe"] = cpe
        if dependency_graph is not UNSET:
            field_dict["dependencyGraph"] = dependency_graph
        if description is not UNSET:
            field_dict["description"] = description
        if direct_dependencies is not UNSET:
            field_dict["directDependencies"] = direct_dependencies
        if expand_dependency_graph is not UNSET:
            field_dict["expandDependencyGraph"] = expand_dependency_graph
        if extension is not UNSET:
            field_dict["extension"] = extension
        if external_references is not UNSET:
            field_dict["externalReferences"] = external_references
        if filename is not UNSET:
            field_dict["filename"] = filename
        if group is not UNSET:
            field_dict["group"] = group
        if is_internal is not UNSET:
            field_dict["isInternal"] = is_internal
        if last_inherited_risk_score is not UNSET:
            field_dict["lastInheritedRiskScore"] = last_inherited_risk_score
        if license_ is not UNSET:
            field_dict["license"] = license_
        if license_expression is not UNSET:
            field_dict["licenseExpression"] = license_expression
        if license_url is not UNSET:
            field_dict["licenseUrl"] = license_url
        if md5 is not UNSET:
            field_dict["md5"] = md5
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if name is not UNSET:
            field_dict["name"] = name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if occurrence_count is not UNSET:
            field_dict["occurrenceCount"] = occurrence_count
        if parent is not UNSET:
            field_dict["parent"] = parent
        if properties is not UNSET:
            field_dict["properties"] = properties
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if purl is not UNSET:
            field_dict["purl"] = purl
        if purl_coordinates is not UNSET:
            field_dict["purlCoordinates"] = purl_coordinates
        if repository_meta is not UNSET:
            field_dict["repositoryMeta"] = repository_meta
        if resolved_license is not UNSET:
            field_dict["resolvedLicense"] = resolved_license
        if scope is not UNSET:
            field_dict["scope"] = scope
        if sha1 is not UNSET:
            field_dict["sha1"] = sha1
        if sha256 is not UNSET:
            field_dict["sha256"] = sha256
        if sha384 is not UNSET:
            field_dict["sha384"] = sha384
        if sha3_256 is not UNSET:
            field_dict["sha3_256"] = sha3_256
        if sha3_384 is not UNSET:
            field_dict["sha3_384"] = sha3_384
        if sha3_512 is not UNSET:
            field_dict["sha3_512"] = sha3_512
        if sha512 is not UNSET:
            field_dict["sha512"] = sha512
        if supplier is not UNSET:
            field_dict["supplier"] = supplier
        if swid_tag_id is not UNSET:
            field_dict["swidTagId"] = swid_tag_id
        if version is not UNSET:
            field_dict["version"] = version
        if vulnerabilities is not UNSET:
            field_dict["vulnerabilities"] = vulnerabilities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.component_property import ComponentProperty
        from ..models.dependency_metrics import DependencyMetrics
        from ..models.external_reference import ExternalReference
        from ..models.license_ import License
        from ..models.organizational_contact import OrganizationalContact
        from ..models.organizational_entity import OrganizationalEntity
        from ..models.project import Project
        from ..models.repository_meta_component import RepositoryMetaComponent
        from ..models.vulnerability import Vulnerability

        d = dict(src_dict)
        project = Project.from_dict(d.pop("project"))

        uuid = UUID(d.pop("uuid"))

        author = d.pop("author", UNSET)

        _authors = d.pop("authors", UNSET)
        authors: list[OrganizationalContact] | Unset = UNSET
        if _authors is not UNSET:
            authors = []
            for authors_item_data in _authors:
                authors_item = OrganizationalContact.from_dict(authors_item_data)

                authors.append(authors_item)

        blake2b_256 = d.pop("blake2b_256", UNSET)

        blake2b_384 = d.pop("blake2b_384", UNSET)

        blake2b_512 = d.pop("blake2b_512", UNSET)

        blake3 = d.pop("blake3", UNSET)

        _children = d.pop("children", UNSET)
        children: list[Component] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = Component.from_dict(children_item_data)

                children.append(children_item)

        _classifier = d.pop("classifier", UNSET)
        classifier: ComponentClassifier | Unset
        if isinstance(_classifier, Unset):
            classifier = UNSET
        else:
            classifier = ComponentClassifier(_classifier)

        copyright_ = d.pop("copyright", UNSET)

        cpe = d.pop("cpe", UNSET)

        dependency_graph = cast(list[str], d.pop("dependencyGraph", UNSET))

        description = d.pop("description", UNSET)

        direct_dependencies = d.pop("directDependencies", UNSET)

        expand_dependency_graph = d.pop("expandDependencyGraph", UNSET)

        extension = d.pop("extension", UNSET)

        _external_references = d.pop("externalReferences", UNSET)
        external_references: list[ExternalReference] | Unset = UNSET
        if _external_references is not UNSET:
            external_references = []
            for external_references_item_data in _external_references:
                external_references_item = ExternalReference.from_dict(
                    external_references_item_data
                )

                external_references.append(external_references_item)

        filename = d.pop("filename", UNSET)

        group = d.pop("group", UNSET)

        is_internal = d.pop("isInternal", UNSET)

        last_inherited_risk_score = d.pop("lastInheritedRiskScore", UNSET)

        license_ = d.pop("license", UNSET)

        license_expression = d.pop("licenseExpression", UNSET)

        license_url = d.pop("licenseUrl", UNSET)

        md5 = d.pop("md5", UNSET)

        _metrics = d.pop("metrics", UNSET)
        metrics: DependencyMetrics | Unset
        if isinstance(_metrics, Unset):
            metrics = UNSET
        else:
            metrics = DependencyMetrics.from_dict(_metrics)

        name = d.pop("name", UNSET)

        notes = d.pop("notes", UNSET)

        occurrence_count = d.pop("occurrenceCount", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: Component | Unset
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = Component.from_dict(_parent)

        _properties = d.pop("properties", UNSET)
        properties: list[ComponentProperty] | Unset = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = ComponentProperty.from_dict(properties_item_data)

                properties.append(properties_item)

        publisher = d.pop("publisher", UNSET)

        purl = d.pop("purl", UNSET)

        purl_coordinates = d.pop("purlCoordinates", UNSET)

        _repository_meta = d.pop("repositoryMeta", UNSET)
        repository_meta: RepositoryMetaComponent | Unset
        if isinstance(_repository_meta, Unset):
            repository_meta = UNSET
        else:
            repository_meta = RepositoryMetaComponent.from_dict(_repository_meta)

        _resolved_license = d.pop("resolvedLicense", UNSET)
        resolved_license: License | Unset
        if isinstance(_resolved_license, Unset):
            resolved_license = UNSET
        else:
            resolved_license = License.from_dict(_resolved_license)

        _scope = d.pop("scope", UNSET)
        scope: ComponentScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = ComponentScope(_scope)

        sha1 = d.pop("sha1", UNSET)

        sha256 = d.pop("sha256", UNSET)

        sha384 = d.pop("sha384", UNSET)

        sha3_256 = d.pop("sha3_256", UNSET)

        sha3_384 = d.pop("sha3_384", UNSET)

        sha3_512 = d.pop("sha3_512", UNSET)

        sha512 = d.pop("sha512", UNSET)

        _supplier = d.pop("supplier", UNSET)
        supplier: OrganizationalEntity | Unset
        if isinstance(_supplier, Unset):
            supplier = UNSET
        else:
            supplier = OrganizationalEntity.from_dict(_supplier)

        swid_tag_id = d.pop("swidTagId", UNSET)

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

        component = cls(
            project=project,
            uuid=uuid,
            author=author,
            authors=authors,
            blake2b_256=blake2b_256,
            blake2b_384=blake2b_384,
            blake2b_512=blake2b_512,
            blake3=blake3,
            children=children,
            classifier=classifier,
            copyright_=copyright_,
            cpe=cpe,
            dependency_graph=dependency_graph,
            description=description,
            direct_dependencies=direct_dependencies,
            expand_dependency_graph=expand_dependency_graph,
            extension=extension,
            external_references=external_references,
            filename=filename,
            group=group,
            is_internal=is_internal,
            last_inherited_risk_score=last_inherited_risk_score,
            license_=license_,
            license_expression=license_expression,
            license_url=license_url,
            md5=md5,
            metrics=metrics,
            name=name,
            notes=notes,
            occurrence_count=occurrence_count,
            parent=parent,
            properties=properties,
            publisher=publisher,
            purl=purl,
            purl_coordinates=purl_coordinates,
            repository_meta=repository_meta,
            resolved_license=resolved_license,
            scope=scope,
            sha1=sha1,
            sha256=sha256,
            sha384=sha384,
            sha3_256=sha3_256,
            sha3_384=sha3_384,
            sha3_512=sha3_512,
            sha512=sha512,
            supplier=supplier,
            swid_tag_id=swid_tag_id,
            version=version,
            vulnerabilities=vulnerabilities,
        )

        component.additional_properties = d
        return component

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
