from enum import Enum


class TaskQueueType(str, Enum):
    ACTIVITY = "ACTIVITY"
    WORKFLOW = "WORKFLOW"

    def __str__(self) -> str:
        return str(self.value)
