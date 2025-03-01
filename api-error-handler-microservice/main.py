from fastapi import FastAPI
import uvicorn
from routes.errorHandlerRoutes import router as error_router
from db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Error Handler Microservice", version="1.0")

app.include_router(error_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3002)
