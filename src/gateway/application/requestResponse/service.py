from src.gateway.domain.request.entity import RequestEntity
from src.gateway.domain.request.interface import RequestRepositoryInterface
from src.gateway.domain.request.repository import RequestRepository
from src.gateway.domain.response.entity import ResponseEntity
from src.gateway.domain.response.repository import ResponseRepository
from src.gateway.domain.response.interface import ResponseRepositoryInterface

class RequestResponseService:
    def __init__(self, request: RequestRepositoryInterface, response: ResponseRepositoryInterface) -> None:
        self.request = request
        self.response = response

    def save(self, request, response) -> None:
        self.request.save(request)
        self.response.save(response)