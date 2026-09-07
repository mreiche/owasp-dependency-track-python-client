from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user import User
from ...types import Response


def _get_kwargs(
    permission: str,
    username: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/permission/{permission}/user/{username}".format(
            permission=quote(str(permission), safe=""),
            username=quote(str(username), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | User | None:
    if response.status_code == 200:
        response_200 = User.from_dict(response.json())

        return response_200

    if response.status_code == 304:
        response_304 = cast(Any, None)
        return response_304

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
) -> Response[Any | User]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    permission: str,
    username: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | User]:
    """Removes the permission from the user.

     <p>Requires permission <strong>ACCESS_MANAGEMENT</strong> or
    <strong>ACCESS_MANAGEMENT_DELETE</strong></p>

    Args:
        permission (str):
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | User]
    """

    kwargs = _get_kwargs(
        permission=permission,
        username=username,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    permission: str,
    username: str,
    *,
    client: AuthenticatedClient,
) -> Any | User | None:
    """Removes the permission from the user.

     <p>Requires permission <strong>ACCESS_MANAGEMENT</strong> or
    <strong>ACCESS_MANAGEMENT_DELETE</strong></p>

    Args:
        permission (str):
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | User
    """

    return sync_detailed(
        permission=permission,
        username=username,
        client=client,
    ).parsed


async def asyncio_detailed(
    permission: str,
    username: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | User]:
    """Removes the permission from the user.

     <p>Requires permission <strong>ACCESS_MANAGEMENT</strong> or
    <strong>ACCESS_MANAGEMENT_DELETE</strong></p>

    Args:
        permission (str):
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | User]
    """

    kwargs = _get_kwargs(
        permission=permission,
        username=username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    permission: str,
    username: str,
    *,
    client: AuthenticatedClient,
) -> Any | User | None:
    """Removes the permission from the user.

     <p>Requires permission <strong>ACCESS_MANAGEMENT</strong> or
    <strong>ACCESS_MANAGEMENT_DELETE</strong></p>

    Args:
        permission (str):
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | User
    """

    return (
        await asyncio_detailed(
            permission=permission,
            username=username,
            client=client,
        )
    ).parsed
