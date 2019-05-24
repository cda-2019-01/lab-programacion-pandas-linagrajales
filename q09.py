##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 
import pandas as pd
import numpy as np
import itertools
data = pd.read_csv("tbl0.tsv", sep="\t")
c1 = sorted(data['_c1'].unique())
lista = []
for val in c1:
    df = (data[data['_c1'] == val])
    df1 = sorted(df['_c2'].tolist())
    df2 = ":".join(map (str, df1))
    lista.append(df2)
out = pd.DataFrame({"_c0":c1,"lista":lista})
print(out)
