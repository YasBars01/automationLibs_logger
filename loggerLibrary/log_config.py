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
        

BASE_DIR = os.environ.get('LOG_BASE_DIR') or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_NAME = "logger_library"
CURRENT_LOG_DIR = os.path.join(BASE_DIR, 'logs', datetime.today().strftime('%Y'), datetime.today().strftime('%B'))

#checks if directory exists, if not create it
pathlib.Path(CURRENT_LOG_DIR).mkdir(parents=True, exist_ok=True) 

LOG_DIR = os.path.join(CURRENT_LOG_DIR,  APP_NAME + '_log_' + datetime.today().strftime('%Y-%m-%d') + '.log')


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] : [%(levelname)s] : %(pathname)s : %(message)s;')
file_handler = logging.FileHandler(LOG_DIR)
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




