import pathlib
import logging
import os
import sys
from datetime import datetime


class OldLogger:
    def __init__(self, log_dir=1, log_name_id=None, enable_stdout: bool = False):
        """
        For reference: https://docs.python.org/3/library/logging.html
        :param log_dir: Complete folder location, where the log file will be created. If 1 or None: Logs will be created
        in Logs folder. If 2: logs will be created in Logs/<year>/<Month> Folder, e.g. logs/2022/March
        :type log_dir: int
        :param log_name_id: identifying name of the log. Could be based on the app name and/or machine to make the log
            file easier to identify. e.g. myLog_myMachine --> myLog_myMachine_log_2022-03-28.log.
            Otherwise, log file will be named: log_2022-03-28.log
        :type log_name_id: string
        """
        self.base_dir = os.environ.get('LOG_BASE_DIR') or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        if log_dir == 1 or log_dir is None:
            self.LOG_DIR = os.path.join(self.base_dir, 'logs')
        elif log_dir == 2:
            self.LOG_DIR = os.path.join(self.base_dir,
                                        'logs',
                                        datetime.today().strftime('%Y'),
                                        datetime.today().strftime('%B'))
        else:
            self.LOG_DIR = log_dir

        if log_name_id is None:
            self.LOG_DIR = os.path.join(self.LOG_DIR,
                                        'log_' + datetime.today().strftime('%Y-%m-%d') + '.log')
        else:
            self.LOG_DIR = os.path.join(self.LOG_DIR,
                                        log_name_id + '_log_' + datetime.today().strftime('%Y-%m-%d') + '.log')

        self.enable_stdout = enable_stdout

    def logger(self):
        # log format in log file
        # for more formats, check here: https://docs.python.org/3/library/logging.html#logrecord-attributes
        logging.basicConfig(filename=self.LOG_DIR,
                            filemode='a',
                            level=logging.DEBUG,
                            format='[%(asctime)s]: [%(levelname)s]: [%(pathname)s:%(lineno)d] : %(message)s;',
                            datefmt='%Y-%m-%d %H:%M:%S')

        # create logger
        logger = logging.getLogger(self.LOG_DIR)
        logger.setLevel(logging.DEBUG)

        # create console handler, for console/terminal log
        if self.enable_stdout:
            ch = logging.StreamHandler(sys.stdout)
        else:
            ch = logging.StreamHandler()

        ch.setLevel(logging.DEBUG)

        # log format in PyCharm terminal
        # for more formats, check here: https://docs.python.org/3/library/logging.html#logrecord-attributes
        formatter = logging.Formatter('[%(asctime)s]: [%(levelname)s]: [%(pathname)s:%(lineno)d] : %(message)s;',
                                      '%Y-%m-%d %H:%M:%S')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)

        return logger
