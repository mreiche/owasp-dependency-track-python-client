from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    team_uuid: UUID,
    project_uuid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/acl/mapping/team/{team_uuid}/project/{project_uuid}".format(
            team_uuid=quote(str(team_uuid), safe=""),
            project_uuid=quote(str(project_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


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
    team_uuid: UUID,
    project_uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ProblemDetails]:
    """Removes an ACL mapping

     <p>Requires permission <strong>ACCESS_MANAGEMENT</strong> or
    <strong>ACCESS_MANAGEMENT_DELETE</strong></p>

    Args:
        team_uuid (UUID):
        project_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        team_uuid=team_uuid,
        project_uuid=project_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    team_uuid: UUID,
    project_uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | ProblemDetails | None:
    """Removes an ACL mapping

     <p>Requires permission <strong>ACCESS_MANAGEMENT</strong> or
    <strong>ACCESS_MANAGEMENT_DELETE</strong></p>

    Args:
        team_uuid (UUID):
        project_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return sync_detailed(
        team_uuid=team_uuid,
        project_uuid=project_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    team_uuid: UUID,
    project_uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ProblemDetails]:
    """Removes an ACL mapping

     <p>Requires permission <strong>ACCESS_MANAGEMENT</strong> or
    <strong>ACCESS_MANAGEMENT_DELETE</strong></p>

    Args:
        team_uuid (UUID):
        project_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        team_uuid=team_uuid,
        project_uuid=project_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_uuid: UUID,
    project_uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | ProblemDetails | None:
    """Removes an ACL mapping

     <p>Requires permission <strong>ACCESS_MANAGEMENT</strong> or
    <strong>ACCESS_MANAGEMENT_DELETE</strong></p>

    Args:
        team_uuid (UUID):
        project_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return (
        await asyncio_detailed(
            team_uuid=team_uuid,
            project_uuid=project_uuid,
            client=client,
        )
    ).parsed
