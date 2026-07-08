from enum import Enum


class ProjectPropertyPropertyType(str, Enum):
    BOOLEAN = "BOOLEAN"
    INTEGER = "INTEGER"
    NUMBER = "NUMBER"
    STRING = "STRING"
    TIMESTAMP = "TIMESTAMP"
    URL = "URL"
    UUID = "UUID"

    def __str__(self) -> str:
        return str(self.value)
