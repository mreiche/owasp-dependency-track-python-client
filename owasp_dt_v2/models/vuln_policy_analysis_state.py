from enum import StrEnum


class VulnPolicyAnalysisState(StrEnum):
    EXPLOITABLE = "EXPLOITABLE"
    FALSE_POSITIVE = "FALSE_POSITIVE"
    IN_TRIAGE = "IN_TRIAGE"
    NOT_AFFECTED = "NOT_AFFECTED"
    RESOLVED = "RESOLVED"

    def __str__(self) -> str:
        return str(self.value)
