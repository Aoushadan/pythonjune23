from openpyxl import Workbook,load_workbook


wb = Workbook()
ws = wb.active

# example of writing 1,000,000 rows
for i in range(1, 1000001):
    ws.append([f"Row {i}", f"Value {i}"])

# Save the workbook
wb.save(r'C:\Users\MANOJ\OneDrive\Documents\csv7prac.csv')
