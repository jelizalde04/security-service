from fastapi import FastAPI
from db import Base, engine
from routes.asyncHandlerRoutes import router as async_routes
import uvicorn

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Async Handler Microservice",
    description="Handles async tasks via Celery + Redis",
    version="1.0.0"
)

app.include_router(async_routes)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3003)
