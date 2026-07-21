from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.project import Project
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Project | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/project",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | Project | None:
    if response.status_code == 201:
        response_201 = Project.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403

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
    *,
    client: AuthenticatedClient,
    body: Project | Unset = UNSET,
) -> Response[Any | ProblemDetails | Project]:
    """Creates a new project

     <p>
      To create the project under a parent, set <code>parent</code> to an object
      containing the parent's <code>uuid</code>. To create a top-level project,
      omit <code>parent</code> or set it to <code>null</code>. Providing
      <code>parent</code> without a non-null <code>uuid</code> is rejected with 400.
    </p>
    <p>
      When portfolio access control is enabled, one or more teams to grant access
      to can be provided via <code>accessTeams</code>. Either <code>uuid</code> or
      <code>name</code> of a team must be specified. Only teams which the authenticated
      principal is a member of can be assigned. Principals with <strong>ACCESS_MANAGEMENT</strong>
      permission can assign <em>any</em> team.
    </p>
    <p>Requires permission <strong>PORTFOLIO_MANAGEMENT</strong> or
    <strong>PORTFOLIO_MANAGEMENT_CREATE</strong></p>

    Args:
        body (Project | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | Project]
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
    body: Project | Unset = UNSET,
) -> Any | ProblemDetails | Project | None:
    """Creates a new project

     <p>
      To create the project under a parent, set <code>parent</code> to an object
      containing the parent's <code>uuid</code>. To create a top-level project,
      omit <code>parent</code> or set it to <code>null</code>. Providing
      <code>parent</code> without a non-null <code>uuid</code> is rejected with 400.
    </p>
    <p>
      When portfolio access control is enabled, one or more teams to grant access
      to can be provided via <code>accessTeams</code>. Either <code>uuid</code> or
      <code>name</code> of a team must be specified. Only teams which the authenticated
      principal is a member of can be assigned. Principals with <strong>ACCESS_MANAGEMENT</strong>
      permission can assign <em>any</em> team.
    </p>
    <p>Requires permission <strong>PORTFOLIO_MANAGEMENT</strong> or
    <strong>PORTFOLIO_MANAGEMENT_CREATE</strong></p>

    Args:
        body (Project | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | Project
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Project | Unset = UNSET,
) -> Response[Any | ProblemDetails | Project]:
    """Creates a new project

     <p>
      To create the project under a parent, set <code>parent</code> to an object
      containing the parent's <code>uuid</code>. To create a top-level project,
      omit <code>parent</code> or set it to <code>null</code>. Providing
      <code>parent</code> without a non-null <code>uuid</code> is rejected with 400.
    </p>
    <p>
      When portfolio access control is enabled, one or more teams to grant access
      to can be provided via <code>accessTeams</code>. Either <code>uuid</code> or
      <code>name</code> of a team must be specified. Only teams which the authenticated
      principal is a member of can be assigned. Principals with <strong>ACCESS_MANAGEMENT</strong>
      permission can assign <em>any</em> team.
    </p>
    <p>Requires permission <strong>PORTFOLIO_MANAGEMENT</strong> or
    <strong>PORTFOLIO_MANAGEMENT_CREATE</strong></p>

    Args:
        body (Project | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | Project]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Project | Unset = UNSET,
) -> Any | ProblemDetails | Project | None:
    """Creates a new project

     <p>
      To create the project under a parent, set <code>parent</code> to an object
      containing the parent's <code>uuid</code>. To create a top-level project,
      omit <code>parent</code> or set it to <code>null</code>. Providing
      <code>parent</code> without a non-null <code>uuid</code> is rejected with 400.
    </p>
    <p>
      When portfolio access control is enabled, one or more teams to grant access
      to can be provided via <code>accessTeams</code>. Either <code>uuid</code> or
      <code>name</code> of a team must be specified. Only teams which the authenticated
      principal is a member of can be assigned. Principals with <strong>ACCESS_MANAGEMENT</strong>
      permission can assign <em>any</em> team.
    </p>
    <p>Requires permission <strong>PORTFOLIO_MANAGEMENT</strong> or
    <strong>PORTFOLIO_MANAGEMENT_CREATE</strong></p>

    Args:
        body (Project | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | Project
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
