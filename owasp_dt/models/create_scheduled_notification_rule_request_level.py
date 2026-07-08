from enum import Enum


class CreateScheduledNotificationRuleRequestLevel(str, Enum):
    ERROR = "ERROR"
    INFORMATIONAL = "INFORMATIONAL"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
