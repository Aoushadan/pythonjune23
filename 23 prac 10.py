from openpyxl import Workbook

wb = Workbook(write_only=True)
ws = wb.create_sheet()

# Writing large data efficiently
for i in range(1, 1000001):
    ws.append([f"Row {i}", f"Data {i}"])

wb.save(r'C:\Users\MANOJ\OneDrive\Documents\csv7prac.csv')