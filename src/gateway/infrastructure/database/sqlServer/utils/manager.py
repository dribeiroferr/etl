from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.gateway.infrastructure.database.sqlServer.utils.config import SQLServerConfig as config

class DatabaseManager: 
    def __init__(self) -> None:
        self.engine = create_engine(
            config.SQLALCHEMY_DATABASE_URL,
            pool_size = config.POOL_SIZE,
            max_overflow= config.MAX_OVERFLOW
        )
        self.SessionLocal = sessionmaker(bind=self.engine)
    def get_db(self) -> None:
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()