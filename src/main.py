from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from fastapi.middleware.cors import CORSMiddleware
import logging
import httpx

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Instrumentator().instrument(app).expose(app)

@app.get("/api/health")
def read_root():
    logging.info("Health check endpoint called")
    return {"status": "ok"}

@app.get("/api/serve")
async def serve():
    logging.info("Quote endpoint called")
    async with httpx.AsyncClient() as client:
        response = await client.get("https://dummyjson.com/quotes/1")
        return response.json()
