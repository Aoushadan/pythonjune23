from bs4 import BeautifulSoup
xml_data = """
    <books>
        <book id = "1">
            <title>AlChemist</title>
            <author>Stephen</author>
"""
soup = BeautifulSoup(xml_data,"xml")
with open(r"C:\Users\MANOJ\OneDrive\Desktop\python\job.xml","w") as file:
    file.write(soup.prettify())
with open(r"C:\Users\MANOJ\OneDrive\Desktop\python\job.xml","r") as file:
    soup = BeautifulSoup(file,'xml')
    title = soup.find('title').text
    print(title)