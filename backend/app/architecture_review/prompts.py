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