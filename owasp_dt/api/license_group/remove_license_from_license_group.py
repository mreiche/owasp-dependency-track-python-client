from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.license_group import LicenseGroup
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    license_uuid: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/licenseGroup/{uuid}/license/{license_uuid}".format(
            uuid=uuid,
            license_uuid=license_uuid,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, LicenseGroup]]:
    if response.status_code == 200:
        response_200 = LicenseGroup.from_dict(response.json())

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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, LicenseGroup]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    license_uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, LicenseGroup]]:
    """Removes the license from the license group.

     <p>Requires permission <strong>POLICY_MANAGEMENT</strong></p>

    Args:
        uuid (UUID):
        license_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LicenseGroup]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        license_uuid=license_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    license_uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, LicenseGroup]]:
    """Removes the license from the license group.

     <p>Requires permission <strong>POLICY_MANAGEMENT</strong></p>

    Args:
        uuid (UUID):
        license_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LicenseGroup]
    """

    return sync_detailed(
        uuid=uuid,
        license_uuid=license_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    license_uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, LicenseGroup]]:
    """Removes the license from the license group.

     <p>Requires permission <strong>POLICY_MANAGEMENT</strong></p>

    Args:
        uuid (UUID):
        license_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LicenseGroup]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        license_uuid=license_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    license_uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, LicenseGroup]]:
    """Removes the license from the license group.

     <p>Requires permission <strong>POLICY_MANAGEMENT</strong></p>

    Args:
        uuid (UUID):
        license_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LicenseGroup]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            license_uuid=license_uuid,
            client=client,
        )
    ).parsed
