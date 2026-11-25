from enum import StrEnum


class GetRepositoriesByTypeSortOrder(StrEnum):
    ASC = "asc"
    DESC = "desc"

    def __str__(self) -> str:
        return str(self.value)
