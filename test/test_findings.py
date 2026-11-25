import pytest

import owasp_dt
import test
from owasp_dt.api.finding import get_all_findings
from owasp_dt.models import Finding, GetAllFindingsTotalCount
from owasp_dt.types import Unset


@pytest.mark.depends(on=['test/test_upload.py::test_upload_first_sbom'])
def test_get_findings(client: owasp_dt.Client):
    def _get_findings():
        resp = get_all_findings.sync_detailed(
            client=client,
            show_inactive=False,
            total_count=GetAllFindingsTotalCount.BOUNDED,
            page_size=10,
            page_number=1
        )
        findings = resp.parsed
        assert len(findings) > 0
        assert_finding_model(findings[0])
    test.retry(_get_findings, 600)

def assert_finding_model(finding: Finding):
    assert isinstance(finding.vulnerability.cvss_v2_base_score, Unset) or finding.vulnerability.cvss_v2_base_score > 0
    assert isinstance(finding.vulnerability.cvss_v3_base_score, Unset) or finding.vulnerability.cvss_v3_base_score > 0
    assert isinstance(finding.vulnerability.cvss_v4_score, Unset) or finding.vulnerability.cvss_v4_score > 0
