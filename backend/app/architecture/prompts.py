ARCHITECTURE_ANALYSIS_PROMPT = """
Analyze this software architecture diagram.

Identify:

1. Architecture summary
2. Components present
3. Data flow
4. Architecture type
5. Strengths
6. Design issues
7. Missing components
8. Architecture score (0-100)

Consider:

- Scalability
- Reliability
- Availability
- Single Points of Failure
- Load Balancers
- Caching
- Message Queues
- Database Replication
- Monitoring
- API Gateways

Return ONLY valid JSON.

{
  "score": 0,
  "summary": "",
  "components": [],
  "data_flow": "",
  "architecture_type": "",
  "strengths": [],
  "issues": [],
  "missing_components": [],
   "recommendations": []
}
"""

ARCHITECTURE_EVALUATION_PROMPT = """
You are a Staff+ System Design interviewer.

Evaluate the architecture using the architecture description and review findings.

Architecture Description:
{architecture_description}

Review Findings:
{review_findings}

Score the architecture from 0 to 100.

Evaluate the following categories:

- Scalability
- Reliability
- Availability
- Performance
- Security
- Maintainability

For each category:
- Give a score between 0 and 100.
- Explain the reasoning.

Return ONLY valid JSON.

{{
  "overall_score": 0,
  "category_scores": [
    {{
      "category": "Scalability",
      "score": 0,
      "reasoning": ""
    }}
  ],
  "strengths": [],
  "weaknesses": [],
  "recommendations": []
}}
"""