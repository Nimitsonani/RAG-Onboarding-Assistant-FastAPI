import requests
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='.env')
API_KEY = os.getenv('MISTRAL_API_KEY')


def api_call(query,vector_list):
    msg = f"You are an onboarding assistant for new employees in a chemical company; the user question is '{query}'; the following is context from the internal knowledge base (top 3 results with distance ≤ 1.2): {vector_list}; use ONLY this context to answer; if the context is empty or does not contain the answer, clearly state that you do not have this information; do not guess, invent, or assume facts; keep the response clear, concise, professional, and easy for new employees to understand."
    payload = {
        'model': 'mistral-large-latest',
        "messages": [{
                "role": "system",
                "content": msg
    }]
    }
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    response = requests.post(url='https://api.mistral.ai/v1/chat/completions', json=payload, headers=headers)
    response = response.json()

    try:
        ans = response['choices'][0]['message']['content']
        return ans
    except Exception as e:
        print(e)
        return 'Model is not Available Right Now. Try Again Later.'
