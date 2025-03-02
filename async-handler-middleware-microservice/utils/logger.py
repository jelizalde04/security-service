import logging

# Configure logging
logging.basicConfig(filename="tasks.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def log_to_file(message):
    """
    Logs an async task message to a file.
    """
    logging.info(message)
