import os
from dotenv import load_dotenv

class SQLServerConfig:
    load_dotenv()
    SQLALCHEMY_DATABASE_URL = os.environ.get("SQLALCHEMY_DATABASE_URL")
    POOL_SIZE = int(os.environ.get("POOL_SIZE"))
    MAX_OVERFLOW = int(os.environ.get("MAX_OVERFLOW"))
