from fastapi import APIRouter
import os

router = APIRouter()
nationality = os.getenv("NATIONALITY", "us")
port = os.getenv("PORT", "unknown")

@router.get("/")
def root():
    return {"message": f"{nationality.upper()} People API is running on port {port}"}