from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.project import Project
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: Project | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/project/{uuid}".format(
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
) -> Any | ProblemDetails | Project | None:
    if response.status_code == 200:
        response_200 = Project.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
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

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ProblemDetails | Project]:
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
    body: Project | Unset = UNSET,
) -> Response[Any | ProblemDetails | Project]:
    """Partially updates a project

     <p>
      To re-parent the project, set <code>parent</code> to an object containing
      the new parent's <code>uuid</code>. Omit <code>parent</code> (or set it to
      <code>null</code>) to leave the parent unchanged. Providing <code>parent</code>
      without a non-null <code>uuid</code> is rejected with 400.
    </p>
    <p>Requires permission <strong>PORTFOLIO_MANAGEMENT</strong> or
    <strong>PORTFOLIO_MANAGEMENT_UPDATE</strong></p>

    Args:
        uuid (UUID):
        body (Project | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | Project]
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
    client: AuthenticatedClient,
    body: Project | Unset = UNSET,
) -> Any | ProblemDetails | Project | None:
    """Partially updates a project

     <p>
      To re-parent the project, set <code>parent</code> to an object containing
      the new parent's <code>uuid</code>. Omit <code>parent</code> (or set it to
      <code>null</code>) to leave the parent unchanged. Providing <code>parent</code>
      without a non-null <code>uuid</code> is rejected with 400.
    </p>
    <p>Requires permission <strong>PORTFOLIO_MANAGEMENT</strong> or
    <strong>PORTFOLIO_MANAGEMENT_UPDATE</strong></p>

    Args:
        uuid (UUID):
        body (Project | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | Project
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: Project | Unset = UNSET,
) -> Response[Any | ProblemDetails | Project]:
    """Partially updates a project

     <p>
      To re-parent the project, set <code>parent</code> to an object containing
      the new parent's <code>uuid</code>. Omit <code>parent</code> (or set it to
      <code>null</code>) to leave the parent unchanged. Providing <code>parent</code>
      without a non-null <code>uuid</code> is rejected with 400.
    </p>
    <p>Requires permission <strong>PORTFOLIO_MANAGEMENT</strong> or
    <strong>PORTFOLIO_MANAGEMENT_UPDATE</strong></p>

    Args:
        uuid (UUID):
        body (Project | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | Project]
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
    client: AuthenticatedClient,
    body: Project | Unset = UNSET,
) -> Any | ProblemDetails | Project | None:
    """Partially updates a project

     <p>
      To re-parent the project, set <code>parent</code> to an object containing
      the new parent's <code>uuid</code>. Omit <code>parent</code> (or set it to
      <code>null</code>) to leave the parent unchanged. Providing <code>parent</code>
      without a non-null <code>uuid</code> is rejected with 400.
    </p>
    <p>Requires permission <strong>PORTFOLIO_MANAGEMENT</strong> or
    <strong>PORTFOLIO_MANAGEMENT_UPDATE</strong></p>

    Args:
        uuid (UUID):
        body (Project | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | Project
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
