from enum import StrEnum


class WorkloadIdentityProviderType(StrEnum):
    OIDC = "OIDC"
    SPIFFE = "SPIFFE"

    def __str__(self) -> str:
        return str(self.value)
