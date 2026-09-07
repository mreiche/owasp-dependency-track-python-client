from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.repository_response import RepositoryResponse
from ...models.update_repository_request import UpdateRepositoryRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UpdateRepositoryRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/repository",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RepositoryResponse | None:
    if response.status_code == 200:
        response_200 = RepositoryResponse.from_dict(response.json())

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
) -> Response[Any | RepositoryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateRepositoryRequest | Unset = UNSET,
) -> Response[Any | RepositoryResponse]:
    """Updates a repository

     <p>Requires permission <strong>SYSTEM_CONFIGURATION</strong> or
    <strong>SYSTEM_CONFIGURATION_UPDATE</strong></p>

    Args:
        body (UpdateRepositoryRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RepositoryResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: UpdateRepositoryRequest | Unset = UNSET,
) -> Any | RepositoryResponse | None:
    """Updates a repository

     <p>Requires permission <strong>SYSTEM_CONFIGURATION</strong> or
    <strong>SYSTEM_CONFIGURATION_UPDATE</strong></p>

    Args:
        body (UpdateRepositoryRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RepositoryResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateRepositoryRequest | Unset = UNSET,
) -> Response[Any | RepositoryResponse]:
    """Updates a repository

     <p>Requires permission <strong>SYSTEM_CONFIGURATION</strong> or
    <strong>SYSTEM_CONFIGURATION_UPDATE</strong></p>

    Args:
        body (UpdateRepositoryRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RepositoryResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UpdateRepositoryRequest | Unset = UNSET,
) -> Any | RepositoryResponse | None:
    """Updates a repository

     <p>Requires permission <strong>SYSTEM_CONFIGURATION</strong> or
    <strong>SYSTEM_CONFIGURATION_UPDATE</strong></p>

    Args:
        body (UpdateRepositoryRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RepositoryResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
