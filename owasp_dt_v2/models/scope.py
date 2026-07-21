from enum import Enum


class Scope(str, Enum):
    EXCLUDED = "EXCLUDED"
    OPTIONAL = "OPTIONAL"
    REQUIRED = "REQUIRED"

    def __str__(self) -> str:
        return str(self.value)
