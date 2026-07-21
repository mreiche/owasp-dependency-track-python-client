from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cwe import Cwe
from ...types import Response


def _get_kwargs(
    cwe_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/cwe/{cwe_id}".format(
            cwe_id=quote(str(cwe_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Cwe | None:
    if response.status_code == 200:
        response_200 = Cwe.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Cwe]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cwe_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Cwe]:
    """Returns a specific CWE

    Args:
        cwe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Cwe]
    """

    kwargs = _get_kwargs(
        cwe_id=cwe_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cwe_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | Cwe | None:
    """Returns a specific CWE

    Args:
        cwe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Cwe
    """

    return sync_detailed(
        cwe_id=cwe_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    cwe_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Cwe]:
    """Returns a specific CWE

    Args:
        cwe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Cwe]
    """

    kwargs = _get_kwargs(
        cwe_id=cwe_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cwe_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | Cwe | None:
    """Returns a specific CWE

    Args:
        cwe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Cwe
    """

    return (
        await asyncio_detailed(
            cwe_id=cwe_id,
            client=client,
        )
    ).parsed
