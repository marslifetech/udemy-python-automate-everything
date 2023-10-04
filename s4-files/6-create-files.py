#!/bin/env python3 

from pathlib import Path 

root_path = Path('files')

for i in range(10,31):
    file_name = f"{i}.txt"
    file_path = root_path / Path(file_name)
    file_path.touch()  