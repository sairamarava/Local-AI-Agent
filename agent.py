import requests
import json

# Your OpenRouter API key should be pasted here.
api_key = ""

# OpenRouter API endpoint this can be changed according to which model you want.
api_url = "https://openrouter.ai/api/v1/chat/completions"

# Headers--> strictly needed
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# you can change the messages content for output. 

# Request payload--> you can manipulate the payload["messages"][0]["content"] here
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
