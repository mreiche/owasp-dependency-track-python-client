from enum import StrEnum


class GetAllNotificationRulesSortOrder(StrEnum):
    ASC_DESC = "asc, desc"

    def __str__(self) -> str:
        return str(self.value)
