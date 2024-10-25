
# Google Gemini API Integration Example

import requests

def generate_gemini_questions(prompt, api_key):
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.post(
        "https://api.google.com/gemini/v1/generate_questions",
        headers=headers,
        json={"prompt": prompt, "max_tokens": 500}
    )
    return response.json().get("generated_text", "").strip()
