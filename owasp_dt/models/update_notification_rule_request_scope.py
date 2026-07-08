from enum import Enum


class UpdateNotificationRuleRequestScope(str, Enum):
    PORTFOLIO = "PORTFOLIO"
    SYSTEM = "SYSTEM"

    def __str__(self) -> str:
        return str(self.value)
