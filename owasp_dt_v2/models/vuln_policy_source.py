from enum import StrEnum


class VulnPolicySource(StrEnum):
    BUNDLE = "BUNDLE"
    USER = "USER"

    def __str__(self) -> str:
        return str(self.value)
