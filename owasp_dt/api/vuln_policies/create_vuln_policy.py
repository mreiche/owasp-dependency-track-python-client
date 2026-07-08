from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_vuln_policy_request import CreateVulnPolicyRequest
from ...models.create_vuln_policy_response_201 import CreateVulnPolicyResponse201
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    *,
    body: CreateVulnPolicyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/vuln-policies",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateVulnPolicyResponse201 | ProblemDetails:
    if response.status_code == 201:
        response_201 = CreateVulnPolicyResponse201.from_dict(response.json())

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
) -> Response[CreateVulnPolicyResponse201 | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateVulnPolicyRequest,
) -> Response[CreateVulnPolicyResponse201 | ProblemDetails]:
    """Create a vulnerability policy

     Creates a user-managed vulnerability policy.

    CEL conditions are compiled server-side. On compilation failure,
    a 400 response with structured error details is returned.

    Requires permission `POLICY_MANAGEMENT` or `POLICY_MANAGEMENT_CREATE`.

    Args:
        body (CreateVulnPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateVulnPolicyResponse201 | ProblemDetails]
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
    body: CreateVulnPolicyRequest,
) -> CreateVulnPolicyResponse201 | ProblemDetails | None:
    """Create a vulnerability policy

     Creates a user-managed vulnerability policy.

    CEL conditions are compiled server-side. On compilation failure,
    a 400 response with structured error details is returned.

    Requires permission `POLICY_MANAGEMENT` or `POLICY_MANAGEMENT_CREATE`.

    Args:
        body (CreateVulnPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateVulnPolicyResponse201 | ProblemDetails
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateVulnPolicyRequest,
) -> Response[CreateVulnPolicyResponse201 | ProblemDetails]:
    """Create a vulnerability policy

     Creates a user-managed vulnerability policy.

    CEL conditions are compiled server-side. On compilation failure,
    a 400 response with structured error details is returned.

    Requires permission `POLICY_MANAGEMENT` or `POLICY_MANAGEMENT_CREATE`.

    Args:
        body (CreateVulnPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateVulnPolicyResponse201 | ProblemDetails]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateVulnPolicyRequest,
) -> CreateVulnPolicyResponse201 | ProblemDetails | None:
    """Create a vulnerability policy

     Creates a user-managed vulnerability policy.

    CEL conditions are compiled server-side. On compilation failure,
    a 400 response with structured error details is returned.

    Requires permission `POLICY_MANAGEMENT` or `POLICY_MANAGEMENT_CREATE`.

    Args:
        body (CreateVulnPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateVulnPolicyResponse201 | ProblemDetails
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
