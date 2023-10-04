#!/bin/env python3 

from pathlib import Path 

root_dir = Path('files')
file_paths = root_dir.glob("**/*")

for path in file_paths: 
    if path.is_file():
        name_parts = list(path.parts)
        new_path_name = path.with_name(f"{name_parts[-3]}-{name_parts[-2]}-{name_parts[-1]}")
        path.rename(new_path_name)
gg