#!/bin/env python3 

import pandas
from fpdf import FPDF

df = pandas.read_excel('data.xlsx')

for index, row in df.iterrows():
    pdf = FPDF(orientation='P', unit='pt',format='A4')
    pdf.add_page()

    for header,value in row.items(): 
        if header == "name":
            pdf.set_font(family='Times', style='B',size=24)
            pdf.cell(w=0,h=50,txt=row['name'], align='C',ln=1 )
        else:
            pdf.set_font(family='Times',style='B',size=14)
            pdf.cell(w=100,h=25,txt=f"{header.capitalize()}: ")
            pdf.set_font(family='Times',size=14)
            pdf.cell(w=100,h=25,txt=f"{value}",ln=1)
    
    pdf.output(f"{row['name']}.pdf")



