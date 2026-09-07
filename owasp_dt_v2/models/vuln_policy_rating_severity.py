from enum import StrEnum


class VulnPolicyRatingSeverity(StrEnum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    INFO = "INFO"
    LOW = "LOW"
    MEDIUM = "MEDIUM"

    def __str__(self) -> str:
        return str(self.value)
