from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_workload_identity_binding_request import (
    CreateWorkloadIdentityBindingRequest,
)
from ...models.create_workload_identity_binding_response import (
    CreateWorkloadIdentityBindingResponse,
)
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    name: str,
    *,
    body: CreateWorkloadIdentityBindingRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/service-accounts/{name}/workload-identity-bindings".format(
            name=quote(str(name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateWorkloadIdentityBindingResponse | ProblemDetails:
    if response.status_code == 201:
        response_201 = CreateWorkloadIdentityBindingResponse.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404

    response_default = ProblemDetails.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateWorkloadIdentityBindingResponse | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateWorkloadIdentityBindingRequest,
) -> Response[CreateWorkloadIdentityBindingResponse | ProblemDetails]:
    """Create a workload identity binding for a service account

     Creates a workload identity binding for a service account.

    A trailing `*` in `subject` makes it a prefix match, for example `repo:acme/app:*`.
    For `SPIFFE` providers, the prefix must end with `/`.

    For multi-tenant issuers like GitHub and GitLab, ensure that the prefix contains
    *at least* your organization to prevent cross-tenant abuse. For example:

    ```json
    {
      "provider_name": "github-actions",
      "subject": "repo:acme-inc/*"
    }
    ```

    To match a prefix within a name, add a `condition` such as
    `claims.sub.startsWith("repo:acme/app-")`.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_CREATE` permission.

    Args:
        name (str): The name of the service account, without the reserved `svc:` prefix. Example:
            ci-pipeline.
        body (CreateWorkloadIdentityBindingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWorkloadIdentityBindingResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateWorkloadIdentityBindingRequest,
) -> CreateWorkloadIdentityBindingResponse | ProblemDetails | None:
    """Create a workload identity binding for a service account

     Creates a workload identity binding for a service account.

    A trailing `*` in `subject` makes it a prefix match, for example `repo:acme/app:*`.
    For `SPIFFE` providers, the prefix must end with `/`.

    For multi-tenant issuers like GitHub and GitLab, ensure that the prefix contains
    *at least* your organization to prevent cross-tenant abuse. For example:

    ```json
    {
      "provider_name": "github-actions",
      "subject": "repo:acme-inc/*"
    }
    ```

    To match a prefix within a name, add a `condition` such as
    `claims.sub.startsWith("repo:acme/app-")`.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_CREATE` permission.

    Args:
        name (str): The name of the service account, without the reserved `svc:` prefix. Example:
            ci-pipeline.
        body (CreateWorkloadIdentityBindingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWorkloadIdentityBindingResponse | ProblemDetails
    """

    return sync_detailed(
        name=name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateWorkloadIdentityBindingRequest,
) -> Response[CreateWorkloadIdentityBindingResponse | ProblemDetails]:
    """Create a workload identity binding for a service account

     Creates a workload identity binding for a service account.

    A trailing `*` in `subject` makes it a prefix match, for example `repo:acme/app:*`.
    For `SPIFFE` providers, the prefix must end with `/`.

    For multi-tenant issuers like GitHub and GitLab, ensure that the prefix contains
    *at least* your organization to prevent cross-tenant abuse. For example:

    ```json
    {
      "provider_name": "github-actions",
      "subject": "repo:acme-inc/*"
    }
    ```

    To match a prefix within a name, add a `condition` such as
    `claims.sub.startsWith("repo:acme/app-")`.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_CREATE` permission.

    Args:
        name (str): The name of the service account, without the reserved `svc:` prefix. Example:
            ci-pipeline.
        body (CreateWorkloadIdentityBindingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWorkloadIdentityBindingResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateWorkloadIdentityBindingRequest,
) -> CreateWorkloadIdentityBindingResponse | ProblemDetails | None:
    """Create a workload identity binding for a service account

     Creates a workload identity binding for a service account.

    A trailing `*` in `subject` makes it a prefix match, for example `repo:acme/app:*`.
    For `SPIFFE` providers, the prefix must end with `/`.

    For multi-tenant issuers like GitHub and GitLab, ensure that the prefix contains
    *at least* your organization to prevent cross-tenant abuse. For example:

    ```json
    {
      "provider_name": "github-actions",
      "subject": "repo:acme-inc/*"
    }
    ```

    To match a prefix within a name, add a `condition` such as
    `claims.sub.startsWith("repo:acme/app-")`.

    Requires the `ACCESS_MANAGEMENT` or `ACCESS_MANAGEMENT_CREATE` permission.

    Args:
        name (str): The name of the service account, without the reserved `svc:` prefix. Example:
            ci-pipeline.
        body (CreateWorkloadIdentityBindingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWorkloadIdentityBindingResponse | ProblemDetails
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            body=body,
        )
    ).parsed
