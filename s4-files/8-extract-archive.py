#!/bin/env python3 

from pathlib import Path 
import zipfile

root_dir = Path('.')
destination_folder = Path('files')

for path in root_dir.glob('*.zip'):
    with zipfile.ZipFile(path,'r') as zf: 
        final_path = destination_folder / Path(path.stem)
        zf.extractall(final_path)