from fastapi import APIRouter, HTTPException, Request, Depends
from sqlalchemy.orm import Session
from db.connection import SessionLocal
from services.person_service import person_exists
from services.history_logger import log_request

router = APIRouter()

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/person/{firstname}")
def check_person_exists(
    firstname: str,
    request: Request,
    db: Session = Depends(get_db)
):
    #Checking database people table
    exists = person_exists(firstname, db)
    #Inserting to history
    log_request(str(request.url), exists, db)
    return {"exists": exists}
