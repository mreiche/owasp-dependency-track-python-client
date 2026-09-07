from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.list_components_hash_type import ListComponentsHashType
from ...models.paginated_response import PaginatedResponse
from ...models.problem_details import ProblemDetails
from ...models.project_state import ProjectState
from ...models.sort_direction import SortDirection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    group_contains: str | Unset = UNSET,
    name_contains: str | Unset = UNSET,
    version_contains: str | Unset = UNSET,
    purl_prefix: str | Unset = UNSET,
    cpe: str | Unset = UNSET,
    swid_tag_id_contains: str | Unset = UNSET,
    hash_type: ListComponentsHashType | Unset = UNSET,
    hash_: str | Unset = UNSET,
    package_artifact_published_since: int | Unset = UNSET,
    package_artifact_published_before: int | Unset = UNSET,
    project_state: ProjectState | Unset = UNSET,
    project_latest_version: bool | Unset = UNSET,
    expand: list[str] | Unset = UNSET,
    limit: int | Unset = 100,
    page_token: str | Unset = UNSET,
    sort_direction: SortDirection | Unset = UNSET,
    sort_by: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["group_contains"] = group_contains

    params["name_contains"] = name_contains

    params["version_contains"] = version_contains

    params["purl_prefix"] = purl_prefix

    params["cpe"] = cpe

    params["swid_tag_id_contains"] = swid_tag_id_contains

    json_hash_type: str | Unset = UNSET
    if not isinstance(hash_type, Unset):
        json_hash_type = hash_type.value

    params["hash_type"] = json_hash_type

    params["hash"] = hash_

    params["package_artifact_published_since"] = package_artifact_published_since

    params["package_artifact_published_before"] = package_artifact_published_before

    json_project_state: str | Unset = UNSET
    if not isinstance(project_state, Unset):
        json_project_state = project_state.value

    params["project_state"] = json_project_state

    params["project_latest_version"] = project_latest_version

    json_expand: list[str] | Unset = UNSET
    if not isinstance(expand, Unset):
        json_expand = expand

    params["expand"] = json_expand

    params["limit"] = limit

    params["page_token"] = page_token

    json_sort_direction: str | Unset = UNSET
    if not isinstance(sort_direction, Unset):
        json_sort_direction = sort_direction.value

    params["sort_direction"] = json_sort_direction

    params["sort_by"] = sort_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/components",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedResponse | ProblemDetails:
    if response.status_code == 200:
        response_200 = PaginatedResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:

        def _parse_response_400(data: object) -> ProblemDetails:
            if not isinstance(data, dict):
                raise TypeError()
            response_400_type_0 = ProblemDetails.from_dict(data)

            return response_400_type_0

        response_400 = _parse_response_400(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProblemDetails.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403

    response_default = ProblemDetails.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedResponse | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    group_contains: str | Unset = UNSET,
    name_contains: str | Unset = UNSET,
    version_contains: str | Unset = UNSET,
    purl_prefix: str | Unset = UNSET,
    cpe: str | Unset = UNSET,
    swid_tag_id_contains: str | Unset = UNSET,
    hash_type: ListComponentsHashType | Unset = UNSET,
    hash_: str | Unset = UNSET,
    package_artifact_published_since: int | Unset = UNSET,
    package_artifact_published_before: int | Unset = UNSET,
    project_state: ProjectState | Unset = UNSET,
    project_latest_version: bool | Unset = UNSET,
    expand: list[str] | Unset = UNSET,
    limit: int | Unset = 100,
    page_token: str | Unset = UNSET,
    sort_direction: SortDirection | Unset = UNSET,
    sort_by: str | Unset = UNSET,
) -> Response[PaginatedResponse | ProblemDetails]:
    """List all components

     Retrieves a list of all components matching the provided filter criteria.

    Text filters are case-insensitive.

    ### Sortable fields

    Sorting is supported for the following fields:

    * `name`
    * `group`
    * `last_inherited_risk_score`

    ### Expandable fields

    The following fields can be included via `expand`:

    * `metrics`
    * `package_metadata`
    * `package_artifact_metadata`

    Requires permission `VIEW_PORTFOLIO`

    Args:
        group_contains (str | Unset):
        name_contains (str | Unset):
        version_contains (str | Unset):
        purl_prefix (str | Unset):
        cpe (str | Unset):
        swid_tag_id_contains (str | Unset):
        hash_type (ListComponentsHashType | Unset):
        hash_ (str | Unset):
        package_artifact_published_since (int | Unset): Epoch timestamp in milliseconds since
            January 1, 1970 UTC. Example: 1752209050377.
        package_artifact_published_before (int | Unset): Epoch timestamp in milliseconds since
            January 1, 1970 UTC. Example: 1752209050377.
        project_state (ProjectState | Unset):
        project_latest_version (bool | Unset):
        expand (list[str] | Unset):
        limit (int | Unset):  Default: 100.
        page_token (str | Unset):
        sort_direction (SortDirection | Unset):
        sort_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        group_contains=group_contains,
        name_contains=name_contains,
        version_contains=version_contains,
        purl_prefix=purl_prefix,
        cpe=cpe,
        swid_tag_id_contains=swid_tag_id_contains,
        hash_type=hash_type,
        hash_=hash_,
        package_artifact_published_since=package_artifact_published_since,
        package_artifact_published_before=package_artifact_published_before,
        project_state=project_state,
        project_latest_version=project_latest_version,
        expand=expand,
        limit=limit,
        page_token=page_token,
        sort_direction=sort_direction,
        sort_by=sort_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    group_contains: str | Unset = UNSET,
    name_contains: str | Unset = UNSET,
    version_contains: str | Unset = UNSET,
    purl_prefix: str | Unset = UNSET,
    cpe: str | Unset = UNSET,
    swid_tag_id_contains: str | Unset = UNSET,
    hash_type: ListComponentsHashType | Unset = UNSET,
    hash_: str | Unset = UNSET,
    package_artifact_published_since: int | Unset = UNSET,
    package_artifact_published_before: int | Unset = UNSET,
    project_state: ProjectState | Unset = UNSET,
    project_latest_version: bool | Unset = UNSET,
    expand: list[str] | Unset = UNSET,
    limit: int | Unset = 100,
    page_token: str | Unset = UNSET,
    sort_direction: SortDirection | Unset = UNSET,
    sort_by: str | Unset = UNSET,
) -> PaginatedResponse | ProblemDetails | None:
    """List all components

     Retrieves a list of all components matching the provided filter criteria.

    Text filters are case-insensitive.

    ### Sortable fields

    Sorting is supported for the following fields:

    * `name`
    * `group`
    * `last_inherited_risk_score`

    ### Expandable fields

    The following fields can be included via `expand`:

    * `metrics`
    * `package_metadata`
    * `package_artifact_metadata`

    Requires permission `VIEW_PORTFOLIO`

    Args:
        group_contains (str | Unset):
        name_contains (str | Unset):
        version_contains (str | Unset):
        purl_prefix (str | Unset):
        cpe (str | Unset):
        swid_tag_id_contains (str | Unset):
        hash_type (ListComponentsHashType | Unset):
        hash_ (str | Unset):
        package_artifact_published_since (int | Unset): Epoch timestamp in milliseconds since
            January 1, 1970 UTC. Example: 1752209050377.
        package_artifact_published_before (int | Unset): Epoch timestamp in milliseconds since
            January 1, 1970 UTC. Example: 1752209050377.
        project_state (ProjectState | Unset):
        project_latest_version (bool | Unset):
        expand (list[str] | Unset):
        limit (int | Unset):  Default: 100.
        page_token (str | Unset):
        sort_direction (SortDirection | Unset):
        sort_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponse | ProblemDetails
    """

    return sync_detailed(
        client=client,
        group_contains=group_contains,
        name_contains=name_contains,
        version_contains=version_contains,
        purl_prefix=purl_prefix,
        cpe=cpe,
        swid_tag_id_contains=swid_tag_id_contains,
        hash_type=hash_type,
        hash_=hash_,
        package_artifact_published_since=package_artifact_published_since,
        package_artifact_published_before=package_artifact_published_before,
        project_state=project_state,
        project_latest_version=project_latest_version,
        expand=expand,
        limit=limit,
        page_token=page_token,
        sort_direction=sort_direction,
        sort_by=sort_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    group_contains: str | Unset = UNSET,
    name_contains: str | Unset = UNSET,
    version_contains: str | Unset = UNSET,
    purl_prefix: str | Unset = UNSET,
    cpe: str | Unset = UNSET,
    swid_tag_id_contains: str | Unset = UNSET,
    hash_type: ListComponentsHashType | Unset = UNSET,
    hash_: str | Unset = UNSET,
    package_artifact_published_since: int | Unset = UNSET,
    package_artifact_published_before: int | Unset = UNSET,
    project_state: ProjectState | Unset = UNSET,
    project_latest_version: bool | Unset = UNSET,
    expand: list[str] | Unset = UNSET,
    limit: int | Unset = 100,
    page_token: str | Unset = UNSET,
    sort_direction: SortDirection | Unset = UNSET,
    sort_by: str | Unset = UNSET,
) -> Response[PaginatedResponse | ProblemDetails]:
    """List all components

     Retrieves a list of all components matching the provided filter criteria.

    Text filters are case-insensitive.

    ### Sortable fields

    Sorting is supported for the following fields:

    * `name`
    * `group`
    * `last_inherited_risk_score`

    ### Expandable fields

    The following fields can be included via `expand`:

    * `metrics`
    * `package_metadata`
    * `package_artifact_metadata`

    Requires permission `VIEW_PORTFOLIO`

    Args:
        group_contains (str | Unset):
        name_contains (str | Unset):
        version_contains (str | Unset):
        purl_prefix (str | Unset):
        cpe (str | Unset):
        swid_tag_id_contains (str | Unset):
        hash_type (ListComponentsHashType | Unset):
        hash_ (str | Unset):
        package_artifact_published_since (int | Unset): Epoch timestamp in milliseconds since
            January 1, 1970 UTC. Example: 1752209050377.
        package_artifact_published_before (int | Unset): Epoch timestamp in milliseconds since
            January 1, 1970 UTC. Example: 1752209050377.
        project_state (ProjectState | Unset):
        project_latest_version (bool | Unset):
        expand (list[str] | Unset):
        limit (int | Unset):  Default: 100.
        page_token (str | Unset):
        sort_direction (SortDirection | Unset):
        sort_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        group_contains=group_contains,
        name_contains=name_contains,
        version_contains=version_contains,
        purl_prefix=purl_prefix,
        cpe=cpe,
        swid_tag_id_contains=swid_tag_id_contains,
        hash_type=hash_type,
        hash_=hash_,
        package_artifact_published_since=package_artifact_published_since,
        package_artifact_published_before=package_artifact_published_before,
        project_state=project_state,
        project_latest_version=project_latest_version,
        expand=expand,
        limit=limit,
        page_token=page_token,
        sort_direction=sort_direction,
        sort_by=sort_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    group_contains: str | Unset = UNSET,
    name_contains: str | Unset = UNSET,
    version_contains: str | Unset = UNSET,
    purl_prefix: str | Unset = UNSET,
    cpe: str | Unset = UNSET,
    swid_tag_id_contains: str | Unset = UNSET,
    hash_type: ListComponentsHashType | Unset = UNSET,
    hash_: str | Unset = UNSET,
    package_artifact_published_since: int | Unset = UNSET,
    package_artifact_published_before: int | Unset = UNSET,
    project_state: ProjectState | Unset = UNSET,
    project_latest_version: bool | Unset = UNSET,
    expand: list[str] | Unset = UNSET,
    limit: int | Unset = 100,
    page_token: str | Unset = UNSET,
    sort_direction: SortDirection | Unset = UNSET,
    sort_by: str | Unset = UNSET,
) -> PaginatedResponse | ProblemDetails | None:
    """List all components

     Retrieves a list of all components matching the provided filter criteria.

    Text filters are case-insensitive.

    ### Sortable fields

    Sorting is supported for the following fields:

    * `name`
    * `group`
    * `last_inherited_risk_score`

    ### Expandable fields

    The following fields can be included via `expand`:

    * `metrics`
    * `package_metadata`
    * `package_artifact_metadata`

    Requires permission `VIEW_PORTFOLIO`

    Args:
        group_contains (str | Unset):
        name_contains (str | Unset):
        version_contains (str | Unset):
        purl_prefix (str | Unset):
        cpe (str | Unset):
        swid_tag_id_contains (str | Unset):
        hash_type (ListComponentsHashType | Unset):
        hash_ (str | Unset):
        package_artifact_published_since (int | Unset): Epoch timestamp in milliseconds since
            January 1, 1970 UTC. Example: 1752209050377.
        package_artifact_published_before (int | Unset): Epoch timestamp in milliseconds since
            January 1, 1970 UTC. Example: 1752209050377.
        project_state (ProjectState | Unset):
        project_latest_version (bool | Unset):
        expand (list[str] | Unset):
        limit (int | Unset):  Default: 100.
        page_token (str | Unset):
        sort_direction (SortDirection | Unset):
        sort_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponse | ProblemDetails
    """

    return (
        await asyncio_detailed(
            client=client,
            group_contains=group_contains,
            name_contains=name_contains,
            version_contains=version_contains,
            purl_prefix=purl_prefix,
            cpe=cpe,
            swid_tag_id_contains=swid_tag_id_contains,
            hash_type=hash_type,
            hash_=hash_,
            package_artifact_published_since=package_artifact_published_since,
            package_artifact_published_before=package_artifact_published_before,
            project_state=project_state,
            project_latest_version=project_latest_version,
            expand=expand,
            limit=limit,
            page_token=page_token,
            sort_direction=sort_direction,
            sort_by=sort_by,
        )
    ).parsed
