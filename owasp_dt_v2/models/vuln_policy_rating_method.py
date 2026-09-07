from enum import StrEnum


class VulnPolicyRatingMethod(StrEnum):
    CVSSV2 = "CVSSV2"
    CVSSV3 = "CVSSV3"
    CVSSV4 = "CVSSV4"
    OWASP = "OWASP"

    def __str__(self) -> str:
        return str(self.value)
