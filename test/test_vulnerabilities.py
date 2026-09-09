import pytest

import owasp_dt
import test
from owasp_dt.api.metrics import get_vulnerability_metrics
from owasp_dt.api.vulnerability import get_all_vulnerabilities
from owasp_dt_v2.api.extensions import update_extension_config
from owasp_dt_v2.api.vuln_data_sources import trigger_vuln_data_source_mirror_run
from owasp_dt_v2.models import UpdateExtensionConfigRequest, UpdateExtensionConfigRequestConfig


def test_change_nvd_mirror(client_v2: owasp_dt.Client):
    config = {
        "enabled": True,
        "cveFeedsUrl": "https://nvd.reiche.world/feeds"
    }
    request_body = UpdateExtensionConfigRequest(config=UpdateExtensionConfigRequestConfig.from_dict(config))
    resp = update_extension_config.sync_detailed(
        client=client_v2,
        extension_point_name="vuln-data-source",
        extension_name="nvd",
        body=request_body
    )
    assert resp.status_code in [200, 304]

@pytest.mark.depends(on=['test_change_nvd_mirror'])
def test_trigger_mirror_nvd(client_v2: owasp_dt.Client):
    resp = trigger_vuln_data_source_mirror_run.sync_detailed(client=client_v2, name="nvd")
    assert resp.status_code in [202, 409]


@pytest.mark.depends(on=['test_trigger_mirror_nvd'])
def test_get_vulnerabilities(client: owasp_dt.Client):
    def _get_vulnerabilities():
        resp = get_all_vulnerabilities.sync_detailed(client=client, page_size=1)
        vulnerabilities = resp.parsed
        assert len(vulnerabilities) > 0
    test.retry(_get_vulnerabilities, 600)


@pytest.mark.depends(on=['test/test_upload.py::test_upload_first_sbom'])
@pytest.mark.xfail(reason="https://github.com/DependencyTrack/dependency-track/issues/5401")
def test_get_vulnerability_metrics(client: owasp_dt.Client):
    def _get_vulnerability_metrics():
        resp = get_vulnerability_metrics.sync_detailed(client=client)
        vulnerabilities = resp.parsed
        assert len(vulnerabilities) > 0

    test.retry(_get_vulnerability_metrics, 10)
