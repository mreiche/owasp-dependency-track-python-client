import owasp_dt
from owasp_dt.api.config_property import update_config_property
from owasp_dt.models import ConfigProperty, ConfigPropertyPropertyType


def test_trigger_vulnerabilities_update(client: owasp_dt.Client):
    config = ConfigProperty(
        group_name="task-scheduler",
        property_name="nist.mirror.cadence",
        property_value="1",
        property_type=ConfigPropertyPropertyType.NUMBER,
    )
    resp = update_config_property.sync_detailed(client=client, body=config)
    assert resp.status_code == 200
