import math
import time
from pathlib import Path
from typing import Callable

from dotenv import load_dotenv

import owasp_dt
from owasp_dt import Client
from test import config

__base_dir = Path(__file__).parent

project_name = "test-api"
upload_token: str | None = None
project_uuid: str | None = None
mit_license_uuid: str | None = None

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
