#!/bin/env python3 
 
from pathlib import Path

root_dir = Path('.')
search_term = "archive"

paths = root_dir.rglob(f"*{search_term}*")
for path in paths: 
        print(path.absolute())
