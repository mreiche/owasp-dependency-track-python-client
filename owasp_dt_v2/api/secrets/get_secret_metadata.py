from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.secret_metadata import SecretMetadata
from ...types import Response


def _get_kwargs(
    name: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/secrets/{name}".format(
            name=quote(str(name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | SecretMetadata:
    if response.status_code == 200:
        response_200 = SecretMetadata.from_dict(response.json())

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
) -> Response[ProblemDetails | SecretMetadata]:
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
) -> Response[ProblemDetails | SecretMetadata]:
    """Get secret metadata

     Returns metadata about a given secret.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_READ` permission.

    Args:
        name (str):  Example: MY_SECRET.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | SecretMetadata]
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
) -> ProblemDetails | SecretMetadata | None:
    """Get secret metadata

     Returns metadata about a given secret.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_READ` permission.

    Args:
        name (str):  Example: MY_SECRET.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | SecretMetadata
    """

    return sync_detailed(
        name=name,
        client=client,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | SecretMetadata]:
    """Get secret metadata

     Returns metadata about a given secret.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_READ` permission.

    Args:
        name (str):  Example: MY_SECRET.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | SecretMetadata]
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
) -> ProblemDetails | SecretMetadata | None:
    """Get secret metadata

     Returns metadata about a given secret.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_READ` permission.

    Args:
        name (str):  Example: MY_SECRET.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | SecretMetadata
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
        )
    ).parsed
