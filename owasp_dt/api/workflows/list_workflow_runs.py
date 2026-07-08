from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.paginated_response import PaginatedResponse
from ...models.problem_details import ProblemDetails
from ...models.sort_direction import SortDirection
from ...models.workflow_run_status import WorkflowRunStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    workflow_name: str | Unset = UNSET,
    workflow_version: int | Unset = UNSET,
    workflow_instance_id: str | Unset = UNSET,
    status: WorkflowRunStatus | Unset = UNSET,
    label: list[str] | Unset = UNSET,
    created_since: int | Unset = UNSET,
    created_before: int | Unset = UNSET,
    completed_since: int | Unset = UNSET,
    completed_before: int | Unset = UNSET,
    limit: int | Unset = 100,
    page_token: str | Unset = UNSET,
    sort_direction: SortDirection | Unset = UNSET,
    sort_by: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["workflow_name"] = workflow_name

    params["workflow_version"] = workflow_version

    params["workflow_instance_id"] = workflow_instance_id

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_label: list[str] | Unset = UNSET
    if not isinstance(label, Unset):
        json_label = label

    params["label"] = json_label

    params["created_since"] = created_since

    params["created_before"] = created_before

    params["completed_since"] = completed_since

    params["completed_before"] = completed_before

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
        "url": "/internal/workflow-runs",
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
    workflow_name: str | Unset = UNSET,
    workflow_version: int | Unset = UNSET,
    workflow_instance_id: str | Unset = UNSET,
    status: WorkflowRunStatus | Unset = UNSET,
    label: list[str] | Unset = UNSET,
    created_since: int | Unset = UNSET,
    created_before: int | Unset = UNSET,
    completed_since: int | Unset = UNSET,
    completed_before: int | Unset = UNSET,
    limit: int | Unset = 100,
    page_token: str | Unset = UNSET,
    sort_direction: SortDirection | Unset = UNSET,
    sort_by: str | Unset = UNSET,
) -> Response[PaginatedResponse | ProblemDetails]:
    """List all workflow runs

     Returns a paginated list of workflow runs.

    ### Sortable fields

    Sorting is supported for the for the following fields:

    * `id`
    * `created_at`
    * `completed_at`

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_READ` permission.

    Args:
        workflow_name (str | Unset):
        workflow_version (int | Unset):
        workflow_instance_id (str | Unset):
        status (WorkflowRunStatus | Unset):
        label (list[str] | Unset):
        created_since (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC.
            Example: 1752209050377.
        created_before (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC.
            Example: 1752209050377.
        completed_since (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC.
            Example: 1752209050377.
        completed_before (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC.
            Example: 1752209050377.
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
        workflow_name=workflow_name,
        workflow_version=workflow_version,
        workflow_instance_id=workflow_instance_id,
        status=status,
        label=label,
        created_since=created_since,
        created_before=created_before,
        completed_since=completed_since,
        completed_before=completed_before,
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
    workflow_name: str | Unset = UNSET,
    workflow_version: int | Unset = UNSET,
    workflow_instance_id: str | Unset = UNSET,
    status: WorkflowRunStatus | Unset = UNSET,
    label: list[str] | Unset = UNSET,
    created_since: int | Unset = UNSET,
    created_before: int | Unset = UNSET,
    completed_since: int | Unset = UNSET,
    completed_before: int | Unset = UNSET,
    limit: int | Unset = 100,
    page_token: str | Unset = UNSET,
    sort_direction: SortDirection | Unset = UNSET,
    sort_by: str | Unset = UNSET,
) -> PaginatedResponse | ProblemDetails | None:
    """List all workflow runs

     Returns a paginated list of workflow runs.

    ### Sortable fields

    Sorting is supported for the for the following fields:

    * `id`
    * `created_at`
    * `completed_at`

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_READ` permission.

    Args:
        workflow_name (str | Unset):
        workflow_version (int | Unset):
        workflow_instance_id (str | Unset):
        status (WorkflowRunStatus | Unset):
        label (list[str] | Unset):
        created_since (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC.
            Example: 1752209050377.
        created_before (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC.
            Example: 1752209050377.
        completed_since (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC.
            Example: 1752209050377.
        completed_before (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC.
            Example: 1752209050377.
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
        workflow_name=workflow_name,
        workflow_version=workflow_version,
        workflow_instance_id=workflow_instance_id,
        status=status,
        label=label,
        created_since=created_since,
        created_before=created_before,
        completed_since=completed_since,
        completed_before=completed_before,
        limit=limit,
        page_token=page_token,
        sort_direction=sort_direction,
        sort_by=sort_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    workflow_name: str | Unset = UNSET,
    workflow_version: int | Unset = UNSET,
    workflow_instance_id: str | Unset = UNSET,
    status: WorkflowRunStatus | Unset = UNSET,
    label: list[str] | Unset = UNSET,
    created_since: int | Unset = UNSET,
    created_before: int | Unset = UNSET,
    completed_since: int | Unset = UNSET,
    completed_before: int | Unset = UNSET,
    limit: int | Unset = 100,
    page_token: str | Unset = UNSET,
    sort_direction: SortDirection | Unset = UNSET,
    sort_by: str | Unset = UNSET,
) -> Response[PaginatedResponse | ProblemDetails]:
    """List all workflow runs

     Returns a paginated list of workflow runs.

    ### Sortable fields

    Sorting is supported for the for the following fields:

    * `id`
    * `created_at`
    * `completed_at`

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_READ` permission.

    Args:
        workflow_name (str | Unset):
        workflow_version (int | Unset):
        workflow_instance_id (str | Unset):
        status (WorkflowRunStatus | Unset):
        label (list[str] | Unset):
        created_since (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC.
            Example: 1752209050377.
        created_before (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC.
            Example: 1752209050377.
        completed_since (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC.
            Example: 1752209050377.
        completed_before (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC.
            Example: 1752209050377.
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
        workflow_name=workflow_name,
        workflow_version=workflow_version,
        workflow_instance_id=workflow_instance_id,
        status=status,
        label=label,
        created_since=created_since,
        created_before=created_before,
        completed_since=completed_since,
        completed_before=completed_before,
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
    workflow_name: str | Unset = UNSET,
    workflow_version: int | Unset = UNSET,
    workflow_instance_id: str | Unset = UNSET,
    status: WorkflowRunStatus | Unset = UNSET,
    label: list[str] | Unset = UNSET,
    created_since: int | Unset = UNSET,
    created_before: int | Unset = UNSET,
    completed_since: int | Unset = UNSET,
    completed_before: int | Unset = UNSET,
    limit: int | Unset = 100,
    page_token: str | Unset = UNSET,
    sort_direction: SortDirection | Unset = UNSET,
    sort_by: str | Unset = UNSET,
) -> PaginatedResponse | ProblemDetails | None:
    """List all workflow runs

     Returns a paginated list of workflow runs.

    ### Sortable fields

    Sorting is supported for the for the following fields:

    * `id`
    * `created_at`
    * `completed_at`

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_READ` permission.

    Args:
        workflow_name (str | Unset):
        workflow_version (int | Unset):
        workflow_instance_id (str | Unset):
        status (WorkflowRunStatus | Unset):
        label (list[str] | Unset):
        created_since (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC.
            Example: 1752209050377.
        created_before (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC.
            Example: 1752209050377.
        completed_since (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC.
            Example: 1752209050377.
        completed_before (int | Unset): Epoch timestamp in milliseconds since January 1, 1970 UTC.
            Example: 1752209050377.
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
            workflow_name=workflow_name,
            workflow_version=workflow_version,
            workflow_instance_id=workflow_instance_id,
            status=status,
            label=label,
            created_since=created_since,
            created_before=created_before,
            completed_since=completed_since,
            completed_before=completed_before,
            limit=limit,
            page_token=page_token,
            sort_direction=sort_direction,
            sort_by=sort_by,
        )
    ).parsed
