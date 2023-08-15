from pydantic import BaseModel
from typing import Dict, Any

class ResponseEntity(BaseModel):
    status_code: int
    headers: Dict[str, str]
    body: Any

    def save(self):
        # Logic to save the response data, e.g., to a database
        pass