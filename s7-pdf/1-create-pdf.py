#!/bin/env python3 

from fpdf import FPDF

pdf = FPDF(orientation="P",unit="pt",format="A4")
pdf.add_page()

pdf.image('tiger.jpeg',w=80,h=50, x=500)
pdf.set_font(family='Times',style='B', size=24)
pdf.cell(w=0,h=50, txt="Tiger is Watching you.",align='C',ln=1)
pdf.cell()
pdf.output('output.pdf')
