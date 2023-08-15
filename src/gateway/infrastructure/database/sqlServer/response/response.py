from domain.response.entity import ResponseEntity
from domain.response.interface import ResponseRepositoryInterface
from src.gateway.infrastructure.database.sqlServer.utils.manager import DatabaseManager as Db
from sqlalchemy.exc import SQLAlchemyError

class SQLServerResponseRepository(ResponseRepositoryInterface):
    def __init__(self, db: Db) -> None:
        self.db = db

    def save(self, response: ResponseEntity) -> None: 
        session: self.db.get_db()
        try:
            reqsponse_model = ResponseEntity(**response.model_dump)
            self.session.add(reqsponse_model)
            self.session.commit()

        except SQLAlchemyError as e:
            self.session.rollback()
            
            raise e
        finally: 
            session.close()