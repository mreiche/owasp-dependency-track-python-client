from enum import Enum


class TaskQueueStatus(str, Enum):
    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"

    def __str__(self) -> str:
        return str(self.value)
