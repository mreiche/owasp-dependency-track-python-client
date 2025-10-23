import math
import time
from pathlib import Path
from typing import Callable

from dotenv import load_dotenv

import owasp_dt
from owasp_dt import Client
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
            # "no_proxy": getenv("NO_PROXY", "")
        }
    )


def retry(callable: Callable, seconds: float, wait_time: float = 3):
    retries = math.ceil(seconds / wait_time)
    #start_date = datetime.now()
    exception = None
    ret = None
    for i in range(retries):
        try:
            exception = None
            ret = callable()
            break
        except Exception as e:
            exception = e
        time.sleep(wait_time)

    if exception:
        raise exception
        #raise Exception(f"{exception} after {datetime.now()-start_date}")

    return ret


def setup_module():
    assert load_dotenv(__base_dir / "test.env")


def teardown_module():
    pass
