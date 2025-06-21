from pydantic import BaseModel
from typing import List

class ResumeData(BaseModel):
    name: str
    skills: List[str]

class ScoringRequest(BaseModel):
    transcript: str
    role: str

class ScoringFeedback(BaseModel):
    scores: dict
    feedback: dict
