#!/bin/env python3 

import fitz

with fitz.open('students.pdf') as pdf:
    text = ''
    for page in pdf:
        text += page.get_text()

    print(text)