# ##extract all text
# import fitz

# with fitz.open("students.pdf") as pdf:
#   for page in pdf:
#     # print(20*'-')
#     # print(page.get_text())
#     text = text + page.get_text()
#     print(text)

##extract table
import tabula

table = tabula.read_pdf('weather.pdf', pages=1)

print(table)
