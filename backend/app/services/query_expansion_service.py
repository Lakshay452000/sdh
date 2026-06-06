class QueryExpansionService:

    def generate_queries(
        self,
        question: str
    ) -> list[str]:

        queries = [question]

        lower_question = question.lower()

        if "work" in lower_question:

            queries.extend(
                [
                    "current employer",
                    "current company",
                    "workplace"
                ]
            )

        if "experience" in lower_question:

            queries.extend(
                [
                    "professional experience",
                    "employment history"
                ]
            )

        return list(
            set(queries)
        )