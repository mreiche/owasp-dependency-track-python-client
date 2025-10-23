import pytest

import owasp_dt
import test
from owasp_dt.api.metrics import get_vulnerability_metrics
from owasp_dt.api.vulnerability import get_all_vulnerabilities


@pytest.mark.depends(on=['test/test_config.py::test_trigger_vulnerabilities_update'])
def test_get_vulnerabilities(client: owasp_dt.Client):
    def _get_vulnerabilities():
        resp = get_all_vulnerabilities.sync_detailed(client=client, page_size=1)
        vulnerabilities = resp.parsed
        assert len(vulnerabilities) > 0

    test.retry(_get_vulnerabilities, 10)


@pytest.mark.depends(on=["test_get_vulnerabilities", 'test/test_upload.py::test_upload_sbom'])
@pytest.mark.xfail(reason="https://github.com/DependencyTrack/dependency-track/issues/5401")
def test_get_vulnerability_metrics(client: owasp_dt.Client):
    def _get_vulnerability_metrics():
        resp = get_vulnerability_metrics.sync_detailed(client=client)
        vulnerabilities = resp.parsed
        assert len(vulnerabilities) > 0

    test.retry(_get_vulnerability_metrics, 10)
