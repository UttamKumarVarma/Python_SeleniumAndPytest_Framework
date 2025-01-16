import inspect
import logging

import pytest

@pytest.mark.usefixtures("browserSetup")
class BaseClass:

    def getLogger(self):
        logger_name = inspect.stack()[1][3]  # Get the calling function name
        logger = logging.getLogger(logger_name)

        if not logger.hasHandlers():  # Avoid duplicate handlers
            file_handler = logging.FileHandler("output.log")
            formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s: %(message)s")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        logger.setLevel(logging.INFO)
        return logger
