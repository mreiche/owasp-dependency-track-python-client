from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.violation_analysis import ViolationAnalysis
from ...models.violation_analysis_request import ViolationAnalysisRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ViolationAnalysisRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/violation/analysis",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | ViolationAnalysis | None:
    if response.status_code == 200:
        response_200 = ViolationAnalysis.from_dict(response.json())

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
) -> Response[Any | ProblemDetails | ViolationAnalysis]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ViolationAnalysisRequest | Unset = UNSET,
) -> Response[Any | ProblemDetails | ViolationAnalysis]:
    """Records a violation analysis decision

     <p>Requires permission <strong>POLICY_VIOLATION_ANALYSIS</strong></p>

    Args:
        body (ViolationAnalysisRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | ViolationAnalysis]
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
    body: ViolationAnalysisRequest | Unset = UNSET,
) -> Any | ProblemDetails | ViolationAnalysis | None:
    """Records a violation analysis decision

     <p>Requires permission <strong>POLICY_VIOLATION_ANALYSIS</strong></p>

    Args:
        body (ViolationAnalysisRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | ViolationAnalysis
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ViolationAnalysisRequest | Unset = UNSET,
) -> Response[Any | ProblemDetails | ViolationAnalysis]:
    """Records a violation analysis decision

     <p>Requires permission <strong>POLICY_VIOLATION_ANALYSIS</strong></p>

    Args:
        body (ViolationAnalysisRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | ViolationAnalysis]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ViolationAnalysisRequest | Unset = UNSET,
) -> Any | ProblemDetails | ViolationAnalysis | None:
    """Records a violation analysis decision

     <p>Requires permission <strong>POLICY_VIOLATION_ANALYSIS</strong></p>

    Args:
        body (ViolationAnalysisRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | ViolationAnalysis
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
