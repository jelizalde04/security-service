from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from services.errorHandlerService import log_error
from db import get_db
from pydantic import BaseModel

router = APIRouter()

class ErrorReport(BaseModel):
    error_message: str
    error_type: str
    endpoint: str
    status_code: int

@router.post("/log-error")
def report_error(error: ErrorReport, db: Session = Depends(get_db)):
    return log_error(db, error.error_message, error.error_type, error.endpoint, error.status_code)

@router.get("/errors")
def get_errors(db: Session = Depends(get_db)):
    errors = db.query(ErrorLog).all()
    return errors
