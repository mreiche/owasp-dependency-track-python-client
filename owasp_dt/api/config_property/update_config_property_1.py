from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.config_property_response import ConfigPropertyResponse
from ...models.update_config_property_request import UpdateConfigPropertyRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UpdateConfigPropertyRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/configProperty",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ConfigPropertyResponse | None:
    if response.status_code == 200:
        response_200 = ConfigPropertyResponse.from_dict(response.json())

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
) -> Response[Any | ConfigPropertyResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateConfigPropertyRequest | Unset = UNSET,
) -> Response[Any | ConfigPropertyResponse]:
    """Updates a config property

     <p>Requires permission <strong>SYSTEM_CONFIGURATION</strong> or
    <strong>SYSTEM_CONFIGURATION_UPDATE</strong></p>

    Args:
        body (UpdateConfigPropertyRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConfigPropertyResponse]
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
    body: UpdateConfigPropertyRequest | Unset = UNSET,
) -> Any | ConfigPropertyResponse | None:
    """Updates a config property

     <p>Requires permission <strong>SYSTEM_CONFIGURATION</strong> or
    <strong>SYSTEM_CONFIGURATION_UPDATE</strong></p>

    Args:
        body (UpdateConfigPropertyRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConfigPropertyResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateConfigPropertyRequest | Unset = UNSET,
) -> Response[Any | ConfigPropertyResponse]:
    """Updates a config property

     <p>Requires permission <strong>SYSTEM_CONFIGURATION</strong> or
    <strong>SYSTEM_CONFIGURATION_UPDATE</strong></p>

    Args:
        body (UpdateConfigPropertyRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConfigPropertyResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UpdateConfigPropertyRequest | Unset = UNSET,
) -> Any | ConfigPropertyResponse | None:
    """Updates a config property

     <p>Requires permission <strong>SYSTEM_CONFIGURATION</strong> or
    <strong>SYSTEM_CONFIGURATION_UPDATE</strong></p>

    Args:
        body (UpdateConfigPropertyRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConfigPropertyResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
