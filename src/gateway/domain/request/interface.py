from abc import ABC, abstractclassmethod
from domain.request.entity import RequestEntity

class RequestRepositoryInterface(ABC): 
    
    @abstractclassmethod
    def save(self, request: RequestEntity):
        pass
    
    @abstractclassmethod
    def find(self) -> dict[RequestEntity]:
        # Method needs to be implemented
        pass

    @abstractclassmethod
    def find_by_id(self, request_id: int) -> RequestEntity:
        # Method needs to be implemented
        pass

    @abstractclassmethod
    def find_by_installer(self, installer: str) -> RequestEntity:
        # Method needs to be implemented
        pass
