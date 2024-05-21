import logging
import sys

def setup_logger():
    # Create a logger object
    logger = logging.getLogger("Application Logger")
    logger.setLevel(logging.DEBUG)

    # Create console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)

    # Create file handler
    file_handler = logging.FileHandler('logs/application.log')
    file_handler.setLevel(logging.DEBUG)

    # Create formatter
    formatter = logging.Formatter("[%(levelname)s] - %(message)s")

    # Attach formatter to console handler
    console_handler.setFormatter(formatter)

    # Attach formatter to file handler
    file_handler.setFormatter(formatter)

    # Add console handler to logger
    logger.addHandler(console_handler)
    
    # Add file handler to logger
    logger.addHandler(file_handler)

    return logger
