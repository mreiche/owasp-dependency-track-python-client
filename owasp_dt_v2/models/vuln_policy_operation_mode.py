from enum import Enum


class VulnPolicyOperationMode(str, Enum):
    APPLY = "APPLY"
    DISABLED = "DISABLED"
    LOG = "LOG"

    def __str__(self) -> str:
        return str(self.value)
