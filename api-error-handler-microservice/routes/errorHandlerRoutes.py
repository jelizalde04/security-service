from fastapi import APIRouter
from controllers.errorHandlerController import router as error_router

router = APIRouter()

router.include_router(error_router, prefix="/errors", tags=["Error Handling"])
