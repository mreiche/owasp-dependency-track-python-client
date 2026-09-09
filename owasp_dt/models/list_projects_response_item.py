from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_projects_response_item_classifier import (
    ListProjectsResponseItemClassifier,
)
from ..models.list_projects_response_item_collection_logic import (
    ListProjectsResponseItemCollectionLogic,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_reference import ExternalReference
    from ..models.organizational_contact import OrganizationalContact
    from ..models.organizational_entity import OrganizationalEntity
    from ..models.parent import Parent
    from ..models.project_metadata import ProjectMetadata
    from ..models.project_metrics import ProjectMetrics
    from ..models.tag import Tag


T = TypeVar("T", bound="ListProjectsResponseItem")


@_attrs_define
class ListProjectsResponseItem:
    """
    Attributes:
        has_children (bool): Whether the project has child projects
        name (str):
        uuid (UUID):
        active (bool | Unset):
        authors (list[OrganizationalContact] | Unset):
        classifier (ListProjectsResponseItemClassifier | Unset):
        collection_logic (ListProjectsResponseItemCollectionLogic | Unset):
        collection_tag (Tag | Unset):
        cpe (str | Unset):
        description (str | Unset):
        direct_dependencies (str | Unset):
        external_references (list[ExternalReference] | Unset):
        group (str | Unset):
        inactive_since (int | Unset): UNIX epoch timestamp in milliseconds
        is_latest (bool | Unset):
        last_bom_import (int | Unset): UNIX epoch timestamp in milliseconds
        last_bom_import_format (str | Unset):
        last_inherited_risk_score (float | Unset):
        last_vulnerability_analysis (int | Unset): UNIX epoch timestamp in milliseconds
        manufacturer (OrganizationalEntity | Unset):
        metadata (ProjectMetadata | Unset):
        metrics (ProjectMetrics | Unset):
        parent (Parent | Unset):
        publisher (str | Unset):
        purl (str | Unset):
        supplier (OrganizationalEntity | Unset):
        swid_tag_id (str | Unset):
        tags (list[Tag] | Unset):
        version (str | Unset):
    """

    has_children: bool
    name: str
    uuid: UUID
    active: bool | Unset = UNSET
    authors: list[OrganizationalContact] | Unset = UNSET
    classifier: ListProjectsResponseItemClassifier | Unset = UNSET
    collection_logic: ListProjectsResponseItemCollectionLogic | Unset = UNSET
    collection_tag: Tag | Unset = UNSET
    cpe: str | Unset = UNSET
    description: str | Unset = UNSET
    direct_dependencies: str | Unset = UNSET
    external_references: list[ExternalReference] | Unset = UNSET
    group: str | Unset = UNSET
    inactive_since: int | Unset = UNSET
    is_latest: bool | Unset = UNSET
    last_bom_import: int | Unset = UNSET
    last_bom_import_format: str | Unset = UNSET
    last_inherited_risk_score: float | Unset = UNSET
    last_vulnerability_analysis: int | Unset = UNSET
    manufacturer: OrganizationalEntity | Unset = UNSET
    metadata: ProjectMetadata | Unset = UNSET
    metrics: ProjectMetrics | Unset = UNSET
    parent: Parent | Unset = UNSET
    publisher: str | Unset = UNSET
    purl: str | Unset = UNSET
    supplier: OrganizationalEntity | Unset = UNSET
    swid_tag_id: str | Unset = UNSET
    tags: list[Tag] | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_children = self.has_children

        name = self.name

        uuid = str(self.uuid)

        active = self.active

        authors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.authors, Unset):
            authors = []
            for authors_item_data in self.authors:
                authors_item = authors_item_data.to_dict()
                authors.append(authors_item)

        classifier: str | Unset = UNSET
        if not isinstance(self.classifier, Unset):
            classifier = self.classifier.value

        collection_logic: str | Unset = UNSET
        if not isinstance(self.collection_logic, Unset):
            collection_logic = self.collection_logic.value

        collection_tag: dict[str, Any] | Unset = UNSET
        if not isinstance(self.collection_tag, Unset):
            collection_tag = self.collection_tag.to_dict()

        cpe = self.cpe

        description = self.description

        direct_dependencies = self.direct_dependencies

        external_references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.external_references, Unset):
            external_references = []
            for external_references_item_data in self.external_references:
                external_references_item = external_references_item_data.to_dict()
                external_references.append(external_references_item)

        group = self.group

        inactive_since = self.inactive_since

        is_latest = self.is_latest

        last_bom_import = self.last_bom_import

        last_bom_import_format = self.last_bom_import_format

        last_inherited_risk_score = self.last_inherited_risk_score

        last_vulnerability_analysis = self.last_vulnerability_analysis

        manufacturer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.manufacturer, Unset):
            manufacturer = self.manufacturer.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics.to_dict()

        parent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        publisher = self.publisher

        purl = self.purl

        supplier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.supplier, Unset):
            supplier = self.supplier.to_dict()

        swid_tag_id = self.swid_tag_id

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hasChildren": has_children,
                "name": name,
                "uuid": uuid,
            }
        )
        if active is not UNSET:
            field_dict["active"] = active
        if authors is not UNSET:
            field_dict["authors"] = authors
        if classifier is not UNSET:
            field_dict["classifier"] = classifier
        if collection_logic is not UNSET:
            field_dict["collectionLogic"] = collection_logic
        if collection_tag is not UNSET:
            field_dict["collectionTag"] = collection_tag
        if cpe is not UNSET:
            field_dict["cpe"] = cpe
        if description is not UNSET:
            field_dict["description"] = description
        if direct_dependencies is not UNSET:
            field_dict["directDependencies"] = direct_dependencies
        if external_references is not UNSET:
            field_dict["externalReferences"] = external_references
        if group is not UNSET:
            field_dict["group"] = group
        if inactive_since is not UNSET:
            field_dict["inactiveSince"] = inactive_since
        if is_latest is not UNSET:
            field_dict["isLatest"] = is_latest
        if last_bom_import is not UNSET:
            field_dict["lastBomImport"] = last_bom_import
        if last_bom_import_format is not UNSET:
            field_dict["lastBomImportFormat"] = last_bom_import_format
        if last_inherited_risk_score is not UNSET:
            field_dict["lastInheritedRiskScore"] = last_inherited_risk_score
        if last_vulnerability_analysis is not UNSET:
            field_dict["lastVulnerabilityAnalysis"] = last_vulnerability_analysis
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if parent is not UNSET:
            field_dict["parent"] = parent
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if purl is not UNSET:
            field_dict["purl"] = purl
        if supplier is not UNSET:
            field_dict["supplier"] = supplier
        if swid_tag_id is not UNSET:
            field_dict["swidTagId"] = swid_tag_id
        if tags is not UNSET:
            field_dict["tags"] = tags
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.external_reference import ExternalReference
        from ..models.organizational_contact import (
            OrganizationalContact,
        )
        from ..models.organizational_entity import OrganizationalEntity
        from ..models.parent import Parent
        from ..models.project_metadata import ProjectMetadata
        from ..models.project_metrics import ProjectMetrics
        from ..models.tag import Tag

        d = dict(src_dict)
        has_children = d.pop("hasChildren")

        name = d.pop("name")

        uuid = UUID(d.pop("uuid"))

        active = d.pop("active", UNSET)

        _authors = d.pop("authors", UNSET)
        authors: list[OrganizationalContact] | Unset = UNSET
        if _authors is not UNSET:
            authors = []
            for authors_item_data in _authors:
                authors_item = OrganizationalContact.from_dict(authors_item_data)

                authors.append(authors_item)

        _classifier = d.pop("classifier", UNSET)
        classifier: ListProjectsResponseItemClassifier | Unset
        if isinstance(_classifier, Unset):
            classifier = UNSET
        else:
            classifier = ListProjectsResponseItemClassifier(_classifier)

        _collection_logic = d.pop("collectionLogic", UNSET)
        collection_logic: ListProjectsResponseItemCollectionLogic | Unset
        if isinstance(_collection_logic, Unset):
            collection_logic = UNSET
        else:
            collection_logic = ListProjectsResponseItemCollectionLogic(
                _collection_logic
            )

        _collection_tag = d.pop("collectionTag", UNSET)
        collection_tag: Tag | Unset
        if isinstance(_collection_tag, Unset):
            collection_tag = UNSET
        else:
            collection_tag = Tag.from_dict(_collection_tag)

        cpe = d.pop("cpe", UNSET)

        description = d.pop("description", UNSET)

        direct_dependencies = d.pop("directDependencies", UNSET)

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

        inactive_since = d.pop("inactiveSince", UNSET)

        is_latest = d.pop("isLatest", UNSET)

        last_bom_import = d.pop("lastBomImport", UNSET)

        last_bom_import_format = d.pop("lastBomImportFormat", UNSET)

        last_inherited_risk_score = d.pop("lastInheritedRiskScore", UNSET)

        last_vulnerability_analysis = d.pop("lastVulnerabilityAnalysis", UNSET)

        _manufacturer = d.pop("manufacturer", UNSET)
        manufacturer: OrganizationalEntity | Unset
        if isinstance(_manufacturer, Unset):
            manufacturer = UNSET
        else:
            manufacturer = OrganizationalEntity.from_dict(_manufacturer)

        _metadata = d.pop("metadata", UNSET)
        metadata: ProjectMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ProjectMetadata.from_dict(_metadata)

        _metrics = d.pop("metrics", UNSET)
        metrics: ProjectMetrics | Unset
        if isinstance(_metrics, Unset):
            metrics = UNSET
        else:
            metrics = ProjectMetrics.from_dict(_metrics)

        _parent = d.pop("parent", UNSET)
        parent: Parent | Unset
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = Parent.from_dict(_parent)

        publisher = d.pop("publisher", UNSET)

        purl = d.pop("purl", UNSET)

        _supplier = d.pop("supplier", UNSET)
        supplier: OrganizationalEntity | Unset
        if isinstance(_supplier, Unset):
            supplier = UNSET
        else:
            supplier = OrganizationalEntity.from_dict(_supplier)

        swid_tag_id = d.pop("swidTagId", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: list[Tag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = Tag.from_dict(tags_item_data)

                tags.append(tags_item)

        version = d.pop("version", UNSET)

        list_projects_response_item = cls(
            has_children=has_children,
            name=name,
            uuid=uuid,
            active=active,
            authors=authors,
            classifier=classifier,
            collection_logic=collection_logic,
            collection_tag=collection_tag,
            cpe=cpe,
            description=description,
            direct_dependencies=direct_dependencies,
            external_references=external_references,
            group=group,
            inactive_since=inactive_since,
            is_latest=is_latest,
            last_bom_import=last_bom_import,
            last_bom_import_format=last_bom_import_format,
            last_inherited_risk_score=last_inherited_risk_score,
            last_vulnerability_analysis=last_vulnerability_analysis,
            manufacturer=manufacturer,
            metadata=metadata,
            metrics=metrics,
            parent=parent,
            publisher=publisher,
            purl=purl,
            supplier=supplier,
            swid_tag_id=swid_tag_id,
            tags=tags,
            version=version,
        )

        list_projects_response_item.additional_properties = d
        return list_projects_response_item

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
