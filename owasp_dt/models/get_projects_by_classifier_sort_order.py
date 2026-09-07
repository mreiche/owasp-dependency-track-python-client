from enum import StrEnum


class GetProjectsByClassifierSortOrder(StrEnum):
    ASC_DESC = "asc, desc"

    def __str__(self) -> str:
        return str(self.value)
