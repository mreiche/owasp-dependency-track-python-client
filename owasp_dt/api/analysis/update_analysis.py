from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analysis import Analysis
from ...models.analysis_request import AnalysisRequest
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: AnalysisRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/analysis",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Analysis | Any | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = Analysis.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Analysis | Any | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AnalysisRequest | Unset = UNSET,
) -> Response[Analysis | Any | ProblemDetails]:
    """Records an analysis decision

     <p>Requires permission <strong>VULNERABILITY_ANALYSIS</strong></strong> or
    <strong>VULNERABILITY_ANALYSIS_UPDATE</strong></p>

    Args:
        body (AnalysisRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Analysis | Any | ProblemDetails]
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
    body: AnalysisRequest | Unset = UNSET,
) -> Analysis | Any | ProblemDetails | None:
    """Records an analysis decision

     <p>Requires permission <strong>VULNERABILITY_ANALYSIS</strong></strong> or
    <strong>VULNERABILITY_ANALYSIS_UPDATE</strong></p>

    Args:
        body (AnalysisRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Analysis | Any | ProblemDetails
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AnalysisRequest | Unset = UNSET,
) -> Response[Analysis | Any | ProblemDetails]:
    """Records an analysis decision

     <p>Requires permission <strong>VULNERABILITY_ANALYSIS</strong></strong> or
    <strong>VULNERABILITY_ANALYSIS_UPDATE</strong></p>

    Args:
        body (AnalysisRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Analysis | Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AnalysisRequest | Unset = UNSET,
) -> Analysis | Any | ProblemDetails | None:
    """Records an analysis decision

     <p>Requires permission <strong>VULNERABILITY_ANALYSIS</strong></strong> or
    <strong>VULNERABILITY_ANALYSIS_UPDATE</strong></p>

    Args:
        body (AnalysisRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Analysis | Any | ProblemDetails
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
