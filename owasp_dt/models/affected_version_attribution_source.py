from enum import StrEnum


class AffectedVersionAttributionSource(StrEnum):
    CX = "CX"
    GITHUB = "GITHUB"
    INTERNAL = "INTERNAL"
    JVN = "JVN"
    NVD = "NVD"
    OSSINDEX = "OSSINDEX"
    OSV = "OSV"
    SNYK = "SNYK"
    UNKNOWN = "UNKNOWN"
    VULNDB = "VULNDB"

    def __str__(self) -> str:
        return str(self.value)
