from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_projects_sort_order import GetProjectsSortOrder
from ...models.list_projects_response_item import ListProjectsResponseItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetProjectsSortOrder | Unset = UNSET,
    name: str | Unset = UNSET,
    exclude_inactive: bool | Unset = UNSET,
    only_root: bool | Unset = UNSET,
    not_assigned_to_team_with_uuid: UUID | Unset = UNSET,
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

    params["name"] = name

    params["excludeInactive"] = exclude_inactive

    params["onlyRoot"] = only_root

    json_not_assigned_to_team_with_uuid: str | Unset = UNSET
    if not isinstance(not_assigned_to_team_with_uuid, Unset):
        json_not_assigned_to_team_with_uuid = str(not_assigned_to_team_with_uuid)
    params["notAssignedToTeamWithUuid"] = json_not_assigned_to_team_with_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/project",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[ListProjectsResponseItem] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ListProjectsResponseItem.from_dict(
                response_200_item_data
            )

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
) -> Response[Any | list[ListProjectsResponseItem]]:
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
    sort_order: GetProjectsSortOrder | Unset = UNSET,
    name: str | Unset = UNSET,
    exclude_inactive: bool | Unset = UNSET,
    only_root: bool | Unset = UNSET,
    not_assigned_to_team_with_uuid: UUID | Unset = UNSET,
) -> Response[Any | list[ListProjectsResponseItem]]:
    """Returns a list of all projects

     <p>Requires permission <strong>VIEW_PORTFOLIO</strong></p>

    Args:
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetProjectsSortOrder | Unset):
        name (str | Unset):
        exclude_inactive (bool | Unset):
        only_root (bool | Unset):
        not_assigned_to_team_with_uuid (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ListProjectsResponseItem]]
    """

    kwargs = _get_kwargs(
        page_number=page_number,
        page_size=page_size,
        offset=offset,
        limit=limit,
        sort_name=sort_name,
        sort_order=sort_order,
        name=name,
        exclude_inactive=exclude_inactive,
        only_root=only_root,
        not_assigned_to_team_with_uuid=not_assigned_to_team_with_uuid,
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
    sort_order: GetProjectsSortOrder | Unset = UNSET,
    name: str | Unset = UNSET,
    exclude_inactive: bool | Unset = UNSET,
    only_root: bool | Unset = UNSET,
    not_assigned_to_team_with_uuid: UUID | Unset = UNSET,
) -> Any | list[ListProjectsResponseItem] | None:
    """Returns a list of all projects

     <p>Requires permission <strong>VIEW_PORTFOLIO</strong></p>

    Args:
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetProjectsSortOrder | Unset):
        name (str | Unset):
        exclude_inactive (bool | Unset):
        only_root (bool | Unset):
        not_assigned_to_team_with_uuid (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ListProjectsResponseItem]
    """

    return sync_detailed(
        client=client,
        page_number=page_number,
        page_size=page_size,
        offset=offset,
        limit=limit,
        sort_name=sort_name,
        sort_order=sort_order,
        name=name,
        exclude_inactive=exclude_inactive,
        only_root=only_root,
        not_assigned_to_team_with_uuid=not_assigned_to_team_with_uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetProjectsSortOrder | Unset = UNSET,
    name: str | Unset = UNSET,
    exclude_inactive: bool | Unset = UNSET,
    only_root: bool | Unset = UNSET,
    not_assigned_to_team_with_uuid: UUID | Unset = UNSET,
) -> Response[Any | list[ListProjectsResponseItem]]:
    """Returns a list of all projects

     <p>Requires permission <strong>VIEW_PORTFOLIO</strong></p>

    Args:
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetProjectsSortOrder | Unset):
        name (str | Unset):
        exclude_inactive (bool | Unset):
        only_root (bool | Unset):
        not_assigned_to_team_with_uuid (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ListProjectsResponseItem]]
    """

    kwargs = _get_kwargs(
        page_number=page_number,
        page_size=page_size,
        offset=offset,
        limit=limit,
        sort_name=sort_name,
        sort_order=sort_order,
        name=name,
        exclude_inactive=exclude_inactive,
        only_root=only_root,
        not_assigned_to_team_with_uuid=not_assigned_to_team_with_uuid,
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
    sort_order: GetProjectsSortOrder | Unset = UNSET,
    name: str | Unset = UNSET,
    exclude_inactive: bool | Unset = UNSET,
    only_root: bool | Unset = UNSET,
    not_assigned_to_team_with_uuid: UUID | Unset = UNSET,
) -> Any | list[ListProjectsResponseItem] | None:
    """Returns a list of all projects

     <p>Requires permission <strong>VIEW_PORTFOLIO</strong></p>

    Args:
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetProjectsSortOrder | Unset):
        name (str | Unset):
        exclude_inactive (bool | Unset):
        only_root (bool | Unset):
        not_assigned_to_team_with_uuid (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ListProjectsResponseItem]
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
            name=name,
            exclude_inactive=exclude_inactive,
            only_root=only_root,
            not_assigned_to_team_with_uuid=not_assigned_to_team_with_uuid,
        )
    ).parsed
