from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_oauth_token_request import CreateOauthTokenRequest
from ...models.create_oauth_token_response import CreateOauthTokenResponse
from ...models.oauth_token_error import OauthTokenError
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    *,
    body: CreateOauthTokenRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/oauth/token",
    }

    _kwargs["data"] = body.to_dict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateOauthTokenResponse | OauthTokenError | ProblemDetails:
    if response.status_code == 200:
        response_200 = CreateOauthTokenResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = OauthTokenError.from_dict(response.json())

        return response_400

    if response.status_code == 503:
        response_503 = ProblemDetails.from_dict(response.json())

        return response_503

    response_default = ProblemDetails.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateOauthTokenResponse | OauthTokenError | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateOauthTokenRequest,
) -> Response[CreateOauthTokenResponse | OauthTokenError | ProblemDetails]:
    """Create a Dependency-Track access token

     Creates an access token for the requested grant.

    The access token is an opaque session token. Send it in the `Authorization` header,
    as `Bearer <access_token>`. `scope` is not supported.

    The only grant supported is RFC 8693 token exchange, which requires `subject_token` and
    `subject_token_type`.
    Exchanges for a session of a service account also require `workload_identity_provider` and
    `service_account`,
    and succeed when a binding of the requested service account matches the subject token.
    The resulting session has all permissions of the service account.

    Args:
        body (CreateOauthTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOauthTokenResponse | OauthTokenError | ProblemDetails]
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
    client: AuthenticatedClient | Client,
    body: CreateOauthTokenRequest,
) -> CreateOauthTokenResponse | OauthTokenError | ProblemDetails | None:
    """Create a Dependency-Track access token

     Creates an access token for the requested grant.

    The access token is an opaque session token. Send it in the `Authorization` header,
    as `Bearer <access_token>`. `scope` is not supported.

    The only grant supported is RFC 8693 token exchange, which requires `subject_token` and
    `subject_token_type`.
    Exchanges for a session of a service account also require `workload_identity_provider` and
    `service_account`,
    and succeed when a binding of the requested service account matches the subject token.
    The resulting session has all permissions of the service account.

    Args:
        body (CreateOauthTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOauthTokenResponse | OauthTokenError | ProblemDetails
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateOauthTokenRequest,
) -> Response[CreateOauthTokenResponse | OauthTokenError | ProblemDetails]:
    """Create a Dependency-Track access token

     Creates an access token for the requested grant.

    The access token is an opaque session token. Send it in the `Authorization` header,
    as `Bearer <access_token>`. `scope` is not supported.

    The only grant supported is RFC 8693 token exchange, which requires `subject_token` and
    `subject_token_type`.
    Exchanges for a session of a service account also require `workload_identity_provider` and
    `service_account`,
    and succeed when a binding of the requested service account matches the subject token.
    The resulting session has all permissions of the service account.

    Args:
        body (CreateOauthTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOauthTokenResponse | OauthTokenError | ProblemDetails]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateOauthTokenRequest,
) -> CreateOauthTokenResponse | OauthTokenError | ProblemDetails | None:
    """Create a Dependency-Track access token

     Creates an access token for the requested grant.

    The access token is an opaque session token. Send it in the `Authorization` header,
    as `Bearer <access_token>`. `scope` is not supported.

    The only grant supported is RFC 8693 token exchange, which requires `subject_token` and
    `subject_token_type`.
    Exchanges for a session of a service account also require `workload_identity_provider` and
    `service_account`,
    and succeed when a binding of the requested service account matches the subject token.
    The resulting session has all permissions of the service account.

    Args:
        body (CreateOauthTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOauthTokenResponse | OauthTokenError | ProblemDetails
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
