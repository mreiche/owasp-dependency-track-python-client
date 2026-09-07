from enum import StrEnum


class ViolationAnalysisAnalysisState(StrEnum):
    APPROVED = "APPROVED"
    NOT_SET = "NOT_SET"
    REJECTED = "REJECTED"

    def __str__(self) -> str:
        return str(self.value)
