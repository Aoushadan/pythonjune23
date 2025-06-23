
import csv


data = [
    ['Name', 'Age', 'City'],
    ['Alice', 28, 'Boston'],
    ['Bob', 35, 'San Francisco']
]


with open(r'C:\Users\MANOJ\OneDrive\Documents\csv7prac.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)

    csv_writer.writerows(data)


