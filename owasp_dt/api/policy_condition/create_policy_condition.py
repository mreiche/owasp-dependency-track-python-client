from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.policy_condition import PolicyCondition
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: PolicyCondition | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/policy/{uuid}/condition".format(
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
) -> Any | PolicyCondition | None:
    if response.status_code == 201:
        response_201 = PolicyCondition.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PolicyCondition]:
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
    body: PolicyCondition | Unset = UNSET,
) -> Response[Any | PolicyCondition]:
    """Creates a new policy condition for an existing policy

     <p>Requires permission <strong>POLICY_MANAGEMENT</strong> or
    <strong>POLICY_MANAGEMENT_UPDATE</strong></p>

    Args:
        uuid (UUID):
        body (PolicyCondition | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PolicyCondition]
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
    body: PolicyCondition | Unset = UNSET,
) -> Any | PolicyCondition | None:
    """Creates a new policy condition for an existing policy

     <p>Requires permission <strong>POLICY_MANAGEMENT</strong> or
    <strong>POLICY_MANAGEMENT_UPDATE</strong></p>

    Args:
        uuid (UUID):
        body (PolicyCondition | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PolicyCondition
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
    body: PolicyCondition | Unset = UNSET,
) -> Response[Any | PolicyCondition]:
    """Creates a new policy condition for an existing policy

     <p>Requires permission <strong>POLICY_MANAGEMENT</strong> or
    <strong>POLICY_MANAGEMENT_UPDATE</strong></p>

    Args:
        uuid (UUID):
        body (PolicyCondition | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PolicyCondition]
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
    body: PolicyCondition | Unset = UNSET,
) -> Any | PolicyCondition | None:
    """Creates a new policy condition for an existing policy

     <p>Requires permission <strong>POLICY_MANAGEMENT</strong> or
    <strong>POLICY_MANAGEMENT_UPDATE</strong></p>

    Args:
        uuid (UUID):
        body (PolicyCondition | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PolicyCondition
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
