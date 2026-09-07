from enum import StrEnum


class CreateNotificationRuleRequestScope(StrEnum):
    PORTFOLIO = "PORTFOLIO"
    SYSTEM = "SYSTEM"

    def __str__(self) -> str:
        return str(self.value)
