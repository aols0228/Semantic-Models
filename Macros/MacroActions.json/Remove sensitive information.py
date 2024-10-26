# Author: Andreas Heuser Nordgaard og ChatGPT
# Description:
# Python script to remove content after 'adb-' and 'sql/' prefixes,
# and replace words starting with 'dap_' with 'fso' in MacroActions.json,
# while preserving escaped quotes and minimizing terminal output.

import json
import shutil
from pathlib import Path
import re

# Define prefixes and replacement patterns
PREFIXES = ['adb-', 'sql/']
PREFIX_PATTERNS = {prefix: re.compile(rf'({re.escape(prefix)})[^"\s]*') for prefix in PREFIXES}
DAP_PATTERN = re.compile(r'\bdap_\w*\b')

# Define paths
current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent.parent
file_path = parent_dir / 'Configuration Files' / 'MacroActions.json'
backup_dir = Path(r'C:\Temp')
backup_path = backup_dir / file_path.name

# Create backup
backup_dir.mkdir(parents=True, exist_ok=True)
shutil.copy(file_path, backup_path)
print(f"✅ Backup JSON created at {backup_path}")

# Load JSON data
with open(file_path, 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

def process(data):
    if isinstance(data, dict):
        return {k: process(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [process(item) for item in data]
    elif isinstance(data, str):
        # Remove content after specified prefixes
        for prefix, pattern in PREFIX_PATTERNS.items():
            data = pattern.sub(r'\1', data)
        # Replace words starting with 'dap_' with 'fso'
        data = DAP_PATTERN.sub('fso', data)
        return data
    return data

# Process data
updated_data = process(data)

# Save updated JSON
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(updated_data, f, indent=2, ensure_ascii=False)
print(f"✅ Updated JSON saved to {file_path}")
