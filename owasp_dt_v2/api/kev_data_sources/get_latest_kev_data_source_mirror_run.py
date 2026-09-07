from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.kev_data_source_mirror_status import KevDataSourceMirrorStatus
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/kev-data-sources/{name}/mirror-runs/latest".format(
            name=quote(str(name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> KevDataSourceMirrorStatus | ProblemDetails:
    if response.status_code == 200:
        response_200 = KevDataSourceMirrorStatus.from_dict(response.json())

        return response_200

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
) -> Response[KevDataSourceMirrorStatus | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[KevDataSourceMirrorStatus | ProblemDetails]:
    """Get the latest KEV data source mirror run

     Returns the status of the most recent mirror run for a given
    KEV data source.

    Returns 404 if no mirror run is available
    (e.g. none has been triggered yet, or the most recent run
    is no longer retained), or if the data source is unknown.

    Requires permission `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_READ`.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KevDataSourceMirrorStatus | ProblemDetails]
    """

    kwargs = _get_kwargs(
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient | Client,
) -> KevDataSourceMirrorStatus | ProblemDetails | None:
    """Get the latest KEV data source mirror run

     Returns the status of the most recent mirror run for a given
    KEV data source.

    Returns 404 if no mirror run is available
    (e.g. none has been triggered yet, or the most recent run
    is no longer retained), or if the data source is unknown.

    Requires permission `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_READ`.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KevDataSourceMirrorStatus | ProblemDetails
    """

    return sync_detailed(
        name=name,
        client=client,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[KevDataSourceMirrorStatus | ProblemDetails]:
    """Get the latest KEV data source mirror run

     Returns the status of the most recent mirror run for a given
    KEV data source.

    Returns 404 if no mirror run is available
    (e.g. none has been triggered yet, or the most recent run
    is no longer retained), or if the data source is unknown.

    Requires permission `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_READ`.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KevDataSourceMirrorStatus | ProblemDetails]
    """

    kwargs = _get_kwargs(
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
) -> KevDataSourceMirrorStatus | ProblemDetails | None:
    """Get the latest KEV data source mirror run

     Returns the status of the most recent mirror run for a given
    KEV data source.

    Returns 404 if no mirror run is available
    (e.g. none has been triggered yet, or the most recent run
    is no longer retained), or if the data source is unknown.

    Requires permission `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_READ`.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KevDataSourceMirrorStatus | ProblemDetails
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
        )
    ).parsed
