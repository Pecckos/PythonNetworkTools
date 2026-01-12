import logging
import os
# Function to set up logging configuration, Create log dir "logs" and log file "pythonnetworktools.log"
def setup_logging():
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "pythonnetworktools.log")

    # Configure logging
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    #If handlers already exist, clear them to avoid duplicate logs
    if logger.hasHandlers():
        logger.handlers.clear()
    # Create file handler by open the log file and add formatter
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)
    
    # Add the file handler to the logger
    logger.addHandler(file_handler)

    logging.info("Logging initialized.")