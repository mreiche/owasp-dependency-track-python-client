from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.config_property_response import ConfigPropertyResponse
from ...types import Response


def _get_kwargs(
    group_name: str,
    property_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/configProperty/public/{group_name}/{property_name}".format(
            group_name=quote(str(group_name), safe=""),
            property_name=quote(str(property_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ConfigPropertyResponse | None:
    if response.status_code == 200:
        response_200 = ConfigPropertyResponse.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

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
    group_name: str,
    property_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ConfigPropertyResponse]:
    """Returns a public ConfigProperty

     <p></p>

    Args:
        group_name (str):
        property_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConfigPropertyResponse]
    """

    kwargs = _get_kwargs(
        group_name=group_name,
        property_name=property_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_name: str,
    property_name: str,
    *,
    client: AuthenticatedClient,
) -> Any | ConfigPropertyResponse | None:
    """Returns a public ConfigProperty

     <p></p>

    Args:
        group_name (str):
        property_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConfigPropertyResponse
    """

    return sync_detailed(
        group_name=group_name,
        property_name=property_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_name: str,
    property_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ConfigPropertyResponse]:
    """Returns a public ConfigProperty

     <p></p>

    Args:
        group_name (str):
        property_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConfigPropertyResponse]
    """

    kwargs = _get_kwargs(
        group_name=group_name,
        property_name=property_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_name: str,
    property_name: str,
    *,
    client: AuthenticatedClient,
) -> Any | ConfigPropertyResponse | None:
    """Returns a public ConfigProperty

     <p></p>

    Args:
        group_name (str):
        property_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConfigPropertyResponse
    """

    return (
        await asyncio_detailed(
            group_name=group_name,
            property_name=property_name,
            client=client,
        )
    ).parsed
