from fastapi import FastAPI
from domain.logging.interfaces import LoggerInterface
from infrastructure.logging.console_logger import ConsoleLogger
from infrastructure.middleware.logging_middleware import LoggingMiddleware
from dotenv import load_dotenv
import uvicorn
import os

app = FastAPI()
logger: LoggerInterface = ConsoleLogger()
app.middleware("http")(LoggingMiddleware(app, logger))

if __name__ == "__main__":
    load_dotenv()
    uvicorn.run("main.app", 
        host=os.environ.get("APP_HOSTNAME"),
        port= int(os.environ.get("APP_PORT")),
        reload= bool(os.environ.get("Reload")))