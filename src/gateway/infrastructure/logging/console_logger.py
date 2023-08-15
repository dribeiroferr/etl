import logging
from src.gateway.domain.logging.interfaces import LoggerInterface

class ConsoleLogger(LoggerInterface):

    def __init__(self):
        logging.basicConfig(level=logging.INFO)

    def log(self, message: str) -> None:
        logging.info(message)