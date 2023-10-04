#!/bin/env python3 

from pathlib import Path

path = Path('files')

path_files = path.rglob("*")

for file in path_files:
    if file.is_file():
        new_filename = file.with_suffix(".csv")
        file.rename(new_filename)
