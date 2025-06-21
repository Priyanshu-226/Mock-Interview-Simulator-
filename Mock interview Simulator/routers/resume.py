from fastapi import APIRouter, File, UploadFile
from services.resume_parser import extract_resume_data

router = APIRouter()

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    content = await file.read()
    parsed_data = extract_resume_data(content)
    return parsed_data