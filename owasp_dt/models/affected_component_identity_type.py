from enum import StrEnum


class AffectedComponentIdentityType(StrEnum):
    CPE = "CPE"
    PURL = "PURL"

    def __str__(self) -> str:
        return str(self.value)
