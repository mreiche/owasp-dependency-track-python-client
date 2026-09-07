from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.scope import Scope
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dependency_metrics import DependencyMetrics
    from ..models.hashes import Hashes
    from ..models.license_ import License
    from ..models.package_artifact_metadata import PackageArtifactMetadata
    from ..models.package_metadata import PackageMetadata


T = TypeVar("T", bound="ListProjectComponentsResponseItem")


@_attrs_define
class ListProjectComponentsResponseItem:
    """
    Attributes:
        name (str):
        uuid (UUID):
        version (str | Unset):
        group (str | Unset):
        classifier (str | Unset):
        hashes (Hashes | Unset):
        cpe (str | Unset):
        purl (str | Unset):
        swid_tag_id (str | Unset):
        internal (bool | Unset):
        copyright_ (str | Unset):
        license_ (str | Unset):
        license_expression (str | Unset):
        license_url (str | Unset):
        resolved_license (License | Unset):
        occurrence_count (int | Unset):
        scope (Scope | Unset):
        last_inherited_risk_score (float | Unset):
        metrics (DependencyMetrics | Unset):
        package_metadata (PackageMetadata | Unset): Latest version information from configured package registries. Only
            present when the component has a PURL with a type supported by at least one configured repository, and metadata
            has been successfully resolved from an upstream repository. Metadata resolution is asynchronous and runs in the
            background after a component is created or updated. This field may be absent for recently created components
            until resolution completes.
        package_artifact_metadata (PackageArtifactMetadata | Unset): Artifact-level metadata for the component's exact
            version from configured package repositories. Only present when the component has a PURL with a version, the
            PURL type is supported by at least one configured repository, and artifact metadata has been successfully
            resolved from an upstream repository. Metadata resolution is asynchronous and runs in the background after a
            component is created or updated. This field may be absent for recently created components until resolution
            completes.
    """

    name: str
    uuid: UUID
    version: str | Unset = UNSET
    group: str | Unset = UNSET
    classifier: str | Unset = UNSET
    hashes: Hashes | Unset = UNSET
    cpe: str | Unset = UNSET
    purl: str | Unset = UNSET
    swid_tag_id: str | Unset = UNSET
    internal: bool | Unset = UNSET
    copyright_: str | Unset = UNSET
    license_: str | Unset = UNSET
    license_expression: str | Unset = UNSET
    license_url: str | Unset = UNSET
    resolved_license: License | Unset = UNSET
    occurrence_count: int | Unset = UNSET
    scope: Scope | Unset = UNSET
    last_inherited_risk_score: float | Unset = UNSET
    metrics: DependencyMetrics | Unset = UNSET
    package_metadata: PackageMetadata | Unset = UNSET
    package_artifact_metadata: PackageArtifactMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        uuid = str(self.uuid)

        version = self.version

        group = self.group

        classifier = self.classifier

        hashes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hashes, Unset):
            hashes = self.hashes.to_dict()

        cpe = self.cpe

        purl = self.purl

        swid_tag_id = self.swid_tag_id

        internal = self.internal

        copyright_ = self.copyright_

        license_ = self.license_

        license_expression = self.license_expression

        license_url = self.license_url

        resolved_license: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resolved_license, Unset):
            resolved_license = self.resolved_license.to_dict()

        occurrence_count = self.occurrence_count

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        last_inherited_risk_score = self.last_inherited_risk_score

        metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics.to_dict()

        package_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.package_metadata, Unset):
            package_metadata = self.package_metadata.to_dict()

        package_artifact_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.package_artifact_metadata, Unset):
            package_artifact_metadata = self.package_artifact_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "uuid": uuid,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version
        if group is not UNSET:
            field_dict["group"] = group
        if classifier is not UNSET:
            field_dict["classifier"] = classifier
        if hashes is not UNSET:
            field_dict["hashes"] = hashes
        if cpe is not UNSET:
            field_dict["cpe"] = cpe
        if purl is not UNSET:
            field_dict["purl"] = purl
        if swid_tag_id is not UNSET:
            field_dict["swid_tag_id"] = swid_tag_id
        if internal is not UNSET:
            field_dict["internal"] = internal
        if copyright_ is not UNSET:
            field_dict["copyright"] = copyright_
        if license_ is not UNSET:
            field_dict["license"] = license_
        if license_expression is not UNSET:
            field_dict["license_expression"] = license_expression
        if license_url is not UNSET:
            field_dict["license_url"] = license_url
        if resolved_license is not UNSET:
            field_dict["resolved_license"] = resolved_license
        if occurrence_count is not UNSET:
            field_dict["occurrence_count"] = occurrence_count
        if scope is not UNSET:
            field_dict["scope"] = scope
        if last_inherited_risk_score is not UNSET:
            field_dict["last_inherited_risk_score"] = last_inherited_risk_score
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if package_metadata is not UNSET:
            field_dict["package_metadata"] = package_metadata
        if package_artifact_metadata is not UNSET:
            field_dict["package_artifact_metadata"] = package_artifact_metadata

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dependency_metrics import DependencyMetrics
        from ..models.hashes import Hashes
        from ..models.license_ import License
        from ..models.package_artifact_metadata import (
            PackageArtifactMetadata,
        )
        from ..models.package_metadata import PackageMetadata

        d = dict(src_dict)
        name = d.pop("name")

        uuid = UUID(d.pop("uuid"))

        version = d.pop("version", UNSET)

        group = d.pop("group", UNSET)

        classifier = d.pop("classifier", UNSET)

        _hashes = d.pop("hashes", UNSET)
        hashes: Hashes | Unset
        if isinstance(_hashes, Unset):
            hashes = UNSET
        else:
            hashes = Hashes.from_dict(_hashes)

        cpe = d.pop("cpe", UNSET)

        purl = d.pop("purl", UNSET)

        swid_tag_id = d.pop("swid_tag_id", UNSET)

        internal = d.pop("internal", UNSET)

        copyright_ = d.pop("copyright", UNSET)

        license_ = d.pop("license", UNSET)

        license_expression = d.pop("license_expression", UNSET)

        license_url = d.pop("license_url", UNSET)

        _resolved_license = d.pop("resolved_license", UNSET)
        resolved_license: License | Unset
        if isinstance(_resolved_license, Unset):
            resolved_license = UNSET
        else:
            resolved_license = License.from_dict(_resolved_license)

        occurrence_count = d.pop("occurrence_count", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: Scope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = Scope(_scope)

        last_inherited_risk_score = d.pop("last_inherited_risk_score", UNSET)

        _metrics = d.pop("metrics", UNSET)
        metrics: DependencyMetrics | Unset
        if isinstance(_metrics, Unset):
            metrics = UNSET
        else:
            metrics = DependencyMetrics.from_dict(_metrics)

        _package_metadata = d.pop("package_metadata", UNSET)
        package_metadata: PackageMetadata | Unset
        if isinstance(_package_metadata, Unset):
            package_metadata = UNSET
        else:
            package_metadata = PackageMetadata.from_dict(_package_metadata)

        _package_artifact_metadata = d.pop("package_artifact_metadata", UNSET)
        package_artifact_metadata: PackageArtifactMetadata | Unset
        if isinstance(_package_artifact_metadata, Unset):
            package_artifact_metadata = UNSET
        else:
            package_artifact_metadata = PackageArtifactMetadata.from_dict(
                _package_artifact_metadata
            )

        list_project_components_response_item = cls(
            name=name,
            uuid=uuid,
            version=version,
            group=group,
            classifier=classifier,
            hashes=hashes,
            cpe=cpe,
            purl=purl,
            swid_tag_id=swid_tag_id,
            internal=internal,
            copyright_=copyright_,
            license_=license_,
            license_expression=license_expression,
            license_url=license_url,
            resolved_license=resolved_license,
            occurrence_count=occurrence_count,
            scope=scope,
            last_inherited_risk_score=last_inherited_risk_score,
            metrics=metrics,
            package_metadata=package_metadata,
            package_artifact_metadata=package_artifact_metadata,
        )

        list_project_components_response_item.additional_properties = d
        return list_project_components_response_item

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
