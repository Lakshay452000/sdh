from abc import ABC, abstractmethod

from app.architecture.models import (
    ArchitectureReviewResponse
)


class ArchitectureRule(ABC):

    @abstractmethod
    def apply(
            self,
            review: ArchitectureReviewResponse
    ) -> None:
        pass