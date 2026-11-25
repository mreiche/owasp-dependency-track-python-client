from enum import StrEnum


class GetProjectChildrenConciseSortOrder(StrEnum):
    ASC = "asc"
    DESC = "desc"

    def __str__(self) -> str:
        return str(self.value)
