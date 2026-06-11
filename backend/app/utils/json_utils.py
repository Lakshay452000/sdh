import json


def extract_json(
        response: str
) -> dict:

    cleaned_response = (
        response
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(
        cleaned_response
    )