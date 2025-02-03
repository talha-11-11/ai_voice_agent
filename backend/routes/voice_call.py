from fastapi import APIRouter
import requests
import os

voice_call_router = APIRouter()
MILLIS_API_URL = "https://api.millis.ai/voice-session"
MILLIS_API_KEY = os.getenv("MILLIS_API_KEY")

@voice_call_router.post("/start")
def start_voice_call(metadata: dict):
    headers = {
        "Authorization": f"Bearer {MILLIS_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(MILLIS_API_URL, headers=headers, json=metadata)
    if response.status_code == 200:
        return {"status": "Voice call started successfully!", "response": response.json()}
    return {"status": "Error starting voice call", "details": response.text}