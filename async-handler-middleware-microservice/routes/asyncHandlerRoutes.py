from fastapi import APIRouter
from controllers.asyncHandlerController import router as async_handler_router

router = APIRouter()
router.include_router(async_handler_router, prefix="/async", tags=["Async Handler"])