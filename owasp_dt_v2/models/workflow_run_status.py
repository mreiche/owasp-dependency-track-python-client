from enum import StrEnum


class WorkflowRunStatus(StrEnum):
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    CREATED = "CREATED"
    FAILED = "FAILED"
    RUNNING = "RUNNING"
    SUSPENDED = "SUSPENDED"

    def __str__(self) -> str:
        return str(self.value)
