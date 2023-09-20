import pandas as pd

df = pd.read_excel("./raw_data.xlsx", engine="openpyxl")

print(df)

