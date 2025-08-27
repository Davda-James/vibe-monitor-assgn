from fastapi import FastAPI
import requests as req
from prometheus_fastapi_instrumentator import Instrumentator
from fastapi.responses import Response
import logging

app = FastAPI()

Instrumentator().instrument(app).expose(app)

@app.get("/api/health")
def read_root():
    logging.info("Health check endpoint called")
    return {"status": "ok"}

@app.get("/api/serve")
async def serve():
    logging.info("Quote endpoint called")
    response = await req.get("/api/quotes/random")
    return response.json()
