from enum import StrEnum


class DataClassificationDirection(StrEnum):
    BI_DIRECTIONAL = "BI_DIRECTIONAL"
    INBOUND = "INBOUND"
    OUTBOUND = "OUTBOUND"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
