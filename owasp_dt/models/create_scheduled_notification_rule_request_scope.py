from enum import StrEnum


class CreateScheduledNotificationRuleRequestScope(StrEnum):
    PORTFOLIO = "PORTFOLIO"
    SYSTEM = "SYSTEM"

    def __str__(self) -> str:
        return str(self.value)
