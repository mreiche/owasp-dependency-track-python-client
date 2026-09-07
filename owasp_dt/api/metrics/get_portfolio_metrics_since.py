from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.portfolio_metrics import PortfolioMetrics
from ...types import Response


def _get_kwargs(
    date: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/metrics/portfolio/since/{date}".format(
            date=quote(str(date), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[PortfolioMetrics] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PortfolioMetrics.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Any | list[PortfolioMetrics]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    date: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[PortfolioMetrics]]:
    """Returns historical metrics for the entire portfolio from a specific date

     <p>Date format must be <code>YYYYMMDD</code>. The number of days returned is computed against the
    current UTC date.
    </p>
    <p>Requires permission <strong>VIEW_PORTFOLIO</strong></p>

    Args:
        date (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[PortfolioMetrics]]
    """

    kwargs = _get_kwargs(
        date=date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    date: str,
    *,
    client: AuthenticatedClient,
) -> Any | list[PortfolioMetrics] | None:
    """Returns historical metrics for the entire portfolio from a specific date

     <p>Date format must be <code>YYYYMMDD</code>. The number of days returned is computed against the
    current UTC date.
    </p>
    <p>Requires permission <strong>VIEW_PORTFOLIO</strong></p>

    Args:
        date (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[PortfolioMetrics]
    """

    return sync_detailed(
        date=date,
        client=client,
    ).parsed


async def asyncio_detailed(
    date: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[PortfolioMetrics]]:
    """Returns historical metrics for the entire portfolio from a specific date

     <p>Date format must be <code>YYYYMMDD</code>. The number of days returned is computed against the
    current UTC date.
    </p>
    <p>Requires permission <strong>VIEW_PORTFOLIO</strong></p>

    Args:
        date (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[PortfolioMetrics]]
    """

    kwargs = _get_kwargs(
        date=date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    date: str,
    *,
    client: AuthenticatedClient,
) -> Any | list[PortfolioMetrics] | None:
    """Returns historical metrics for the entire portfolio from a specific date

     <p>Date format must be <code>YYYYMMDD</code>. The number of days returned is computed against the
    current UTC date.
    </p>
    <p>Requires permission <strong>VIEW_PORTFOLIO</strong></p>

    Args:
        date (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[PortfolioMetrics]
    """

    return (
        await asyncio_detailed(
            date=date,
            client=client,
        )
    ).parsed
