from app.architecture.rules.missing_load_balancer_rule import (
    MissingLoadBalancerRule
)
from app.architecture.rules.missing_load_balancer_rule import (
    MissingLoadBalancerRule
)

class RuleEngine:

    def __init__(self):

        self.rules = [
            MissingLoadBalancerRule()
        ]

    def execute(
            self,
            review
    ):

        for rule in self.rules:
            rule.apply(review)

        return review