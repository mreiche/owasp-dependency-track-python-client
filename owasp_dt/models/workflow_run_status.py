from enum import Enum


class WorkflowRunStatus(str, Enum):
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    CREATED = "CREATED"
    FAILED = "FAILED"
    RUNNING = "RUNNING"
    SUSPENDED = "SUSPENDED"

    def __str__(self) -> str:
        return str(self.value)
