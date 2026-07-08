from enum import Enum


class ListComponentsHashType(str, Enum):
    BLAKE2B_256 = "BLAKE2B_256"
    BLAKE2B_384 = "BLAKE2B_384"
    BLAKE2B_512 = "BLAKE2B_512"
    BLAKE3 = "BLAKE3"
    MD5 = "MD5"
    SHA1 = "SHA1"
    SHA3_256 = "SHA3_256"
    SHA3_384 = "SHA3_384"
    SHA3_512 = "SHA3_512"
    SHA_256 = "SHA_256"
    SHA_384 = "SHA_384"
    SHA_512 = "SHA_512"

    def __str__(self) -> str:
        return str(self.value)
