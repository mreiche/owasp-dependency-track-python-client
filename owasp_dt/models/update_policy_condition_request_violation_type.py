from enum import StrEnum


class UpdatePolicyConditionRequestViolationType(StrEnum):
    LICENSE = "LICENSE"
    OPERATIONAL = "OPERATIONAL"
    SECURITY = "SECURITY"

    def __str__(self) -> str:
        return str(self.value)
