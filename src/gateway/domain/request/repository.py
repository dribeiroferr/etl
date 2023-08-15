from src.gateway.domain.request.entity import RequestEntity

class RequestRepository: 
    def save(self, request: RequestEntity) -> None:
        pass
    def find_by_id(self, id: str) -> list[str]:
        pass