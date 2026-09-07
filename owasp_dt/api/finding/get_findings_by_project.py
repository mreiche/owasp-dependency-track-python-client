from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.finding import Finding
from ...models.get_findings_by_project_sort_order import GetFindingsByProjectSortOrder
from ...models.get_findings_by_project_source import GetFindingsByProjectSource
from ...models.get_findings_by_project_total_count import GetFindingsByProjectTotalCount
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    search_text: str | Unset = UNSET,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetFindingsByProjectSortOrder | Unset = UNSET,
    suppressed: bool | Unset = UNSET,
    source: GetFindingsByProjectSource | Unset = UNSET,
    has_analysis: bool | Unset = UNSET,
    epss_from: float | Unset = UNSET,
    epss_to: float | Unset = UNSET,
    is_kev: bool | Unset = UNSET,
    total_count: GetFindingsByProjectTotalCount
    | Unset = GetFindingsByProjectTotalCount.EXACT,
    accept: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept, Unset):
        headers["accept"] = accept

    params: dict[str, Any] = {}

    params["searchText"] = search_text

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    params["offset"] = offset

    params["limit"] = limit

    params["sortName"] = sort_name

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params["suppressed"] = suppressed

    json_source: str | Unset = UNSET
    if not isinstance(source, Unset):
        json_source = source.value

    params["source"] = json_source

    params["hasAnalysis"] = has_analysis

    params["epssFrom"] = epss_from

    params["epssTo"] = epss_to

    params["isKev"] = is_kev

    json_total_count: str | Unset = UNSET
    if not isinstance(total_count, Unset):
        json_total_count = total_count.value

    params["totalCount"] = json_total_count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/finding/project/{uuid}".format(
            uuid=quote(str(uuid), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | list[Finding] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Finding.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = ProblemDetails.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ProblemDetails | list[Finding]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    search_text: str | Unset = UNSET,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetFindingsByProjectSortOrder | Unset = UNSET,
    suppressed: bool | Unset = UNSET,
    source: GetFindingsByProjectSource | Unset = UNSET,
    has_analysis: bool | Unset = UNSET,
    epss_from: float | Unset = UNSET,
    epss_to: float | Unset = UNSET,
    is_kev: bool | Unset = UNSET,
    total_count: GetFindingsByProjectTotalCount
    | Unset = GetFindingsByProjectTotalCount.EXACT,
    accept: str | Unset = UNSET,
) -> Response[Any | ProblemDetails | list[Finding]]:
    """Returns a list of all findings for a specific project or generates SARIF file if Accept:
    application/sarif+json header is provided

     <p>Requires permission <strong>VIEW_VULNERABILITY</strong></p>

    Args:
        uuid (UUID):
        search_text (str | Unset):
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetFindingsByProjectSortOrder | Unset):
        suppressed (bool | Unset):
        source (GetFindingsByProjectSource | Unset):
        has_analysis (bool | Unset):
        epss_from (float | Unset):
        epss_to (float | Unset):
        is_kev (bool | Unset):
        total_count (GetFindingsByProjectTotalCount | Unset): The counting mode for the `X-Total-
            Count` response header. Default: GetFindingsByProjectTotalCount.EXACT.
        accept (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | list[Finding]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        search_text=search_text,
        page_number=page_number,
        page_size=page_size,
        offset=offset,
        limit=limit,
        sort_name=sort_name,
        sort_order=sort_order,
        suppressed=suppressed,
        source=source,
        has_analysis=has_analysis,
        epss_from=epss_from,
        epss_to=epss_to,
        is_kev=is_kev,
        total_count=total_count,
        accept=accept,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    search_text: str | Unset = UNSET,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetFindingsByProjectSortOrder | Unset = UNSET,
    suppressed: bool | Unset = UNSET,
    source: GetFindingsByProjectSource | Unset = UNSET,
    has_analysis: bool | Unset = UNSET,
    epss_from: float | Unset = UNSET,
    epss_to: float | Unset = UNSET,
    is_kev: bool | Unset = UNSET,
    total_count: GetFindingsByProjectTotalCount
    | Unset = GetFindingsByProjectTotalCount.EXACT,
    accept: str | Unset = UNSET,
) -> Any | ProblemDetails | list[Finding] | None:
    """Returns a list of all findings for a specific project or generates SARIF file if Accept:
    application/sarif+json header is provided

     <p>Requires permission <strong>VIEW_VULNERABILITY</strong></p>

    Args:
        uuid (UUID):
        search_text (str | Unset):
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetFindingsByProjectSortOrder | Unset):
        suppressed (bool | Unset):
        source (GetFindingsByProjectSource | Unset):
        has_analysis (bool | Unset):
        epss_from (float | Unset):
        epss_to (float | Unset):
        is_kev (bool | Unset):
        total_count (GetFindingsByProjectTotalCount | Unset): The counting mode for the `X-Total-
            Count` response header. Default: GetFindingsByProjectTotalCount.EXACT.
        accept (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | list[Finding]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        search_text=search_text,
        page_number=page_number,
        page_size=page_size,
        offset=offset,
        limit=limit,
        sort_name=sort_name,
        sort_order=sort_order,
        suppressed=suppressed,
        source=source,
        has_analysis=has_analysis,
        epss_from=epss_from,
        epss_to=epss_to,
        is_kev=is_kev,
        total_count=total_count,
        accept=accept,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    search_text: str | Unset = UNSET,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetFindingsByProjectSortOrder | Unset = UNSET,
    suppressed: bool | Unset = UNSET,
    source: GetFindingsByProjectSource | Unset = UNSET,
    has_analysis: bool | Unset = UNSET,
    epss_from: float | Unset = UNSET,
    epss_to: float | Unset = UNSET,
    is_kev: bool | Unset = UNSET,
    total_count: GetFindingsByProjectTotalCount
    | Unset = GetFindingsByProjectTotalCount.EXACT,
    accept: str | Unset = UNSET,
) -> Response[Any | ProblemDetails | list[Finding]]:
    """Returns a list of all findings for a specific project or generates SARIF file if Accept:
    application/sarif+json header is provided

     <p>Requires permission <strong>VIEW_VULNERABILITY</strong></p>

    Args:
        uuid (UUID):
        search_text (str | Unset):
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetFindingsByProjectSortOrder | Unset):
        suppressed (bool | Unset):
        source (GetFindingsByProjectSource | Unset):
        has_analysis (bool | Unset):
        epss_from (float | Unset):
        epss_to (float | Unset):
        is_kev (bool | Unset):
        total_count (GetFindingsByProjectTotalCount | Unset): The counting mode for the `X-Total-
            Count` response header. Default: GetFindingsByProjectTotalCount.EXACT.
        accept (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | list[Finding]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        search_text=search_text,
        page_number=page_number,
        page_size=page_size,
        offset=offset,
        limit=limit,
        sort_name=sort_name,
        sort_order=sort_order,
        suppressed=suppressed,
        source=source,
        has_analysis=has_analysis,
        epss_from=epss_from,
        epss_to=epss_to,
        is_kev=is_kev,
        total_count=total_count,
        accept=accept,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    search_text: str | Unset = UNSET,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetFindingsByProjectSortOrder | Unset = UNSET,
    suppressed: bool | Unset = UNSET,
    source: GetFindingsByProjectSource | Unset = UNSET,
    has_analysis: bool | Unset = UNSET,
    epss_from: float | Unset = UNSET,
    epss_to: float | Unset = UNSET,
    is_kev: bool | Unset = UNSET,
    total_count: GetFindingsByProjectTotalCount
    | Unset = GetFindingsByProjectTotalCount.EXACT,
    accept: str | Unset = UNSET,
) -> Any | ProblemDetails | list[Finding] | None:
    """Returns a list of all findings for a specific project or generates SARIF file if Accept:
    application/sarif+json header is provided

     <p>Requires permission <strong>VIEW_VULNERABILITY</strong></p>

    Args:
        uuid (UUID):
        search_text (str | Unset):
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetFindingsByProjectSortOrder | Unset):
        suppressed (bool | Unset):
        source (GetFindingsByProjectSource | Unset):
        has_analysis (bool | Unset):
        epss_from (float | Unset):
        epss_to (float | Unset):
        is_kev (bool | Unset):
        total_count (GetFindingsByProjectTotalCount | Unset): The counting mode for the `X-Total-
            Count` response header. Default: GetFindingsByProjectTotalCount.EXACT.
        accept (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | list[Finding]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            search_text=search_text,
            page_number=page_number,
            page_size=page_size,
            offset=offset,
            limit=limit,
            sort_name=sort_name,
            sort_order=sort_order,
            suppressed=suppressed,
            source=source,
            has_analysis=has_analysis,
            epss_from=epss_from,
            epss_to=epss_to,
            is_kev=is_kev,
            total_count=total_count,
            accept=accept,
        )
    ).parsed
