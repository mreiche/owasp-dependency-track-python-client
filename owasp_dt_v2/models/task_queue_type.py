from enum import StrEnum


class TaskQueueType(StrEnum):
    ACTIVITY = "ACTIVITY"
    WORKFLOW = "WORKFLOW"

    def __str__(self) -> str:
        return str(self.value)
