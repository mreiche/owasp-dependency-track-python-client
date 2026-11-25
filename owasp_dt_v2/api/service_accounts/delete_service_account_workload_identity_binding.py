from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    name: str,
    binding_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/service-accounts/{name}/workload-identity-bindings/{binding_id}".format(
            name=quote(str(name), safe=""),
            binding_id=quote(str(binding_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
    binding_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ProblemDetails]:
    """Delete a workload identity binding of a service account

     Deletes a service account's workload identity binding.

    Sessions already created stay valid until they expire.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_DELETE` permission.

    Args:
        name (str): The name of the service account, without the reserved `svc:` prefix. Example:
            ci-pipeline.
        binding_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        name=name,
        binding_id=binding_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    binding_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ProblemDetails | None:
    """Delete a workload identity binding of a service account

     Deletes a service account's workload identity binding.

    Sessions already created stay valid until they expire.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_DELETE` permission.

    Args:
        name (str): The name of the service account, without the reserved `svc:` prefix. Example:
            ci-pipeline.
        binding_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return sync_detailed(
        name=name,
        binding_id=binding_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    name: str,
    binding_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ProblemDetails]:
    """Delete a workload identity binding of a service account

     Deletes a service account's workload identity binding.

    Sessions already created stay valid until they expire.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_DELETE` permission.

    Args:
        name (str): The name of the service account, without the reserved `svc:` prefix. Example:
            ci-pipeline.
        binding_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        name=name,
        binding_id=binding_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    binding_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ProblemDetails | None:
    """Delete a workload identity binding of a service account

     Deletes a service account's workload identity binding.

    Sessions already created stay valid until they expire.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_DELETE` permission.

    Args:
        name (str): The name of the service account, without the reserved `svc:` prefix. Example:
            ci-pipeline.
        binding_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return (
        await asyncio_detailed(
            name=name,
            binding_id=binding_id,
            client=client,
        )
    ).parsed
