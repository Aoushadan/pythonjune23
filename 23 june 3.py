import pandas as pd
data = {'Name':['Tom','nick','job','jack'],'Age':[23,34,56,26]}
df = pd.DataFrame(data)
print(df)
df.to_excel(r"C:\Users\MANOJ\OneDrive\Documents\py\exclpy2.xlsx",index = False)
df.pd.read_excel(r"C:\Users\MANOJ\OneDrive\Documents\py\exclpy2.xlsx")
print(df)