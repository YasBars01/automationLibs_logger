import pathlib
import logging
import os
from datetime import datetime


class ContextFilter(logging.Filter):
    """
    This is a filter which injects contextual information into the log.
    """

    def filter(self, record):
        record.today = datetime.today().strftime('%Y-%m-%d')
        record.time = datetime.today().strftime('%H:%M:%S')
        return True


class Logger:
    """
        Logger class that sets up python logger
        :params str app_name: name of the app, would be part of the file name of the log file.
        :params str set_logger_name: set the name of the app to logger name, so that you can choose which file to log if
         you have multiple log files.

        Sample use 1:
        logger = Logger(app_name).logger

        Sample use 2:
        import logging

        Logger(app_name_a, True)
        Logger(app_name_b, True)

        logger_a = logging.getLogger("app_name_a")
        logger_b = logging.getLogger("app_name_b")

        logger_a.info("Hello")
        logger_b.info("Hi")
    """

    def __init__(self, app_name, set_logger_name: bool = False) -> None:
        self.base_dir = os.environ.get('LOG_BASE_DIR') or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.app_name = app_name
        self.set_logger_name = set_logger_name
        self.LOG_DIR = os.path.join(self.base_dir, 'logs', datetime.today().strftime('%Y'),
                                    datetime.today().strftime('%B'))
        self.logger = self.make_logger()

    def make_logger(self):
        # checks if directory exists, if not create it
        pathlib.Path(self.LOG_DIR).mkdir(parents=True, exist_ok=True)

        self.LOG_DIR = os.path.join(self.LOG_DIR,
                                    self.app_name + '_log_' + datetime.today().strftime('%Y-%m-%d') + '.log')

        if self.set_logger_name:
            logger = logging.getLogger(self.app_name)
        else:
            logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('[%(asctime)s] : [%(levelname)s] : [%(pathname)s:%(lineno)d] : %(message)s;')

        file_handler = logging.FileHandler(self.LOG_DIR)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.addFilter(ContextFilter())

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)

        return logger




