from enum import StrEnum


class PolicyOperator(StrEnum):
    ALL = "ALL"
    ANY = "ANY"

    def __str__(self) -> str:
        return str(self.value)
