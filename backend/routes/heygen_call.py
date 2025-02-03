from fastapi import APIRouter
import requests
import os

heygen_call_router = APIRouter()
HEYGEN_API_URL = "https://api.heygen.com/avatar-streaming"
HEYGEN_API_KEY = os.getenv("HEYGEN_API_KEY")

@heygen_call_router.post("/start")
def start_heygen_call(text: str):
    headers = {
        "Authorization": f"Bearer {HEYGEN_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "voice_id": "default_voice",
        "avatar_id": "default_avatar"
    }
    response = requests.post(HEYGEN_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return {"status": "HeyGen avatar call started successfully!", "response": response.json()}
    return {"status": "Error starting HeyGen call", "details": response.text}