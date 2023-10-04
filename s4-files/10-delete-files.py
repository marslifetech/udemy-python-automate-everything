#!/bin/env python3
 
from pathlib import Path

root_dir = Path('files')
for path in root_dir.rglob('*.txt'): 
    with open(path, 'wb') as file: 
        file.write(b'')
    path.unlink()