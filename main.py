import os
import logging
import time

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from security.cors import add_app_cors
from logger import get_logger
from services.engine_router import engine_router

load_dotenv()
logging.basicConfig(level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = get_logger(__name__)

app = FastAPI()
add_app_cors(app)
app.include_router(engine_router)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.exception_handler(HTTPException)
async def exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={'message': f"Something went wrong {exc}, there is rainbow"})


@app.get("/healthz")
@app.get("/")
async def main():
    return {"message": "Hello World"}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app="main:app",
                host=os.getenv("APP_PORT", '0.0.0.0'),
                port=os.getenv("APP_PORT", 5055),
                log_level="info",
                access_log=True,
                reload=True)
