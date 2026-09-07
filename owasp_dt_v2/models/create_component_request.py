from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.classifier import Classifier
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hashes import Hashes
    from ..models.organizational_contact import OrganizationalContact
    from ..models.organizational_entity import OrganizationalEntity


T = TypeVar("T", bound="CreateComponentRequest")


@_attrs_define
class CreateComponentRequest:
    """
    Attributes:
        project_uuid (UUID):
        name (str):
        description (str | Unset):
        group (str | Unset):
        version (str | Unset):
        classifier (Classifier | Unset):
        filename (str | Unset):
        extension (str | Unset):
        hashes (Hashes | Unset):
        cpe (str | Unset):
        publisher (str | Unset):
        supplier (OrganizationalEntity | Unset):
        authors (list[OrganizationalContact] | Unset):
        purl (str | Unset):
        swid_tag_id (str | Unset):
        internal (bool | Unset):
        copyright_ (str | Unset):
        license_ (str | Unset):
        license_expression (str | Unset):
        license_url (str | Unset):
        notes (str | Unset):
    """

    project_uuid: UUID
    name: str
    description: str | Unset = UNSET
    group: str | Unset = UNSET
    version: str | Unset = UNSET
    classifier: Classifier | Unset = UNSET
    filename: str | Unset = UNSET
    extension: str | Unset = UNSET
    hashes: Hashes | Unset = UNSET
    cpe: str | Unset = UNSET
    publisher: str | Unset = UNSET
    supplier: OrganizationalEntity | Unset = UNSET
    authors: list[OrganizationalContact] | Unset = UNSET
    purl: str | Unset = UNSET
    swid_tag_id: str | Unset = UNSET
    internal: bool | Unset = UNSET
    copyright_: str | Unset = UNSET
    license_: str | Unset = UNSET
    license_expression: str | Unset = UNSET
    license_url: str | Unset = UNSET
    notes: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_uuid = str(self.project_uuid)

        name = self.name

        description = self.description

        group = self.group

        version = self.version

        classifier: str | Unset = UNSET
        if not isinstance(self.classifier, Unset):
            classifier = self.classifier.value

        filename = self.filename

        extension = self.extension

        hashes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hashes, Unset):
            hashes = self.hashes.to_dict()

        cpe = self.cpe

        publisher = self.publisher

        supplier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.supplier, Unset):
            supplier = self.supplier.to_dict()

        authors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.authors, Unset):
            authors = []
            for authors_item_data in self.authors:
                authors_item = authors_item_data.to_dict()
                authors.append(authors_item)

        purl = self.purl

        swid_tag_id = self.swid_tag_id

        internal = self.internal

        copyright_ = self.copyright_

        license_ = self.license_

        license_expression = self.license_expression

        license_url = self.license_url

        notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_uuid": project_uuid,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if group is not UNSET:
            field_dict["group"] = group
        if version is not UNSET:
            field_dict["version"] = version
        if classifier is not UNSET:
            field_dict["classifier"] = classifier
        if filename is not UNSET:
            field_dict["filename"] = filename
        if extension is not UNSET:
            field_dict["extension"] = extension
        if hashes is not UNSET:
            field_dict["hashes"] = hashes
        if cpe is not UNSET:
            field_dict["cpe"] = cpe
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if supplier is not UNSET:
            field_dict["supplier"] = supplier
        if authors is not UNSET:
            field_dict["authors"] = authors
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
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.hashes import Hashes
        from ..models.organizational_contact import (
            OrganizationalContact,
        )
        from ..models.organizational_entity import OrganizationalEntity

        d = dict(src_dict)
        project_uuid = UUID(d.pop("project_uuid"))

        name = d.pop("name")

        description = d.pop("description", UNSET)

        group = d.pop("group", UNSET)

        version = d.pop("version", UNSET)

        _classifier = d.pop("classifier", UNSET)
        classifier: Classifier | Unset
        if isinstance(_classifier, Unset):
            classifier = UNSET
        else:
            classifier = Classifier(_classifier)

        filename = d.pop("filename", UNSET)

        extension = d.pop("extension", UNSET)

        _hashes = d.pop("hashes", UNSET)
        hashes: Hashes | Unset
        if isinstance(_hashes, Unset):
            hashes = UNSET
        else:
            hashes = Hashes.from_dict(_hashes)

        cpe = d.pop("cpe", UNSET)

        publisher = d.pop("publisher", UNSET)

        _supplier = d.pop("supplier", UNSET)
        supplier: OrganizationalEntity | Unset
        if isinstance(_supplier, Unset):
            supplier = UNSET
        else:
            supplier = OrganizationalEntity.from_dict(_supplier)

        _authors = d.pop("authors", UNSET)
        authors: list[OrganizationalContact] | Unset = UNSET
        if _authors is not UNSET:
            authors = []
            for authors_item_data in _authors:
                authors_item = OrganizationalContact.from_dict(authors_item_data)

                authors.append(authors_item)

        purl = d.pop("purl", UNSET)

        swid_tag_id = d.pop("swid_tag_id", UNSET)

        internal = d.pop("internal", UNSET)

        copyright_ = d.pop("copyright", UNSET)

        license_ = d.pop("license", UNSET)

        license_expression = d.pop("license_expression", UNSET)

        license_url = d.pop("license_url", UNSET)

        notes = d.pop("notes", UNSET)

        create_component_request = cls(
            project_uuid=project_uuid,
            name=name,
            description=description,
            group=group,
            version=version,
            classifier=classifier,
            filename=filename,
            extension=extension,
            hashes=hashes,
            cpe=cpe,
            publisher=publisher,
            supplier=supplier,
            authors=authors,
            purl=purl,
            swid_tag_id=swid_tag_id,
            internal=internal,
            copyright_=copyright_,
            license_=license_,
            license_expression=license_expression,
            license_url=license_url,
            notes=notes,
        )

        create_component_request.additional_properties = d
        return create_component_request

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
