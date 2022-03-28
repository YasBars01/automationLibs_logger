# automationLibs_logger Library

automationLibs is a collection of Python packages that are created by ISG's Automation Squad.
automationLibs aims to create boilerplate functions that will allow you to start coding immediately.
Here is a list of other libraries:
* [automationLibs_logger Library][1] - Logger Library
* automationLibs_Gdrive Library - GDrive and GSheet helper Library
* automationLibs_PyAutoGUI Library - PyAutoGUI related Library
* automationLibs_Web Library - Selenium and other web related Library
* automationLibs_remote Library - sftp Library
* automationLibs_service Library - other helper Libraries

[1]:https://gitlab.com/yasmin.barrientos/automationLibs_logger

## Installation and updating
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install automationLibs like below. 
Rerun this command to check for and install  updates .
```bash
pip install -e git+https://gitlab.com/blaise.cosico/automation_team_libraries#egg=automationLibs
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
```
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

## License
[MIT](https://choosealicense.com/licenses/mit/)
