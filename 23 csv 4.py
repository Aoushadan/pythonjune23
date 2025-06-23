

import csv
data = [['Name','Age'],
        ['John', 25],
        ['Job', 21]]
with open(r'C:\Users\MANOJ\OneDrive\Documents\excsv3','w',newline = '') as file:
    writer = csv.writer(file)
    writer.writerows(data)
with open(r'C:\Users\MANOJ\OneDrive\Documents\excsv3.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)



