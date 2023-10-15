#!/bin/env python3 

import tabula 

table = tabula.read_pdf('pdf/Table+and+Text.pdf',pages=1)

table[0].to_excel('excel/weather.xlsx',index=None)