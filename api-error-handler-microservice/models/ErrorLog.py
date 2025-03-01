from sqlalchemy import Column, Integer, String, Text, DateTime
from db import Base
from datetime import datetime

class ErrorLog(Base):
    __tablename__ = "error_logs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    error_message = Column(Text, nullable=False)
    error_type = Column(String, nullable=False)
    endpoint = Column(String, nullable=True)
    status_code = Column(Integer, nullable=False)
