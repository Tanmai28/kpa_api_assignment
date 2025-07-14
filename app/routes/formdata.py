from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/formdata", response_model=List[schemas.FormDataResponse])
def get_formdata(db: Session = Depends(get_db)):
    return crud.get_all_formdata(db)