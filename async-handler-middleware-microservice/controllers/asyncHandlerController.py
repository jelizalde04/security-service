from fastapi import APIRouter, HTTPException
from services.asyncHandlerService import async_task

router = APIRouter()

@router.post("/execute/")
async def execute_task(data: str):
    task = async_task.apply_async(args=[data])
    return {"task_id": task.id, "status": "Task started"}
