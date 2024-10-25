
# ChatGPT API Integration Example

import openai

def generate_chatgpt_questions(prompt, api_key):
    openai.api_key = api_key
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()
