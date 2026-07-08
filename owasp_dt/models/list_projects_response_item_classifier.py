from enum import Enum


class ListProjectsResponseItemClassifier(str, Enum):
    APPLICATION = "APPLICATION"
    CONTAINER = "CONTAINER"
    CRYPTOGRAPHIC_ASSET = "CRYPTOGRAPHIC_ASSET"
    DATA = "DATA"
    DEVICE = "DEVICE"
    DEVICE_DRIVER = "DEVICE_DRIVER"
    FILE = "FILE"
    FIRMWARE = "FIRMWARE"
    FRAMEWORK = "FRAMEWORK"
    LIBRARY = "LIBRARY"
    MACHINE_LEARNING_MODEL = "MACHINE_LEARNING_MODEL"
    OPERATING_SYSTEM = "OPERATING_SYSTEM"
    PLATFORM = "PLATFORM"

    def __str__(self) -> str:
        return str(self.value)
