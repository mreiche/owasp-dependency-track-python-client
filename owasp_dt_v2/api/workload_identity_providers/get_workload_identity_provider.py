from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.workload_identity_provider import WorkloadIdentityProvider
from ...types import Response


def _get_kwargs(
    name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workload-identity-providers/{name}".format(
            name=quote(str(name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | WorkloadIdentityProvider:
    if response.status_code == 200:
        response_200 = WorkloadIdentityProvider.from_dict(response.json())

        return response_200

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
) -> Response[ProblemDetails | WorkloadIdentityProvider]:
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
) -> Response[ProblemDetails | WorkloadIdentityProvider]:
    """Get a workload identity provider

     Returns details about a workload identity provider.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_READ` permission.

    Args:
        name (str): The name of the workload identity provider. Example: github-actions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | WorkloadIdentityProvider]
    """

    kwargs = _get_kwargs(
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | WorkloadIdentityProvider | None:
    """Get a workload identity provider

     Returns details about a workload identity provider.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_READ` permission.

    Args:
        name (str): The name of the workload identity provider. Example: github-actions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | WorkloadIdentityProvider
    """

    return sync_detailed(
        name=name,
        client=client,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | WorkloadIdentityProvider]:
    """Get a workload identity provider

     Returns details about a workload identity provider.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_READ` permission.

    Args:
        name (str): The name of the workload identity provider. Example: github-actions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | WorkloadIdentityProvider]
    """

    kwargs = _get_kwargs(
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | WorkloadIdentityProvider | None:
    """Get a workload identity provider

     Returns details about a workload identity provider.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_READ` permission.

    Args:
        name (str): The name of the workload identity provider. Example: github-actions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | WorkloadIdentityProvider
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
        )
    ).parsed
