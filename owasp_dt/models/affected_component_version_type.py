from enum import StrEnum


class AffectedComponentVersionType(StrEnum):
    EXACT = "EXACT"
    RANGE = "RANGE"

    def __str__(self) -> str:
        return str(self.value)
