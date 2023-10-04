== Files ==
 
=== library ===
- pathlib 
    - installed by default 
    - replacement for os (strings vs new object types)

```
from pathlib import PATH
```


== Add Prefix ==


## pathlib methods 
**from pathlib import Path**
|glob()| Search | list
|rglob | recursive search | list 
|is_file()| is object a file? | boolean
|rename()| renames object | object
|with_suffix| changes suffix of file | object
| with_name() | return file path | object 
|.touch()| simply touch or create file if non-existing | N/A
|absolute() | get absolute file path | Sting
### pathlib attributes
| 


## zipfile 
| w | write archive file 
| r | extract archive file