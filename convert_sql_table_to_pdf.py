import sqlite3
from fpdf import FPDF

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

columns = cursor.execute("PRAGMA table_info(ips)").fetchall()
print(columns)

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

for column in columns:
  pdf.set_font(family="Times", style="B", size=14)
  pdf.cell(w=100, h=30, txt = column[1], border=1, align = 'C')

pdf.ln()

cursor.execute("SELECT * FROM ips")
rows = cursor.fetchall()
for row in rows:
  for element in row:
    pdf.set_font(family="Times", size=14)
    pdf.cell(w=100, h=30, txt = str(element), border=1, align = 'C')
  pdf.ln()
  
pdf.output("output.pdf")