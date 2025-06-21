from fastapi import APIRouter
from services.tts_generator import generate_intro_audio

router = APIRouter()

@router.post("/generate")
def generate_intro(name: str, role: str):
    audio_path = generate_intro_audio(name, role)
    return {"audio_url": audio_path}