from enum import Enum


class GetFindingsByProjectSource(str, Enum):
    GITHUB = "GITHUB"
    INTERNAL = "INTERNAL"
    NVD = "NVD"
    OSSINDEX = "OSSINDEX"
    OSV = "OSV"
    SNYK = "SNYK"
    UNKNOWN = "UNKNOWN"
    VULNDB = "VULNDB"

    def __str__(self) -> str:
        return str(self.value)
