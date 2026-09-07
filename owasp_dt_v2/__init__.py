"""A client library for accessing OWASP Dependency-Track (Server v5.1.0)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
