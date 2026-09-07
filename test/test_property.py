import pytest
from tinystream import Stream

import owasp_dt
import test
from owasp_dt.api.project_property import get_properties_1
from owasp_dt.models import ProjectPropertyResponse, CreateProjectPropertyRequest, CreateProjectPropertyRequestPropertyType
from test import api


@pytest.mark.depends(on=['test/test_projects.py::test_search_project_by_name'])
def test_upsert_project_property(client: owasp_dt.Client):
    property = CreateProjectPropertyRequest(
        group_name="owasp-dtrack-python-client",
        property_name="test",
        property_type=CreateProjectPropertyRequestPropertyType.STRING,
        property_value="set",
        description="Custom property test"
    )
    #test.project_uuid = 'e8558bee-1cea-4a39-83fa-c265f124479b'
    api.upsert_project_property(client=client, uuid=test.project_uuid, property=property)

    def _filter_property(property:ProjectPropertyResponse):
        return property.group_name == "owasp-dtrack-python-client" and property.property_name == "test"

    resp = get_properties_1.sync_detailed(client=client, uuid=test.project_uuid)
    properties = resp.parsed
    opt_property = Stream(properties).find(_filter_property)
    assert opt_property.present
    assert opt_property.get().property_value == "set"

    property.property_value = "new_value"
    api.upsert_project_property(client=client, uuid=test.project_uuid, property=property)
    resp = get_properties_1.sync_detailed(client=client, uuid=test.project_uuid)
    properties = resp.parsed
    opt_property = Stream(properties).find(_filter_property)
    assert opt_property.present
    assert opt_property.get().property_value == "new_value"
