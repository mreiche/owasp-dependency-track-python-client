from enum import StrEnum


class PolicyViolationState(StrEnum):
    FAIL = "FAIL"
    INFO = "INFO"
    WARN = "WARN"

    def __str__(self) -> str:
        return str(self.value)
