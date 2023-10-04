#!/bin/env python3 

from pathlib import Path
import zipfile

root_dir = Path('files')
archive_file = root_dir / Path('archive.zip')

with zipfile.ZipFile(archive_file,'w') as zf:
    for path in root_dir.rglob('*.txt'):
        # is object a file?
        if path.is_file():
            # write file to archive file
            zf.write(path)
            # remove file 
            path.unlink()