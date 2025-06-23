import json
data = {
    "person":{
        "name":"JOB",
        "age":"23"
    },
    "students":[
        {
            "name":"JOB",
            "age":"25"
        }
    ]
}
with open(r"C:\Users\MANOJ\OneDrive\Desktop\python\job.json","w") as file:
    json.dump(data, file, indent = 4)
with open(r"C:\Users\MANOJ\OneDrive\Desktop\python\job.json","r") as file:
    data = json.load(file)
print(data["students"]["name"])
print(data["person"])s