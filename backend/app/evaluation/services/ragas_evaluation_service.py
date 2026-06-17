from app.services.rag_service import (
    RagService
)
from app.evaluation.services.dataset_loader import (
    DatasetLoader
)
from app.evaluation.models.evaluation_sample import (
    EvaluationSample
)
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings
)

from app.config.settings import settings
from datasets import Dataset

from ragas import evaluate as ragas_evaluate

from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall
)

from app.evaluation.models.evaluation_result import (
    EvaluationResult
)
from app.evaluation.services.evaluation_report_service import (
    EvaluationReportService
)

class RagasEvaluationService:

    def __init__(
        self,
        rag_service: RagService,
        dataset_loader: DatasetLoader,
        report_service: EvaluationReportService
    ):
        self._rag_service = rag_service
        self._dataset_loader = dataset_loader
        self._report_service = report_service

    def build_samples(
        self
    ) -> list[EvaluationSample]:

        dataset = (
            self._dataset_loader.load()
        )

        samples = []

        for item in dataset:

            response = (
                self._rag_service.ask(
                    session_id="evaluation",
                    question=item.question,
                    evaluation_mode=True
                )
            )

            samples.append(
                EvaluationSample(
                    question=item.question,
                    ground_truth=item.ground_truth,
                    answer=response.answer,
                    contexts=[
                        chunk.content
                        for chunk in response.retrieved_chunks
                    ]
                )
            )

        return samples
    
    def run_evaluation(
        self
    ) -> EvaluationResult:

        samples = self.build_samples()

        dataset = Dataset.from_list(
            [
                {
                    "question": sample.question,
                    "answer": sample.answer,
                    "contexts": sample.contexts,
                    "ground_truth": sample.ground_truth
                }
                for sample in samples
            ]
        )
        gemini_llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=settings.gemini_api_key
        )

        gemini_embeddings = (
            GoogleGenerativeAIEmbeddings(
                model="models/text-embedding-004",
                google_api_key=settings.gemini_api_key
            )
        )
        result = ragas_evaluate(
            dataset=dataset,
            metrics=[
                faithfulness
                # answer_relevancy,
                # context_precision,
                # context_recall
            ],
            llm=gemini_llm,
            embeddings=gemini_embeddings
        )

        scores = result.to_pandas().mean(
            numeric_only=True
        )

        faithfulness_score = float(
            scores["faithfulness"]
        )

        # answer_relevancy_score = float(
        #     scores["answer_relevancy"]
        # )

        # context_precision_score = float(
        #     scores["context_precision"]
        # )

        # context_recall_score = float(
        #     scores["context_recall"]
        # )

        # overall_score = (
        #     faithfulness_score +
        #     answer_relevancy_score +
        #     context_precision_score +
        #     context_recall_score
        # ) / 4

        # evaluation_result = EvaluationResult(
        #     overall_score=overall_score,
        #     faithfulness=faithfulness_score,
        #     answer_relevancy=answer_relevancy_score,
        #     context_precision=context_precision_score,
        #     context_recall=context_recall_score
        # )
        evaluation_result = EvaluationResult(
            overall_score=faithfulness_score,
            faithfulness=faithfulness_score,
            answer_relevancy=0.0,
            context_precision=0.0,
            context_recall=0.0
        )
        self._report_service.save(
            evaluation_result
        )
        return evaluation_result