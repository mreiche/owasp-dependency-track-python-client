from enum import Enum


class VulnPolicySource(str, Enum):
    BUNDLE = "BUNDLE"
    USER = "USER"

    def __str__(self) -> str:
        return str(self.value)
