
import json

# Reading JSON data from a file
with open(r"C:\Users\MANOJ\OneDrive\Desktop\python\hello.json", "r") as file:
    data = json.load(file)

print(data)


# JSON string
json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Parse JSON string into a Python dictionary
data = json.loads(json_string)

print(data)

