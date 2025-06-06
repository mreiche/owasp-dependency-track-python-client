from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analysis import Analysis
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    project: Union[Unset, UUID] = UNSET,
    component: UUID,
    vulnerability: UUID,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_project: Union[Unset, str] = UNSET
    if not isinstance(project, Unset):
        json_project = str(project)
    params["project"] = json_project

    json_component = str(component)
    params["component"] = json_component

    json_vulnerability = str(vulnerability)
    params["vulnerability"] = json_vulnerability

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analysis",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Analysis, Any]]:
    if response.status_code == 200:
        response_200 = Analysis.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Analysis, Any]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    project: Union[Unset, UUID] = UNSET,
    component: UUID,
    vulnerability: UUID,
) -> Response[Union[Analysis, Any]]:
    """Retrieves an analysis trail

     <p>Requires permission <strong>VIEW_VULNERABILITY</strong></p>

    Args:
        project (Union[Unset, UUID]):
        component (UUID):
        vulnerability (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Analysis, Any]]
    """

    kwargs = _get_kwargs(
        project=project,
        component=component,
        vulnerability=vulnerability,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    project: Union[Unset, UUID] = UNSET,
    component: UUID,
    vulnerability: UUID,
) -> Optional[Union[Analysis, Any]]:
    """Retrieves an analysis trail

     <p>Requires permission <strong>VIEW_VULNERABILITY</strong></p>

    Args:
        project (Union[Unset, UUID]):
        component (UUID):
        vulnerability (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Analysis, Any]
    """

    return sync_detailed(
        client=client,
        project=project,
        component=component,
        vulnerability=vulnerability,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    project: Union[Unset, UUID] = UNSET,
    component: UUID,
    vulnerability: UUID,
) -> Response[Union[Analysis, Any]]:
    """Retrieves an analysis trail

     <p>Requires permission <strong>VIEW_VULNERABILITY</strong></p>

    Args:
        project (Union[Unset, UUID]):
        component (UUID):
        vulnerability (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Analysis, Any]]
    """

    kwargs = _get_kwargs(
        project=project,
        component=component,
        vulnerability=vulnerability,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    project: Union[Unset, UUID] = UNSET,
    component: UUID,
    vulnerability: UUID,
) -> Optional[Union[Analysis, Any]]:
    """Retrieves an analysis trail

     <p>Requires permission <strong>VIEW_VULNERABILITY</strong></p>

    Args:
        project (Union[Unset, UUID]):
        component (UUID):
        vulnerability (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Analysis, Any]
    """

    return (
        await asyncio_detailed(
            client=client,
            project=project,
            component=component,
            vulnerability=vulnerability,
        )
    ).parsed
