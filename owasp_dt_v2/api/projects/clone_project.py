from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.clone_project_request import CloneProjectRequest
from ...models.clone_project_response import CloneProjectResponse
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: CloneProjectRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{uuid}/clone".format(
            uuid=quote(str(uuid), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CloneProjectResponse | ProblemDetails:
    if response.status_code == 201:
        response_201 = CloneProjectResponse.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = ProblemDetails.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ProblemDetails.from_dict(response.json())

        return response_409

    response_default = ProblemDetails.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CloneProjectResponse | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CloneProjectRequest | Unset = UNSET,
) -> Response[CloneProjectResponse | ProblemDetails]:
    """Clones a given project.

     Requires permission `PORTFOLIO_MANAGEMENT` or `PORTFOLIO_MANAGEMENT_CREATE`

    Args:
        uuid (UUID):
        body (CloneProjectRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloneProjectResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CloneProjectRequest | Unset = UNSET,
) -> CloneProjectResponse | ProblemDetails | None:
    """Clones a given project.

     Requires permission `PORTFOLIO_MANAGEMENT` or `PORTFOLIO_MANAGEMENT_CREATE`

    Args:
        uuid (UUID):
        body (CloneProjectRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloneProjectResponse | ProblemDetails
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CloneProjectRequest | Unset = UNSET,
) -> Response[CloneProjectResponse | ProblemDetails]:
    """Clones a given project.

     Requires permission `PORTFOLIO_MANAGEMENT` or `PORTFOLIO_MANAGEMENT_CREATE`

    Args:
        uuid (UUID):
        body (CloneProjectRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloneProjectResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CloneProjectRequest | Unset = UNSET,
) -> CloneProjectResponse | ProblemDetails | None:
    """Clones a given project.

     Requires permission `PORTFOLIO_MANAGEMENT` or `PORTFOLIO_MANAGEMENT_CREATE`

    Args:
        uuid (UUID):
        body (CloneProjectRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloneProjectResponse | ProblemDetails
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
