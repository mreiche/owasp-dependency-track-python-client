from enum import StrEnum


class AnalysisSeverity(StrEnum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    INFO = "INFO"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    UNASSIGNED = "UNASSIGNED"

    def __str__(self) -> str:
        return str(self.value)
