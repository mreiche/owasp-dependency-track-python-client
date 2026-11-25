from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.paginated_response import PaginatedResponse
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    *,
    page_token: str | Unset = UNSET,
    limit: int | Unset = 100,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page_token"] = page_token

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/service-accounts/{name}/api-keys".format(
            name=quote(str(name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedResponse | ProblemDetails:
    if response.status_code == 200:
        response_200 = PaginatedResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ProblemDetails.from_dict(response.json())

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
) -> Response[PaginatedResponse | ProblemDetails]:
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
    page_token: str | Unset = UNSET,
    limit: int | Unset = 100,
) -> Response[PaginatedResponse | ProblemDetails]:
    """List the API keys of a service account

     Returns a paginated list of the API keys a service account owns, newest first.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_READ` permission.

    Args:
        name (str): The name of the service account, without the reserved `svc:` prefix. Example:
            ci-pipeline.
        page_token (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        name=name,
        page_token=page_token,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    limit: int | Unset = 100,
) -> PaginatedResponse | ProblemDetails | None:
    """List the API keys of a service account

     Returns a paginated list of the API keys a service account owns, newest first.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_READ` permission.

    Args:
        name (str): The name of the service account, without the reserved `svc:` prefix. Example:
            ci-pipeline.
        page_token (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponse | ProblemDetails
    """

    return sync_detailed(
        name=name,
        client=client,
        page_token=page_token,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    limit: int | Unset = 100,
) -> Response[PaginatedResponse | ProblemDetails]:
    """List the API keys of a service account

     Returns a paginated list of the API keys a service account owns, newest first.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_READ` permission.

    Args:
        name (str): The name of the service account, without the reserved `svc:` prefix. Example:
            ci-pipeline.
        page_token (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        name=name,
        page_token=page_token,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    limit: int | Unset = 100,
) -> PaginatedResponse | ProblemDetails | None:
    """List the API keys of a service account

     Returns a paginated list of the API keys a service account owns, newest first.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_READ` permission.

    Args:
        name (str): The name of the service account, without the reserved `svc:` prefix. Example:
            ci-pipeline.
        page_token (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponse | ProblemDetails
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            page_token=page_token,
            limit=limit,
        )
    ).parsed
