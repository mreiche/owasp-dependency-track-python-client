from enum import StrEnum


class VulnPolicyAnalysisVendorResponse(StrEnum):
    CAN_NOT_FIX = "CAN_NOT_FIX"
    ROLLBACK = "ROLLBACK"
    UPDATE = "UPDATE"
    WILL_NOT_FIX = "WILL_NOT_FIX"
    WORKAROUND_AVAILABLE = "WORKAROUND_AVAILABLE"

    def __str__(self) -> str:
        return str(self.value)
