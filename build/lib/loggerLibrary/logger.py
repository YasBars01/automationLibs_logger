import pathlib
import logging
import os
from datetime import datetime
import sys


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

        return
        logger : logger object
        log_dir str: params
    """

    def __init__(self,
                 log_dir,
                 log_id,
                 set_logger_name: bool = False,
                 show_logger_id: bool = False,
                 enable_stdout: bool = False) -> None:
        self.base_dir = log_dir or os.environ.get('LOG_BASE_DIR') or os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))) + '\\logs\\'
        self.log_id = log_id
        self.set_logger_name = set_logger_name
        self.show_logger_id = show_logger_id
        self.logger_name = ''
        self.LOG_DIR = os.path.join(self.base_dir, datetime.today().strftime('%Y'),
                                    datetime.today().strftime('%B'))
        self.with_milliseconds = True
        self.enable_stdout = enable_stdout

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
                                    self.log_id + '_' + datetime.today().strftime('%Y-%m-%d') + '.log')

        if self.set_logger_name is not False:
            logger = logging.getLogger(self.log_id)
        else:
            logger = logging.getLogger(__name__)

        if self.show_logger_id is not False:
            self.logger_name = ' [%(name)-12s]:'

        logger.setLevel(logging.DEBUG)

        # log format: for more formats, check here: https://docs.python.org/3/library/logging.html#logrecord-attributes
        if self.with_milliseconds:
            formatter = logging.Formatter(f'[%(asctime)s]:{self.logger_name} [%(levelname)s]: '
                                          f'[%(pathname)s:%(lineno)d]: %(message)s;')

        else:
            formatter = logging.Formatter(f'[%(asctime)s]:{self.logger_name} [%(levelname)s]: '
                                          f'[%(pathname)s:%(lineno)d]: %(message)s;',
                                          '%Y-%m-%d %H:%M:%S')

        # create console handler, for console/terminal log
        if self.enable_stdout:
            ch = logging.StreamHandler(sys.stdout)
        else:
            ch = logging.StreamHandler()

        # create file handler, for file log
        file_handler = logging.FileHandler(self.LOG_DIR)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.addFilter(ContextFilter())

        # Console Handler, set level to debug
        ch.setLevel(logging.DEBUG)

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)

        return logger
