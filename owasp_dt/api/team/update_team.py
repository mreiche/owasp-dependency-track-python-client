from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.team import Team
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Team | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/team",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Team | None:
    if response.status_code == 200:
        response_200 = Team.from_dict(response.json())

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
) -> Response[Any | Team]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Team | Unset = UNSET,
) -> Response[Any | Team]:
    """Updates a team's fields

     <p>Requires permission <strong>ACCESS_MANAGEMENT</strong> or
    <strong>ACCESS_MANAGEMENT_UPDATE</strong></p>

    Args:
        body (Team | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Team]
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
    body: Team | Unset = UNSET,
) -> Any | Team | None:
    """Updates a team's fields

     <p>Requires permission <strong>ACCESS_MANAGEMENT</strong> or
    <strong>ACCESS_MANAGEMENT_UPDATE</strong></p>

    Args:
        body (Team | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Team
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Team | Unset = UNSET,
) -> Response[Any | Team]:
    """Updates a team's fields

     <p>Requires permission <strong>ACCESS_MANAGEMENT</strong> or
    <strong>ACCESS_MANAGEMENT_UPDATE</strong></p>

    Args:
        body (Team | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Team]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Team | Unset = UNSET,
) -> Any | Team | None:
    """Updates a team's fields

     <p>Requires permission <strong>ACCESS_MANAGEMENT</strong> or
    <strong>ACCESS_MANAGEMENT_UPDATE</strong></p>

    Args:
        body (Team | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Team
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
