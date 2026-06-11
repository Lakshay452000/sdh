from abc import ABC, abstractmethod

from app.architecture_review.models import (
    ArchitectureReviewResponse
)


class ArchitectureRule(ABC):

    @abstractmethod
    def apply(
            self,
            review: ArchitectureReviewResponse
    ) -> None:
        pass