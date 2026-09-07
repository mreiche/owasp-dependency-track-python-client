from enum import StrEnum


class GetAllVulnerabilitiesSortOrder(StrEnum):
    ASC_DESC = "asc, desc"

    def __str__(self) -> str:
        return str(self.value)
