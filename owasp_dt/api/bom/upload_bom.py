from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bom_upload_response import BomUploadResponse
from ...models.problem_details import ProblemDetails
from ...models.upload_bom_body import UploadBomBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UploadBomBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/bom",
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BomUploadResponse | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = BomUploadResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
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
) -> Response[Any | BomUploadResponse | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UploadBomBody | Unset = UNSET,
) -> Response[Any | BomUploadResponse | ProblemDetails]:
    """Upload a supported bill of material format document

     <p>
      Expects CycloneDX and a valid project UUID. If a UUID is not specified,
      then the <code>projectName</code> and <code>projectVersion</code> must be specified.
      Optionally, if <code>autoCreate</code> is specified and <code>true</code> and the project does not
    exist,
      the project will be created. In this scenario, the principal making the request will
      additionally need the <strong>PORTFOLIO_MANAGEMENT</strong>,
    <strong>PORTFOLIO_MANAGEMENT_CREATE</strong>,
      or <strong>PROJECT_CREATION_UPLOAD</strong> permission.
    </p>
    <p>
      MediaType supported for BOM artifact is 'application/xml' or 'application/json'.
      The BOM will be validated against the CycloneDX schema. If schema validation fails,
      a response with problem details in RFC 9457 format will be returned. In this case,
      the response's content type will be <code>application/problem+json</code>.
    </p>
    <p>Requires permission <strong>BOM_UPLOAD</strong></p>

    Args:
        body (UploadBomBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BomUploadResponse | ProblemDetails]
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
    body: UploadBomBody | Unset = UNSET,
) -> Any | BomUploadResponse | ProblemDetails | None:
    """Upload a supported bill of material format document

     <p>
      Expects CycloneDX and a valid project UUID. If a UUID is not specified,
      then the <code>projectName</code> and <code>projectVersion</code> must be specified.
      Optionally, if <code>autoCreate</code> is specified and <code>true</code> and the project does not
    exist,
      the project will be created. In this scenario, the principal making the request will
      additionally need the <strong>PORTFOLIO_MANAGEMENT</strong>,
    <strong>PORTFOLIO_MANAGEMENT_CREATE</strong>,
      or <strong>PROJECT_CREATION_UPLOAD</strong> permission.
    </p>
    <p>
      MediaType supported for BOM artifact is 'application/xml' or 'application/json'.
      The BOM will be validated against the CycloneDX schema. If schema validation fails,
      a response with problem details in RFC 9457 format will be returned. In this case,
      the response's content type will be <code>application/problem+json</code>.
    </p>
    <p>Requires permission <strong>BOM_UPLOAD</strong></p>

    Args:
        body (UploadBomBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BomUploadResponse | ProblemDetails
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UploadBomBody | Unset = UNSET,
) -> Response[Any | BomUploadResponse | ProblemDetails]:
    """Upload a supported bill of material format document

     <p>
      Expects CycloneDX and a valid project UUID. If a UUID is not specified,
      then the <code>projectName</code> and <code>projectVersion</code> must be specified.
      Optionally, if <code>autoCreate</code> is specified and <code>true</code> and the project does not
    exist,
      the project will be created. In this scenario, the principal making the request will
      additionally need the <strong>PORTFOLIO_MANAGEMENT</strong>,
    <strong>PORTFOLIO_MANAGEMENT_CREATE</strong>,
      or <strong>PROJECT_CREATION_UPLOAD</strong> permission.
    </p>
    <p>
      MediaType supported for BOM artifact is 'application/xml' or 'application/json'.
      The BOM will be validated against the CycloneDX schema. If schema validation fails,
      a response with problem details in RFC 9457 format will be returned. In this case,
      the response's content type will be <code>application/problem+json</code>.
    </p>
    <p>Requires permission <strong>BOM_UPLOAD</strong></p>

    Args:
        body (UploadBomBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BomUploadResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UploadBomBody | Unset = UNSET,
) -> Any | BomUploadResponse | ProblemDetails | None:
    """Upload a supported bill of material format document

     <p>
      Expects CycloneDX and a valid project UUID. If a UUID is not specified,
      then the <code>projectName</code> and <code>projectVersion</code> must be specified.
      Optionally, if <code>autoCreate</code> is specified and <code>true</code> and the project does not
    exist,
      the project will be created. In this scenario, the principal making the request will
      additionally need the <strong>PORTFOLIO_MANAGEMENT</strong>,
    <strong>PORTFOLIO_MANAGEMENT_CREATE</strong>,
      or <strong>PROJECT_CREATION_UPLOAD</strong> permission.
    </p>
    <p>
      MediaType supported for BOM artifact is 'application/xml' or 'application/json'.
      The BOM will be validated against the CycloneDX schema. If schema validation fails,
      a response with problem details in RFC 9457 format will be returned. In this case,
      the response's content type will be <code>application/problem+json</code>.
    </p>
    <p>Requires permission <strong>BOM_UPLOAD</strong></p>

    Args:
        body (UploadBomBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BomUploadResponse | ProblemDetails
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
