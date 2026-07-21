from enum import Enum


class TotalCountType(str, Enum):
    AT_LEAST = "AT_LEAST"
    EXACT = "EXACT"

    def __str__(self) -> str:
        return str(self.value)
