from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.finding import Finding
from ...models.get_all_findings_sort_order import GetAllFindingsSortOrder
from ...models.get_all_findings_total_count import GetAllFindingsTotalCount
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetAllFindingsSortOrder | Unset = UNSET,
    show_inactive: bool | Unset = UNSET,
    severity: str | Unset = UNSET,
    publish_date_from: str | Unset = UNSET,
    publish_date_to: str | Unset = UNSET,
    text_search_field: str | Unset = UNSET,
    text_search_input: str | Unset = UNSET,
    cvssv_2_from: str | Unset = UNSET,
    cvssv_2_to: str | Unset = UNSET,
    cvssv_3_from: str | Unset = UNSET,
    cvssv_3_to: str | Unset = UNSET,
    cvssv_4_from: str | Unset = UNSET,
    cvssv_4_to: str | Unset = UNSET,
    epss_from: str | Unset = UNSET,
    epss_to: str | Unset = UNSET,
    epss_percentile_from: str | Unset = UNSET,
    epss_percentile_to: str | Unset = UNSET,
    occurrences_from: str | Unset = UNSET,
    occurrences_to: str | Unset = UNSET,
    is_kev: bool | Unset = UNSET,
    total_count: GetAllFindingsTotalCount | Unset = GetAllFindingsTotalCount.EXACT,
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

    params["showInactive"] = show_inactive

    params["severity"] = severity

    params["publishDateFrom"] = publish_date_from

    params["publishDateTo"] = publish_date_to

    params["textSearchField"] = text_search_field

    params["textSearchInput"] = text_search_input

    params["cvssv2From"] = cvssv_2_from

    params["cvssv2To"] = cvssv_2_to

    params["cvssv3From"] = cvssv_3_from

    params["cvssv3To"] = cvssv_3_to

    params["cvssv4From"] = cvssv_4_from

    params["cvssv4To"] = cvssv_4_to

    params["epssFrom"] = epss_from

    params["epssTo"] = epss_to

    params["epssPercentileFrom"] = epss_percentile_from

    params["epssPercentileTo"] = epss_percentile_to

    params["occurrencesFrom"] = occurrences_from

    params["occurrencesTo"] = occurrences_to

    params["isKev"] = is_kev

    json_total_count: str | Unset = UNSET
    if not isinstance(total_count, Unset):
        json_total_count = total_count.value

    params["totalCount"] = json_total_count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/finding/grouped",
        "params": params,
    }

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
    *,
    client: AuthenticatedClient,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetAllFindingsSortOrder | Unset = UNSET,
    show_inactive: bool | Unset = UNSET,
    severity: str | Unset = UNSET,
    publish_date_from: str | Unset = UNSET,
    publish_date_to: str | Unset = UNSET,
    text_search_field: str | Unset = UNSET,
    text_search_input: str | Unset = UNSET,
    cvssv_2_from: str | Unset = UNSET,
    cvssv_2_to: str | Unset = UNSET,
    cvssv_3_from: str | Unset = UNSET,
    cvssv_3_to: str | Unset = UNSET,
    cvssv_4_from: str | Unset = UNSET,
    cvssv_4_to: str | Unset = UNSET,
    epss_from: str | Unset = UNSET,
    epss_to: str | Unset = UNSET,
    epss_percentile_from: str | Unset = UNSET,
    epss_percentile_to: str | Unset = UNSET,
    occurrences_from: str | Unset = UNSET,
    occurrences_to: str | Unset = UNSET,
    is_kev: bool | Unset = UNSET,
    total_count: GetAllFindingsTotalCount | Unset = GetAllFindingsTotalCount.EXACT,
) -> Response[Any | ProblemDetails | list[Finding]]:
    """Returns a list of all findings grouped by vulnerability

     <p>Requires permission <strong>VIEW_VULNERABILITY</strong></p>

    Args:
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetAllFindingsSortOrder | Unset):
        show_inactive (bool | Unset):
        severity (str | Unset):
        publish_date_from (str | Unset):
        publish_date_to (str | Unset):
        text_search_field (str | Unset):
        text_search_input (str | Unset):
        cvssv_2_from (str | Unset):
        cvssv_2_to (str | Unset):
        cvssv_3_from (str | Unset):
        cvssv_3_to (str | Unset):
        cvssv_4_from (str | Unset):
        cvssv_4_to (str | Unset):
        epss_from (str | Unset):
        epss_to (str | Unset):
        epss_percentile_from (str | Unset):
        epss_percentile_to (str | Unset):
        occurrences_from (str | Unset):
        occurrences_to (str | Unset):
        is_kev (bool | Unset):
        total_count (GetAllFindingsTotalCount | Unset): The counting mode for the `X-Total-Count`
            response header. Default: GetAllFindingsTotalCount.EXACT.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | list[Finding]]
    """

    kwargs = _get_kwargs(
        page_number=page_number,
        page_size=page_size,
        offset=offset,
        limit=limit,
        sort_name=sort_name,
        sort_order=sort_order,
        show_inactive=show_inactive,
        severity=severity,
        publish_date_from=publish_date_from,
        publish_date_to=publish_date_to,
        text_search_field=text_search_field,
        text_search_input=text_search_input,
        cvssv_2_from=cvssv_2_from,
        cvssv_2_to=cvssv_2_to,
        cvssv_3_from=cvssv_3_from,
        cvssv_3_to=cvssv_3_to,
        cvssv_4_from=cvssv_4_from,
        cvssv_4_to=cvssv_4_to,
        epss_from=epss_from,
        epss_to=epss_to,
        epss_percentile_from=epss_percentile_from,
        epss_percentile_to=epss_percentile_to,
        occurrences_from=occurrences_from,
        occurrences_to=occurrences_to,
        is_kev=is_kev,
        total_count=total_count,
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
    sort_order: GetAllFindingsSortOrder | Unset = UNSET,
    show_inactive: bool | Unset = UNSET,
    severity: str | Unset = UNSET,
    publish_date_from: str | Unset = UNSET,
    publish_date_to: str | Unset = UNSET,
    text_search_field: str | Unset = UNSET,
    text_search_input: str | Unset = UNSET,
    cvssv_2_from: str | Unset = UNSET,
    cvssv_2_to: str | Unset = UNSET,
    cvssv_3_from: str | Unset = UNSET,
    cvssv_3_to: str | Unset = UNSET,
    cvssv_4_from: str | Unset = UNSET,
    cvssv_4_to: str | Unset = UNSET,
    epss_from: str | Unset = UNSET,
    epss_to: str | Unset = UNSET,
    epss_percentile_from: str | Unset = UNSET,
    epss_percentile_to: str | Unset = UNSET,
    occurrences_from: str | Unset = UNSET,
    occurrences_to: str | Unset = UNSET,
    is_kev: bool | Unset = UNSET,
    total_count: GetAllFindingsTotalCount | Unset = GetAllFindingsTotalCount.EXACT,
) -> Any | ProblemDetails | list[Finding] | None:
    """Returns a list of all findings grouped by vulnerability

     <p>Requires permission <strong>VIEW_VULNERABILITY</strong></p>

    Args:
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetAllFindingsSortOrder | Unset):
        show_inactive (bool | Unset):
        severity (str | Unset):
        publish_date_from (str | Unset):
        publish_date_to (str | Unset):
        text_search_field (str | Unset):
        text_search_input (str | Unset):
        cvssv_2_from (str | Unset):
        cvssv_2_to (str | Unset):
        cvssv_3_from (str | Unset):
        cvssv_3_to (str | Unset):
        cvssv_4_from (str | Unset):
        cvssv_4_to (str | Unset):
        epss_from (str | Unset):
        epss_to (str | Unset):
        epss_percentile_from (str | Unset):
        epss_percentile_to (str | Unset):
        occurrences_from (str | Unset):
        occurrences_to (str | Unset):
        is_kev (bool | Unset):
        total_count (GetAllFindingsTotalCount | Unset): The counting mode for the `X-Total-Count`
            response header. Default: GetAllFindingsTotalCount.EXACT.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | list[Finding]
    """

    return sync_detailed(
        client=client,
        page_number=page_number,
        page_size=page_size,
        offset=offset,
        limit=limit,
        sort_name=sort_name,
        sort_order=sort_order,
        show_inactive=show_inactive,
        severity=severity,
        publish_date_from=publish_date_from,
        publish_date_to=publish_date_to,
        text_search_field=text_search_field,
        text_search_input=text_search_input,
        cvssv_2_from=cvssv_2_from,
        cvssv_2_to=cvssv_2_to,
        cvssv_3_from=cvssv_3_from,
        cvssv_3_to=cvssv_3_to,
        cvssv_4_from=cvssv_4_from,
        cvssv_4_to=cvssv_4_to,
        epss_from=epss_from,
        epss_to=epss_to,
        epss_percentile_from=epss_percentile_from,
        epss_percentile_to=epss_percentile_to,
        occurrences_from=occurrences_from,
        occurrences_to=occurrences_to,
        is_kev=is_kev,
        total_count=total_count,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetAllFindingsSortOrder | Unset = UNSET,
    show_inactive: bool | Unset = UNSET,
    severity: str | Unset = UNSET,
    publish_date_from: str | Unset = UNSET,
    publish_date_to: str | Unset = UNSET,
    text_search_field: str | Unset = UNSET,
    text_search_input: str | Unset = UNSET,
    cvssv_2_from: str | Unset = UNSET,
    cvssv_2_to: str | Unset = UNSET,
    cvssv_3_from: str | Unset = UNSET,
    cvssv_3_to: str | Unset = UNSET,
    cvssv_4_from: str | Unset = UNSET,
    cvssv_4_to: str | Unset = UNSET,
    epss_from: str | Unset = UNSET,
    epss_to: str | Unset = UNSET,
    epss_percentile_from: str | Unset = UNSET,
    epss_percentile_to: str | Unset = UNSET,
    occurrences_from: str | Unset = UNSET,
    occurrences_to: str | Unset = UNSET,
    is_kev: bool | Unset = UNSET,
    total_count: GetAllFindingsTotalCount | Unset = GetAllFindingsTotalCount.EXACT,
) -> Response[Any | ProblemDetails | list[Finding]]:
    """Returns a list of all findings grouped by vulnerability

     <p>Requires permission <strong>VIEW_VULNERABILITY</strong></p>

    Args:
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetAllFindingsSortOrder | Unset):
        show_inactive (bool | Unset):
        severity (str | Unset):
        publish_date_from (str | Unset):
        publish_date_to (str | Unset):
        text_search_field (str | Unset):
        text_search_input (str | Unset):
        cvssv_2_from (str | Unset):
        cvssv_2_to (str | Unset):
        cvssv_3_from (str | Unset):
        cvssv_3_to (str | Unset):
        cvssv_4_from (str | Unset):
        cvssv_4_to (str | Unset):
        epss_from (str | Unset):
        epss_to (str | Unset):
        epss_percentile_from (str | Unset):
        epss_percentile_to (str | Unset):
        occurrences_from (str | Unset):
        occurrences_to (str | Unset):
        is_kev (bool | Unset):
        total_count (GetAllFindingsTotalCount | Unset): The counting mode for the `X-Total-Count`
            response header. Default: GetAllFindingsTotalCount.EXACT.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | list[Finding]]
    """

    kwargs = _get_kwargs(
        page_number=page_number,
        page_size=page_size,
        offset=offset,
        limit=limit,
        sort_name=sort_name,
        sort_order=sort_order,
        show_inactive=show_inactive,
        severity=severity,
        publish_date_from=publish_date_from,
        publish_date_to=publish_date_to,
        text_search_field=text_search_field,
        text_search_input=text_search_input,
        cvssv_2_from=cvssv_2_from,
        cvssv_2_to=cvssv_2_to,
        cvssv_3_from=cvssv_3_from,
        cvssv_3_to=cvssv_3_to,
        cvssv_4_from=cvssv_4_from,
        cvssv_4_to=cvssv_4_to,
        epss_from=epss_from,
        epss_to=epss_to,
        epss_percentile_from=epss_percentile_from,
        epss_percentile_to=epss_percentile_to,
        occurrences_from=occurrences_from,
        occurrences_to=occurrences_to,
        is_kev=is_kev,
        total_count=total_count,
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
    sort_order: GetAllFindingsSortOrder | Unset = UNSET,
    show_inactive: bool | Unset = UNSET,
    severity: str | Unset = UNSET,
    publish_date_from: str | Unset = UNSET,
    publish_date_to: str | Unset = UNSET,
    text_search_field: str | Unset = UNSET,
    text_search_input: str | Unset = UNSET,
    cvssv_2_from: str | Unset = UNSET,
    cvssv_2_to: str | Unset = UNSET,
    cvssv_3_from: str | Unset = UNSET,
    cvssv_3_to: str | Unset = UNSET,
    cvssv_4_from: str | Unset = UNSET,
    cvssv_4_to: str | Unset = UNSET,
    epss_from: str | Unset = UNSET,
    epss_to: str | Unset = UNSET,
    epss_percentile_from: str | Unset = UNSET,
    epss_percentile_to: str | Unset = UNSET,
    occurrences_from: str | Unset = UNSET,
    occurrences_to: str | Unset = UNSET,
    is_kev: bool | Unset = UNSET,
    total_count: GetAllFindingsTotalCount | Unset = GetAllFindingsTotalCount.EXACT,
) -> Any | ProblemDetails | list[Finding] | None:
    """Returns a list of all findings grouped by vulnerability

     <p>Requires permission <strong>VIEW_VULNERABILITY</strong></p>

    Args:
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetAllFindingsSortOrder | Unset):
        show_inactive (bool | Unset):
        severity (str | Unset):
        publish_date_from (str | Unset):
        publish_date_to (str | Unset):
        text_search_field (str | Unset):
        text_search_input (str | Unset):
        cvssv_2_from (str | Unset):
        cvssv_2_to (str | Unset):
        cvssv_3_from (str | Unset):
        cvssv_3_to (str | Unset):
        cvssv_4_from (str | Unset):
        cvssv_4_to (str | Unset):
        epss_from (str | Unset):
        epss_to (str | Unset):
        epss_percentile_from (str | Unset):
        epss_percentile_to (str | Unset):
        occurrences_from (str | Unset):
        occurrences_to (str | Unset):
        is_kev (bool | Unset):
        total_count (GetAllFindingsTotalCount | Unset): The counting mode for the `X-Total-Count`
            response header. Default: GetAllFindingsTotalCount.EXACT.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | list[Finding]
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
            show_inactive=show_inactive,
            severity=severity,
            publish_date_from=publish_date_from,
            publish_date_to=publish_date_to,
            text_search_field=text_search_field,
            text_search_input=text_search_input,
            cvssv_2_from=cvssv_2_from,
            cvssv_2_to=cvssv_2_to,
            cvssv_3_from=cvssv_3_from,
            cvssv_3_to=cvssv_3_to,
            cvssv_4_from=cvssv_4_from,
            cvssv_4_to=cvssv_4_to,
            epss_from=epss_from,
            epss_to=epss_to,
            epss_percentile_from=epss_percentile_from,
            epss_percentile_to=epss_percentile_to,
            occurrences_from=occurrences_from,
            occurrences_to=occurrences_to,
            is_kev=is_kev,
            total_count=total_count,
        )
    ).parsed
