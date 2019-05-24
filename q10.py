##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
## 
import pandas as pd
import numpy as np
import itertools
data1 = pd.read_csv("tbl1.tsv", sep="\t")
c0 = sorted(data1['_c0'].unique())
lista = []
for val in c0:
    df = (data1[data1['_c0'] == val])
    df1 = sorted(df['_c4'].tolist())
    df2 = ",".join(map (str, df1))
    lista.append(df2)
out = pd.DataFrame({"_c0":c0,"lista":lista})
print(out)
