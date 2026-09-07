from enum import StrEnum


class ScoreLikelihood(StrEnum):
    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"

    def __str__(self) -> str:
        return str(self.value)
