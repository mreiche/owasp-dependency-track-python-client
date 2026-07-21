from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.update_vuln_policy_request import UpdateVulnPolicyRequest
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: UpdateVulnPolicyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/vuln-policies/{uuid}".format(
            uuid=quote(str(uuid), safe=""),
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
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateVulnPolicyRequest,
) -> Response[Any | ProblemDetails]:
    """Replace a vulnerability policy

     Replaces a user-managed vulnerability policy with the provided data.

    Policies managed by a bundle can not be modified.

    Requires permission `POLICY_MANAGEMENT` or `POLICY_MANAGEMENT_UPDATE`.

    Args:
        uuid (UUID):
        body (UpdateVulnPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateVulnPolicyRequest,
) -> Any | ProblemDetails | None:
    """Replace a vulnerability policy

     Replaces a user-managed vulnerability policy with the provided data.

    Policies managed by a bundle can not be modified.

    Requires permission `POLICY_MANAGEMENT` or `POLICY_MANAGEMENT_UPDATE`.

    Args:
        uuid (UUID):
        body (UpdateVulnPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateVulnPolicyRequest,
) -> Response[Any | ProblemDetails]:
    """Replace a vulnerability policy

     Replaces a user-managed vulnerability policy with the provided data.

    Policies managed by a bundle can not be modified.

    Requires permission `POLICY_MANAGEMENT` or `POLICY_MANAGEMENT_UPDATE`.

    Args:
        uuid (UUID):
        body (UpdateVulnPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateVulnPolicyRequest,
) -> Any | ProblemDetails | None:
    """Replace a vulnerability policy

     Replaces a user-managed vulnerability policy with the provided data.

    Policies managed by a bundle can not be modified.

    Requires permission `POLICY_MANAGEMENT` or `POLICY_MANAGEMENT_UPDATE`.

    Args:
        uuid (UUID):
        body (UpdateVulnPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
