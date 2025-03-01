from sqlalchemy.orm import Session
from models.ErrorLog import ErrorLog
from datetime import datetime

def log_error(db: Session, error_message: str, error_type: str, endpoint: str, status_code: int):
    error_entry = ErrorLog(
        error_message=error_message,
        error_type=error_type,
        endpoint=endpoint,
        status_code=status_code,
        timestamp=datetime.utcnow()
    )
    db.add(error_entry)
    db.commit()
    return {"message": "Error logged successfully"}
