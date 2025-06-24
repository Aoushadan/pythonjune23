import pyodbc

server = r'localhost'
database = 'ECOMM'

conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    rf'SERVER={server};'
    rf'DATABASE={database};'
    r'Trusted_Connection=yes;'
)
cursor = conn.cursor()
cursor.execute("SELECT TOP 5 * FROM [ECOMM].[dbo].[Products]")
for row in cursor.fetchall():
    print(row)
cursor.close()
conn.close()