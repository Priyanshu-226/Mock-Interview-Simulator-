from fastapi import APIRouter
from services.scorer import evaluate_intro

router = APIRouter()

@router.post("/evaluate")
def evaluate_intro_route(transcript: str, role: str):
    return evaluate_intro(transcript, role)