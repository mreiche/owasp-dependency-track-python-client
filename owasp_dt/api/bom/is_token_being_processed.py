from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.is_token_being_processed_response import IsTokenBeingProcessedResponse
from ...types import Response


def _get_kwargs(
    uuid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/bom/token/{uuid}".format(
            uuid=quote(str(uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | IsTokenBeingProcessedResponse | None:
    if response.status_code == 200:
        response_200 = IsTokenBeingProcessedResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | IsTokenBeingProcessedResponse]:
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
) -> Response[Any | IsTokenBeingProcessedResponse]:
    """Determines if there are any tasks associated with the token that are being processed, or in the
    queue to be processed.

     <p>
      This endpoint is intended to be used in conjunction with uploading a supported BOM document.
      Upon upload, a token will be returned. The token can then be queried using this endpoint to
      determine if any tasks (such as vulnerability analysis) is being performed on the BOM:
      <ul>
        <li>A value of <code>true</code> indicates processing is occurring.</li>
        <li>A value of <code>false</code> indicates that no processing is occurring for the specified
    token.</li>
      </ul>
      However, a value of <code>false</code> also does not confirm the token is valid,
      only that no processing is associated with the specified token.
    </p>
    <p>Requires permission <strong>BOM_UPLOAD</strong></p>
    <p><strong>Deprecated</strong>. Use <code>/v1/event/token/{uuid}</code> instead.</p>

    Args:
        uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IsTokenBeingProcessedResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | IsTokenBeingProcessedResponse | None:
    """Determines if there are any tasks associated with the token that are being processed, or in the
    queue to be processed.

     <p>
      This endpoint is intended to be used in conjunction with uploading a supported BOM document.
      Upon upload, a token will be returned. The token can then be queried using this endpoint to
      determine if any tasks (such as vulnerability analysis) is being performed on the BOM:
      <ul>
        <li>A value of <code>true</code> indicates processing is occurring.</li>
        <li>A value of <code>false</code> indicates that no processing is occurring for the specified
    token.</li>
      </ul>
      However, a value of <code>false</code> also does not confirm the token is valid,
      only that no processing is associated with the specified token.
    </p>
    <p>Requires permission <strong>BOM_UPLOAD</strong></p>
    <p><strong>Deprecated</strong>. Use <code>/v1/event/token/{uuid}</code> instead.</p>

    Args:
        uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IsTokenBeingProcessedResponse
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any | IsTokenBeingProcessedResponse]:
    """Determines if there are any tasks associated with the token that are being processed, or in the
    queue to be processed.

     <p>
      This endpoint is intended to be used in conjunction with uploading a supported BOM document.
      Upon upload, a token will be returned. The token can then be queried using this endpoint to
      determine if any tasks (such as vulnerability analysis) is being performed on the BOM:
      <ul>
        <li>A value of <code>true</code> indicates processing is occurring.</li>
        <li>A value of <code>false</code> indicates that no processing is occurring for the specified
    token.</li>
      </ul>
      However, a value of <code>false</code> also does not confirm the token is valid,
      only that no processing is associated with the specified token.
    </p>
    <p>Requires permission <strong>BOM_UPLOAD</strong></p>
    <p><strong>Deprecated</strong>. Use <code>/v1/event/token/{uuid}</code> instead.</p>

    Args:
        uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IsTokenBeingProcessedResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | IsTokenBeingProcessedResponse | None:
    """Determines if there are any tasks associated with the token that are being processed, or in the
    queue to be processed.

     <p>
      This endpoint is intended to be used in conjunction with uploading a supported BOM document.
      Upon upload, a token will be returned. The token can then be queried using this endpoint to
      determine if any tasks (such as vulnerability analysis) is being performed on the BOM:
      <ul>
        <li>A value of <code>true</code> indicates processing is occurring.</li>
        <li>A value of <code>false</code> indicates that no processing is occurring for the specified
    token.</li>
      </ul>
      However, a value of <code>false</code> also does not confirm the token is valid,
      only that no processing is associated with the specified token.
    </p>
    <p>Requires permission <strong>BOM_UPLOAD</strong></p>
    <p><strong>Deprecated</strong>. Use <code>/v1/event/token/{uuid}</code> instead.</p>

    Args:
        uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IsTokenBeingProcessedResponse
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
        )
    ).parsed
