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
        :params str log_dir: exact path to where the logs will be created
        :params str log_id: name of the app, would be part of the file name of the log file.
        :params str set_logger_name: set the name of the app to logger name, so that you can choose which file to log if
         you have multiple log files.

        Sample use 1:
        logger = Logger(log_id).logger

        Sample use 2:
        import logging

        Logger(log_dir, log_id_a, True)
        Logger(log_dir, log_id_b, True)

        logger_a = logging.getLogger("log_id_a")
        logger_b = logging.getLogger("log_id_b")

        logger_a.info("Hello")
        logger_b.info("Hi")
    """

    def __init__(self, log_dir, log_id, set_logger_name: bool = False) -> None:
        self.base_dir = log_dir or os.environ.get('LOG_BASE_DIR') or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.log_id = log_id
        self.set_logger_name = set_logger_name
        self.LOG_DIR = os.path.join(self.base_dir, 'logs', datetime.today().strftime('%Y'),
                                    datetime.today().strftime('%B'))
        self.with_milliseconds = True

        self.logger = self.make_logger()

    def make_logger(self):
        # checks if directory exists, if not create it
        # pathlib.Path(self.LOG_DIR).mkdir(parents=True, exist_ok=True)
        try:
            pathlib.Path(self.LOG_DIR).mkdir(parents=True, exist_ok=True)
            os.makedirs(self.LOG_DIR)
        except OSError:
            if not os.path.isdir(self.LOG_DIR):
                raise

        self.LOG_DIR = os.path.join(self.LOG_DIR,
                                    self.log_id + '_log_' + datetime.today().strftime('%Y-%m-%d') + '.log')

        if self.set_logger_name:
            logger = logging.getLogger(self.log_id)
        else:
            logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        # log format: for more formats, check here: https://docs.python.org/3/library/logging.html#logrecord-attributes
        if self.with_milliseconds:
            formatter = logging.Formatter('[%(asctime)s] : [%(levelname)s] : [%(pathname)s:%(lineno)d] : %(message)s;')
        else:
            formatter = logging.Formatter('[%(asctime)s] : [%(levelname)s] : [%(pathname)s:%(lineno)d] : %(message)s;',
                                          '%Y-%m-%d %H:%M:%S')

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
