from app.architecture_review.models import (
    ArchitectureReviewResponse
)

from app.architecture_review.rules.architecture_rule import (
    ArchitectureRule
)


class MissingLoadBalancerRule(
    ArchitectureRule
):
    
    def apply(
            self,
            review: ArchitectureReviewResponse
    ) -> None:

        components = {
            component.lower()
            for component in review.components
        }

        if "load balancer" in components:
            return

        # Prevent duplicate issue if Gemini already found it
        if any(
            "load balancer" in issue.lower()
            for issue in review.issues
        ):
            return

        review.issues.append(
            "No load balancer detected."
        )

        review.missing_components.append(
            "Load Balancer"
        )

        review.score = max(
            0,
            review.score - 5
        )