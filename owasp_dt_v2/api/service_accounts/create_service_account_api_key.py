from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_service_account_api_key_request import (
    CreateServiceAccountApiKeyRequest,
)
from ...models.create_service_account_api_key_response import (
    CreateServiceAccountApiKeyResponse,
)
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    name: str,
    *,
    body: CreateServiceAccountApiKeyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/service-accounts/{name}/api-keys".format(
            name=quote(str(name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateServiceAccountApiKeyResponse | ProblemDetails:
    if response.status_code == 201:
        response_201 = CreateServiceAccountApiKeyResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:

        def _parse_response_400(data: object) -> ProblemDetails:
            if not isinstance(data, dict):
                raise TypeError()
            response_400_type_0 = ProblemDetails.from_dict(data)

            return response_400_type_0

        response_400 = _parse_response_400(response.json())

        return response_400

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
) -> Response[CreateServiceAccountApiKeyResponse | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateServiceAccountApiKeyRequest,
) -> Response[CreateServiceAccountApiKeyResponse | ProblemDetails]:
    """Create an API key for a service account

     Creates a new API key owned by the given service account.

    The plain text key is returned exactly once, in the response body.
    It cannot be retrieved afterwards, because only its hash is stored.

    No API keys can be created for a suspended service account.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_CREATE` permission.

    Args:
        name (str): The name of the service account, without the reserved `svc:` prefix. Example:
            ci-pipeline.
        body (CreateServiceAccountApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateServiceAccountApiKeyResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateServiceAccountApiKeyRequest,
) -> CreateServiceAccountApiKeyResponse | ProblemDetails | None:
    """Create an API key for a service account

     Creates a new API key owned by the given service account.

    The plain text key is returned exactly once, in the response body.
    It cannot be retrieved afterwards, because only its hash is stored.

    No API keys can be created for a suspended service account.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_CREATE` permission.

    Args:
        name (str): The name of the service account, without the reserved `svc:` prefix. Example:
            ci-pipeline.
        body (CreateServiceAccountApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateServiceAccountApiKeyResponse | ProblemDetails
    """

    return sync_detailed(
        name=name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateServiceAccountApiKeyRequest,
) -> Response[CreateServiceAccountApiKeyResponse | ProblemDetails]:
    """Create an API key for a service account

     Creates a new API key owned by the given service account.

    The plain text key is returned exactly once, in the response body.
    It cannot be retrieved afterwards, because only its hash is stored.

    No API keys can be created for a suspended service account.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_CREATE` permission.

    Args:
        name (str): The name of the service account, without the reserved `svc:` prefix. Example:
            ci-pipeline.
        body (CreateServiceAccountApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateServiceAccountApiKeyResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateServiceAccountApiKeyRequest,
) -> CreateServiceAccountApiKeyResponse | ProblemDetails | None:
    """Create an API key for a service account

     Creates a new API key owned by the given service account.

    The plain text key is returned exactly once, in the response body.
    It cannot be retrieved afterwards, because only its hash is stored.

    No API keys can be created for a suspended service account.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_CREATE` permission.

    Args:
        name (str): The name of the service account, without the reserved `svc:` prefix. Example:
            ci-pipeline.
        body (CreateServiceAccountApiKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateServiceAccountApiKeyResponse | ProblemDetails
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            body=body,
        )
    ).parsed
