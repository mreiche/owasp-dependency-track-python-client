from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.policy_condition_response import PolicyConditionResponse
from ...models.update_policy_condition_request import UpdatePolicyConditionRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UpdatePolicyConditionRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/policy/condition",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PolicyConditionResponse | None:
    if response.status_code == 200:
        response_200 = PolicyConditionResponse.from_dict(response.json())

        return response_200

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
) -> Response[Any | PolicyConditionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdatePolicyConditionRequest | Unset = UNSET,
) -> Response[Any | PolicyConditionResponse]:
    """Updates a policy condition

     <p>
      Requires permission <strong>POLICY_MANAGEMENT</strong>
      or <strong>POLICY_MANAGEMENT_UPDATE</strong>
    </p>

    Args:
        body (UpdatePolicyConditionRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PolicyConditionResponse]
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
    body: UpdatePolicyConditionRequest | Unset = UNSET,
) -> Any | PolicyConditionResponse | None:
    """Updates a policy condition

     <p>
      Requires permission <strong>POLICY_MANAGEMENT</strong>
      or <strong>POLICY_MANAGEMENT_UPDATE</strong>
    </p>

    Args:
        body (UpdatePolicyConditionRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PolicyConditionResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdatePolicyConditionRequest | Unset = UNSET,
) -> Response[Any | PolicyConditionResponse]:
    """Updates a policy condition

     <p>
      Requires permission <strong>POLICY_MANAGEMENT</strong>
      or <strong>POLICY_MANAGEMENT_UPDATE</strong>
    </p>

    Args:
        body (UpdatePolicyConditionRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PolicyConditionResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UpdatePolicyConditionRequest | Unset = UNSET,
) -> Any | PolicyConditionResponse | None:
    """Updates a policy condition

     <p>
      Requires permission <strong>POLICY_MANAGEMENT</strong>
      or <strong>POLICY_MANAGEMENT_UPDATE</strong>
    </p>

    Args:
        body (UpdatePolicyConditionRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PolicyConditionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
