from enum import StrEnum


class PolicyConditionResponseSubject(StrEnum):
    AGE = "AGE"
    COMPONENT_HASH = "COMPONENT_HASH"
    COORDINATES = "COORDINATES"
    CPE = "CPE"
    CWE = "CWE"
    EPSS = "EPSS"
    EXPRESSION = "EXPRESSION"
    IS_INTERNAL = "IS_INTERNAL"
    LICENSE = "LICENSE"
    LICENSE_GROUP = "LICENSE_GROUP"
    PACKAGE_URL = "PACKAGE_URL"
    SEVERITY = "SEVERITY"
    SWID_TAGID = "SWID_TAGID"
    VERSION = "VERSION"
    VERSION_DISTANCE = "VERSION_DISTANCE"
    VULNERABILITY_ID = "VULNERABILITY_ID"

    def __str__(self) -> str:
        return str(self.value)
