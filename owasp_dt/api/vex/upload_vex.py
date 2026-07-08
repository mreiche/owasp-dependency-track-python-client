from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bom_upload_response import BomUploadResponse
from ...models.invalid_bom_problem_details import InvalidBomProblemDetails
from ...models.problem_details import ProblemDetails
from ...models.vex_submit_request import VexSubmitRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: VexSubmitRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/vex",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BomUploadResponse | InvalidBomProblemDetails | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = BomUploadResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = InvalidBomProblemDetails.from_dict(response.json())

        return response_400

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
) -> Response[Any | BomUploadResponse | InvalidBomProblemDetails | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: VexSubmitRequest | Unset = UNSET,
) -> Response[Any | BomUploadResponse | InvalidBomProblemDetails | ProblemDetails]:
    """Upload a supported VEX document

     <p>
      Expects CycloneDX and a valid project UUID. If a UUID is not specified,
      then the <code>projectName</code> and <code>projectVersion</code> must be specified.
    </p>
    <p>
      The VEX will be validated against the CycloneDX schema. If schema validation fails,
      a response with problem details in RFC 9457 format will be returned. In this case,
      the response's content type will be <code>application/problem+json</code>.
    </p>
    <p>
      The maximum allowed length of the <code>vex</code> value is 20'000'000 characters.
      When uploading large VEX files, the <code>POST</code> endpoint is preferred,
      as it does not have this limit.
    </p>
    <p>Requires permission <strong>VULNERABILITY_ANALYSIS</strong> or
    <strong>VULNERABILITY_ANALYSIS_UPDATE</strong></p>

    Args:
        body (VexSubmitRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BomUploadResponse | InvalidBomProblemDetails | ProblemDetails]
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
    body: VexSubmitRequest | Unset = UNSET,
) -> Any | BomUploadResponse | InvalidBomProblemDetails | ProblemDetails | None:
    """Upload a supported VEX document

     <p>
      Expects CycloneDX and a valid project UUID. If a UUID is not specified,
      then the <code>projectName</code> and <code>projectVersion</code> must be specified.
    </p>
    <p>
      The VEX will be validated against the CycloneDX schema. If schema validation fails,
      a response with problem details in RFC 9457 format will be returned. In this case,
      the response's content type will be <code>application/problem+json</code>.
    </p>
    <p>
      The maximum allowed length of the <code>vex</code> value is 20'000'000 characters.
      When uploading large VEX files, the <code>POST</code> endpoint is preferred,
      as it does not have this limit.
    </p>
    <p>Requires permission <strong>VULNERABILITY_ANALYSIS</strong> or
    <strong>VULNERABILITY_ANALYSIS_UPDATE</strong></p>

    Args:
        body (VexSubmitRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BomUploadResponse | InvalidBomProblemDetails | ProblemDetails
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: VexSubmitRequest | Unset = UNSET,
) -> Response[Any | BomUploadResponse | InvalidBomProblemDetails | ProblemDetails]:
    """Upload a supported VEX document

     <p>
      Expects CycloneDX and a valid project UUID. If a UUID is not specified,
      then the <code>projectName</code> and <code>projectVersion</code> must be specified.
    </p>
    <p>
      The VEX will be validated against the CycloneDX schema. If schema validation fails,
      a response with problem details in RFC 9457 format will be returned. In this case,
      the response's content type will be <code>application/problem+json</code>.
    </p>
    <p>
      The maximum allowed length of the <code>vex</code> value is 20'000'000 characters.
      When uploading large VEX files, the <code>POST</code> endpoint is preferred,
      as it does not have this limit.
    </p>
    <p>Requires permission <strong>VULNERABILITY_ANALYSIS</strong> or
    <strong>VULNERABILITY_ANALYSIS_UPDATE</strong></p>

    Args:
        body (VexSubmitRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BomUploadResponse | InvalidBomProblemDetails | ProblemDetails]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: VexSubmitRequest | Unset = UNSET,
) -> Any | BomUploadResponse | InvalidBomProblemDetails | ProblemDetails | None:
    """Upload a supported VEX document

     <p>
      Expects CycloneDX and a valid project UUID. If a UUID is not specified,
      then the <code>projectName</code> and <code>projectVersion</code> must be specified.
    </p>
    <p>
      The VEX will be validated against the CycloneDX schema. If schema validation fails,
      a response with problem details in RFC 9457 format will be returned. In this case,
      the response's content type will be <code>application/problem+json</code>.
    </p>
    <p>
      The maximum allowed length of the <code>vex</code> value is 20'000'000 characters.
      When uploading large VEX files, the <code>POST</code> endpoint is preferred,
      as it does not have this limit.
    </p>
    <p>Requires permission <strong>VULNERABILITY_ANALYSIS</strong> or
    <strong>VULNERABILITY_ANALYSIS_UPDATE</strong></p>

    Args:
        body (VexSubmitRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BomUploadResponse | InvalidBomProblemDetails | ProblemDetails
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
