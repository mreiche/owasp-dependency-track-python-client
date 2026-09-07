from enum import StrEnum


class GetTaggedNotificationRulesSortOrder(StrEnum):
    ASC_DESC = "asc, desc"

    def __str__(self) -> str:
        return str(self.value)
