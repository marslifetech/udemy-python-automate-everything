#!/bin/env python3 
 
import tabula 


table = tabula.read_pdf('pdf/weather.pdf',pages=1)

table[0].to_csv('excel/outptut.csv',index=None)
