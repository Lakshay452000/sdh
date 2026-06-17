import json
from pathlib import Path

from app.evaluation.models.evaluation_dataset_item import (
    EvaluationDatasetItem
)


class DatasetLoader:

    DATASET_PATH = (
        Path(__file__)
        .parent.parent
        / "datasets"
        / "rag_eval_dataset.json"
    )

    def load(
        self
    ) -> list[EvaluationDatasetItem]:

        with open(
            self.DATASET_PATH,
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        return [
            EvaluationDatasetItem(**item)
            for item in data
        ]