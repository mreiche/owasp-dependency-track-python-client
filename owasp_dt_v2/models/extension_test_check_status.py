from enum import StrEnum


class ExtensionTestCheckStatus(StrEnum):
    FAILED = "FAILED"
    PASSED = "PASSED"
    SKIPPED = "SKIPPED"

    def __str__(self) -> str:
        return str(self.value)
