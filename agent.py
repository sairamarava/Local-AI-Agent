import requests
import json

# Your OpenRouter API key
api_key = "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"

# OpenRouter API endpoint
api_url = "https://openrouter.ai/api/v1/chat/completions"

# Headers
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Request payload
payload = {
    "model": "mistralai/mistral-7b-instruct",
    "messages": [{"role": "user", "content": "what is capital of India"}]
}

# Send the request
response = requests.post(api_url, headers=headers, json=payload)


# Try parsing JSON response
try:
    response_json = response.json()
    print("AI Response:", response_json["choices"][0]["message"]["content"])
except Exception as e:
    print("Error parsing JSON:", e)
