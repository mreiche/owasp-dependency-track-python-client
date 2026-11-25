from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_workload_identity_provider_request import (
    CreateWorkloadIdentityProviderRequest,
)
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    *,
    body: CreateWorkloadIdentityProviderRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/workload-identity-providers",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails:
    if response.status_code == 201:
        response_201 = cast(Any, None)
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

    if response.status_code == 409:
        response_409 = ProblemDetails.from_dict(response.json())

        return response_409

    response_default = ProblemDetails.from_dict(response.json())

    return response_default


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
    *,
    client: AuthenticatedClient | Client,
    body: CreateWorkloadIdentityProviderRequest,
) -> Response[Any | ProblemDetails]:
    """Create a workload identity provider

     Creates a new workload identity provider.

    Use an `audience` unique to this Dependency-Track instance, such as its URL.

    The signing keys come either from a URL, or inline.

    For `OIDC` providers, omit both `jwks_url` and `jwks` to have the server read the issuer's
    discovery document and store the `jwks_uri` it names. For `SPIFFE` providers, `jwks_url` is
    the trust domain's bundle endpoint.

    Provide `jwks` for issuers the server cannot reach, such as a self-managed Kubernetes cluster.
    Inline keys are never refreshed. When the issuer rotates its keys, update the provider.

    Unless keys are provided inline, the server fetches them and rejects the request if that fails,
    or if the URL resolves to a loopback or link-local address.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_CREATE` permission.

    Args:
        body (CreateWorkloadIdentityProviderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
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
    body: CreateWorkloadIdentityProviderRequest,
) -> Any | ProblemDetails | None:
    """Create a workload identity provider

     Creates a new workload identity provider.

    Use an `audience` unique to this Dependency-Track instance, such as its URL.

    The signing keys come either from a URL, or inline.

    For `OIDC` providers, omit both `jwks_url` and `jwks` to have the server read the issuer's
    discovery document and store the `jwks_uri` it names. For `SPIFFE` providers, `jwks_url` is
    the trust domain's bundle endpoint.

    Provide `jwks` for issuers the server cannot reach, such as a self-managed Kubernetes cluster.
    Inline keys are never refreshed. When the issuer rotates its keys, update the provider.

    Unless keys are provided inline, the server fetches them and rejects the request if that fails,
    or if the URL resolves to a loopback or link-local address.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_CREATE` permission.

    Args:
        body (CreateWorkloadIdentityProviderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateWorkloadIdentityProviderRequest,
) -> Response[Any | ProblemDetails]:
    """Create a workload identity provider

     Creates a new workload identity provider.

    Use an `audience` unique to this Dependency-Track instance, such as its URL.

    The signing keys come either from a URL, or inline.

    For `OIDC` providers, omit both `jwks_url` and `jwks` to have the server read the issuer's
    discovery document and store the `jwks_uri` it names. For `SPIFFE` providers, `jwks_url` is
    the trust domain's bundle endpoint.

    Provide `jwks` for issuers the server cannot reach, such as a self-managed Kubernetes cluster.
    Inline keys are never refreshed. When the issuer rotates its keys, update the provider.

    Unless keys are provided inline, the server fetches them and rejects the request if that fails,
    or if the URL resolves to a loopback or link-local address.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_CREATE` permission.

    Args:
        body (CreateWorkloadIdentityProviderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateWorkloadIdentityProviderRequest,
) -> Any | ProblemDetails | None:
    """Create a workload identity provider

     Creates a new workload identity provider.

    Use an `audience` unique to this Dependency-Track instance, such as its URL.

    The signing keys come either from a URL, or inline.

    For `OIDC` providers, omit both `jwks_url` and `jwks` to have the server read the issuer's
    discovery document and store the `jwks_uri` it names. For `SPIFFE` providers, `jwks_url` is
    the trust domain's bundle endpoint.

    Provide `jwks` for issuers the server cannot reach, such as a self-managed Kubernetes cluster.
    Inline keys are never refreshed. When the issuer rotates its keys, update the provider.

    Unless keys are provided inline, the server fetches them and rejects the request if that fails,
    or if the URL resolves to a loopback or link-local address.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_CREATE` permission.

    Args:
        body (CreateWorkloadIdentityProviderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
