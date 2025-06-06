from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.license_ import License
from ...types import Response


def _get_kwargs(
    license_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/license/{license_id}".format(
            license_id=license_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, License]]:
    if response.status_code == 200:
        response_200 = License.from_dict(response.json())

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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, License]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    license_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, License]]:
    """Returns a specific license

    Args:
        license_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, License]]
    """

    kwargs = _get_kwargs(
        license_id=license_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    license_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, License]]:
    """Returns a specific license

    Args:
        license_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, License]
    """

    return sync_detailed(
        license_id=license_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    license_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, License]]:
    """Returns a specific license

    Args:
        license_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, License]]
    """

    kwargs = _get_kwargs(
        license_id=license_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    license_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, License]]:
    """Returns a specific license

    Args:
        license_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, License]
    """

    return (
        await asyncio_detailed(
            license_id=license_id,
            client=client,
        )
    ).parsed
