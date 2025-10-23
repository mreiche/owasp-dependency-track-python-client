from typing import Generator, Callable, TypeVar

from owasp_dt import Client
from owasp_dt.api.project_property import create_property_1, update_property
from owasp_dt.models import ProjectProperty
from owasp_dt.types import Response
from test import config


def create_client_from_env() -> Client:
    base_url = config.reqenv("OWASP_DTRACK_URL")
    return Client(
        base_url=f"{base_url}/api",
        headers={
            "X-Api-Key": config.reqenv("OWASP_DTRACK_API_KEY")
        },
        verify_ssl=config.getenv("OWASP_DTRACK_VERIFY_SSL", "1", config.parse_true),
        raise_on_unexpected_status=False,
        httpx_args={
            "proxy": config.getenv("HTTPS_PROXY", lambda: config.getenv("HTTP_PROXY", None)),
            #"no_proxy": getenv("NO_PROXY", "")
        }
    )

def upsert_project_property(client: Client, uuid: str, property: ProjectProperty):
    resp = create_property_1.sync_detailed(client=client, uuid=uuid, body=property)
    if resp.status_code == 409:
        resp = update_property.sync_detailed(client=client, uuid=uuid, body=property)

    assert resp.status_code in [200, 201]

T = TypeVar('T')

def page_result(cb: Callable[[int], Response[list[T]]]) -> Generator[list[T]]:
    page_number = 0
    while True:
        page_number += 1
        resp = cb(page_number)
        assert resp.status_code == 200
        items = resp.parsed
        if len(items) == 0:
            break
        else:
            yield items
