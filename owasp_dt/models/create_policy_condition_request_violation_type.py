from enum import StrEnum


class CreatePolicyConditionRequestViolationType(StrEnum):
    LICENSE = "LICENSE"
    OPERATIONAL = "OPERATIONAL"
    SECURITY = "SECURITY"

    def __str__(self) -> str:
        return str(self.value)
