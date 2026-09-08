from time import sleep
from types import SimpleNamespace

import pytest

import test
from owasp_dt import Client
from owasp_dt.api.bom import upload_bom
from owasp_dt.api.event import is_token_being_processed_1
from owasp_dt.api.project import get_project_by_name_and_version
from owasp_dt.models import UploadBomBody, IsTokenBeingProcessedResponse
from owasp_dt.types import File
from owasp_dt_v2.api.projects import list_project_components

__test_project = SimpleNamespace(
    name="test-api",
    version="upload",
    uuid=None,
    upload_token=None,
)

#@pytest.mark.depends(on=['test/test_vulnerabilities.py::test_get_vulnerabilities'])
def test_upload_sbom(client: Client):
    with open(test.base_dir / "files/test.sbom.xml") as sbom_io:
        sbom_file = File(payload=sbom_io.read())
        resp = upload_bom.sync_detailed(client=client, body=UploadBomBody(
            project_name=__test_project.name,
            auto_create=True,
            project_version=__test_project.version,
            bom=sbom_file
        ))
        upload = resp.parsed
        assert upload is not None, "API call failed. Check client permissions."
        assert upload.token is not None
        __test_project.upload_token = upload.token


def assert_upload(client: Client, token_uuid: str):
    max_tries = 10
    i = 0
    for i in range(max_tries):
        resp = is_token_being_processed_1.sync_detailed(client=client, uuid=token_uuid)
        status = resp.parsed
        assert isinstance(status, IsTokenBeingProcessedResponse)
        if not status.processing:
            break
        sleep(1)

    assert i < max_tries, f"Scan not finished within {max_tries} seconds"

@pytest.mark.depends(on=['test_upload_sbom'])
def test_get_scan_status(client: Client):
    assert_upload(client, __test_project.upload_token)

@pytest.mark.depends(on=['test_get_scan_status'])
def test_get_project_uuid(client: Client):
    resp = get_project_by_name_and_version.sync_detailed(client=client, name=__test_project.name, version=__test_project.version)
    project = resp.parsed
    __test_project.uuid = project.uuid

@pytest.mark.depends(on=['test_get_project_uuid'])
def test_components_present(client_v2: Client):
    resp = list_project_components.sync_detailed(client=client_v2, uuid=__test_project.uuid)
    components_page = resp.parsed
    assert components_page.total.count == 39

@pytest.mark.depends(on=['test_components_present'])
def test_upload_other_sbom(client: Client):
    with open(test.base_dir / "files/other.sbom.json") as sbom_io:
        sbom_file = File(payload=sbom_io.read())
        resp = upload_bom.sync_detailed(client=client, body=UploadBomBody(
            project_name=__test_project.name,
            auto_create=True,
            project_version=__test_project.version,
            bom=sbom_file
        ))
        upload = resp.parsed
        assert upload is not None, "API call failed. Check client permissions."
        assert upload.token is not None

        assert_upload(client, upload.token)

@pytest.mark.depends(on=['test_upload_other_sbom'])
def test_other_components_present(client_v2: Client):
    resp = list_project_components.sync_detailed(client=client_v2, uuid=__test_project.uuid)
    components_page = resp.parsed
    assert components_page.total.count == 57
