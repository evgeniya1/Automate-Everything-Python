import pandas as pd

#load public google sheet
url_gsheets = "https://docs.google.com/spreadsheets/d/1D7U4A9c-hwWWYokmGWAQnUTKsyvEmV9syig8NJuVa84/gviz/tq?tqx=out:csv&sheet="

sheet_name = "2013"
data = pd.read_csv(url_gsheets + sheet_name)
print(data[0])

# sheet_name = "2014"
# data = pd.read_csv(url_gsheets + sheet_name)
# print(data[0])
"""
# #load private google sheet
import gspread

gc = gspread.service_account('secrets.json')

spreadsheet = gc.open('test_read_google_sheets')
#worksheet_1 = spreadsheet.get_worksheet(0)
worksheet_1 = spreadsheet.worksheet("2023")

# get all data
data = worksheet_1.get_all_values()
# get specific rows by cells
data = worksheet_1.get_values('A5:E5')
# get row by undex
data = worksheet_1.row_values(1)
# get column by undex
data = worksheet_1.col_values(2)[:1]
#get cell value
cell1 = worksheet_1.acell('D5').value
#find cell indexes
cell3 = worksheet_1.find("-10")
cells = worksheet_1.findall("-9")

import re
reg = re.compile(r'99')
cells = worksheet_1.findall(reg)

for cell in cellsL
  print(cells.row, cells.col, cells.value)


#update cell
worksheet_1.update('E5', -29)
#update cell based on row, col, undexes
worksheet_1.update_cell(5,5, 39)
#update column
existing_column = worksheet_1.get_values('E2:E25')
new_column = [[round(float(i[0]) * 9/5 + 32, 2)] for i in existing_column]
print(new_column)
worksheet_1.update('G1:G25',[['Fahrenheit']] + new_column)

import statistics 
temp_F = worksheet_1.get_values('G2:G25')
worksheet_1.update('G26', round(statistics.mean([float(i[0]) for i in temp_F]),2))

#listen for changes
import time
worksheet_1 = spreadsheet.worksheet("2023")
worksheet_2 = spreadsheet.worksheet("watch")
while True:
  value1 = worksheet_1.acell('G26').value
  time.sleep(2)
  value2 = worksheet_1.acell('G26').value
  if value1 != value2:
    worksheet_2.update('A1', 'CHANGED')
    break



#https://docs.google.com/spreadsheets/d/1jrNxXTeuEo_2T3678RxLb08xP5S8wxO12thTan3oIYw/edit?usp=sharing

"""
