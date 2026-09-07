from enum import StrEnum


class NotificationRuleScope(StrEnum):
    PORTFOLIO = "PORTFOLIO"
    SYSTEM = "SYSTEM"

    def __str__(self) -> str:
        return str(self.value)
