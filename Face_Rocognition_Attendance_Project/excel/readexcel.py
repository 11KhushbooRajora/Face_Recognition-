from openpyxl.workbook import workbook
from openpyxl import load_workbook

wb=workbook()

wb=wb.active()

wb=load_workbook('Data.xlsx')
