from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.paginated_response import PaginatedResponse
from ...models.problem_details import ProblemDetails
from ...models.task_queue_type import TaskQueueType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    type_: TaskQueueType,
    *,
    limit: int | Unset = 100,
    page_token: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["page_token"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/internal/task-queues/{type_}".format(
            type_=quote(str(type_), safe=""),
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
    type_: TaskQueueType,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    page_token: str | Unset = UNSET,
) -> Response[PaginatedResponse | ProblemDetails]:
    """List task queues

     Returns a paginated list of task queues of the given type.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_READ` permission.

    Args:
        type_ (TaskQueueType):
        limit (int | Unset):  Default: 100.
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        type_=type_,
        limit=limit,
        page_token=page_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    type_: TaskQueueType,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    page_token: str | Unset = UNSET,
) -> PaginatedResponse | ProblemDetails | None:
    """List task queues

     Returns a paginated list of task queues of the given type.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_READ` permission.

    Args:
        type_ (TaskQueueType):
        limit (int | Unset):  Default: 100.
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponse | ProblemDetails
    """

    return sync_detailed(
        type_=type_,
        client=client,
        limit=limit,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    type_: TaskQueueType,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    page_token: str | Unset = UNSET,
) -> Response[PaginatedResponse | ProblemDetails]:
    """List task queues

     Returns a paginated list of task queues of the given type.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_READ` permission.

    Args:
        type_ (TaskQueueType):
        limit (int | Unset):  Default: 100.
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        type_=type_,
        limit=limit,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    type_: TaskQueueType,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    page_token: str | Unset = UNSET,
) -> PaginatedResponse | ProblemDetails | None:
    """List task queues

     Returns a paginated list of task queues of the given type.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_READ` permission.

    Args:
        type_ (TaskQueueType):
        limit (int | Unset):  Default: 100.
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponse | ProblemDetails
    """

    return (
        await asyncio_detailed(
            type_=type_,
            client=client,
            limit=limit,
            page_token=page_token,
        )
    ).parsed
