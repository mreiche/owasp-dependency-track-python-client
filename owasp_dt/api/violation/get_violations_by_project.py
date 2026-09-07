from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_violations_by_project_sort_order import (
    GetViolationsByProjectSortOrder,
)
from ...models.policy_violation import PolicyViolation
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetViolationsByProjectSortOrder | Unset = UNSET,
    suppressed: bool | Unset = UNSET,
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

    params["suppressed"] = suppressed

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/violation/project/{uuid}".format(
            uuid=quote(str(uuid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | list[PolicyViolation] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PolicyViolation.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

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
) -> Response[Any | ProblemDetails | list[PolicyViolation]]:
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
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetViolationsByProjectSortOrder | Unset = UNSET,
    suppressed: bool | Unset = UNSET,
) -> Response[Any | ProblemDetails | list[PolicyViolation]]:
    """Returns a list of all policy violations for a specific project

     <p>Requires permission <strong>VIEW_POLICY_VIOLATION</strong></p>

    Args:
        uuid (UUID):
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetViolationsByProjectSortOrder | Unset):
        suppressed (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | list[PolicyViolation]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        page_number=page_number,
        page_size=page_size,
        offset=offset,
        limit=limit,
        sort_name=sort_name,
        sort_order=sort_order,
        suppressed=suppressed,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetViolationsByProjectSortOrder | Unset = UNSET,
    suppressed: bool | Unset = UNSET,
) -> Any | ProblemDetails | list[PolicyViolation] | None:
    """Returns a list of all policy violations for a specific project

     <p>Requires permission <strong>VIEW_POLICY_VIOLATION</strong></p>

    Args:
        uuid (UUID):
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetViolationsByProjectSortOrder | Unset):
        suppressed (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | list[PolicyViolation]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        page_number=page_number,
        page_size=page_size,
        offset=offset,
        limit=limit,
        sort_name=sort_name,
        sort_order=sort_order,
        suppressed=suppressed,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetViolationsByProjectSortOrder | Unset = UNSET,
    suppressed: bool | Unset = UNSET,
) -> Response[Any | ProblemDetails | list[PolicyViolation]]:
    """Returns a list of all policy violations for a specific project

     <p>Requires permission <strong>VIEW_POLICY_VIOLATION</strong></p>

    Args:
        uuid (UUID):
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetViolationsByProjectSortOrder | Unset):
        suppressed (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | list[PolicyViolation]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        page_number=page_number,
        page_size=page_size,
        offset=offset,
        limit=limit,
        sort_name=sort_name,
        sort_order=sort_order,
        suppressed=suppressed,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    page_number: str | Unset = "1",
    page_size: str | Unset = "100",
    offset: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    sort_name: str | Unset = UNSET,
    sort_order: GetViolationsByProjectSortOrder | Unset = UNSET,
    suppressed: bool | Unset = UNSET,
) -> Any | ProblemDetails | list[PolicyViolation] | None:
    """Returns a list of all policy violations for a specific project

     <p>Requires permission <strong>VIEW_POLICY_VIOLATION</strong></p>

    Args:
        uuid (UUID):
        page_number (str | Unset):  Default: '1'.
        page_size (str | Unset):  Default: '100'.
        offset (str | Unset):
        limit (str | Unset):
        sort_name (str | Unset):
        sort_order (GetViolationsByProjectSortOrder | Unset):
        suppressed (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | list[PolicyViolation]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            page_number=page_number,
            page_size=page_size,
            offset=offset,
            limit=limit,
            sort_name=sort_name,
            sort_order=sort_order,
            suppressed=suppressed,
        )
    ).parsed
