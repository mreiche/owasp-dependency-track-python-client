from enum import Enum


class ExtensionTestCheckStatus(str, Enum):
    FAILED = "FAILED"
    PASSED = "PASSED"
    SKIPPED = "SKIPPED"

    def __str__(self) -> str:
        return str(self.value)
