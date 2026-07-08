from enum import Enum


class AnalysisSeverity(str, Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    INFO = "INFO"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    UNASSIGNED = "UNASSIGNED"

    def __str__(self) -> str:
        return str(self.value)
