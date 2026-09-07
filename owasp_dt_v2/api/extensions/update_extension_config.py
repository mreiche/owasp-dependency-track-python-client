from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.update_extension_config_request import UpdateExtensionConfigRequest
from ...types import Response


def _get_kwargs(
    extension_point_name: str,
    extension_name: str,
    *,
    body: UpdateExtensionConfigRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/extension-points/{extension_point_name}/extensions/{extension_name}/config".format(
            extension_point_name=quote(str(extension_point_name), safe=""),
            extension_name=quote(str(extension_name), safe=""),
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

    if response.status_code == 304:
        response_304 = cast(Any, None)
        return response_304

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
    extension_point_name: str,
    extension_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateExtensionConfigRequest,
) -> Response[Any | ProblemDetails]:
    """Update extension configuration

     Updates the configuration of an extension.

    **Do not use clear text credentials in the supplied config**.
    Fields annotated with `x-secret-ref` in the config schema expect
    a name of a managed secret, which is resolved internally by the API.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_UPDATE` permission.

    Args:
        extension_point_name (str):
        extension_name (str):
        body (UpdateExtensionConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        extension_point_name=extension_point_name,
        extension_name=extension_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    extension_point_name: str,
    extension_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateExtensionConfigRequest,
) -> Any | ProblemDetails | None:
    """Update extension configuration

     Updates the configuration of an extension.

    **Do not use clear text credentials in the supplied config**.
    Fields annotated with `x-secret-ref` in the config schema expect
    a name of a managed secret, which is resolved internally by the API.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_UPDATE` permission.

    Args:
        extension_point_name (str):
        extension_name (str):
        body (UpdateExtensionConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return sync_detailed(
        extension_point_name=extension_point_name,
        extension_name=extension_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    extension_point_name: str,
    extension_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateExtensionConfigRequest,
) -> Response[Any | ProblemDetails]:
    """Update extension configuration

     Updates the configuration of an extension.

    **Do not use clear text credentials in the supplied config**.
    Fields annotated with `x-secret-ref` in the config schema expect
    a name of a managed secret, which is resolved internally by the API.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_UPDATE` permission.

    Args:
        extension_point_name (str):
        extension_name (str):
        body (UpdateExtensionConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        extension_point_name=extension_point_name,
        extension_name=extension_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    extension_point_name: str,
    extension_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateExtensionConfigRequest,
) -> Any | ProblemDetails | None:
    """Update extension configuration

     Updates the configuration of an extension.

    **Do not use clear text credentials in the supplied config**.
    Fields annotated with `x-secret-ref` in the config schema expect
    a name of a managed secret, which is resolved internally by the API.

    Requires the `SYSTEM_CONFIGURATION` or `SYSTEM_CONFIGURATION_UPDATE` permission.

    Args:
        extension_point_name (str):
        extension_name (str):
        body (UpdateExtensionConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return (
        await asyncio_detailed(
            extension_point_name=extension_point_name,
            extension_name=extension_name,
            client=client,
            body=body,
        )
    ).parsed
