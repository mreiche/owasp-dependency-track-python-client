[![Code Coverage Status](https://codecov.io/github/mreiche/owasp-dependency-track-python-client/branch/main/graph/badge.svg)](https://app.codecov.io/github/mreiche/owasp-dependency-track-python-client)
[![Test](https://github.com/mreiche/owasp-dependency-track-python-client/actions/workflows/test.yml/badge.svg)](https://github.com/mreiche/owasp-dependency-track-python-client/actions/workflows/test.yml)
[![PyPI version](https://badge.fury.io/py/owasp-dependency-track-client.svg)](https://badge.fury.io/py/owasp-dependency-track-client)

# OWASP Dependency Track Python API client

This is a generated library based on the official OWASP Dependency Track OpenAPI spec using [openapi-python-client](https://github.com/openapi-generators/openapi-python-client) including some sanity patches.

## Usage

```shell
pip install owasp-dependency-track-client
```

Create the client
```python
from owasp_dt import Client

client = Client(
    base_url="http://localhost:8080/api",
    # base_url="http://localhost:8080/api/v2",  # For v2 API
    headers={
        "X-Api-Key": "YOUR API KEY"
    },
    verify_ssl=False,
)
```

Call endpoints:
```python
from owasp_dt.api.project import get_projects

projects = get_projects.sync(client=client)
assert len(projects) > 0
```

## OWASP Dependency Track CLI

Looking for a CLI? Check out https://github.com/mreiche/owasp-dependency-track-cli

## Development

### Update the library

1. Install the requirements: `pip install -e ".[test]` or `uv sync --extra test`
2. Start an OWASP DT instance locally (see [Start the test environment](#start-the-test-environment)): https://docs.dependencytrack.org/getting-started/deploy-docker/
3. Run `regenerate-api-client.sh`
4. Check if bugs are still in effect
   - https://github.com/openapi-generators/openapi-python-client/issues/1256
   - https://github.com/DependencyTrack/dependency-track/issues/2590
5. Publish this library with the API version tag

### Start the test environment

```shell
cd test
podman|docker compose up
```

- Preconfigured user: `admin:admin2`
- Preconfigured API key: see `test/test.env`

### Clean database init

- Prepare `test/docker-compose.yml`
```yaml
init-keys:
  volumes:
    # Comment out init dir
    # - './init:/init:ro'

apiserver:
  environment:
    # Comment in proxy env variables
    HTTP_PROXY: "http://localhost"
    HTTPS_PROXY: "http://localhost"

postgres:
  volumes:
    # Comment out init.sql
    # - "./init/init.sql:/docker-entrypoint-initdb.d/init.sql"
```

- Delete the volumes first
   ```shell
   podman volume rm test_postgres-data
   podman volume rm test_apiserver-data
   ```
- Start the stack
- Perform login and change password to `admin2`
- Create an *Administrators* API key and update `test/test.env`

- Dump the data
  ```shell
  podman exec test_postgres_1 bash -c "pg_dump -U \$POSTGRES_USER -d \$POSTGRES_DB > /tmp/init.sql"
  podman cp test_postgres_1:/tmp/init.sql "$(pwd)/test/init/init.sql"
  ```

- Remove all data from tables
  - `dex_workflow_run`
  - `dex_workflow_history*`
  

- Save the KEK key
  ```shell
  podman cp test_apiserver_1:/data/.dependency-track/keys/secret-management-kek.json "$(pwd)/test/init/secret-management-kek.json"
  ```
- Revert changes in `test/docker-compose.yml`
- Restart the stack