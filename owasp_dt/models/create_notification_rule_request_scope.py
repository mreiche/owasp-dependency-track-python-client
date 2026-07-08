from enum import Enum


class CreateNotificationRuleRequestScope(str, Enum):
    PORTFOLIO = "PORTFOLIO"
    SYSTEM = "SYSTEM"

    def __str__(self) -> str:
        return str(self.value)
