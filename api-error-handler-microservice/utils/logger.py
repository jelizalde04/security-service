import logging

# Configure logging
logging.basicConfig(filename="errors.log", level=logging.ERROR, format="%(asctime)s - %(message)s")

def log_to_file(message):
    """
    Logs an error message to a file.
    """
    logging.error(message)
