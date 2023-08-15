from domain.request.entity import RequestEntity
from domain.request.interface import RequestRepositoryInterface
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.gateway.infrastructure.database.sqlServer.utils.manager import DatabaseManager as Db

class SQLServerRequestRepository(RequestRepositoryInterface): 
    def __init__(self, db: Db) -> None:
        self.db = db

    def save(self, request: RequestEntity) -> None: 
        session = self.db.get_db()
        try:
            request_model = RequestEntity(**request.model_dump)
            self.session.add(request_model)
            self.session.commit()

        except SQLAlchemyError as e:
            self.session.rollback()
            
            raise e
        finally:
            session.close()
