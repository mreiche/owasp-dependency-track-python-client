from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.concise_project_classifier import ConciseProjectClassifier
from ..models.concise_project_collection_logic import ConciseProjectCollectionLogic
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.concise_project_metrics import ConciseProjectMetrics
    from ..models.tag import Tag
    from ..models.team import Team


T = TypeVar("T", bound="ConciseProject")


@_attrs_define
class ConciseProject:
    """A concise representation of a project

    Attributes:
        active (bool): Whether the project is active
        has_children (bool): Whether the project has children
        name (str): Name of the project
        uuid (UUID): UUID of the project
        classifier (ConciseProjectClassifier | Unset): Classifier of the project
        collection_logic (ConciseProjectCollectionLogic | Unset): Collection logic for aggregating child metrics
        group (str | Unset): Group or namespace of the project
        is_latest (bool | Unset): Whether the project version is latest
        last_bom_import (int | Unset): Timestamp of the last BOM import
        last_bom_import_format (str | Unset): Format of the last imported BOM
        last_risk_score (float | Unset): Last observed risk score
        metrics (ConciseProjectMetrics | Unset): A concise representation of a project's metrics
        tags (list[Tag] | Unset): Tags associated with the project
        teams (list[Team] | Unset): Teams associated with the project
        version (str | Unset): Version of the project
    """

    active: bool
    has_children: bool
    name: str
    uuid: UUID
    classifier: ConciseProjectClassifier | Unset = UNSET
    collection_logic: ConciseProjectCollectionLogic | Unset = UNSET
    group: str | Unset = UNSET
    is_latest: bool | Unset = UNSET
    last_bom_import: int | Unset = UNSET
    last_bom_import_format: str | Unset = UNSET
    last_risk_score: float | Unset = UNSET
    metrics: ConciseProjectMetrics | Unset = UNSET
    tags: list[Tag] | Unset = UNSET
    teams: list[Team] | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        has_children = self.has_children

        name = self.name

        uuid = str(self.uuid)

        classifier: str | Unset = UNSET
        if not isinstance(self.classifier, Unset):
            classifier = self.classifier.value

        collection_logic: str | Unset = UNSET
        if not isinstance(self.collection_logic, Unset):
            collection_logic = self.collection_logic.value

        group = self.group

        is_latest = self.is_latest

        last_bom_import = self.last_bom_import

        last_bom_import_format = self.last_bom_import_format

        last_risk_score = self.last_risk_score

        metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics.to_dict()

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        teams: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()
                teams.append(teams_item)

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
                "hasChildren": has_children,
                "name": name,
                "uuid": uuid,
            }
        )
        if classifier is not UNSET:
            field_dict["classifier"] = classifier
        if collection_logic is not UNSET:
            field_dict["collectionLogic"] = collection_logic
        if group is not UNSET:
            field_dict["group"] = group
        if is_latest is not UNSET:
            field_dict["isLatest"] = is_latest
        if last_bom_import is not UNSET:
            field_dict["lastBomImport"] = last_bom_import
        if last_bom_import_format is not UNSET:
            field_dict["lastBomImportFormat"] = last_bom_import_format
        if last_risk_score is not UNSET:
            field_dict["lastRiskScore"] = last_risk_score
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if tags is not UNSET:
            field_dict["tags"] = tags
        if teams is not UNSET:
            field_dict["teams"] = teams
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.concise_project_metrics import (
            ConciseProjectMetrics,
        )
        from ..models.tag import Tag
        from ..models.team import Team

        d = dict(src_dict)
        active = d.pop("active")

        has_children = d.pop("hasChildren")

        name = d.pop("name")

        uuid = UUID(d.pop("uuid"))

        _classifier = d.pop("classifier", UNSET)
        classifier: ConciseProjectClassifier | Unset
        if isinstance(_classifier, Unset):
            classifier = UNSET
        else:
            classifier = ConciseProjectClassifier(_classifier)

        _collection_logic = d.pop("collectionLogic", UNSET)
        collection_logic: ConciseProjectCollectionLogic | Unset
        if isinstance(_collection_logic, Unset):
            collection_logic = UNSET
        else:
            collection_logic = ConciseProjectCollectionLogic(_collection_logic)

        group = d.pop("group", UNSET)

        is_latest = d.pop("isLatest", UNSET)

        last_bom_import = d.pop("lastBomImport", UNSET)

        last_bom_import_format = d.pop("lastBomImportFormat", UNSET)

        last_risk_score = d.pop("lastRiskScore", UNSET)

        _metrics = d.pop("metrics", UNSET)
        metrics: ConciseProjectMetrics | Unset
        if isinstance(_metrics, Unset):
            metrics = UNSET
        else:
            metrics = ConciseProjectMetrics.from_dict(_metrics)

        _tags = d.pop("tags", UNSET)
        tags: list[Tag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = Tag.from_dict(tags_item_data)

                tags.append(tags_item)

        _teams = d.pop("teams", UNSET)
        teams: list[Team] | Unset = UNSET
        if _teams is not UNSET:
            teams = []
            for teams_item_data in _teams:
                teams_item = Team.from_dict(teams_item_data)

                teams.append(teams_item)

        version = d.pop("version", UNSET)

        concise_project = cls(
            active=active,
            has_children=has_children,
            name=name,
            uuid=uuid,
            classifier=classifier,
            collection_logic=collection_logic,
            group=group,
            is_latest=is_latest,
            last_bom_import=last_bom_import,
            last_bom_import_format=last_bom_import_format,
            last_risk_score=last_risk_score,
            metrics=metrics,
            tags=tags,
            teams=teams,
            version=version,
        )

        concise_project.additional_properties = d
        return concise_project

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
