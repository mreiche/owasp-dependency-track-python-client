from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
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
            uuid=quote(str(uuid), safe=""),
            license_uuid=quote(str(license_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | LicenseGroup | None:
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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | LicenseGroup]:
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
) -> Response[Any | LicenseGroup]:
    """Removes the license from the license group.

     <p>Requires permission <strong>POLICY_MANAGEMENT</strong> or
    <strong>POLICY_MANAGEMENT_UPDATE</strong></p>

    Args:
        uuid (UUID):
        license_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LicenseGroup]
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
) -> Any | LicenseGroup | None:
    """Removes the license from the license group.

     <p>Requires permission <strong>POLICY_MANAGEMENT</strong> or
    <strong>POLICY_MANAGEMENT_UPDATE</strong></p>

    Args:
        uuid (UUID):
        license_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LicenseGroup
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
) -> Response[Any | LicenseGroup]:
    """Removes the license from the license group.

     <p>Requires permission <strong>POLICY_MANAGEMENT</strong> or
    <strong>POLICY_MANAGEMENT_UPDATE</strong></p>

    Args:
        uuid (UUID):
        license_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LicenseGroup]
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
) -> Any | LicenseGroup | None:
    """Removes the license from the license group.

     <p>Requires permission <strong>POLICY_MANAGEMENT</strong> or
    <strong>POLICY_MANAGEMENT_UPDATE</strong></p>

    Args:
        uuid (UUID):
        license_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LicenseGroup
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            license_uuid=license_uuid,
            client=client,
        )
    ).parsed
