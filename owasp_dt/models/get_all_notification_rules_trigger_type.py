from enum import StrEnum


class GetAllNotificationRulesTriggerType(StrEnum):
    EVENT = "EVENT"
    SCHEDULE = "SCHEDULE"

    def __str__(self) -> str:
        return str(self.value)
