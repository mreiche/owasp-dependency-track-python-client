from time import sleep

import pytest

import owasp_dt
import test
from owasp_dt.api.bom import upload_bom
from owasp_dt.api.event import is_token_being_processed_1
from owasp_dt.models import UploadBomBody, IsTokenBeingProcessedResponse
from owasp_dt.types import File

@pytest.mark.depends(on=['test/test_vulnerabilities.py::test_get_vulnerabilities'])
def test_upload_sbom(client: owasp_dt.Client):
    with open(test.base_dir / "files/test.sbom.xml") as sbom_io:
        sbom_file = File(payload=sbom_io.read())
        resp = upload_bom.sync_detailed(client=client, body=UploadBomBody(
            project_name=test.project_name,
            auto_create=True,
            bom=sbom_file
        ))
        upload = resp.parsed
        assert upload is not None, "API call failed. Check client permissions."
        assert upload.token is not None
        test.upload_token = upload.token


@pytest.mark.depends(on=['test_upload_sbom'])
def test_get_scan_status(client: owasp_dt.Client):
    max_tries = 10
    i = 0
    for i in range(max_tries):
        resp = is_token_being_processed_1.sync_detailed(client=client, uuid=test.upload_token)
        status = resp.parsed
        assert isinstance(status, IsTokenBeingProcessedResponse)
        if not status.processing:
            break
        sleep(1)

    assert i < max_tries, f"Scan not finished within {max_tries} seconds"
