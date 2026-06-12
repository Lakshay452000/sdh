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

ARCHITECTURE_CORRECTION_PROMPT = """
You are a Principal Software Architect.

Original Architecture:
{architecture_description}

Review Findings:
{review_findings}

Evaluation:
{evaluation}

Your responsibilities:

1. Fix all identified issues.
2. Improve scalability, reliability, availability and maintainability.
3. Redesign the architecture where necessary instead of only patching issues.
4. Introduce appropriate architectural components when beneficial:
   - Load Balancers
   - API Gateway
   - Redis Cache
   - Message Queue (Kafka/RabbitMQ)
   - Database Replicas
   - Monitoring
   - Service Separation

Return ONLY valid JSON.

{{
  "corrected_architecture": "",
  "changes": [
    {{
      "issue": "",
      "applied_fix": "",
      "reasoning": ""
    }}
  ],
  "summary": {{
    "major_improvements": [],
    "expected_benefits": [],
    "tradeoffs": []
  }}
}}

Do not add additional fields.
"""

ARCHITECTURE_MERMAID_PROMPT = """
You are an expert software architect.

Convert the following architecture into a valid Mermaid graph TD diagram.

Architecture:
{architecture}

Requirements:
- Return ONLY Mermaid code.
- Start with 'graph TD'.
- Do not include explanations.
- Do not include markdown code fences.
- Do not include ```mermaid.
- Do not include any text before or after the diagram.
"""