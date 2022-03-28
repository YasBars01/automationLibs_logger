# loggerLibrary

automationLibs is a collection of Python packages that are created by ISG's Automation Squad to help in something something

## Installation and updating
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install automationLibs like below. 
Rerun this command to check for and install  updates .
```bash
pip install -e git+https://gitlab.com/blaise.cosico/automation_team_libraries#egg=automationLibs
```

## Usage
Features:
##### GDrive
* functions.files_in_folder  --> returns all files in a specified google drive folder
* functions.if_file_exists_in_folder  --> checks if file exists in a google drive folder
* functions.create_gsheet_copy_from_spread_sheet  --> creates a copy of an existing google sheets

##### AutoguiHelper
* functions.find_this  --> looks for item given an img path
* functions.click_this  --> clicks on found item


#### Demo of some of the features:
```python
import automationLibs
from automationLibs import GDrive


service_account = /Path-To-Service-Account/
drive = GDrive(service_account)


files = drive.files_in_folder(folder_id: str)
exists = drive.if_file_exists_in_folder(file_name: str, folder_id: str)

```


## License
[MIT](https://choosealicense.com/licenses/mit/)
