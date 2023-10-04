#!/bin/env python3 

from pathlib import Path

root_dir = Path('files')
file_paths = root_dir.glob('**/*')

for path in file_paths: 
    if path.is_file(): 
        
        file_path = path.with_name(f"{path.parts[-2]}-{path.name}")
        path.rename(file_path)
