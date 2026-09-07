from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.component import Component
from ...models.get_component_by_identity_sort_order import (
    GetComponentByIdentitySortOrder,
)
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetComponentByIdentitySortOrder | Unset = UNSET,
    group: str | Unset = UNSET,
    name: str | Unset = UNSET,
    version: str | Unset = UNSET,
    purl: str | Unset = UNSET,
    cpe: str | Unset = UNSET,
    swid_tag_id: str | Unset = UNSET,
    project: UUID | Unset = UNSET,
    exclude_inactive_projects: bool | Unset = UNSET,
    only_latest_project_versions: bool | Unset = UNSET,
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

    params["group"] = group

    params["name"] = name

    params["version"] = version

    params["purl"] = purl

    params["cpe"] = cpe

    params["swidTagId"] = swid_tag_id

    json_project: str | Unset = UNSET
    if not isinstance(project, Unset):
        json_project = str(project)
    params["project"] = json_project

    params["excludeInactiveProjects"] = exclude_inactive_projects

    params["onlyLatestProjectVersions"] = only_latest_project_versions

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/component/identity",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | list[Component] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Component.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ProblemDetails | list[Component]]:
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
    sort_order: GetComponentByIdentitySortOrder | Unset = UNSET,
    group: str | Unset = UNSET,
    name: str | Unset = UNSET,
    version: str | Unset = UNSET,
    purl: str | Unset = UNSET,
    cpe: str | Unset = UNSET,
    swid_tag_id: str | Unset = UNSET,
    project: UUID | Unset = UNSET,
    exclude_inactive_projects: bool | Unset = UNSET,
    only_latest_project_versions: bool | Unset = UNSET,
) -> Response[Any | ProblemDetails | list[Component]]:
    """Returns a list of components that have the specified component identity. This resource accepts
    coordinates (group, name, version) or purl, cpe, or swidTagId

     <p>Requires permission <strong>VIEW_PORTFOLIO</strong></p>
    <p><strong>Deprecated</strong>! Use <code>/api/v2/components</code> instead.</p>

    Args:
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetComponentByIdentitySortOrder | Unset):
        group (str | Unset):
        name (str | Unset):
        version (str | Unset):
        purl (str | Unset):
        cpe (str | Unset):
        swid_tag_id (str | Unset):
        project (UUID | Unset):
        exclude_inactive_projects (bool | Unset):
        only_latest_project_versions (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | list[Component]]
    """

    kwargs = _get_kwargs(
        page_number=page_number,
        page_size=page_size,
        offset=offset,
        limit=limit,
        sort_name=sort_name,
        sort_order=sort_order,
        group=group,
        name=name,
        version=version,
        purl=purl,
        cpe=cpe,
        swid_tag_id=swid_tag_id,
        project=project,
        exclude_inactive_projects=exclude_inactive_projects,
        only_latest_project_versions=only_latest_project_versions,
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
    sort_order: GetComponentByIdentitySortOrder | Unset = UNSET,
    group: str | Unset = UNSET,
    name: str | Unset = UNSET,
    version: str | Unset = UNSET,
    purl: str | Unset = UNSET,
    cpe: str | Unset = UNSET,
    swid_tag_id: str | Unset = UNSET,
    project: UUID | Unset = UNSET,
    exclude_inactive_projects: bool | Unset = UNSET,
    only_latest_project_versions: bool | Unset = UNSET,
) -> Any | ProblemDetails | list[Component] | None:
    """Returns a list of components that have the specified component identity. This resource accepts
    coordinates (group, name, version) or purl, cpe, or swidTagId

     <p>Requires permission <strong>VIEW_PORTFOLIO</strong></p>
    <p><strong>Deprecated</strong>! Use <code>/api/v2/components</code> instead.</p>

    Args:
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetComponentByIdentitySortOrder | Unset):
        group (str | Unset):
        name (str | Unset):
        version (str | Unset):
        purl (str | Unset):
        cpe (str | Unset):
        swid_tag_id (str | Unset):
        project (UUID | Unset):
        exclude_inactive_projects (bool | Unset):
        only_latest_project_versions (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | list[Component]
    """

    return sync_detailed(
        client=client,
        page_number=page_number,
        page_size=page_size,
        offset=offset,
        limit=limit,
        sort_name=sort_name,
        sort_order=sort_order,
        group=group,
        name=name,
        version=version,
        purl=purl,
        cpe=cpe,
        swid_tag_id=swid_tag_id,
        project=project,
        exclude_inactive_projects=exclude_inactive_projects,
        only_latest_project_versions=only_latest_project_versions,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetComponentByIdentitySortOrder | Unset = UNSET,
    group: str | Unset = UNSET,
    name: str | Unset = UNSET,
    version: str | Unset = UNSET,
    purl: str | Unset = UNSET,
    cpe: str | Unset = UNSET,
    swid_tag_id: str | Unset = UNSET,
    project: UUID | Unset = UNSET,
    exclude_inactive_projects: bool | Unset = UNSET,
    only_latest_project_versions: bool | Unset = UNSET,
) -> Response[Any | ProblemDetails | list[Component]]:
    """Returns a list of components that have the specified component identity. This resource accepts
    coordinates (group, name, version) or purl, cpe, or swidTagId

     <p>Requires permission <strong>VIEW_PORTFOLIO</strong></p>
    <p><strong>Deprecated</strong>! Use <code>/api/v2/components</code> instead.</p>

    Args:
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetComponentByIdentitySortOrder | Unset):
        group (str | Unset):
        name (str | Unset):
        version (str | Unset):
        purl (str | Unset):
        cpe (str | Unset):
        swid_tag_id (str | Unset):
        project (UUID | Unset):
        exclude_inactive_projects (bool | Unset):
        only_latest_project_versions (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | list[Component]]
    """

    kwargs = _get_kwargs(
        page_number=page_number,
        page_size=page_size,
        offset=offset,
        limit=limit,
        sort_name=sort_name,
        sort_order=sort_order,
        group=group,
        name=name,
        version=version,
        purl=purl,
        cpe=cpe,
        swid_tag_id=swid_tag_id,
        project=project,
        exclude_inactive_projects=exclude_inactive_projects,
        only_latest_project_versions=only_latest_project_versions,
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
    sort_order: GetComponentByIdentitySortOrder | Unset = UNSET,
    group: str | Unset = UNSET,
    name: str | Unset = UNSET,
    version: str | Unset = UNSET,
    purl: str | Unset = UNSET,
    cpe: str | Unset = UNSET,
    swid_tag_id: str | Unset = UNSET,
    project: UUID | Unset = UNSET,
    exclude_inactive_projects: bool | Unset = UNSET,
    only_latest_project_versions: bool | Unset = UNSET,
) -> Any | ProblemDetails | list[Component] | None:
    """Returns a list of components that have the specified component identity. This resource accepts
    coordinates (group, name, version) or purl, cpe, or swidTagId

     <p>Requires permission <strong>VIEW_PORTFOLIO</strong></p>
    <p><strong>Deprecated</strong>! Use <code>/api/v2/components</code> instead.</p>

    Args:
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetComponentByIdentitySortOrder | Unset):
        group (str | Unset):
        name (str | Unset):
        version (str | Unset):
        purl (str | Unset):
        cpe (str | Unset):
        swid_tag_id (str | Unset):
        project (UUID | Unset):
        exclude_inactive_projects (bool | Unset):
        only_latest_project_versions (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | list[Component]
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
            group=group,
            name=name,
            version=version,
            purl=purl,
            cpe=cpe,
            swid_tag_id=swid_tag_id,
            project=project,
            exclude_inactive_projects=exclude_inactive_projects,
            only_latest_project_versions=only_latest_project_versions,
        )
    ).parsed
