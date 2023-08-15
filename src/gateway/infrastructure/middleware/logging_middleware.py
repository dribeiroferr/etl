from fastapi import Request
from typing import Callable
from domain.logging.interfaces import LoggerInterface

class LoggingMiddleware:

    def __init__(self, app, logger: LoggerInterface):
        self.app = app
        self.logger = logger

    async def __call__(self, request: Request, call_next: Callable):
        # Log the incoming request
        self.logger.log(f"Request: {request.method} {request.url}")

        # Continue processing the request
        response = await call_next(request)

        # Log the outgoing response
        self.logger.log(f"Response: {response.status_code}")

        return response