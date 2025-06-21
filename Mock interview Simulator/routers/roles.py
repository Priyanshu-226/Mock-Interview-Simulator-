from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_roles():
    return ["Software Engineer", "Data Scientist", "Product Manager"]