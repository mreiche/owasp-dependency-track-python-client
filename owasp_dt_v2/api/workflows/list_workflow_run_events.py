from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.paginated_response import PaginatedResponse
from ...models.problem_details import ProblemDetails
from ...models.sort_direction import SortDirection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    from_sequence_number: int | Unset = UNSET,
    limit: int | Unset = 100,
    page_token: str | Unset = UNSET,
    sort_direction: SortDirection | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["from_sequence_number"] = from_sequence_number

    params["limit"] = limit

    params["page_token"] = page_token

    json_sort_direction: str | Unset = UNSET
    if not isinstance(sort_direction, Unset):
        json_sort_direction = sort_direction.value

    params["sort_direction"] = json_sort_direction

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/internal/workflow-runs/{id}/events".format(
            id=quote(str(id), safe=""),
        ),
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
        response_400 = ProblemDetails.from_dict(response.json())

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
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_sequence_number: int | Unset = UNSET,
    limit: int | Unset = 100,
    page_token: str | Unset = UNSET,
    sort_direction: SortDirection | Unset = UNSET,
) -> Response[PaginatedResponse | ProblemDetails]:
    """List all events of a workflow run

     Returns a paginated list of workflow run events, sorted by sequence number.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_READ` permission.

    Args:
        id (UUID):
        from_sequence_number (int | Unset):
        limit (int | Unset):  Default: 100.
        page_token (str | Unset):
        sort_direction (SortDirection | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        id=id,
        from_sequence_number=from_sequence_number,
        limit=limit,
        page_token=page_token,
        sort_direction=sort_direction,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_sequence_number: int | Unset = UNSET,
    limit: int | Unset = 100,
    page_token: str | Unset = UNSET,
    sort_direction: SortDirection | Unset = UNSET,
) -> PaginatedResponse | ProblemDetails | None:
    """List all events of a workflow run

     Returns a paginated list of workflow run events, sorted by sequence number.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_READ` permission.

    Args:
        id (UUID):
        from_sequence_number (int | Unset):
        limit (int | Unset):  Default: 100.
        page_token (str | Unset):
        sort_direction (SortDirection | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponse | ProblemDetails
    """

    return sync_detailed(
        id=id,
        client=client,
        from_sequence_number=from_sequence_number,
        limit=limit,
        page_token=page_token,
        sort_direction=sort_direction,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_sequence_number: int | Unset = UNSET,
    limit: int | Unset = 100,
    page_token: str | Unset = UNSET,
    sort_direction: SortDirection | Unset = UNSET,
) -> Response[PaginatedResponse | ProblemDetails]:
    """List all events of a workflow run

     Returns a paginated list of workflow run events, sorted by sequence number.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_READ` permission.

    Args:
        id (UUID):
        from_sequence_number (int | Unset):
        limit (int | Unset):  Default: 100.
        page_token (str | Unset):
        sort_direction (SortDirection | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        id=id,
        from_sequence_number=from_sequence_number,
        limit=limit,
        page_token=page_token,
        sort_direction=sort_direction,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_sequence_number: int | Unset = UNSET,
    limit: int | Unset = 100,
    page_token: str | Unset = UNSET,
    sort_direction: SortDirection | Unset = UNSET,
) -> PaginatedResponse | ProblemDetails | None:
    """List all events of a workflow run

     Returns a paginated list of workflow run events, sorted by sequence number.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_READ` permission.

    Args:
        id (UUID):
        from_sequence_number (int | Unset):
        limit (int | Unset):  Default: 100.
        page_token (str | Unset):
        sort_direction (SortDirection | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponse | ProblemDetails
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            from_sequence_number=from_sequence_number,
            limit=limit,
            page_token=page_token,
            sort_direction=sort_direction,
        )
    ).parsed
