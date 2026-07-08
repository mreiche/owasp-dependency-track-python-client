from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bom_upload_response import BomUploadResponse
from ...models.clone_project_request import CloneProjectRequest
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CloneProjectRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/project/clone",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BomUploadResponse | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = BomUploadResponse.from_dict(response.json())

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
) -> Response[Any | BomUploadResponse | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CloneProjectRequest | Unset = UNSET,
) -> Response[Any | BomUploadResponse | ProblemDetails]:
    """Clones a project

     <p>Requires permission <strong>PORTFOLIO_MANAGEMENT</strong> or
    <strong>PORTFOLIO_MANAGEMENT_CREATE</strong></p>
    <p><strong>Deprecated</strong>! Use <code>/api/v2/projects/{uuid}/clone</code> instead.</p>

    Args:
        body (CloneProjectRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BomUploadResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CloneProjectRequest | Unset = UNSET,
) -> Any | BomUploadResponse | ProblemDetails | None:
    """Clones a project

     <p>Requires permission <strong>PORTFOLIO_MANAGEMENT</strong> or
    <strong>PORTFOLIO_MANAGEMENT_CREATE</strong></p>
    <p><strong>Deprecated</strong>! Use <code>/api/v2/projects/{uuid}/clone</code> instead.</p>

    Args:
        body (CloneProjectRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BomUploadResponse | ProblemDetails
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CloneProjectRequest | Unset = UNSET,
) -> Response[Any | BomUploadResponse | ProblemDetails]:
    """Clones a project

     <p>Requires permission <strong>PORTFOLIO_MANAGEMENT</strong> or
    <strong>PORTFOLIO_MANAGEMENT_CREATE</strong></p>
    <p><strong>Deprecated</strong>! Use <code>/api/v2/projects/{uuid}/clone</code> instead.</p>

    Args:
        body (CloneProjectRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BomUploadResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CloneProjectRequest | Unset = UNSET,
) -> Any | BomUploadResponse | ProblemDetails | None:
    """Clones a project

     <p>Requires permission <strong>PORTFOLIO_MANAGEMENT</strong> or
    <strong>PORTFOLIO_MANAGEMENT_CREATE</strong></p>
    <p><strong>Deprecated</strong>! Use <code>/api/v2/projects/{uuid}/clone</code> instead.</p>

    Args:
        body (CloneProjectRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BomUploadResponse | ProblemDetails
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
