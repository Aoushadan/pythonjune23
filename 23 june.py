with open("C:\\Users\\MANOJ\\OneDrive\\Desktop\\python\\filehandling.txt","w") as file:
    file.write("Learning file handling \n")

with open("C:\\Users\\MANOJ\\OneDrive\\Desktop\\python\\filehandling.txt","r") as file:
    content = file.read()

with open("C:\\Users\\MANOJ\\OneDrive\\Desktop\\python\\filehandling.txt","a") as file:
    file.write("Learning file handling ")