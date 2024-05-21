from logger_config import setup_logger

# Create a logger
logger = setup_logger()

def application():
    # Use the logger
    logger.debug("This is a debug message.")
    logger.info("This is an informative message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")

if __name__ == "__main__":
    application()
