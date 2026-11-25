from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.update_workload_identity_provider_request import (
    UpdateWorkloadIdentityProviderRequest,
)
from ...types import Response


def _get_kwargs(
    name: str,
    *,
    body: UpdateWorkloadIdentityProviderRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/workload-identity-providers/{name}".format(
            name=quote(str(name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateWorkloadIdentityProviderRequest,
) -> Response[Any | ProblemDetails]:
    """Update a workload identity provider

     Updates a workload identity provider.

    Only the given fields are changed. The name and type of a provider cannot change.

    Providing `jwks_url` switches the provider to that URL. Providing `jwks` switches it to inline keys.
    Changing the `issuer` of an `OIDC` provider that fetches its keys from a URL re-reads the new
    issuer's
    discovery document and replaces the stored `jwks_url`, unless `jwks_url` or `jwks` is given as well.
    Bindings of a `SPIFFE` provider stop matching when its trust domain changes.
    When the key source changes, the server fetches the new keys and rejects the request if that fails.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_UPDATE` permission.

    Args:
        name (str): The name of the workload identity provider. Example: github-actions.
        body (UpdateWorkloadIdentityProviderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
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
    body: UpdateWorkloadIdentityProviderRequest,
) -> Any | ProblemDetails | None:
    """Update a workload identity provider

     Updates a workload identity provider.

    Only the given fields are changed. The name and type of a provider cannot change.

    Providing `jwks_url` switches the provider to that URL. Providing `jwks` switches it to inline keys.
    Changing the `issuer` of an `OIDC` provider that fetches its keys from a URL re-reads the new
    issuer's
    discovery document and replaces the stored `jwks_url`, unless `jwks_url` or `jwks` is given as well.
    Bindings of a `SPIFFE` provider stop matching when its trust domain changes.
    When the key source changes, the server fetches the new keys and rejects the request if that fails.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_UPDATE` permission.

    Args:
        name (str): The name of the workload identity provider. Example: github-actions.
        body (UpdateWorkloadIdentityProviderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
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
    body: UpdateWorkloadIdentityProviderRequest,
) -> Response[Any | ProblemDetails]:
    """Update a workload identity provider

     Updates a workload identity provider.

    Only the given fields are changed. The name and type of a provider cannot change.

    Providing `jwks_url` switches the provider to that URL. Providing `jwks` switches it to inline keys.
    Changing the `issuer` of an `OIDC` provider that fetches its keys from a URL re-reads the new
    issuer's
    discovery document and replaces the stored `jwks_url`, unless `jwks_url` or `jwks` is given as well.
    Bindings of a `SPIFFE` provider stop matching when its trust domain changes.
    When the key source changes, the server fetches the new keys and rejects the request if that fails.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_UPDATE` permission.

    Args:
        name (str): The name of the workload identity provider. Example: github-actions.
        body (UpdateWorkloadIdentityProviderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
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
    body: UpdateWorkloadIdentityProviderRequest,
) -> Any | ProblemDetails | None:
    """Update a workload identity provider

     Updates a workload identity provider.

    Only the given fields are changed. The name and type of a provider cannot change.

    Providing `jwks_url` switches the provider to that URL. Providing `jwks` switches it to inline keys.
    Changing the `issuer` of an `OIDC` provider that fetches its keys from a URL re-reads the new
    issuer's
    discovery document and replaces the stored `jwks_url`, unless `jwks_url` or `jwks` is given as well.
    Bindings of a `SPIFFE` provider stop matching when its trust domain changes.
    When the key source changes, the server fetches the new keys and rejects the request if that fails.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_UPDATE` permission.

    Args:
        name (str): The name of the workload identity provider. Example: github-actions.
        body (UpdateWorkloadIdentityProviderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            body=body,
        )
    ).parsed
