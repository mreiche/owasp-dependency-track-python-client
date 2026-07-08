from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.license_group import LicenseGroup
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: LicenseGroup | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/licenseGroup",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | LicenseGroup | None:
    if response.status_code == 200:
        response_200 = LicenseGroup.from_dict(response.json())

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
) -> Response[Any | LicenseGroup]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: LicenseGroup | Unset = UNSET,
) -> Response[Any | LicenseGroup]:
    """Updates a license group

     <p>Requires permission <strong>POLICY_MANAGEMENT</strong> or
    <strong>POLICY_MANAGEMENT_UPDATE</strong></p>

    Args:
        body (LicenseGroup | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LicenseGroup]
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
    body: LicenseGroup | Unset = UNSET,
) -> Any | LicenseGroup | None:
    """Updates a license group

     <p>Requires permission <strong>POLICY_MANAGEMENT</strong> or
    <strong>POLICY_MANAGEMENT_UPDATE</strong></p>

    Args:
        body (LicenseGroup | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LicenseGroup
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: LicenseGroup | Unset = UNSET,
) -> Response[Any | LicenseGroup]:
    """Updates a license group

     <p>Requires permission <strong>POLICY_MANAGEMENT</strong> or
    <strong>POLICY_MANAGEMENT_UPDATE</strong></p>

    Args:
        body (LicenseGroup | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LicenseGroup]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: LicenseGroup | Unset = UNSET,
) -> Any | LicenseGroup | None:
    """Updates a license group

     <p>Requires permission <strong>POLICY_MANAGEMENT</strong> or
    <strong>POLICY_MANAGEMENT_UPDATE</strong></p>

    Args:
        body (LicenseGroup | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LicenseGroup
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
