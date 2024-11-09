# Author: Andreas Heuser Nordgaard og ChatGPT
# Link to source: 
# Description:
## Pythonscript that assigns new numerical id's to MacroActions.json
## MacroActions.json is the file that programs the model developers local macros through %localappdata%\TabularEditor3
## The reason for the script is due to the fact that I as a macro developer sometimes changes the order of the macros in the json-script itself.
## This requires re-enumerating all macros from 1...n.
## The script dynamically checks if the macros are either in a dictionary or in a list, and proceeds with the first list in the MacroActions dictionary using next(...).
## Because of this first item behaviour, we do not need to specify the key.
## This is tedious given that a macro could be moved from the end to the beginning and a hundred macros then need to have their Id's reassigned.
## -------------------------
## The file path of the MacroActions.json script itself is dynamic according to the location of this script.
## This entails that you need to define the dynamic file path.
## This is especially useful if you like me have MacroActions in a model developer repo, with which you push macros, BPA's and layouts to model developers from a folder called e.g. Configurations Files.
## Then you can have this script located in an adjacent folder.
## -------------------------
## Please notice that python needs to be installed on your local machine.
## The script is most easily handled in Visual Studio Code with Python Extension fra Microsoft.
## -------------------------
# Change Log:
## ---------------------------------------------------------------
## Ver. | Date dd-MM-yyyy | Author    | Description
## 1.0    22-10-2024        Andreas     Initialized

# Common path libraries for python
import json
import shutil
from pathlib import Path

# Get the current directory of this script
current_directory = Path(__file__).resolve().parent

# Navigate to the parental directory (it is called parental since we sometimes have to change the depth of the folders and we do not want to rename underlying variables each time e.g. parent/grandparent)
parental_directory = current_directory.parent.parent

# Define the path to the file in the parental directory
file_path = parental_directory / 'Configuration Files' / 'MacroActions.json'

# Backup directory and backup file path
backup_dir = Path(r'C:\Temp')
backup_file_path = backup_dir / file_path.name

# Step 1: Create the backup directory if it doesn't exist
backup_dir.mkdir(parents=True, exist_ok=True)

# Step 2: Create a backup of the existing JSON file
try:
    shutil.copy(file_path, backup_file_path)
    print(f"✅ Backup JSON created at {backup_file_path}")
except Exception as e:
    print(f"Error creating backup: {e}")
    raise

# Step 3: Load the JSON data from the file
try:
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        data = json.load(file)
except json.JSONDecodeError as e:
    print(f"Error reading JSON file: {e}")
    print("Please ensure the file contains valid JSON.")
    raise
except Exception as e:
    print(f"Unexpected error: {e}")
    raise

# Step 4: Identify the list to be processed
# If data is a dictionary, search for the first list within its values
if isinstance(data, dict):
    list_to_enumerate = next((value for value in data.values() if isinstance(value, list)), None)
    if list_to_enumerate is None:
        raise ValueError("No list found inside the dictionary.")
# If data is already a list, use it directly
elif isinstance(data, list):
    list_to_enumerate = data
else:
    raise ValueError("Expected the JSON file to contain a dictionary with a list or a list.")

# Step 5: Assign incremental IDs to elements in the list
for index, item in enumerate(list_to_enumerate):
    item['Id'] = index + 1

# Step 6: Write the updated data back to the same JSON file
try:
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)  # ensure_ascii=False to preserve special characters
    print(f"✅ Updated JSON saved to {file_path}")
except Exception as e:
    print(f"Error writing to JSON file: {e}")
    raise