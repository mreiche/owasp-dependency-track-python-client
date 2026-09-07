from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.paginated_response import PaginatedResponse
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    source: str,
    vuln_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/vulns/{source}/{vuln_id}/kev-assertions".format(
            source=quote(str(source), safe=""),
            vuln_id=quote(str(vuln_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedResponse | ProblemDetails:
    if response.status_code == 200:
        response_200 = PaginatedResponse.from_dict(response.json())

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
) -> Response[PaginatedResponse | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    source: str,
    vuln_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[PaginatedResponse | ProblemDetails]:
    """Lists KEV assertions for a vulnerability

     Returns all Known Exploited Vulnerability (KEV) assertions for the given
    vulnerability, including those asserted for any of its aliases.

    Requires permission `VIEW_VULNERABILITY`.

    Args:
        source (str):
        vuln_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        source=source,
        vuln_id=vuln_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source: str,
    vuln_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> PaginatedResponse | ProblemDetails | None:
    """Lists KEV assertions for a vulnerability

     Returns all Known Exploited Vulnerability (KEV) assertions for the given
    vulnerability, including those asserted for any of its aliases.

    Requires permission `VIEW_VULNERABILITY`.

    Args:
        source (str):
        vuln_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponse | ProblemDetails
    """

    return sync_detailed(
        source=source,
        vuln_id=vuln_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    source: str,
    vuln_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[PaginatedResponse | ProblemDetails]:
    """Lists KEV assertions for a vulnerability

     Returns all Known Exploited Vulnerability (KEV) assertions for the given
    vulnerability, including those asserted for any of its aliases.

    Requires permission `VIEW_VULNERABILITY`.

    Args:
        source (str):
        vuln_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        source=source,
        vuln_id=vuln_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source: str,
    vuln_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> PaginatedResponse | ProblemDetails | None:
    """Lists KEV assertions for a vulnerability

     Returns all Known Exploited Vulnerability (KEV) assertions for the given
    vulnerability, including those asserted for any of its aliases.

    Requires permission `VIEW_VULNERABILITY`.

    Args:
        source (str):
        vuln_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponse | ProblemDetails
    """

    return (
        await asyncio_detailed(
            source=source,
            vuln_id=vuln_id,
            client=client,
        )
    ).parsed
