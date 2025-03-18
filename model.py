import requests
import os

DEEPSEEK_API_ENDPOINT = os.getenv("https://deepseekhub6947024926.services.ai.azure.com/models/chat/completions?api-version=2024-05-01-preview")
DEEPSEEK_API_KEY = os.getenv("2Ss0sjP9U6f0ronN6JAlZ4bnEOcAE6njPMZFPqOSUec1reyILr5CJQQJ99BCACYeBjFXJ3w3AAAAACOGOFRS")
DEEPSEEK_MODEL_NAME = os.getenv("DeepSeek-R1")

def deepseek_chat(message):
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": DEEPSEEK_MODEL_NAME,
        "messages": [{"role": "user", "content": message}]
    }
    response = requests.post(DEEPSEEK_API_ENDPOINT, json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "Error en respuesta")
    return "Error en la conexión con DeepSeek"
