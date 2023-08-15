from fastapi import FastAPI, APIRouter, Depends
from src.gateway.infrastructure.database.sqlServer.utils.manager import DatabaseManager as SqlServerDB
from src.gateway.infrastructure.database.sqlServer.request.request import SQLServerRequestRepository as request_repository
from src.gateway.domain.request.entity import RequestEntity
from src.gateway.domain.request.interface import RequestRepositoryInterface
from src.gateway.domain.response.entity import ResponseEntity
from src.gateway.domain.response.interface import ResponseRepositoryInterface
from src.gateway.infrastructure.database.sqlServer.response.response import SQLServerResponseRepository as response_repository
from src.gateway.domain.response.entity import ResponseEntity
from src.gateway.application.requestResponse.service import RequestResponseService


app = FastAPI()
router = APIRouter(prefix="/gateway/v1")
db = SqlServerDB()


@router.post("/save/request_response")
def save_request_response(request_data: RequestEntity, response_data: ResponseEntity, 
                          request_repo: RequestRepositoryInterface = Depends(request_repository),
                          response_repo: ResponseRepositoryInterface = Depends(response_repository)):
    
    service = RequestResponseService(request_repo, response_repo)
    service.save(request_data, response_data)
    
    return {"status": "success"}

app.include_router(router)