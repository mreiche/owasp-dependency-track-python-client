from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    format_: str | Unset = UNSET,
    version: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["format"] = format_

    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/bom/cyclonedx/component/{uuid}".format(
            uuid=quote(str(uuid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
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
) -> Response[Any | ProblemDetails | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    format_: str | Unset = UNSET,
    version: str | Unset = UNSET,
) -> Response[Any | ProblemDetails | str]:
    """Returns dependency metadata for a specific component in CycloneDX format

     <p>Requires permission <strong>VIEW_PORTFOLIO</strong></p>

    Args:
        uuid (UUID):
        format_ (str | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | str]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        format_=format_,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    format_: str | Unset = UNSET,
    version: str | Unset = UNSET,
) -> Any | ProblemDetails | str | None:
    """Returns dependency metadata for a specific component in CycloneDX format

     <p>Requires permission <strong>VIEW_PORTFOLIO</strong></p>

    Args:
        uuid (UUID):
        format_ (str | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | str
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        format_=format_,
        version=version,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    format_: str | Unset = UNSET,
    version: str | Unset = UNSET,
) -> Response[Any | ProblemDetails | str]:
    """Returns dependency metadata for a specific component in CycloneDX format

     <p>Requires permission <strong>VIEW_PORTFOLIO</strong></p>

    Args:
        uuid (UUID):
        format_ (str | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | str]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        format_=format_,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    format_: str | Unset = UNSET,
    version: str | Unset = UNSET,
) -> Any | ProblemDetails | str | None:
    """Returns dependency metadata for a specific component in CycloneDX format

     <p>Requires permission <strong>VIEW_PORTFOLIO</strong></p>

    Args:
        uuid (UUID):
        format_ (str | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | str
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            format_=format_,
            version=version,
        )
    ).parsed
