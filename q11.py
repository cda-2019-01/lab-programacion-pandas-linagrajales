##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
## 
import pandas as pd
import numpy as np
data2 = pd.read_csv("tbl2.tsv", sep="\t")
data2['_c']=data2['_c5a']+":"+data2['_c5b'].astype(str)
c0 = sorted(data2['_c0'].unique())
lista = []
for val in c0:
    df = (data2[data2['_c0'] == val])
    df1 = sorted(df['_c'].tolist())
    df2 = ",".join(map (str, df1))
    lista.append(df2)
out = pd.DataFrame({"_c0":c0,"lista":lista})
print(out)
