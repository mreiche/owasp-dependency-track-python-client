from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.test_extension_request import TestExtensionRequest
from ...models.test_extension_response import TestExtensionResponse
from ...types import Response


def _get_kwargs(
    extension_point_name: str,
    extension_name: str,
    *,
    body: TestExtensionRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/extension-points/{extension_point_name}/extensions/{extension_name}/test".format(
            extension_point_name=quote(str(extension_point_name), safe=""),
            extension_name=quote(str(extension_name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | TestExtensionResponse:
    if response.status_code == 200:
        response_200 = TestExtensionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:

        def _parse_response_400(data: object) -> ProblemDetails:
            if not isinstance(data, dict):
                raise TypeError()
            response_400_type_0 = ProblemDetails.from_dict(data)

            return response_400_type_0

        response_400 = _parse_response_400(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProblemDetails.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404

    response_default = ProblemDetails.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProblemDetails | TestExtensionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    extension_point_name: str,
    extension_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: TestExtensionRequest,
) -> Response[ProblemDetails | TestExtensionResponse]:
    """Test extension

     Tests an extension.

    If the extension is configurable (i.e. `/config-schema` returns status `200`),
    a valid configuration **must** be provided in the test request.
    The configuration is validated against the applicable JSON schema.

    **Do not use clear text credentials in the supplied config**.
    Fields annotated with `x-secret-ref` in the config schema expect
    a name of a managed secret, which is resolved internally by the API.

    Test results contain one or more checks, each of which can have a status of
    `PASSED`, `FAILED`, or `SKIPPED`. If *at least one* check is `FAILED`,
    the entire test should be considered `FAILED`.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_UPDATE` permission.

    Args:
        extension_point_name (str):
        extension_name (str):
        body (TestExtensionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | TestExtensionResponse]
    """

    kwargs = _get_kwargs(
        extension_point_name=extension_point_name,
        extension_name=extension_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    extension_point_name: str,
    extension_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: TestExtensionRequest,
) -> ProblemDetails | TestExtensionResponse | None:
    """Test extension

     Tests an extension.

    If the extension is configurable (i.e. `/config-schema` returns status `200`),
    a valid configuration **must** be provided in the test request.
    The configuration is validated against the applicable JSON schema.

    **Do not use clear text credentials in the supplied config**.
    Fields annotated with `x-secret-ref` in the config schema expect
    a name of a managed secret, which is resolved internally by the API.

    Test results contain one or more checks, each of which can have a status of
    `PASSED`, `FAILED`, or `SKIPPED`. If *at least one* check is `FAILED`,
    the entire test should be considered `FAILED`.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_UPDATE` permission.

    Args:
        extension_point_name (str):
        extension_name (str):
        body (TestExtensionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | TestExtensionResponse
    """

    return sync_detailed(
        extension_point_name=extension_point_name,
        extension_name=extension_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    extension_point_name: str,
    extension_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: TestExtensionRequest,
) -> Response[ProblemDetails | TestExtensionResponse]:
    """Test extension

     Tests an extension.

    If the extension is configurable (i.e. `/config-schema` returns status `200`),
    a valid configuration **must** be provided in the test request.
    The configuration is validated against the applicable JSON schema.

    **Do not use clear text credentials in the supplied config**.
    Fields annotated with `x-secret-ref` in the config schema expect
    a name of a managed secret, which is resolved internally by the API.

    Test results contain one or more checks, each of which can have a status of
    `PASSED`, `FAILED`, or `SKIPPED`. If *at least one* check is `FAILED`,
    the entire test should be considered `FAILED`.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_UPDATE` permission.

    Args:
        extension_point_name (str):
        extension_name (str):
        body (TestExtensionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | TestExtensionResponse]
    """

    kwargs = _get_kwargs(
        extension_point_name=extension_point_name,
        extension_name=extension_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    extension_point_name: str,
    extension_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: TestExtensionRequest,
) -> ProblemDetails | TestExtensionResponse | None:
    """Test extension

     Tests an extension.

    If the extension is configurable (i.e. `/config-schema` returns status `200`),
    a valid configuration **must** be provided in the test request.
    The configuration is validated against the applicable JSON schema.

    **Do not use clear text credentials in the supplied config**.
    Fields annotated with `x-secret-ref` in the config schema expect
    a name of a managed secret, which is resolved internally by the API.

    Test results contain one or more checks, each of which can have a status of
    `PASSED`, `FAILED`, or `SKIPPED`. If *at least one* check is `FAILED`,
    the entire test should be considered `FAILED`.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_UPDATE` permission.

    Args:
        extension_point_name (str):
        extension_name (str):
        body (TestExtensionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | TestExtensionResponse
    """

    return (
        await asyncio_detailed(
            extension_point_name=extension_point_name,
            extension_name=extension_name,
            client=client,
            body=body,
        )
    ).parsed
