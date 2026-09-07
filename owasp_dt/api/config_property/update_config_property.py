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
    body: list[UpdateConfigPropertyRequest] | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/configProperty/aggregate",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = []
        for body_item_data in body:
            body_item = body_item_data.to_dict()
            _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[ConfigPropertyResponse | str] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:

            def _parse_response_200_item(data: object) -> ConfigPropertyResponse | str:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_0 = ConfigPropertyResponse.from_dict(data)

                    return response_200_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(ConfigPropertyResponse | str, data)

            response_200_item = _parse_response_200_item(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | list[ConfigPropertyResponse | str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: list[UpdateConfigPropertyRequest] | Unset = UNSET,
) -> Response[Any | list[ConfigPropertyResponse | str]]:
    """Updates an array of config properties

     <p>Requires permission <strong>SYSTEM_CONFIGURATION</strong> or
    <strong>SYSTEM_CONFIGURATION_UPDATE</strong></p>

    Args:
        body (list[UpdateConfigPropertyRequest] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ConfigPropertyResponse | str]]
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
    body: list[UpdateConfigPropertyRequest] | Unset = UNSET,
) -> Any | list[ConfigPropertyResponse | str] | None:
    """Updates an array of config properties

     <p>Requires permission <strong>SYSTEM_CONFIGURATION</strong> or
    <strong>SYSTEM_CONFIGURATION_UPDATE</strong></p>

    Args:
        body (list[UpdateConfigPropertyRequest] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ConfigPropertyResponse | str]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: list[UpdateConfigPropertyRequest] | Unset = UNSET,
) -> Response[Any | list[ConfigPropertyResponse | str]]:
    """Updates an array of config properties

     <p>Requires permission <strong>SYSTEM_CONFIGURATION</strong> or
    <strong>SYSTEM_CONFIGURATION_UPDATE</strong></p>

    Args:
        body (list[UpdateConfigPropertyRequest] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ConfigPropertyResponse | str]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: list[UpdateConfigPropertyRequest] | Unset = UNSET,
) -> Any | list[ConfigPropertyResponse | str] | None:
    """Updates an array of config properties

     <p>Requires permission <strong>SYSTEM_CONFIGURATION</strong> or
    <strong>SYSTEM_CONFIGURATION_UPDATE</strong></p>

    Args:
        body (list[UpdateConfigPropertyRequest] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ConfigPropertyResponse | str]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
