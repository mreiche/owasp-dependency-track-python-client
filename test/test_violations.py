import pytest
from is_empty import empty

import owasp_dt
import test
from owasp_dt.api.license_ import get_license
from owasp_dt.api.policy import create_policy
from owasp_dt.api.policy_condition import create_policy_condition
from owasp_dt.api.violation import get_violations_by_project, get_violations
from owasp_dt.models import Policy, PolicyViolationState, PolicyCondition, PolicyConditionSubject, PolicyConditionOperator, License, PolicyOperator
from owasp_dt.types import UNSET


def assert_mit_license_uuid(client: owasp_dt.Client):
    if empty(test.mit_license_uuid):
        resp = get_license.sync_detailed(client=client, license_id="MIT")
        assert resp.status_code == 200
        license = resp.parsed
        assert isinstance(license, License)
        __mit_license_uuid = str(license.uuid)
    return test.mit_license_uuid


def test_create_test_policy(client: owasp_dt.Client):
    policy = Policy(
        uuid="",
        name="Forbid MIT license",
        violation_state=PolicyViolationState.FAIL,
        operator=PolicyOperator.ANY,
    )
    resp = create_policy.sync_detailed(client=client, body=policy)
    if resp.status_code == 409:
        return
    assert resp.status_code == 201
    policy = resp.parsed
    assert isinstance(policy, Policy)

    license_uuid = assert_mit_license_uuid(client)

    assert not empty(license_uuid), "MIT license not found"

    condition = PolicyCondition(
        uuid="",
        policy=UNSET,
        subject=PolicyConditionSubject.LICENSE,
        operator=PolicyConditionOperator.IS,
        value=license_uuid,
    )
    resp = create_policy_condition.sync_detailed(client=client, uuid=policy.uuid, body=condition)
    assert resp.status_code == 201


@pytest.mark.depends(on=['test_create_test_policy', 'test/test_upload.py::test_upload_sbom'])
def test_get_violations(client: owasp_dt.Client):
    def _get_violations():
        resp = get_violations.sync_detailed(client=client, page_size=1)
        violations = resp.parsed
        assert len(violations) > 0

    test.retry(_get_violations, 600)


@pytest.mark.depends(on=['test/test_projects.py::test_search_project_by_name', 'test/test_upload.py::test_get_scan_status'])
def test_get_project_violations(client: owasp_dt.Client):
    resp = get_violations_by_project.sync_detailed(client=client, uuid=test.project_uuid)
    violations = resp.parsed
