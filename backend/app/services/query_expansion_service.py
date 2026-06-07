class QueryExpansionService:

    def generate_queries(
        self,
        question: str
    ) -> list[str]:

        queries = [question]

        lower_question = (
            question.lower()
        )

        expansions = {

            "redis": [
                "redis cache",
                "caching",
                "in-memory datastore"
            ],

            "kafka": [
                "event streaming",
                "message queue",
                "pub sub"
            ],

            "vault": [
                "hashicorp vault",
                "secret management",
                "credentials storage"
            ],

            "microservices": [
                "distributed services",
                "service architecture",
                "backend services"
            ],

            "grpc": [
                "remote procedure call",
                "rpc",
                "inter service communication"
            ],

            "work": [
                "current employer",
                "current company",
                "workplace"
            ],

            "experience": [
                "professional experience",
                "employment history"
            ]
        }

        for keyword, synonyms in (
            expansions.items()
        ):

            if keyword in lower_question:

                queries.extend(
                    synonyms
                )

        return list(
            set(queries)
        )