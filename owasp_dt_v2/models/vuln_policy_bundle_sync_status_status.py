from enum import StrEnum


class VulnPolicyBundleSyncStatusStatus(StrEnum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    RUNNING = "RUNNING"

    def __str__(self) -> str:
        return str(self.value)
