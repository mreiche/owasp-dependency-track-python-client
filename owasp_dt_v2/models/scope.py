from enum import StrEnum


class Scope(StrEnum):
    EXCLUDED = "EXCLUDED"
    OPTIONAL = "OPTIONAL"
    REQUIRED = "REQUIRED"

    def __str__(self) -> str:
        return str(self.value)
