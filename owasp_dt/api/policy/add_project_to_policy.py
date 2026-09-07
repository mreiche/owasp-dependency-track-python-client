from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.policy import Policy
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    policy_uuid: UUID,
    project_uuid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/policy/{policy_uuid}/project/{project_uuid}".format(
            policy_uuid=quote(str(policy_uuid), safe=""),
            project_uuid=quote(str(project_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Policy | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = Policy.from_dict(response.json())

        return response_200

    if response.status_code == 304:
        response_304 = cast(Any, None)
        return response_304

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
) -> Response[Any | Policy | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    policy_uuid: UUID,
    project_uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Policy | ProblemDetails]:
    """Adds a project to a policy

     <p>Requires permission <strong>POLICY_MANAGEMENT</strong> or
    <strong>POLICY_MANAGEMENT_UPDATE</strong></p>

    Args:
        policy_uuid (UUID):
        project_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Policy | ProblemDetails]
    """

    kwargs = _get_kwargs(
        policy_uuid=policy_uuid,
        project_uuid=project_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    policy_uuid: UUID,
    project_uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | Policy | ProblemDetails | None:
    """Adds a project to a policy

     <p>Requires permission <strong>POLICY_MANAGEMENT</strong> or
    <strong>POLICY_MANAGEMENT_UPDATE</strong></p>

    Args:
        policy_uuid (UUID):
        project_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Policy | ProblemDetails
    """

    return sync_detailed(
        policy_uuid=policy_uuid,
        project_uuid=project_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    policy_uuid: UUID,
    project_uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Policy | ProblemDetails]:
    """Adds a project to a policy

     <p>Requires permission <strong>POLICY_MANAGEMENT</strong> or
    <strong>POLICY_MANAGEMENT_UPDATE</strong></p>

    Args:
        policy_uuid (UUID):
        project_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Policy | ProblemDetails]
    """

    kwargs = _get_kwargs(
        policy_uuid=policy_uuid,
        project_uuid=project_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    policy_uuid: UUID,
    project_uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | Policy | ProblemDetails | None:
    """Adds a project to a policy

     <p>Requires permission <strong>POLICY_MANAGEMENT</strong> or
    <strong>POLICY_MANAGEMENT_UPDATE</strong></p>

    Args:
        policy_uuid (UUID):
        project_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Policy | ProblemDetails
    """

    return (
        await asyncio_detailed(
            policy_uuid=policy_uuid,
            project_uuid=project_uuid,
            client=client,
        )
    ).parsed
