from enum import StrEnum


class TotalCountType(StrEnum):
    AT_LEAST = "AT_LEAST"
    EXACT = "EXACT"

    def __str__(self) -> str:
        return str(self.value)
