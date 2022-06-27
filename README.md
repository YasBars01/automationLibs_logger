# automationLibs_logger Library

automationLibs is a collection of Python packages that are created by ISG's Automation Squad. automationLibs aims to
create boilerplate functions that will allow you to start coding immediately. Here is a list of other libraries:

* [automationLibs_logger Library][1] - Logger Library
* automationLibs_Gdrive Library - GDrive and GSheet helper Library
* automationLibs_PyAutoGUI Library - PyAutoGUI related Library
* automationLibs_Web Library - Selenium and other web related Library
* automationLibs_remote Library - sftp Library
* automationLibs_service Library - other helper Libraries

[1]:https://gitlab.com/yasmin.barrientos/automationLibs_logger

# Installation and updating

1. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install automationLibs like below. Rerun this command
to check for and install updates .

```bash
pip install -e git+https://gitlab.com/yasmin.barrientos/automationLibs_logger#egg=automationLibs_logger

```

To install a specific branch

```bash
pip install -e git+https://gitlab.com/yasmin.barrientos/automationLibs_logger.git@dev-ver01#egg=automationlibs-logger
```

2. In your .ENV, add the full path where you would like the logs to be created(could be anywhere:
```dotenv
#*** automationLibs_logger ***#
LOG_BASE_DIR="C:\\Users\\my_machine\\PycharmProjects\\my_project"
```

##_pip install is not working, what do I do?_
1. Click the download link: https://gitlab.com/yasmin.barrientos/automationLibs_logger/-/archive/main/automationLibs_logger-main.zip to download the file

2. Install using [pip](https://pip.pypa.io/en/stable/)
```bash
pip install <full path to folder>automationLibs_logger-main.zip
```
3. In your .ENV file, add the full path where you would like the logs to be created(could be anywhere:
```dotenv
#*** automationLibs_logger ***#
LOG_BASE_DIR="C:\\Users\\my_machine\\PycharmProjects\\my_project"
```
 
## Usage

Features:
Install this package to use a pre-formatted logger

##### Logger

* Logger(LOG_NAME_ID).logger
    * instantiates and creates the logger

#### Demo of logger:

```python
from loggerLibrary.logger import Logger
import getpass

LOG_NAME_ID = f'loggerLibrarytest_{getpass.getuser()}'
logger = Logger(LOG_NAME_ID).logger

logger.info('test info')
logger.error('test info')
```

Result in PyCharm Terminal:

```log
[2022-03-28 17:56:30] : [INFO] : [C:\DEV\PYTHON\PycharmProjects\loggerLibrary\tests\test_logger.py:9] : test info;
[2022-03-28 17:56:30] : [ERROR] : [C:\DEV\PYTHON\PycharmProjects\loggerLibrary\tests\test_logger.py:10] : test info;
```

Result in Log File:

```log
[2022-03-28 17:56:30] : [INFO] : [C:\DEV\PYTHON\PycharmProjects\loggerLibrary\tests\test_logger.py:9] : test info;
[2022-03-28 17:56:30] : [ERROR] : [C:\DEV\PYTHON\PycharmProjects\loggerLibrary\tests\test_logger.py:10] : test info;
```

#### Demo of Old Logger:

```python
from loggerLibrary.old_logger import OldLogger
import getpass

LOG_NAME_ID = f'loggerLibrarytest_{getpass.getuser()}'
logger2 = OldLogger(log_dir=2, log_name_id=LOG_NAME_ID).logger()

logger2.info('test info')
logger2.error('test info')

```

Result in PyCharm Terminal:

```log
[2022-03-28 17:56:30]: [INFO]: [test_logger.py:14] : test info;
[2022-03-28 17:56:30]: [ERROR]: [test_logger.py:15] : test info;
```

Result in Log File:

```log
[2022-03-28 17:56:30]: [INFO]: [C:\DEV\PYTHON\PycharmProjects\loggerLibrary\tests\test_logger.py:14] : test info;
[2022-03-28 17:56:30]: [ERROR]: [C:\DEV\PYTHON\PycharmProjects\loggerLibrary\tests\test_logger.py:15] : test info;
```

## How to Use
1. In your settings.py, initialize the logger
```python
from common.settings import logger

logger.info('test')
logger.error('test')
```


2. Import settings.py to your other files

## Log Format
For more log formats, check here: https://docs.python.org/3/library/logging.html#logrecord-attributes

## License

[MIT](https://choosealicense.com/licenses/mit/)
