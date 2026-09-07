from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_license_groups_sort_order import GetLicenseGroupsSortOrder
from ...models.license_group_response import LicenseGroupResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetLicenseGroupsSortOrder | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    params["offset"] = offset

    params["limit"] = limit

    params["sortName"] = sort_name

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/licenseGroup",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[LicenseGroupResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = LicenseGroupResponse.from_dict(response_200_item_data)

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
) -> Response[Any | list[LicenseGroupResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetLicenseGroupsSortOrder | Unset = UNSET,
) -> Response[Any | list[LicenseGroupResponse]]:
    """Returns a list of all license groups

     <p>Requires permission <strong>POLICY_MANAGEMENT</strong> or
    <strong>POLICY_MANAGEMENT_READ</strong></p>

    Args:
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetLicenseGroupsSortOrder | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[LicenseGroupResponse]]
    """

    kwargs = _get_kwargs(
        page_number=page_number,
        page_size=page_size,
        offset=offset,
        limit=limit,
        sort_name=sort_name,
        sort_order=sort_order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetLicenseGroupsSortOrder | Unset = UNSET,
) -> Any | list[LicenseGroupResponse] | None:
    """Returns a list of all license groups

     <p>Requires permission <strong>POLICY_MANAGEMENT</strong> or
    <strong>POLICY_MANAGEMENT_READ</strong></p>

    Args:
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetLicenseGroupsSortOrder | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[LicenseGroupResponse]
    """

    return sync_detailed(
        client=client,
        page_number=page_number,
        page_size=page_size,
        offset=offset,
        limit=limit,
        sort_name=sort_name,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetLicenseGroupsSortOrder | Unset = UNSET,
) -> Response[Any | list[LicenseGroupResponse]]:
    """Returns a list of all license groups

     <p>Requires permission <strong>POLICY_MANAGEMENT</strong> or
    <strong>POLICY_MANAGEMENT_READ</strong></p>

    Args:
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetLicenseGroupsSortOrder | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[LicenseGroupResponse]]
    """

    kwargs = _get_kwargs(
        page_number=page_number,
        page_size=page_size,
        offset=offset,
        limit=limit,
        sort_name=sort_name,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetLicenseGroupsSortOrder | Unset = UNSET,
) -> Any | list[LicenseGroupResponse] | None:
    """Returns a list of all license groups

     <p>Requires permission <strong>POLICY_MANAGEMENT</strong> or
    <strong>POLICY_MANAGEMENT_READ</strong></p>

    Args:
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetLicenseGroupsSortOrder | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[LicenseGroupResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            page_number=page_number,
            page_size=page_size,
            offset=offset,
            limit=limit,
            sort_name=sort_name,
            sort_order=sort_order,
        )
    ).parsed
