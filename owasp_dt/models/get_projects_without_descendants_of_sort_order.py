from enum import StrEnum


class GetProjectsWithoutDescendantsOfSortOrder(StrEnum):
    ASC = "asc"
    DESC = "desc"

    def __str__(self) -> str:
        return str(self.value)
