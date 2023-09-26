from openpyxl import Workbook, load_workbook

wb = load_workbook("14-paquetes-populares/winrate.xlsx")
source = wb.active

# ws = source['A1']
ws = source

print(ws)
