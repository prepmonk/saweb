import logging
from logging.handlers import RotatingFileHandler
import os

FORMAT = "[%(levelname)s] [%(asctime)s] : %(message)s"


def get_logger(name, log_file_name="app.log"):
    logger = logging.getLogger(name)
    logger.setLevel(os.getenv("LOG_LEVEL", "DEBUG").upper())
    logger.propagate = False
    formatter = logging.Formatter(fmt=FORMAT)

    console_handler = logging.StreamHandler()
    file_handler = RotatingFileHandler(filename=log_file_name, maxBytes=10000000)

    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
