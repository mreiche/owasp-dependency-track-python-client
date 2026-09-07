from enum import StrEnum


class ListProjectsResponseItemCollectionLogic(StrEnum):
    AGGREGATE_DIRECT_CHILDREN = "AGGREGATE_DIRECT_CHILDREN"
    AGGREGATE_DIRECT_CHILDREN_WITH_TAG = "AGGREGATE_DIRECT_CHILDREN_WITH_TAG"
    AGGREGATE_LATEST_VERSION_CHILDREN = "AGGREGATE_LATEST_VERSION_CHILDREN"

    def __str__(self) -> str:
        return str(self.value)
