from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.concise_project import ConciseProject
from ...models.get_projects_concise_sort_order import GetProjectsConciseSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetProjectsConciseSortOrder | Unset = UNSET,
    name: str | Unset = UNSET,
    version: str | Unset = UNSET,
    classifier: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    team: str | Unset = UNSET,
    active: bool | Unset = UNSET,
    only_root: bool | Unset = UNSET,
    include_metrics: bool | Unset = UNSET,
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

    params["version"] = version

    params["classifier"] = classifier

    params["tag"] = tag

    params["team"] = team

    params["active"] = active

    params["onlyRoot"] = only_root

    params["includeMetrics"] = include_metrics

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/project/concise",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[ConciseProject] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ConciseProject.from_dict(response_200_item_data)

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
) -> Response[Any | list[ConciseProject]]:
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
    sort_order: GetProjectsConciseSortOrder | Unset = UNSET,
    name: str | Unset = UNSET,
    version: str | Unset = UNSET,
    classifier: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    team: str | Unset = UNSET,
    active: bool | Unset = UNSET,
    only_root: bool | Unset = UNSET,
    include_metrics: bool | Unset = UNSET,
) -> Response[Any | list[ConciseProject]]:
    """Returns a list of all projects, in a concise representation.

     <p>Requires permission <strong>VIEW_PORTFOLIO</strong></p>

    Args:
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetProjectsConciseSortOrder | Unset):
        name (str | Unset):
        version (str | Unset):
        classifier (str | Unset):
        tag (str | Unset):
        team (str | Unset):
        active (bool | Unset):
        only_root (bool | Unset):
        include_metrics (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ConciseProject]]
    """

    kwargs = _get_kwargs(
        page_number=page_number,
        page_size=page_size,
        offset=offset,
        limit=limit,
        sort_name=sort_name,
        sort_order=sort_order,
        name=name,
        version=version,
        classifier=classifier,
        tag=tag,
        team=team,
        active=active,
        only_root=only_root,
        include_metrics=include_metrics,
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
    sort_order: GetProjectsConciseSortOrder | Unset = UNSET,
    name: str | Unset = UNSET,
    version: str | Unset = UNSET,
    classifier: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    team: str | Unset = UNSET,
    active: bool | Unset = UNSET,
    only_root: bool | Unset = UNSET,
    include_metrics: bool | Unset = UNSET,
) -> Any | list[ConciseProject] | None:
    """Returns a list of all projects, in a concise representation.

     <p>Requires permission <strong>VIEW_PORTFOLIO</strong></p>

    Args:
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetProjectsConciseSortOrder | Unset):
        name (str | Unset):
        version (str | Unset):
        classifier (str | Unset):
        tag (str | Unset):
        team (str | Unset):
        active (bool | Unset):
        only_root (bool | Unset):
        include_metrics (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ConciseProject]
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
        version=version,
        classifier=classifier,
        tag=tag,
        team=team,
        active=active,
        only_root=only_root,
        include_metrics=include_metrics,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetProjectsConciseSortOrder | Unset = UNSET,
    name: str | Unset = UNSET,
    version: str | Unset = UNSET,
    classifier: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    team: str | Unset = UNSET,
    active: bool | Unset = UNSET,
    only_root: bool | Unset = UNSET,
    include_metrics: bool | Unset = UNSET,
) -> Response[Any | list[ConciseProject]]:
    """Returns a list of all projects, in a concise representation.

     <p>Requires permission <strong>VIEW_PORTFOLIO</strong></p>

    Args:
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetProjectsConciseSortOrder | Unset):
        name (str | Unset):
        version (str | Unset):
        classifier (str | Unset):
        tag (str | Unset):
        team (str | Unset):
        active (bool | Unset):
        only_root (bool | Unset):
        include_metrics (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ConciseProject]]
    """

    kwargs = _get_kwargs(
        page_number=page_number,
        page_size=page_size,
        offset=offset,
        limit=limit,
        sort_name=sort_name,
        sort_order=sort_order,
        name=name,
        version=version,
        classifier=classifier,
        tag=tag,
        team=team,
        active=active,
        only_root=only_root,
        include_metrics=include_metrics,
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
    sort_order: GetProjectsConciseSortOrder | Unset = UNSET,
    name: str | Unset = UNSET,
    version: str | Unset = UNSET,
    classifier: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    team: str | Unset = UNSET,
    active: bool | Unset = UNSET,
    only_root: bool | Unset = UNSET,
    include_metrics: bool | Unset = UNSET,
) -> Any | list[ConciseProject] | None:
    """Returns a list of all projects, in a concise representation.

     <p>Requires permission <strong>VIEW_PORTFOLIO</strong></p>

    Args:
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetProjectsConciseSortOrder | Unset):
        name (str | Unset):
        version (str | Unset):
        classifier (str | Unset):
        tag (str | Unset):
        team (str | Unset):
        active (bool | Unset):
        only_root (bool | Unset):
        include_metrics (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ConciseProject]
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
            version=version,
            classifier=classifier,
            tag=tag,
            team=team,
            active=active,
            only_root=only_root,
            include_metrics=include_metrics,
        )
    ).parsed
