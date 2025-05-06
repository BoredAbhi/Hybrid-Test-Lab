import logging
import os

class Logger:

    @staticmethod
    def get_logger(name="TestLogger"):
        """
        Set up the logger with custom format and log level.
        """
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        # Create log folder if it doesn't exist
        log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_file = os.path.join(log_dir, 'test_log.log')

        # Create file handler to log to a file
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)

        # Create console handler to log to console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Create a formatter and set it for handlers
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger
