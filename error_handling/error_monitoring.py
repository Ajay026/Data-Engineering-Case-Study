import logging

logging.basicConfig(filename='error.log', level=logging.ERROR)

def log_error(message):
    logging.error(message)

# Example usage
log_error("This is a test error message")

