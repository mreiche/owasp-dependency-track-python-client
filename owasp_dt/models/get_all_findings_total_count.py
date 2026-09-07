from enum import StrEnum


class GetAllFindingsTotalCount(StrEnum):
    BOUNDED = "BOUNDED"
    EXACT = "EXACT"

    def __str__(self) -> str:
        return str(self.value)
