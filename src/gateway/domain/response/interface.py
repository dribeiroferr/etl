from abc import ABC, abstractclassmethod
from domain.response.entity import ResponseEntity

class ResponseRepositoryInterface(ABC): 
    
    @abstractclassmethod
    def save(self, response: ResponseEntity) -> None:
        pass
    
    @abstractclassmethod
    def find(self) -> dict[ResponseEntity]:
        # Method needs to be implemented
        pass

    @abstractclassmethod
    def find_by_id(self, response_id: int) -> ResponseEntity:
        # Method needs to be implemented
        pass

    @abstractclassmethod
    def find_by_installer(self, installer: str) -> dict[ResponseEntity]:
        # Method needs to be implemented
        pass
