from enum import StrEnum


class VulnPolicyOperationMode(StrEnum):
    APPLY = "APPLY"
    DISABLED = "DISABLED"
    LOG = "LOG"

    def __str__(self) -> str:
        return str(self.value)
