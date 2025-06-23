import json

# Python data to save as JSON
data = {
    "name": "Alice",
    "age": 25,
    "city": "Boston",
    "skills": ["Python", "SQL", "Machine Learning"]
}

# Write JSON data to a file
with open(r'C:\Users\MANOJ\OneDrive\Desktop\python\hello.json', 'w') as file:
    json.dump(data, file, indent=4)

import json

# Python data to convert into a JSON string
data = {
    "name": "Bob",
    "age": 40,
    "city": "Chicago"
}

# Convert Python data to a JSON string
json_string = json.dumps(data, indent=2)
print(json_string)
