from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.paginated_response import PaginatedResponse
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    extension_point_name: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/extension-points/{extension_point_name}/extensions".format(
            extension_point_name=quote(str(extension_point_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedResponse | ProblemDetails:
    if response.status_code == 200:
        response_200 = PaginatedResponse.from_dict(response.json())

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
) -> Response[PaginatedResponse | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    extension_point_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[PaginatedResponse | ProblemDetails]:
    """List all extensions

     Returns a list of extensions for a given extension point, sorted by name in ascending order.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_READ` permission.

    Args:
        extension_point_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        extension_point_name=extension_point_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    extension_point_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> PaginatedResponse | ProblemDetails | None:
    """List all extensions

     Returns a list of extensions for a given extension point, sorted by name in ascending order.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_READ` permission.

    Args:
        extension_point_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponse | ProblemDetails
    """

    return sync_detailed(
        extension_point_name=extension_point_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    extension_point_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[PaginatedResponse | ProblemDetails]:
    """List all extensions

     Returns a list of extensions for a given extension point, sorted by name in ascending order.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_READ` permission.

    Args:
        extension_point_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        extension_point_name=extension_point_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    extension_point_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> PaginatedResponse | ProblemDetails | None:
    """List all extensions

     Returns a list of extensions for a given extension point, sorted by name in ascending order.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_READ` permission.

    Args:
        extension_point_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponse | ProblemDetails
    """

    return (
        await asyncio_detailed(
            extension_point_name=extension_point_name,
            client=client,
        )
    ).parsed
