from abc import (
    ABC,
    abstractmethod
)


class QueryRewriter(ABC):

    @abstractmethod
    def rewrite(
        self,
        question: str,
        history: str
    ) -> str:
        pass