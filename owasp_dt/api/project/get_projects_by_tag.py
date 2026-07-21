from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_projects_by_tag_sort_order import GetProjectsByTagSortOrder
from ...models.list_projects_response_item import ListProjectsResponseItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tag: str,
    *,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetProjectsByTagSortOrder | Unset = UNSET,
    exclude_inactive: bool | Unset = UNSET,
    only_root: bool | Unset = UNSET,
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

    params["excludeInactive"] = exclude_inactive

    params["onlyRoot"] = only_root

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/project/tag/{tag}".format(
            tag=quote(str(tag), safe=""),
        ),
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
    tag: str,
    *,
    client: AuthenticatedClient,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetProjectsByTagSortOrder | Unset = UNSET,
    exclude_inactive: bool | Unset = UNSET,
    only_root: bool | Unset = UNSET,
) -> Response[Any | list[ListProjectsResponseItem]]:
    """Returns a list of all projects by tag

     <p>Requires permission <strong>VIEW_PORTFOLIO</strong></p>

    Args:
        tag (str):
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetProjectsByTagSortOrder | Unset):
        exclude_inactive (bool | Unset):
        only_root (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ListProjectsResponseItem]]
    """

    kwargs = _get_kwargs(
        tag=tag,
        page_number=page_number,
        page_size=page_size,
        offset=offset,
        limit=limit,
        sort_name=sort_name,
        sort_order=sort_order,
        exclude_inactive=exclude_inactive,
        only_root=only_root,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tag: str,
    *,
    client: AuthenticatedClient,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetProjectsByTagSortOrder | Unset = UNSET,
    exclude_inactive: bool | Unset = UNSET,
    only_root: bool | Unset = UNSET,
) -> Any | list[ListProjectsResponseItem] | None:
    """Returns a list of all projects by tag

     <p>Requires permission <strong>VIEW_PORTFOLIO</strong></p>

    Args:
        tag (str):
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetProjectsByTagSortOrder | Unset):
        exclude_inactive (bool | Unset):
        only_root (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ListProjectsResponseItem]
    """

    return sync_detailed(
        tag=tag,
        client=client,
        page_number=page_number,
        page_size=page_size,
        offset=offset,
        limit=limit,
        sort_name=sort_name,
        sort_order=sort_order,
        exclude_inactive=exclude_inactive,
        only_root=only_root,
    ).parsed


async def asyncio_detailed(
    tag: str,
    *,
    client: AuthenticatedClient,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetProjectsByTagSortOrder | Unset = UNSET,
    exclude_inactive: bool | Unset = UNSET,
    only_root: bool | Unset = UNSET,
) -> Response[Any | list[ListProjectsResponseItem]]:
    """Returns a list of all projects by tag

     <p>Requires permission <strong>VIEW_PORTFOLIO</strong></p>

    Args:
        tag (str):
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetProjectsByTagSortOrder | Unset):
        exclude_inactive (bool | Unset):
        only_root (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ListProjectsResponseItem]]
    """

    kwargs = _get_kwargs(
        tag=tag,
        page_number=page_number,
        page_size=page_size,
        offset=offset,
        limit=limit,
        sort_name=sort_name,
        sort_order=sort_order,
        exclude_inactive=exclude_inactive,
        only_root=only_root,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tag: str,
    *,
    client: AuthenticatedClient,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetProjectsByTagSortOrder | Unset = UNSET,
    exclude_inactive: bool | Unset = UNSET,
    only_root: bool | Unset = UNSET,
) -> Any | list[ListProjectsResponseItem] | None:
    """Returns a list of all projects by tag

     <p>Requires permission <strong>VIEW_PORTFOLIO</strong></p>

    Args:
        tag (str):
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetProjectsByTagSortOrder | Unset):
        exclude_inactive (bool | Unset):
        only_root (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ListProjectsResponseItem]
    """

    return (
        await asyncio_detailed(
            tag=tag,
            client=client,
            page_number=page_number,
            page_size=page_size,
            offset=offset,
            limit=limit,
            sort_name=sort_name,
            sort_order=sort_order,
            exclude_inactive=exclude_inactive,
            only_root=only_root,
        )
    ).parsed
