from pathlib import Path

from dotenv import load_dotenv
from owasp_dt import Client
import owasp_dt
from test import config
__base_dir = Path(__file__).parent

test_project_name = "test-api"

def create_client_from_env() -> owasp_dt.Client:
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

def setup_module():
    assert load_dotenv(__base_dir / "test.env")

def teardown_module():
    pass
