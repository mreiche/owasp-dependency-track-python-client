"""A client library for accessing OWASP Dependency-Track (Server v5.2.2)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
