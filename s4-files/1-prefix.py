#!/bin/env python3 

from pathlib import Path 

root_dir = Path('files')
file_paths = list(root_dir.iterdir())


for path in file_paths: 
    new_filename = "new-" + path.stem + path.suffix
    new_filename = path.with_name(new_filename)
    path.rename(new_filename)