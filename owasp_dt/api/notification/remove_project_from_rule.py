from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.notification_rule import NotificationRule
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    rule_uuid: UUID,
    project_uuid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/notification/rule/{rule_uuid}/project/{project_uuid}".format(
            rule_uuid=quote(str(rule_uuid), safe=""),
            project_uuid=quote(str(project_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | NotificationRule | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = NotificationRule.from_dict(response.json())

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
) -> Response[Any | NotificationRule | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    rule_uuid: UUID,
    project_uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any | NotificationRule | ProblemDetails]:
    """Removes a project from a notification rule

     <p>Requires permission <strong>SYSTEM_CONFIGURATION</strong> or
    <strong>SYSTEM_CONFIGURATION_DELETE</strong></p>

    Args:
        rule_uuid (UUID):
        project_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | NotificationRule | ProblemDetails]
    """

    kwargs = _get_kwargs(
        rule_uuid=rule_uuid,
        project_uuid=project_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    rule_uuid: UUID,
    project_uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | NotificationRule | ProblemDetails | None:
    """Removes a project from a notification rule

     <p>Requires permission <strong>SYSTEM_CONFIGURATION</strong> or
    <strong>SYSTEM_CONFIGURATION_DELETE</strong></p>

    Args:
        rule_uuid (UUID):
        project_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | NotificationRule | ProblemDetails
    """

    return sync_detailed(
        rule_uuid=rule_uuid,
        project_uuid=project_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    rule_uuid: UUID,
    project_uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any | NotificationRule | ProblemDetails]:
    """Removes a project from a notification rule

     <p>Requires permission <strong>SYSTEM_CONFIGURATION</strong> or
    <strong>SYSTEM_CONFIGURATION_DELETE</strong></p>

    Args:
        rule_uuid (UUID):
        project_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | NotificationRule | ProblemDetails]
    """

    kwargs = _get_kwargs(
        rule_uuid=rule_uuid,
        project_uuid=project_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    rule_uuid: UUID,
    project_uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | NotificationRule | ProblemDetails | None:
    """Removes a project from a notification rule

     <p>Requires permission <strong>SYSTEM_CONFIGURATION</strong> or
    <strong>SYSTEM_CONFIGURATION_DELETE</strong></p>

    Args:
        rule_uuid (UUID):
        project_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | NotificationRule | ProblemDetails
    """

    return (
        await asyncio_detailed(
            rule_uuid=rule_uuid,
            project_uuid=project_uuid,
            client=client,
        )
    ).parsed
