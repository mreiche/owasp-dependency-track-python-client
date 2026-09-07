from enum import StrEnum


class NotificationRuleNotificationLevel(StrEnum):
    ERROR = "ERROR"
    INFORMATIONAL = "INFORMATIONAL"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
