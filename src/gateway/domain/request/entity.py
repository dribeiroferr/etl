from pydantic import BaseModel
from typing import Dict, Any

class RequestEntity(BaseModel):
    method: str
    url: str
    headers: Dict[str, str]
    query_params: Dict[str, Any]
    body: Any