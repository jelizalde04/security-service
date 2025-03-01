from sqlalchemy import Column, Integer, String, Boolean
from db import Base

class AsyncTask(Base):
    __tablename__ = "async_tasks"

    id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String, index=True)
    status = Column(String, default="pending")
    result = Column(String, nullable=True)