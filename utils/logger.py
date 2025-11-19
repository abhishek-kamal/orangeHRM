import logging

def get_logger():
    logger = logging.getLogger()
    if not logger.handlers:
        handler = logging.FileHandler("logs/test.log")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger
