from pathlib import Path
from datetime import datetime
import json

from app.evaluation.models.evaluation_result import (
    EvaluationResult
)


class EvaluationReportService:

    def save(
        self,
        result: EvaluationResult
    ) -> None:

        Path(
            "evaluation/results"
        ).mkdir(
            parents=True,
            exist_ok=True
        )

        filename = (
            datetime.now()
            .strftime(
                "%Y%m%d_%H%M%S.json"
            )
        )

        with open(
            f"evaluation/results/{filename}",
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                result.model_dump(),
                file,
                indent=4
            )