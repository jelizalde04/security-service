from fastapi import APIRouter
from controllers.authController import router as auth_router

router = APIRouter()

router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
