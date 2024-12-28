# -*- coding: utf-8 -*-
import logging

def setup_logging():
    logger = logging.getLogger()

    if not logger.handlers:
        handler = logging.FileHandler("py_log.log", encoding="utf-8")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)

        logger.setLevel(logging.INFO)
        logger.addHandler(handler)

    return logger
