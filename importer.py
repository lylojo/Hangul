from pandas import read_excel
import numpy as np

df = read_excel("C://Users/lmjru/Downloads/Book.xlsx")

kor = df[['Kor']].to_numpy()
global flattened_list
flattened_list = [item for sublist in kor for item in sublist]

print(df)
print(kor)
print(flattened_list)