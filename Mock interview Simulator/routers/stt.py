from fastapi import APIRouter, UploadFile, File
from services.stt_transcriber import transcribe_audio

router = APIRouter()

@router.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    audio = await file.read()
    text = transcribe_audio(audio)
    return {"transcript": text}
