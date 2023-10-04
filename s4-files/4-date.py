#!/bin/env python3 

from pathlib import Path 
from datetime import datetime

path = Path("extensions")

for path in path.rglob('*.txt'):
    if path.is_file(): 
        new_filepath = path.with_suffix(".csv")
        path.rename(new_filepath)

