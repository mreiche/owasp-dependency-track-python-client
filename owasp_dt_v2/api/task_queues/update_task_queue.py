from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.task_queue_type import TaskQueueType
from ...models.update_task_queue_request import UpdateTaskQueueRequest
from ...types import Response


def _get_kwargs(
    type_: TaskQueueType,
    name: str,
    *,
    body: UpdateTaskQueueRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/internal/task-queues/{type_}/{name}".format(
            type_=quote(str(type_), safe=""),
            name=quote(str(name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = ProblemDetails.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404

    response_default = ProblemDetails.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    type_: TaskQueueType,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateTaskQueueRequest,
) -> Response[Any | ProblemDetails]:
    """Update a task queue

     Updates the status and/or capacity of a task queue.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_UPDATE` permission.

    Args:
        type_ (TaskQueueType):
        name (str):
        body (UpdateTaskQueueRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        type_=type_,
        name=name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    type_: TaskQueueType,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateTaskQueueRequest,
) -> Any | ProblemDetails | None:
    """Update a task queue

     Updates the status and/or capacity of a task queue.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_UPDATE` permission.

    Args:
        type_ (TaskQueueType):
        name (str):
        body (UpdateTaskQueueRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return sync_detailed(
        type_=type_,
        name=name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    type_: TaskQueueType,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateTaskQueueRequest,
) -> Response[Any | ProblemDetails]:
    """Update a task queue

     Updates the status and/or capacity of a task queue.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_UPDATE` permission.

    Args:
        type_ (TaskQueueType):
        name (str):
        body (UpdateTaskQueueRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        type_=type_,
        name=name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    type_: TaskQueueType,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateTaskQueueRequest,
) -> Any | ProblemDetails | None:
    """Update a task queue

     Updates the status and/or capacity of a task queue.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_UPDATE` permission.

    Args:
        type_ (TaskQueueType):
        name (str):
        body (UpdateTaskQueueRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return (
        await asyncio_detailed(
            type_=type_,
            name=name,
            client=client,
            body=body,
        )
    ).parsed
